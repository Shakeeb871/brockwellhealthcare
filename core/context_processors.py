"""Expose brand, region and SEO defaults to every template."""

from django.conf import settings

from .regions import enabled_regions, get_region


def site_context(request):
    region_code = getattr(request, "region_code", settings.DEFAULT_REGION)
    region = getattr(request, "region", None) or get_region(region_code)

    return {
        "BRAND_NAME": settings.BRAND_NAME,
        "BRAND_TAGLINE": settings.BRAND_TAGLINE,
        "SITE_DOMAIN": settings.SITE_DOMAIN,
        "region": region,
        "region_code": region_code,
        "enabled_regions": enabled_regions(),
        "STRIPE_PUBLISHABLE_KEY": settings.STRIPE_PUBLISHABLE_KEY,
        "DEFAULT_OG_IMAGE": settings.DEFAULT_OG_IMAGE,
    }
