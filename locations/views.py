from collections import OrderedDict

from django.conf import settings
from django.shortcuts import get_object_or_404, render

from core import seo
from core.regions import region_path

from .models import Location


def location_list(request):
    """All clinics for the active region, grouped by state for local SEO."""
    region = request.region
    locations = (
        Location.objects.filter(region=region["code"], is_active=True)
        .prefetch_related("doctors")
    )

    # Group by state (keeps model order: primary first, then order, then city).
    groups = OrderedDict()
    for loc in locations:
        key = loc.state or "Other"
        groups.setdefault(key, []).append(loc)
    grouped = [{"state": state, "locations": locs} for state, locs in groups.items()]

    meta = seo.build_meta(
        request,
        title=f"Our Locations in {region['name']}",
        description=(
            f"Find a {settings.BRAND_NAME} regenerative medicine and longevity clinic "
            f"near you in {region['name']} — addresses, hours and specialists."
        ),
        path="/locations/",
    )
    jsonld = [
        seo.breadcrumb_schema(
            [
                ("Home", seo.absolute(region_path(region["code"], "core:home"))),
                ("Locations", meta["canonical"]),
            ]
        )
    ]
    jsonld += [seo.location_schema(loc, region) for loc in locations]

    return render(
        request,
        "locations/list.html",
        {"meta": meta, "jsonld": jsonld, "grouped": grouped, "total": len(locations)},
    )


def location_detail(request, slug):
    region = request.region
    location = get_object_or_404(
        Location, region=region["code"], slug=slug, is_active=True
    )
    doctors = location.published_doctors

    title = location.seo_title or f"{location.name} — Regenerative Medicine & Longevity"
    description = location.seo_description or location.intro or (
        f"{settings.BRAND_NAME} in {location.city} — {location.full_address}. "
        "Regenerative medicine, longevity and wellness care."
    )
    meta = seo.build_meta(
        request,
        title=title,
        description=description,
        path=f"/locations/{location.slug}/",
        image=location.hero.url if location.hero else None,
    )
    jsonld = [
        seo.location_schema(location, region),
        seo.breadcrumb_schema(
            [
                ("Home", seo.absolute(region_path(region["code"], "core:home"))),
                ("Locations", seo.absolute(region_path(region["code"], "locations:list"))),
                (location.city, meta["canonical"]),
            ]
        ),
    ]
    return render(
        request,
        "locations/detail.html",
        {"meta": meta, "jsonld": jsonld, "location": location, "doctors": doctors},
    )
