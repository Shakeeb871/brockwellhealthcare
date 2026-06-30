import logging

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from core import seo

from . import stripe_service
from events.models import EventRegistration

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
        reg_id = session.get("metadata", {}).get("registration_id")
        updated = EventRegistration.objects.filter(
            id=reg_id
        ).update(paid=True, stripe_session_id=session.get("id", ""))
        if not updated:
            logger.warning("Webhook: registration %s not found", reg_id)

    return HttpResponse(status=200)
