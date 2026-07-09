"""Re-adapt the US content to be location-light: strip the city entirely from the
copy, and let the country appear only once per page — in the hero/H1 heading
("… in the USA"). Everything else (body, sections, FAQs, SEO, alt text, doctor bios)
is rewritten location-free. Source of truth is the UAE content, re-cloned into the
existing US records. Idempotent; reverse is a no-op (0116's reverse removes US)."""

import re

from django.db import migrations

# --- Body adapter: remove the location, neutralise country references, add no
#     "USA" mention (that belongs only to the hero heading). ---
_BODY = [
    (re.compile(r"Dubai Health Authority"), "the state medical board"),
    (re.compile(r"\bDHA[- ]cert\w*", re.I), "state-certified"),
    (re.compile(r"\bDHA[- ]lic\w*", re.I), "state-licensed"),
    (re.compile(r"\bDHA\b"), "state medical board"),
    (re.compile(r"United Arab Emirates"), "the United States"),
    (re.compile(r"Brockwell Healthcare in Dubai"), "Brockwell Healthcare"),
    (re.compile(r"\s+Dubai consultation"), " consultation"),
    (re.compile(r"\bin Dubai\b"), ""),
    (re.compile(r"Dubai['’]s"), "our"),
    (re.compile(r"\bDubai\b"), ""),
    (re.compile(r"\bacross the UAE\b"), "nationwide"),
    (re.compile(r"\bin the UAE\b"), "nationwide"),
    (re.compile(r"\bthe UAE\b"), "the country"),
    (re.compile(r"\bUAE\b"), "the US"),
    (re.compile(r"\bEmirates\b"), "the country"),
]
# Tidy up artefacts left by the removals.
_TIDY = [
    (re.compile(r" +([.,;:!?])"), r"\1"),
    (re.compile(r"\(\s+"), "("),
    (re.compile(r"\s+\)"), ")"),
    (re.compile(r"[ \t]{2,}"), " "),
    (re.compile(r"\|\s*\|"), "|"),
    (re.compile(r"\s+\|"), " |"),
]


def adapt_body(text):
    if not text:
        return text
    for rx, rep in _BODY:
        text = rx.sub(rep, text)
    for rx, rep in _TIDY:
        text = rx.sub(rep, text)
    return text


def adapt_hero(text):
    """The single country mention lives here: '… in Dubai' -> '… in the USA'."""
    if not text:
        return text
    text = re.sub(r"\bin Dubai\b", "in the USA", text)
    text = re.sub(r"\bDubai\b", "the USA", text)
    text = re.sub(r"\bUAE\b", "USA", text)
    return text


def _apply(us_obj, uae_obj, body_fields, hero_fields):
    changed = []
    for f in body_fields:
        val = getattr(uae_obj, f, None)
        if isinstance(val, str):
            setattr(us_obj, f, adapt_body(val))
            changed.append(f)
    for f in hero_fields:
        val = getattr(uae_obj, f, None)
        if isinstance(val, str):
            setattr(us_obj, f, adapt_hero(val))
            changed.append(f)
    if changed:
        us_obj.save(update_fields=changed)


def relight(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    Doctor = apps.get_model("team", "Doctor")
    Page = apps.get_model("core", "Page")
    BlogPost = apps.get_model("blog", "BlogPost")
    BlogCategory = apps.get_model("blog", "BlogCategory")
    Event = apps.get_model("events", "Event")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    uae = lambda M, slug: M.objects.filter(region="uae", slug=slug).first()

    for cat in ServiceCategory.objects.filter(region="us"):
        src = uae(ServiceCategory, cat.slug)
        if src:
            _apply(cat, src,
                   ["summary", "description", "seo_title", "seo_description"],
                   ["hero_heading"])
    for svc in Service.objects.filter(region="us"):
        src = uae(Service, svc.slug)
        if src:
            _apply(svc, src,
                   ["summary", "description", "benefits", "seo_title", "seo_description"],
                   ["hero_heading"])
    for d in Doctor.objects.filter(region="us"):
        src = uae(Doctor, d.slug)
        if src:
            _apply(d, src,
                   ["title", "credentials", "experience", "short_bio", "full_bio",
                    "seo_title", "seo_description"], [])
    for p in Page.objects.filter(region="us"):
        src = uae(Page, p.slug)
        if src:
            _apply(p, src, ["title", "body", "seo_title", "seo_description"], [])
    for bc in BlogCategory.objects.filter(region="us"):
        src = uae(BlogCategory, bc.slug)
        if src:
            _apply(bc, src, ["description"], [])
    for post in BlogPost.objects.filter(region="us"):
        src = uae(BlogPost, post.slug)
        if src:
            _apply(post, src,
                   ["excerpt", "body", "seo_title", "seo_description"], [])
    for e in Event.objects.filter(region="us"):
        src = uae(Event, e.slug)
        if src:
            _apply(e, src,
                   ["summary", "description", "location", "seo_title", "seo_description"], [])

    # FAQs: re-adapt from the UAE counterpart (body wording, no country mention).
    ct_cat = ContentType.objects.filter(app_label="services", model="servicecategory").first()
    ct_svc = ContentType.objects.filter(app_label="services", model="service").first()

    def relight_faqs(ct, Model):
        if not ct:
            return
        for us_obj in Model.objects.filter(region="us"):
            src = uae(Model, us_obj.slug)
            if not src:
                continue
            src_faqs = list(FAQItem.objects.filter(content_type=ct, object_id=src.id).order_by("order"))
            us_faqs = list(FAQItem.objects.filter(content_type=ct, object_id=us_obj.id).order_by("order"))
            for uf, sf in zip(us_faqs, src_faqs):
                uf.question = adapt_body(sf.question)
                uf.answer = adapt_body(sf.answer)
                uf.save(update_fields=["question", "answer"])

    relight_faqs(ct_cat, ServiceCategory)
    relight_faqs(ct_svc, Service)


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0116_clone_uae_to_us"),
    ]

    operations = [migrations.RunPython(relight, migrations.RunPython.noop)]
