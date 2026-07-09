"""Build the USA site by cloning every published UAE content record into the
``us`` region, adapting location wording (Dubai → Philadelphia, UAE → US, DHA →
state medical board). Design, templates, features, images and slugs stay identical
— only the region-scoped content differs. Idempotent: re-running updates the US
copies in place. Reverse deletes all US content.

Images resolve by slug and are shared, so US pages reuse the same hero/content/og
images automatically. FAQs (via contenttypes) are copied too.
"""

import re

from django.db import migrations

# Location wording adaptation. Order matters (specific → general).
_SUBS = [
    (re.compile(r"United Arab Emirates"), "United States"),
    (re.compile(r"Dubai Health Authority"), "the state medical board"),
    (re.compile(r"\bDHA[- ]lic\w*", re.I), "state-licensed"),
    (re.compile(r"\bDHA\b"), "state medical board"),
    (re.compile(r"\bin the UAE\b"), "in the US"),
    (re.compile(r"\bacross the UAE\b"), "across the US"),
    (re.compile(r"\bthe UAE\b"), "the US"),
    (re.compile(r"\bUAE\b"), "US"),
    (re.compile(r"Dubai['’]s"), "Philadelphia's"),
    (re.compile(r"\bDubai\b"), "Philadelphia"),
    (re.compile(r"\bEmirates\b"), "United States"),
]


def adapt(text):
    if not text:
        return text
    for rx, rep in _SUBS:
        text = rx.sub(rep, text)
    return text


def _clone(obj, exclude, adapt_fields):
    """Return a defaults dict of an object's concrete fields (minus ``exclude``),
    with ``adapt_fields`` run through the location adapter."""
    data = {}
    for f in obj._meta.local_concrete_fields:
        if f.primary_key or f.name in exclude:
            continue
        val = getattr(obj, f.attname)
        if f.name in adapt_fields and isinstance(val, str):
            val = adapt(val)
        data[f.attname] = val
    return data


