from django.conf import settings
from django.contrib import messages
from django.contrib.staticfiles import finders
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from core import emails, seo
from core.forms import ContactForm
from core.regions import region_asset_rel, region_path

from .models import Service, ServiceCategory


def _hero_image_for(slug, region_code):
    """Per-service hero background, region-aware: the region's own
    ``img/<code>/services/<slug>-hero.webp`` if present, else the shared file."""
    return region_asset_rel(region_code, f"services/{slug}-hero.webp")


def _category_hero_image(slug, region_code):
    """Per-category hero background, region-aware (falls back to the shared file)."""
    return region_asset_rel(region_code, f"services/categories/{slug}/hero.webp")


def _service_og_image(service, region_code):
    """Region-aware 1200x630 JPEG social-share card for a service page. JPEG so
    WhatsApp/Facebook/X actually render the preview. None → build_meta default."""
    return region_asset_rel(region_code, f"og/svc-{service.slug}.jpg")


def _category_og_image(slug, region_code):
    """Region-aware 1200x630 JPEG social-share card for a category page."""
    return region_asset_rel(region_code, f"og/cat-{slug}.jpg")


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
        request, title=title, description=description, path=f"/services/{cat.slug}/",
        image=_category_og_image(cat.slug, region['code']),
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
         "faqs": faqs, "hero_image": _category_hero_image(cat.slug, region["code"])},
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
    ajax = request.headers.get("x-requested-with") == "XMLHttpRequest"
    form = ContactForm(request.POST or None, region=region)
    if request.method == "POST" and form.is_valid():
        if not form.is_spam():
            lead = form.save(commit=False)
            lead.region = region["code"]
            if not lead.subject:
                lead.subject = f"Booking enquiry: {service.name}"
            lead.save()
            emails.contact_lead(lead)
        thanks = "Thank you — your booking request has been received. Our team will contact you shortly."
        if ajax:
            return JsonResponse({"ok": True, "level": "success", "message": thanks})
        messages.success(request, thanks)
        return redirect(service.get_absolute_url())

    if request.method == "POST" and ajax:
        return JsonResponse(
            {"ok": False, "level": "error", "message": "Please check the form and try again."}
        )

    if parent_service:
        path = f"/services/{cat.slug}/{parent_service.slug}/{service.slug}/"
    else:
        path = f"/services/{cat.slug}/{service.slug}/"

    title = service.seo_title or f"{service.name} in {region['name']}"
    description = service.seo_description or service.summary
    meta = seo.build_meta(
        request, title=title, description=description, path=path, og_type="article",
        image=_service_og_image(service, region['code']),
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
            "hero_image": _hero_image_for(service.slug, region["code"]),
        },
    )
