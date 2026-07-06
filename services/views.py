from django.conf import settings
from django.contrib import messages
from django.contrib.staticfiles import finders
from django.shortcuts import get_object_or_404, redirect, render

from core import seo
from core.forms import ContactForm
from core.regions import region_path

from .models import Service, ServiceCategory


def _hero_image_for(slug):
    """Per-service hero background: static img/services/<slug>-hero.webp if present."""
    rel = f"img/services/{slug}-hero.webp"
    return rel if finders.find(rel) else None


def _category_hero_image(slug):
    """Per-category hero background: static img/services/categories/<slug>/hero.webp
    if present — else None so the shared default hero image is used."""
    rel = f"img/services/categories/{slug}/hero.webp"
    return rel if finders.find(rel) else None


def service_overview(request):
    region = request.region
    categories = (
        ServiceCategory.objects.filter(region=region["code"], is_published=True)
        .prefetch_related("services")
    )

    meta = seo.build_meta(
        request,
        title=f"Our Services in {region['name']}",
        description=(
            f"Explore regenerative wellness, regenerative medicine, longevity, anti-aging "
            f"aesthetics and advanced diagnostics at {settings.BRAND_NAME} in {region['name']}."
        ),
        path="/services/",
    )
    crumbs = seo.breadcrumb_schema(
        [
            ("Home", seo.absolute(region_path(region["code"], "core:home"))),
            ("Services", meta["canonical"]),
        ]
    )
    return render(
        request,
        "services/list.html",
        {"meta": meta, "jsonld": [crumbs], "categories": categories},
    )


def category_detail(request, category):
    region = request.region
    cat = get_object_or_404(
        ServiceCategory, region=region["code"], slug=category, is_published=True
    )
    services = cat.services.filter(is_published=True, parent__isnull=True)

    title = cat.seo_title or f"{cat.name} in {region['name']}"
    description = cat.seo_description or cat.summary
    meta = seo.build_meta(
        request, title=title, description=description, path=f"/services/{cat.slug}/"
    )
    jsonld = [
        seo.category_schema(cat, region),
        seo.breadcrumb_schema(
            [
                ("Home", seo.absolute(region_path(region["code"], "core:home"))),
                ("Services", seo.absolute(region_path(region["code"], "services:list"))),
                (cat.name, meta["canonical"]),
            ]
        ),
    ]
    faqs = list(cat.faqs.filter(is_published=True))
    faq_ld = seo.faq_schema(faqs)
    if faq_ld:
        jsonld.append(faq_ld)
    return render(
        request,
        "services/category.html",
        {"meta": meta, "jsonld": jsonld, "category": cat, "services": services,
         "faqs": faqs, "hero_image": _category_hero_image(cat.slug)},
    )


def service_detail(request, category, slug, parent=None):
    region = request.region
    cat = get_object_or_404(
        ServiceCategory, region=region["code"], slug=category, is_published=True
    )
    parent_service = None
    if parent:
        parent_service = get_object_or_404(
            Service, region=region["code"], category=cat, slug=parent,
            parent__isnull=True, is_published=True,
        )
        service = get_object_or_404(
            Service, region=region["code"], category=cat, slug=slug,
            parent=parent_service, is_published=True,
        )
    else:
        service = get_object_or_404(
            Service, region=region["code"], category=cat, slug=slug,
            parent__isnull=True, is_published=True,
        )

    # Sidebar booking form — saves an enquiry tagged with this service.
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        if not form.is_spam():
            lead = form.save(commit=False)
            lead.region = region["code"]
            if not lead.subject:
                lead.subject = f"Booking enquiry: {service.name}"
            lead.save()
        messages.success(
            request,
            "Thank you — your booking request has been received. Our team will contact you shortly.",
        )
        return redirect(service.get_absolute_url())

    if parent_service:
        path = f"/services/{cat.slug}/{parent_service.slug}/{service.slug}/"
    else:
        path = f"/services/{cat.slug}/{service.slug}/"

    title = service.seo_title or f"{service.name} in {region['name']}"
    description = service.seo_description or service.summary
    meta = seo.build_meta(
        request, title=title, description=description, path=path, og_type="article",
    )
    crumbs = [
        ("Home", seo.absolute(region_path(region["code"], "core:home"))),
        ("Services", seo.absolute(region_path(region["code"], "services:list"))),
        (cat.name, seo.absolute(region_path(region["code"], "services:category", category=cat.slug))),
    ]
    if parent_service:
        crumbs.append((parent_service.name, seo.absolute(parent_service.get_absolute_url())))
    crumbs.append((service.name, meta["canonical"]))
    jsonld = [
        seo.service_schema(service, region),
        seo.breadcrumb_schema(crumbs),
    ]
    faqs = list(service.faqs.filter(is_published=True))
    faq_ld = seo.faq_schema(faqs)
    if faq_ld:
        jsonld.append(faq_ld)

    children = list(service.published_children)

    return render(
        request,
        "services/detail.html",
        {
            "meta": meta,
            "jsonld": jsonld,
            "category": cat,
            "service": service,
            "parent_service": parent_service,
            "children": children,
            "form": form,
            "faqs": faqs,
            "hero_image": _hero_image_for(service.slug),
        },
    )
