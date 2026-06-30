from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from django.http import Http404
from django.db.models import Q

from events.models import Event
from services.models import Service, ServiceCategory
from team.models import Doctor

from . import seo
from .forms import ContactForm
from .models import FAQ, Page
from .regions import region_path


# Dummy content for the home "About / Medical Center Introduction" section.
# Replace text/icons later, or move to a model/admin if it should be editable.
ABOUT_FEATURES = [
    {"icon": "heart", "text": "Women’s health services, including one-stop breast care centre."},
    {"icon": "users", "text": "Internationally acclaimed, multi-disciplinary consultants."},
    {"icon": "shield", "text": "Expert-led teams with rigorous safety standards."},
]
ABOUT_STATS = [
    {"value": 85, "label": "Client Satisfaction"},
    {"value": 95, "label": "Medical Success"},
    {"value": 100, "label": "Client Referral"},
]
ABOUT_PARTNERS = [
    {"name": "HealthCare", "icon": "plus"},
    {"name": "Applo Medic", "icon": "stethoscope"},
    {"name": "Infi-Health", "icon": "heart"},
    {"name": "Medicalo", "icon": "shield"},
    {"name": "HealthyLife", "icon": "leaf"},
]


def home(request):
    region = request.region
    code = region["code"]
    categories = ServiceCategory.objects.filter(region=code, is_published=True)[:8]
    events = Event.objects.filter(region=code, is_published=True).order_by("start")
    upcoming = [e for e in events if e.is_upcoming][:3]
    doctors = Doctor.objects.filter(region=code, is_published=True)[:20]
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
            "categories": categories,
            "upcoming_events": upcoming,
            "doctors": doctors,
            "faqs": faqs,
            "about_features": ABOUT_FEATURES,
            "about_stats": ABOUT_STATS,
            "about_partners": ABOUT_PARTNERS,
        },
    )


def page(request, slug):
    """Render an editable content page (privacy, terms, cookies)."""
    region = request.region
    try:
        obj = Page.objects.get(region=region["code"], slug=slug, is_published=True)
    except Page.DoesNotExist:
        raise Http404("Page not found")

    meta = seo.build_meta(
        request,
        title=obj.seo_title or obj.title,
        description=obj.seo_description or f"{obj.title} — {settings.BRAND_NAME}.",
        path=f"/{slug}/",
    )
    jsonld = [
        seo.page_schema(obj, region),
        seo.breadcrumb_schema(
            [
                ("Home", seo.absolute(region_path(region["code"], "core:home"))),
                (obj.title, meta["canonical"]),
            ]
        ),
    ]
    return render(request, "core/page.html", {"meta": meta, "jsonld": jsonld, "page": obj})


def search(request):
    """Simple service search used by the header 'Search Service' box."""
    region = request.region
    q = (request.GET.get("q") or "").strip()
    services = []
    if q:
        services = list(
            Service.objects.filter(region=region["code"], is_published=True)
            .filter(Q(name__icontains=q) | Q(summary__icontains=q) | Q(description__icontains=q))[:30]
        )
    meta = seo.build_meta(
        request,
        title=f"Search results for “{q}”" if q else "Search our services",
        description="Search stem cell and regenerative services at "
        f"{settings.BRAND_NAME} in {region['name']}.",
        path="/search/",
        robots="noindex, follow",
    )
    return render(
        request,
        "core/search.html",
        {"meta": meta, "jsonld": [], "q": q, "services": services},
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
