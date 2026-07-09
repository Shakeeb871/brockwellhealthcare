from django.conf import settings
from django.contrib import messages
from django.contrib.staticfiles import finders
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from django.http import Http404
from django.db.models import Q

from blog.models import BlogPost
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
    {"icon": "users", "text": "Board-certified specialists guide every stage of your care."},
    {"icon": "leaf", "text": "Advanced, non-surgical regenerative treatments."},
    {"icon": "shield", "text": "Every recommendation held to real clinical evidence."},
]
# About stat circles. `num`/`suffix` are shown as-is; `ring` is the decorative
# arc fill (0–100, visual only — these aren't percentages).
ABOUT_STATS = [
    {"num": "15,000", "suffix": "+", "ring": 96, "label": "Patients Treated"},
    {"num": "25", "suffix": "+", "ring": 80, "label": "Years of Experience"},
    {"num": "4.91", "suffix": "", "suffix_icon": "star", "ring": 98, "label": "Google Rating"},
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
    {"icon": "users", "value": 50, "decimals": 0, "suffix": "+", "ring": 80, "label": "Expert Specialists"},
    {"icon": "heart", "value": 98, "decimals": 0, "suffix": "%", "ring": 98, "label": "Patient Satisfaction"},
    {"icon": "capsule", "value": 12, "decimals": 0, "suffix": "+", "ring": 70, "label": "Regenerative & Wellness Therapies"},
    {"icon": "leaf", "value": 6, "decimals": 0, "suffix": "", "ring": 60, "label": "Core Service Areas"},
    {"icon": "pin", "value": 7, "decimals": 0, "suffix": "", "ring": 90, "label": "Emirates Served"},
]


# Dummy steps for the "Care Journey" process section. Reusable/scalable —
# add 4 to 8 items; numbers are generated automatically in the template.
PROCESS_STEPS = [
    {"icon": "stethoscope", "title": "Consultation",
     "desc": "We start by understanding your symptoms, medical history, lifestyle and what you want to improve."},
    {"icon": "microscope", "title": "Diagnostics & Clinical Review",
     "desc": "Where needed, we recommend testing or imaging to confirm what is driving the problem before treatment begins."},
    {"icon": "clipboard", "title": "Personalised Treatment Plan",
     "desc": "We build your plan around your condition, your safety and the outcomes you can realistically expect."},
    {"icon": "syringe", "title": "Treatment",
     "desc": "This may be regenerative medicine, injection therapy, wellness support or a combination chosen for your case."},
    {"icon": "refresh", "title": "Follow-Up & Outcome Tracking",
     "desc": "We track your progress and adjust the plan, because real improvement rarely comes from a single visit."},
]


