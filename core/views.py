from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from events.models import Event
from services.models import Service

from . import seo
from .forms import ContactForm
from .models import FAQ
from .regions import region_path


def home(request):
    region = request.region
    code = region["code"]
    services = Service.objects.filter(region=code, is_published=True)[:6]
    events = Event.objects.filter(region=code, is_published=True).order_by("start")
    upcoming = [e for e in events if e.is_upcoming][:3]
    faqs = list(FAQ.objects.filter(region=code, is_published=True))

    meta = seo.build_meta(
        request,
        title=f"{settings.BRAND_NAME} — {settings.BRAND_TAGLINE} in {region['name']}",
        description=(
            f"{settings.BRAND_NAME} delivers advanced stem cell and regenerative "
            f"medicine in {region['name']}. Personalised therapies, expert clinicians, "
            "and evidence-based care. Book a consultation today."
        ),
        path="/",
    )
    jsonld = [seo.organization_schema(region), seo.website_schema(region)]
    faq_ld = seo.faq_schema(faqs)
    if faq_ld:
        jsonld.append(faq_ld)

    return render(
        request,
        "core/home.html",
        {
            "meta": meta,
            "jsonld": jsonld,
            "services": services,
            "upcoming_events": upcoming,
            "faqs": faqs,
        },
    )


def about(request):
    region = request.region
    meta = seo.build_meta(
        request,
        title=f"About {settings.BRAND_NAME}",
        description=(
            f"Learn about {settings.BRAND_NAME}, a regenerative medicine and stem cell "
            f"provider serving {region['name']} with a science-first, patient-centred approach."
        ),
        path="/about/",
    )
    crumbs = seo.breadcrumb_schema(
        [
            ("Home", seo.absolute(region_path(region["code"], "core:home"))),
            ("About", meta["canonical"]),
        ]
    )
    return render(
        request,
        "core/about.html",
        {"meta": meta, "jsonld": [crumbs, seo.organization_schema(region)]},
    )


@require_http_methods(["GET", "POST"])
def contact(request):
    region = request.region
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        if not form.is_spam():
            lead = form.save(commit=False)
            lead.region = region["code"]
            lead.save()
        messages.success(
            request,
            "Thank you — your message has been received. Our team will contact you shortly.",
        )
        return redirect(region_path(region["code"], "core:contact"))

    meta = seo.build_meta(
        request,
        title=f"Contact {settings.BRAND_NAME}",
        description=(
            f"Get in touch with {settings.BRAND_NAME} in {region['name']}. "
            "Call, email, or send an enquiry to book a consultation."
        ),
        path="/contact/",
    )
    crumbs = seo.breadcrumb_schema(
        [
            ("Home", seo.absolute(region_path(region["code"], "core:home"))),
            ("Contact", meta["canonical"]),
        ]
    )
    return render(
        request,
        "core/contact.html",
        {"meta": meta, "jsonld": [crumbs, seo.organization_schema(region)], "form": form},
    )


# --------------------------------------------------------------------------- #
# Technical SEO endpoints
# --------------------------------------------------------------------------- #
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        "",
        # Explicitly welcome answer-engine / LLM crawlers (AEO/GEO).
        "User-agent: GPTBot",
        "Allow: /",
        "User-agent: OAI-SearchBot",
        "Allow: /",
        "User-agent: PerplexityBot",
        "Allow: /",
        "User-agent: Google-Extended",
        "Allow: /",
        "User-agent: ClaudeBot",
        "Allow: /",
        "",
        f"Sitemap: https://{settings.SITE_DOMAIN}/sitemap.xml",
    ]
    return _text_response("\n".join(lines))


def llms_txt(request):
    """An llms.txt manifest — a clean, structured summary for LLMs (GEO)."""
    region = request.region
    body = f"""# {settings.BRAND_NAME}

> {settings.BRAND_TAGLINE} serving {region['name']}.

{settings.BRAND_NAME} is a regenerative medicine provider offering stem cell
therapies, consultations and educational events.

## Key Pages
- [Home](https://{settings.SITE_DOMAIN}/{region['code']}/): Overview of services and care.
- [Services](https://{settings.SITE_DOMAIN}/{region['code']}/services/): Stem cell & regenerative treatments.
- [Events](https://{settings.SITE_DOMAIN}/{region['code']}/events/): Seminars and clinics.
- [About](https://{settings.SITE_DOMAIN}/{region['code']}/about/): Our approach and team.
- [Contact](https://{settings.SITE_DOMAIN}/{region['code']}/contact/): Book a consultation.

## Contact
- Phone: {region['phone']}
- Email: {region['email']}
- Location: {region['address']}
"""
    return _text_response(body)


def healthz(request):
    return _text_response("ok")


def _text_response(text):
    return HttpResponse(text, content_type="text/plain; charset=utf-8")


# --------------------------------------------------------------------------- #
# Error handlers
# --------------------------------------------------------------------------- #
def error_404(request, exception):
    return render(request, "core/404.html", status=404)


def error_500(request):
    return render(request, "core/500.html", status=500)
