from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from core import seo
from core.regions import region_absolute, region_path
from payments import stripe_service

from .forms import RegistrationForm
from .models import Event


def event_list(request):
    region = request.region
    events = Event.objects.filter(region=region["code"], is_published=True).order_by("start")
    upcoming = [e for e in events if e.is_upcoming]
    past = [e for e in events if not e.is_upcoming]

    meta = seo.build_meta(
        request,
        title=f"Events & Seminars in {region['name']}",
        description=(
            f"Upcoming stem cell and regenerative medicine events, seminars and clinics "
            f"hosted by {settings.BRAND_NAME} in {region['name']}. Reserve your place."
        ),
        path="/events/",
    )
    jsonld = [
        seo.breadcrumb_schema(
            [
                ("Home", seo.absolute(region_path(region["code"], "core:home"))),
                ("Events", meta["canonical"]),
            ]
        )
    ]
    jsonld += [seo.event_schema(e, region) for e in upcoming]

    return render(
        request,
        "events/list.html",
        {"meta": meta, "jsonld": jsonld, "upcoming": upcoming, "past": past},
    )


def event_detail(request, slug):
    region = request.region
    event = get_object_or_404(Event, region=region["code"], slug=slug, is_published=True)
    form = RegistrationForm()

    title = event.seo_title or f"{event.title} — {region['short']}"
    description = event.seo_description or event.summary
    meta = seo.build_meta(
        request,
        title=title,
        description=description,
        path=f"/events/{event.slug}/",
        og_type="article",
    )
    jsonld = [
        seo.event_schema(event, region),
        seo.breadcrumb_schema(
            [
                ("Home", seo.absolute(region_path(region["code"], "core:home"))),
                ("Events", seo.absolute(region_path(region["code"], "events:list"))),
                (event.title, meta["canonical"]),
            ]
        ),
    ]
    return render(
        request,
        "events/detail.html",
        {"meta": meta, "jsonld": jsonld, "event": event, "form": form},
    )


@require_http_methods(["POST"])
def event_register(request, slug):
    region = request.region
    event = get_object_or_404(Event, region=region["code"], slug=slug, is_published=True)
    form = RegistrationForm(request.POST)

    if not form.is_valid() or form.is_spam():
        messages.error(request, "Please check the form and try again.")
        return redirect(region_path(region["code"], "events:detail", slug=event.slug))

    if event.is_sold_out:
        messages.error(request, "Sorry, this event is sold out.")
        return redirect(region_path(region["code"], "events:detail", slug=event.slug))

    registration = form.save(commit=False)
    registration.event = event
    registration.amount = event.price
    registration.currency = region["currency"]

    # Free event — confirm immediately, no payment needed.
    if event.is_free:
        registration.paid = True
        registration.save()
        messages.success(request, "You're registered! We've emailed you the details.")
        return redirect(region_path(region["code"], "payments:success"))

    # Paid event — needs Stripe. If Stripe isn't configured yet, save the
    # lead and tell the visitor payments are being set up (no hard error).
    registration.save()
    if not stripe_service.is_configured():
        messages.info(
            request,
            "Your place is reserved. Online payment is being set up — our team "
            "will contact you to complete your booking.",
        )
        return redirect(region_path(region["code"], "events:detail", slug=event.slug))

    success_url = region_absolute(region["code"], "payments:success") + "?session_id={CHECKOUT_SESSION_ID}"
    cancel_url = region_absolute(region["code"], "payments:cancel")
    try:
        session = stripe_service.create_checkout_session(
            request=request,
            registration=registration,
            event=event,
            region=region,
            success_url=success_url,
            cancel_url=cancel_url,
        )
        registration.stripe_session_id = session.id
        registration.save(update_fields=["stripe_session_id"])
        return redirect(session.url)
    except Exception:
        messages.error(
            request,
            "We couldn't start the payment just now. Please try again or contact us.",
        )
        return redirect(region_path(region["code"], "events:detail", slug=event.slug))
