from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from core import emails, seo
from core.regions import region_absolute, region_asset_rel, region_path
from payments import stripe_service

from .forms import RegistrationForm
from .models import Event, EventPackage


def _event_hero(slug, region_code):
    """Region-aware event hero image (img/[<region>/]events/<slug>-hero.webp)."""
    return region_asset_rel(region_code, f"events/{slug}-hero.webp")


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
    # Social-share card: region-aware pre-rendered JPEG, then an uploaded image.
    og = region_asset_rel(region["code"], f"og/event-{event.slug}.jpg")
    if og:
        meta["image"] = seo.absolute(settings.STATIC_URL + og)
    elif event.image:
        meta["image"] = seo.absolute(event.image.url)
        try:
            meta["image_w"], meta["image_h"] = event.image.width, event.image.height
        except Exception:
            meta["image_w"] = meta["image_h"] = None
        meta["image_type"] = ""
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
    packages = list(event.packages.filter(is_active=True))
    symbol = region.get("currency_symbol", "")
    for p in packages:
        p.price_label = f"{symbol}{p.amount:,.0f}"
    packages_by_slug = {p.slug: p for p in packages}

    return render(
        request,
        "events/detail.html",
        {"meta": meta, "jsonld": jsonld, "event": event, "form": form,
         "packages": packages, "packages_by_slug": packages_by_slug,
         "hero_image": _event_hero(event.slug, region["code"]),
         "card_image": region_asset_rel(region["code"], f"events/{event.slug}-card.webp"),
         "why_image": region_asset_rel(region["code"], f"events/{event.slug}-why.webp"),
         "learn_image": region_asset_rel(region["code"], f"events/{event.slug}-learn.webp")},
    )


def _wants_json(request):
    """The visitor submitted via fetch (AJAX) and wants a JSON toast, not a reload."""
    return request.headers.get("x-requested-with") == "XMLHttpRequest"


_LEVEL_MSG = {"error": messages.error, "success": messages.success, "info": messages.info}


def _feedback(request, back, level, message):
    """AJAX → JSON toast (no reload); normal request → flash message + redirect back."""
    if _wants_json(request):
        return JsonResponse({"ok": level == "success", "level": level, "message": message})
    _LEVEL_MSG[level](request, message)
    return back


def _go_stripe(request, back, url):
    """AJAX → JSON with the Stripe URL (JS navigates); normal → server redirect."""
    if _wants_json(request):
        return JsonResponse({"ok": True, "redirect": url})
    return redirect(url)


@require_http_methods(["POST"])
def event_register(request, slug):
    region = request.region
    event = get_object_or_404(Event, region=region["code"], slug=slug, is_published=True)
    form = RegistrationForm(request.POST)
    back = redirect(region_path(region["code"], "events:detail", slug=event.slug) + "#register")

    if not form.is_valid() or form.is_spam():
        return _feedback(request, back, "error", "Please check the form and try again.")

    registration = form.save(commit=False)
    registration.event = event
    registration.amount = event.price
    registration.currency = region["currency"]

    # Free event — confirm immediately, no payment needed.
    if event.is_free:
        registration.paid = True
        registration.save()
        emails.event_registration(registration)
        msg = "You're registered! Our team will be in touch with the details."
        if _wants_json(request):
            return JsonResponse({"ok": True, "level": "success", "message": msg})
        messages.success(request, msg)
        return redirect(region_path(region["code"], "payments:success"))

    # Paid event — needs Stripe. If Stripe isn't configured yet, save the
    # lead and tell the visitor payments are being set up (no hard error).
    registration.save()
    if not stripe_service.is_configured():
        emails.event_registration(registration)
        return _feedback(
            request, back, "info",
            "Your place is reserved. Online payment is being set up — our team "
            "will contact you to complete your booking.",
        )

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
        return _go_stripe(request, back, session.url)
    except Exception:
        return _feedback(
            request, back, "error",
            "We couldn't start the payment just now. Please try again or contact us.",
        )


@require_http_methods(["POST"])
def package_checkout(request, slug, package_slug):
    """Start a Stripe Checkout for a specific package tier.

    The price is read from the database (``package.amount``), never from the
    request, so the amount cannot be tampered with. Stripe collects the buyer's
    card and email on its hosted page; the webhook records the paid booking.
    """
    region = request.region
    event = get_object_or_404(Event, region=region["code"], slug=slug, is_published=True)
    package = get_object_or_404(
        EventPackage, event=event, slug=package_slug, is_active=True
    )
    # Normal (non-AJAX) fallback returns to the pricing section, not the top.
    back = redirect(region_path(region["code"], "events:detail", slug=event.slug) + "#pricing")

    # Stripe not set up yet — don't hard-error; reassure the visitor.
    if not stripe_service.is_configured():
        return _feedback(
            request, back, "info",
            "Online payment is being set up. Please call 725-312-2125 or email "
            "fathima@brockwellhealthcare.com to reserve your place.",
        )

    success_url = region_absolute(region["code"], "payments:success") + "?session_id={CHECKOUT_SESSION_ID}"
    cancel_url = region_absolute(region["code"], "payments:cancel")
    try:
        session = stripe_service.create_package_checkout_session(
            event=event,
            package=package,
            region=region,
            success_url=success_url,
            cancel_url=cancel_url,
        )
        return _go_stripe(request, back, session.url)
    except Exception:
        return _feedback(
            request, back, "error",
            "We couldn't start the payment just now. Please try again or contact us.",
        )
