from django.conf import settings
from django.contrib import messages
from django.contrib.staticfiles import finders
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
# Partner/brand logos shown in the About section. Put the 6 logo files in
# static/img/ named brand-1.png … brand-6.png (any image type works — just
# match the path). If a file is missing, a fallback icon + name is shown.
ABOUT_PARTNERS = [
    {"name": "Partner 1", "logo": "img/1.svg", "icon": "plus"},
    {"name": "Partner 2", "logo": "img/2.svg", "icon": "stethoscope"},
    {"name": "Partner 3", "logo": "img/3.svg", "icon": "heart"},
    {"name": "Partner 4", "logo": "img/4.svg", "icon": "shield"},
    {"name": "Partner 5", "logo": "img/5.svg", "icon": "leaf"},
    {"name": "Partner 6", "logo": "img/6.svg", "icon": "microscope"},
]

# Dummy stats for the circular "Our Impact" counters. Placeholder values only —
# edit freely. `decimals`/`suffix` handle the rating; `ring` is the decorative
# arc fill percentage (visual only, not tied to the value).
IMPACT_STATS = [
    {"icon": "bed", "value": 692, "decimals": 0, "suffix": "", "ring": 70, "label": "Hospital Beds"},
    {"icon": "pulse", "value": 1478, "decimals": 0, "suffix": "", "ring": 82, "label": "Outpatients (per day)"},
    {"icon": "user-plus", "value": 44478, "decimals": 0, "suffix": "", "ring": 90, "label": "Inpatients (per day)"},
    {"icon": "scalpel", "value": 1218, "decimals": 0, "suffix": "", "ring": 60, "label": "Surgeries (per day)"},
    {"icon": "star", "value": 4.9, "decimals": 1, "suffix": "/5.0", "ring": 98, "label": "Worldwide Rating"},
]


# Dummy steps for the "Care Journey" process section. Reusable/scalable —
# add 4 to 8 items; numbers are generated automatically in the template.
PROCESS_STEPS = [
    {"icon": "stethoscope", "title": "Initial Consultation & Evaluation",
     "desc": "A thorough one-to-one assessment of your history, goals and suitability."},
    {"icon": "microscope", "title": "Diagnostic Assessment & Lab Analysis",
     "desc": "Advanced imaging and laboratory analysis map your regenerative profile."},
    {"icon": "dna", "title": "Stem Cell Therapy Planning",
     "desc": "A personalised, evidence-based regenerative treatment plan is designed."},
    {"icon": "heart", "title": "Treatment & Recovery Monitoring",
     "desc": "Care is delivered safely, with progress tracked throughout your recovery."},
]


# Dummy verified Google-style patient reviews (UAE names). Edit freely.
PATIENT_REVIEWS = [
    {"name": "Ahmed Al Mansoori", "initial": "A", "time": "2 weeks ago",
     "text": "From my first consultation the team was thorough and reassuring. The "
             "regenerative plan was explained clearly and my recovery has been remarkable."},
    {"name": "Fatima Al Zaabi", "initial": "F", "time": "3 weeks ago",
     "text": "Exceptional, science-led care. The specialists genuinely listened and the "
             "results have exceeded my expectations. Highly recommended."},
    {"name": "Omar Al Nuaimi", "initial": "O", "time": "1 month ago",
     "text": "A truly premium clinical experience — spotless facilities, advanced "
             "diagnostics and a dedicated team that supported me throughout."},
    {"name": "Layla Al Suwaidi", "initial": "L", "time": "1 month ago",
     "text": "Professional and compassionate from start to finish. I felt in safe, "
             "expert hands during every stage of my treatment."},
    {"name": "Khalid Al Maktoum", "initial": "K", "time": "2 months ago",
     "text": "The consultants are world-class. Clear communication, honest advice and "
             "a treatment plan tailored precisely to my needs."},
    {"name": "Mariam Al Qassimi", "initial": "M", "time": "2 months ago",
     "text": "Outstanding regenerative care. The follow-up and recovery monitoring made "
             "a real difference to my results. Thank you to the whole team."},
    {"name": "Yousef Al Hashimi", "initial": "Y", "time": "3 months ago",
     "text": "State-of-the-art clinic with genuinely caring staff. Booking was simple "
             "and the entire experience felt calm and premium."},
    {"name": "Noura Al Falasi", "initial": "N", "time": "4 months ago",
     "text": "Highly skilled specialists and a warm, welcoming environment. I would "
             "confidently recommend them to family and friends."},
]

# Dummy services for the appointment dropdown (edit freely).
BOOKING_SERVICES = [
    "Regenerative Wellness",
    "Regenerative Medicine",
    "Longevity & Healthspan",
    "Anti-Aging & Aesthetics",
    "Advanced Diagnostics",
    "Stem Cell Therapy Consultation",
]


# Dummy UAE clinic network — used by the "Medical Network" map section.
# top/left are percentage positions on the stylised UAE map. Edit freely.
NETWORK_LOCATIONS = [
    {"city": "Abu Dhabi", "name": "Brockwell Abu Dhabi", "icon": "stethoscope",
     "desc": "Flagship regenerative medicine & diagnostics centre.", "top": "60%", "left": "27%"},
    {"city": "Dubai", "name": "Brockwell Dubai", "icon": "plus",
     "desc": "Advanced stem cell therapy & consultation hub.", "top": "42%", "left": "60%"},
    {"city": "Sharjah", "name": "Brockwell Sharjah", "icon": "shield",
     "desc": "Clinical evaluation & patient support.", "top": "36%", "left": "67%"},
    {"city": "Ajman", "name": "Brockwell Ajman", "icon": "microscope",
     "desc": "Longevity & advanced diagnostics clinic.", "top": "31%", "left": "72%"},
    {"city": "Ras Al Khaimah", "name": "Brockwell RAK", "icon": "heart",
     "desc": "Regenerative treatment & recovery care.", "top": "22%", "left": "81%"},
]
NETWORK_FEATURES = [
    "Consultation & Planning Support",
    "International Patient Assistance",
    "Clinical Evaluation Services",
    "Regenerative Treatment Access",
]


