"""Expose brand, region, navigation and SEO defaults to every template."""

from django.conf import settings

from .regions import enabled_regions, get_region


def site_context(request):
    region_code = getattr(request, "region_code", settings.DEFAULT_REGION)
    region = getattr(request, "region", None) or get_region(region_code)

    # Service categories (with their sub-services) power the header mega-menu.
    # Imported lazily to avoid app-loading issues and keep this light.
    nav_categories = []
    try:
        from services.models import ServiceCategory

        nav_categories = list(
            ServiceCategory.objects.filter(region=region_code, is_published=True)
            .prefetch_related("services")
        )
    except Exception:
        nav_categories = []

    return {
        "BRAND_NAME": settings.BRAND_NAME,
        "BRAND_TAGLINE": settings.BRAND_TAGLINE,
        "SITE_DOMAIN": settings.SITE_DOMAIN,
        "region": region,
        "region_code": region_code,
        "enabled_regions": enabled_regions(),
        "nav_categories": nav_categories,
        "STRIPE_PUBLISHABLE_KEY": settings.STRIPE_PUBLISHABLE_KEY,
        "DEFAULT_OG_IMAGE": settings.DEFAULT_OG_IMAGE,
        "SITE_NOINDEX": settings.SITE_NOINDEX,
    }