def build_us(apps, schema_editor):
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    Service = apps.get_model("services", "Service")
    Doctor = apps.get_model("team", "Doctor")
    Page = apps.get_model("core", "Page")
    BlogCategory = apps.get_model("blog", "BlogCategory")
    BlogPost = apps.get_model("blog", "BlogPost")
    Event = apps.get_model("events", "Event")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    # ---- Service categories ----
    cat_adapt = {"hero_heading", "summary", "description", "seo_title", "seo_description"}
    us_cats = {}
    for cat in ServiceCategory.objects.filter(region="uae"):
        defaults = _clone(cat, exclude={"region", "slug"}, adapt_fields=cat_adapt)
        obj, _ = ServiceCategory.objects.update_or_create(
            region="us", slug=cat.slug, defaults=defaults
        )
        us_cats[cat.slug] = obj

    # ---- Services (two passes for the self parent FK) ----
    svc_adapt = {"hero_heading", "summary", "description", "benefits",
                 "seo_title", "seo_description"}
    us_svcs = {}
    for svc in Service.objects.filter(region="uae"):
        defaults = _clone(
            svc, exclude={"region", "slug", "category", "parent"}, adapt_fields=svc_adapt
        )
        defaults["category"] = us_cats.get(svc.category.slug) if svc.category_id else None
        obj, _ = Service.objects.update_or_create(
            region="us", slug=svc.slug, defaults=defaults
        )
        us_svcs[svc.slug] = (obj, svc.parent.slug if svc.parent_id else None)
    for slug, (obj, parent_slug) in us_svcs.items():
        parent = us_svcs[parent_slug][0] if parent_slug and parent_slug in us_svcs else None
        if obj.parent_id != (parent.id if parent else None):
            obj.parent = parent
            obj.save(update_fields=["parent"])

    # ---- Doctors ----
    doc_adapt = {"title", "credentials", "experience", "short_bio", "full_bio",
                 "seo_title", "seo_description"}
    for d in Doctor.objects.filter(region="uae"):
        defaults = _clone(d, exclude={"region", "slug"}, adapt_fields=doc_adapt)
        Doctor.objects.update_or_create(region="us", slug=d.slug, defaults=defaults)

    # ---- Pages (legal etc.) ----
    page_adapt = {"title", "body", "seo_title", "seo_description"}
    for p in Page.objects.filter(region="uae"):
        defaults = _clone(p, exclude={"region", "slug"}, adapt_fields=page_adapt)
        Page.objects.update_or_create(region="us", slug=p.slug, defaults=defaults)

    # ---- Blog categories then posts ----
    us_blogcats = {}
    for bc in BlogCategory.objects.filter(region="uae"):
        defaults = _clone(bc, exclude={"region", "slug"}, adapt_fields={"description"})
        obj, _ = BlogCategory.objects.update_or_create(
            region="us", slug=bc.slug, defaults=defaults
        )
        us_blogcats[bc.slug] = obj
    post_adapt = {"title", "excerpt", "body", "seo_title", "seo_description"}
    for post in BlogPost.objects.filter(region="uae"):
        defaults = _clone(
            post, exclude={"region", "slug", "category"}, adapt_fields=post_adapt
        )
        defaults["category"] = (
            us_blogcats.get(post.category.slug) if post.category_id else None
        )
        BlogPost.objects.update_or_create(region="us", slug=post.slug, defaults=defaults)

    # ---- Events ----
    ev_adapt = {"title", "summary", "description", "location", "seo_title", "seo_description"}
    for e in Event.objects.filter(region="uae"):
        defaults = _clone(e, exclude={"region", "slug"}, adapt_fields=ev_adapt)
        Event.objects.update_or_create(region="us", slug=e.slug, defaults=defaults)

    # ---- FAQs (contenttypes) for US categories and services ----
    ct_cat, _ = ContentType.objects.get_or_create(
        app_label="services", model="servicecategory"
    )
    ct_svc, _ = ContentType.objects.get_or_create(app_label="services", model="service")

    def copy_faqs(ct, uae_obj, us_obj):
        FAQItem.objects.filter(content_type=ct, object_id=us_obj.id).delete()
        for faq in FAQItem.objects.filter(content_type=ct, object_id=uae_obj.id):
            FAQItem.objects.create(
                content_type=ct, object_id=us_obj.id,
                question=adapt(faq.question), answer=adapt(faq.answer),
                order=faq.order, is_published=faq.is_published,
            )

    for cat in ServiceCategory.objects.filter(region="uae"):
        if cat.slug in us_cats:
            copy_faqs(ct_cat, cat, us_cats[cat.slug])
    for svc in Service.objects.filter(region="uae"):
        if svc.slug in us_svcs:
            copy_faqs(ct_svc, svc, us_svcs[svc.slug][0])


def teardown_us(apps, schema_editor):
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    Service = apps.get_model("services", "Service")
    Doctor = apps.get_model("team", "Doctor")
    Page = apps.get_model("core", "Page")
    BlogCategory = apps.get_model("blog", "BlogCategory")
    BlogPost = apps.get_model("blog", "BlogPost")
    Event = apps.get_model("events", "Event")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    for label, model in [("servicecategory", ServiceCategory), ("service", Service)]:
        ct = ContentType.objects.filter(app_label="services", model=label).first()
        if ct:
            ids = list(model.objects.filter(region="us").values_list("id", flat=True))
            FAQItem.objects.filter(content_type=ct, object_id__in=ids).delete()
    for M in [Service, ServiceCategory, Doctor, Page, BlogPost, BlogCategory, Event]:
        M.objects.filter(region="us").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0115_biological_integrative_content_v2"),
        ("team", "0003_seed_real_doctors"),
        ("core", "0010_remove_oscar_tellez"),
        ("blog", "0004_alter_blogpost_custom_head"),
        ("events", "0002_event_image"),
    ]

    operations = [migrations.RunPython(build_us, teardown_us)]
