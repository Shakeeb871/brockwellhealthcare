from django.conf import settings
from django.shortcuts import get_object_or_404, render

from core import seo
from core.models import FAQ
from core.regions import region_path

from .models import Service


def service_list(request):
    region = request.region
    services = Service.objects.filter(region=region["code"], is_published=True)

    meta = seo.build_meta(
        request,
        title=f"Stem Cell & Regenerative Services in {region['name']}",
        description=(
            f"Explore stem cell therapies and regenerative treatments offered by "
            f"{settings.BRAND_NAME} in {region['name']} — personalised, evidence-based care."
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
        {"meta": meta, "jsonld": [crumbs], "services": services},
    )


def service_detail(request, slug):
    region = request.region
    service = get_object_or_404(
        Service, region=region["code"], slug=slug, is_published=True
    )
    others = Service.objects.filter(
        region=region["code"], is_published=True
    ).exclude(pk=service.pk)[:3]
    faqs = list(FAQ.objects.filter(region=region["code"], is_published=True)[:6])

    title = service.seo_title or f"{service.name} in {region['name']}"
    description = service.seo_description or service.summary
    meta = seo.build_meta(
        request,
        title=title,
        description=description,
        path=f"/services/{service.slug}/",
        og_type="article",
    )
    jsonld = [
        seo.service_schema(service, region),
        seo.breadcrumb_schema(
            [
                ("Home", seo.absolute(region_path(region["code"], "core:home"))),
                ("Services", seo.absolute(region_path(region["code"], "services:list"))),
                (service.name, meta["canonical"]),
            ]
        ),
    ]
    faq_ld = seo.faq_schema(faqs)
    if faq_ld:
        jsonld.append(faq_ld)

    return render(
        request,
        "services/detail.html",
        {
            "meta": meta,
            "jsonld": jsonld,
            "service": service,
            "others": others,
            "faqs": faqs,
        },
    )