# "Why Choose Brockwell" — six differentiators shown on the home page.
WHY_CHOOSE = [
    {"icon": "stethoscope", "title": "Physician-led at every step",
     "desc": "A specialist assesses, plans and oversees your care from start to finish, so a qualified "
             "doctor guides every decision."},
    {"icon": "refresh", "title": "One coordinated clinical model",
     "desc": "Regenerative medicine, longevity, diagnostics and functional medicine work from a single plan, "
             "so your whole treatment stays connected and consistent."},
    {"icon": "cells", "title": "Treatments that work with your own biology",
     "desc": "Where clinically suitable, we use your body’s own cells and tissue to support natural repair. "
             "This keeps your care biologic, targeted and low-risk."},
    {"icon": "scan", "title": "Image-guided precision",
     "desc": "We carry out many injections and procedures under ultrasound guidance, so each treatment "
             "reaches its precise target, safely and accurately."},
    {"icon": "chat", "title": "Honest, realistic guidance",
     "desc": "We explain what may help, what may not suit you and what results are reasonable to expect. If "
             "regenerative medicine is not right for you, we tell you clearly."},
    {"icon": "shield", "title": "Safety-gated and evidence-based",
     "desc": "Every therapy follows a clinical assessment and sound medical judgement. We refer emergencies "
             "and cases that need surgery to the right specialist service."},
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
    {"city": "Abu Dhabi", "name": "Abu Dhabi", "icon": "pin",
     "desc": "Patients travel to our Dubai clinic; secure telehealth available.", "top": "60%", "left": "27%"},
    {"city": "Dubai", "name": "Brockwell Healthcare — Dubai", "icon": "pin",
     "desc": "In-person consultations, diagnostics & hands-on treatment.", "top": "42%", "left": "60%"},
    {"city": "Sharjah", "name": "Sharjah", "icon": "pin",
     "desc": "Served via our Dubai clinic and secure telehealth.", "top": "36%", "left": "67%"},
    {"city": "Ajman", "name": "Ajman", "icon": "pin",
     "desc": "Served via our Dubai clinic and secure telehealth.", "top": "31%", "left": "72%"},
    {"city": "Ras Al Khaimah", "name": "Ras Al Khaimah", "icon": "pin",
     "desc": "Served via our Dubai clinic and secure telehealth.", "top": "22%", "left": "81%"},
]
NETWORK_FEATURES = [
    "In-person consultations & treatment in Dubai",
    "Patients cared for across all seven emirates",
    "Secure telehealth available across the UAE",
    "Online follow-ups, prescription & non-emergency reviews",
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
    latest_posts = BlogPost.objects.filter(region=code, is_published=True).select_related("category")[:3]

    meta = seo.build_meta(
        request,
        title="Regenerative Medicine & Longevity Clinic Dubai | Brockwell",
        description=(
            "Brockwell Healthcare is a Dubai regenerative medicine and longevity clinic "
            "offering personalised, non-surgical care for pain, recovery and healthy ageing."
        ),
        path="/",
        image="img/og/default.jpg",
    )
    jsonld = [seo.medical_clinic_schema(region), seo.website_schema(region)]
    jsonld += [seo.category_schema(c, region) for c in categories]
    jsonld += [seo.doctor_schema(d, region) for d in doctors]
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
            "why_choose": WHY_CHOOSE,
            "patient_reviews": PATIENT_REVIEWS,
            "booking_services": BOOKING_SERVICES,
            "facilities": _facilities_with_images(),
            "network_locations": NETWORK_LOCATIONS,
            "network_features": NETWORK_FEATURES,
            "news_posts": latest_posts,
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
    faqs = list(obj.faqs.filter(is_published=True))
    faq_ld = seo.faq_schema(faqs)
    if faq_ld:
        jsonld.append(faq_ld)
    return render(request, "core/page.html", {"meta": meta, "jsonld": jsonld, "page": obj, "faqs": faqs})


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


# Specialists highlighted on the About page (name/role as approved; photo + URL
# pulled from the Doctor records by slug).
ABOUT_SPECIALISTS = [
    {"slug": "dr-adeel-khan-md", "name": "Dr. Adeel Khan", "role": "Regenerative Medicine & Longevity Physician"},
    {"slug": "shirley-dsouza", "name": "Dr. Shirley D’Souza", "role": "Precision Nutritionist"},
    {"slug": "dr-sabine-hazan-md", "name": "Dr. Sabine Hazan", "role": "Diagnostics Director"},
]


def about(request):
    region = request.region
    code = region["code"]
    meta = seo.build_meta(
        request,
        title=f"About {settings.BRAND_NAME} | Regenerative Medicine & Longevity Clinic Dubai",
        description=(
            "Brockwell Healthcare is a Dubai regenerative medicine and longevity clinic built on 25+ "
            "years of experience — doctor-led, root-cause, non-surgical care for pain, recovery and ageing."
        ),
        path="/about/",
        image="img/og/about.jpg",
    )
    crumbs = seo.breadcrumb_schema(
        [
            ("Home", seo.absolute(region_path(code, "core:home"))),
            ("About", meta["canonical"]),
        ]
    )

    categories = ServiceCategory.objects.filter(region=code, is_published=True)[:8]
    founder = Doctor.objects.filter(region=code, slug="dr-hasnain-haider-shah").first()
    docs = {d.slug: d for d in Doctor.objects.filter(
        region=code, slug__in=[s["slug"] for s in ABOUT_SPECIALISTS])}
    specialists = [
        {**s, "photo": getattr(docs.get(s["slug"]), "photo", ""),
         "url": docs[s["slug"]].get_absolute_url() if s["slug"] in docs else ""}
        for s in ABOUT_SPECIALISTS
    ]

    return render(
        request,
        "core/about.html",
        {
            "meta": meta,
            "jsonld": [crumbs, seo.organization_schema(region)],
            "categories": categories,
            "founder": founder,
            "specialists": specialists,
            "about_partners": _partners_with_logos(),
        },
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
