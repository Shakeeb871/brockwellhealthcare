import logging

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from core import seo

from decimal import Decimal, InvalidOperation

from . import stripe_service
from events.models import EventPackage, EventRegistration

logger = logging.getLogger(__name__)


def checkout_success(request):
    region = request.region
    # Best-effort: mark paid on return (the webhook is the source of truth).
    session_id = request.GET.get("session_id")
    if session_id:
        EventRegistration.objects.filter(stripe_session_id=session_id).update(paid=True)

    meta = seo.build_meta(
        request,
        title=f"Booking Confirmed | {settings.BRAND_NAME}",
        description="Your booking has been confirmed.",
        path="/checkout/success/",
        robots="noindex, follow",
    )
    return render(request, "payments/success.html", {"meta": meta, "jsonld": []})


def checkout_cancel(request):
    meta = seo.build_meta(
        request,
        title=f"Checkout Cancelled | {settings.BRAND_NAME}",
        description="Your checkout was cancelled.",
        path="/checkout/cancel/",
        robots="noindex, follow",
    )
    return render(request, "payments/cancel.html", {"meta": meta, "jsonld": []})


@csrf_exempt
@require_POST
def stripe_webhook(request):
    """Stripe's source-of-truth callback. Confirms paid registrations."""
    if not settings.STRIPE_WEBHOOK_SECRET:
        return HttpResponse(status=503)

    payload = request.body
    signature = request.META.get("HTTP_STRIPE_SIGNATURE", "")
    try:
        event = stripe_service.construct_webhook_event(payload, signature)
    except ValueError:
        return HttpResponseBadRequest("Invalid payload")
    except Exception:
        return HttpResponseBadRequest("Invalid signature")

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        _handle_completed_session(session)

    return HttpResponse(status=200)


def _handle_completed_session(session):
    """Mark a booking paid. Two shapes:

    * Registration-first flow (name/email captured on our form) → the session
      carries ``registration_id``; flip that record to paid.
    * Package flow (buyer pays straight from a package card) → the session
      carries ``package_id``; create the paid registration from the buyer's
      Stripe-collected details.
    """
    meta = session.get("metadata", {}) or {}
    session_id = session.get("id", "")

    reg_id = meta.get("registration_id")
    if reg_id:
        updated = EventRegistration.objects.filter(id=reg_id).update(
            paid=True, stripe_session_id=session_id
        )
        if not updated:
            logger.warning("Webhook: registration %s not found", reg_id)
        return

    package_id = meta.get("package_id")
    if not package_id:
        return
    # Idempotency: Stripe can deliver the same event more than once.
    if EventRegistration.objects.filter(stripe_session_id=session_id).exists():
        return

    package = EventPackage.objects.filter(id=package_id).select_related("event").first()
    if not package:
        logger.warning("Webhook: package %s not found", package_id)
        return

    details = session.get("customer_details", {}) or {}
    try:
        amount = Decimal(session.get("amount_total", 0)) / 100
    except (InvalidOperation, TypeError):
        amount = package.amount

    EventRegistration.objects.create(
        event=package.event,
        package=package,
        name=details.get("name") or "Stripe customer",
        email=details.get("email") or "",
        phone=(details.get("phone") or ""),
        amount=amount,
        currency=(session.get("currency") or "").upper(),
        stripe_session_id=session_id,
        paid=True,
    )