# Dummy blog/news articles for the "Recent Articles" section. Edit freely; add
# an "image" static URL to any item to show a photo instead of the icon.
NEWS_ARTICLES = [
    {"category": "Regenerative Medicine", "icon": "dna", "image": "",
     "date": "Jan 30, 2026", "comments": 4,
     "title": "Advances in regenerative medicine for modern treatment",
     "desc": "How the latest cellular therapies are reshaping long-term patient outcomes."},
    {"category": "Stem Cell Therapy", "icon": "leaf", "image": "",
     "date": "Jan 24, 2026", "comments": 6,
     "title": "How stem cell therapy is transforming patient recovery",
     "desc": "A closer look at evidence-based protocols improving recovery and mobility."},
    {"category": "Clinical Research", "icon": "microscope", "image": "",
     "date": "Jan 18, 2026", "comments": 3,
     "title": "What new clinical research means for regenerative care",
     "desc": "Translating emerging studies into safe, personalised treatment plans."},
]


def _facilities_with_images():
    """Show a photo in the circle if a matching file exists, else the icon.
    Drop images into static/img named facility-1 … facility-7 (webp/jpg/png)."""
    out = []
    for i, f in enumerate(FACILITIES, start=1):
        image = ""
        for ext in ("webp", "jpg", "jpeg", "png"):
            path = f"img/facility-{i}.{ext}"
            if finders.find(path):
                image = path
                break
        out.append({**f, "image": image})
    return out


def _partners_with_logos():
    """Only reference a logo file if it actually exists (avoids a manifest
    error in production for logos that haven't been uploaded yet)."""
    out = []
    for p in ABOUT_PARTNERS:
        logo = p["logo"] if finders.find(p["logo"]) else ""
        out.append({**p, "logo": logo})
    return out


# Dummy facilities for the interactive "What Facilities We Provided" tabs.
# Add an "image" static URL to any item to show a photo in the circle instead
# of the icon placeholder.
FACILITIES = [
    {"title": "Regenerative Wellness", "icon": "leaf", "image": "",
     "desc": "Our personalised, science-led wellness programmes are designed to restore vitality and "
             "support your body’s natural ability to heal. Every plan is built around your unique health "
             "profile, so you receive care that is proactive, measurable and genuinely effective."},
    {"title": "Stem Cell Therapy", "icon": "dna", "image": "",
     "desc": "We deliver advanced regenerative treatments using safe, evidence-based cellular therapies. "
             "From joint and tissue repair to overall recovery, our specialists focus on lasting results "
             "and a treatment journey that is comfortable and reassuring."},
    {"title": "Advanced Diagnostics", "icon": "microscope", "image": "",
     "desc": "Precise imaging and comprehensive laboratory analysis let us map your health in detail and "
             "guide every treatment decision. This diagnostic clarity means your care is always targeted, "
             "personalised and grounded in real data."},
    {"title": "Longevity & Healthspan", "icon": "clock", "image": "",
     "desc": "Our proactive, preventive care is designed to extend your healthy, active years and slow "
             "biological ageing. We combine testing, nutrition and lifestyle guidance into one clear plan "
             "focused on long-term wellbeing."},
    {"title": "Aesthetic Medicine", "icon": "sparkles", "image": "",
     "desc": "We offer natural, regenerative aesthetic treatments that rejuvenate the skin from within. "
             "By stimulating your body’s own renewal processes, we help you look refreshed and confident "
             "without an overdone appearance."},
    {"title": "Cellular Recovery", "icon": "heart", "image": "",
     "desc": "Our attentive recovery and rehabilitation support helps you heal safely and confidently. "
             "A dedicated team guides every stage of your recovery, managing comfort and mobility so you "
             "can return to the life you love."},
    {"title": "Specialist Consultation", "icon": "stethoscope", "image": "",
     "desc": "Every journey begins with honest, one-to-one guidance from experienced clinicians. We take "
             "the time to understand your history and goals, then design a personalised treatment plan "
             "with a care team dedicated to your outcome."},
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
            "about_partners": _partners_with_logos(),
            "impact_stats": IMPACT_STATS,
            "process_steps": PROCESS_STEPS,
            "patient_reviews": PATIENT_REVIEWS,
            "booking_services": BOOKING_SERVICES,
            "facilities": _facilities_with_images(),
            "network_locations": NETWORK_LOCATIONS,
            "network_features": NETWORK_FEATURES,
            "news_articles": NEWS_ARTICLES,
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
    if settings.SITE_NOINDEX:
        # De-indexed mode: keep crawling ALLOWED so bots can read the site-wide
        # `noindex` directive (meta + X-Robots-Tag) and drop pages from their
        # index. Blocking here instead would leave already-indexed URLs stuck.
        # The sitemap is withheld so we don't actively invite indexing.
        lines = [
            "# Site is temporarily de-indexed (noindex in effect).",
            "User-agent: *",
            "Allow: /",
            "Disallow: /admin/",
        ]
        return _text_response("\n".join(lines))

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
