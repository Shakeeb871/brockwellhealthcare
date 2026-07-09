"""
Region helpers.

The site serves multiple geographic regions (UAE now, USA later) from a
single codebase under URL prefixes: ``/uae/...`` and ``/us/...``. These
helpers centralise the logic so views, templates, sitemaps and SEO tags
all agree on how region URLs are built.
"""

from django.conf import settings
from django.urls import reverse


def get_region(code: str) -> dict:
    """Return the configuration dict for a region code (falls back to default)."""
    return settings.REGIONS.get(code, settings.REGIONS[settings.DEFAULT_REGION])


# --------------------------------------------------------------------------- #
# Region-aware static assets
# --------------------------------------------------------------------------- #
# Every region can override any image by dropping it under ``static/img/<code>/``
# mirroring the shared layout. The resolver prefers that region-specific file and
# otherwise falls back to the shared ``static/img/…`` file — so nothing has to be
# duplicated, only the images a region wants to differ.

def region_asset_rel(region_code: str, tail: str):
    """Return the *static-relative* path of the best asset for a region, i.e.
    ``img/<code>/<tail>`` if it exists, else ``img/<tail>`` if it exists, else
    ``None``. ``tail`` is the path under ``img/`` e.g. ``services/x-hero.webp``."""
    from django.contrib.staticfiles import finders

    tail = tail.lstrip("/")
    if tail.startswith("img/"):
        tail = tail[4:]
    for candidate in (f"img/{region_code}/{tail}", f"img/{tail}"):
        if finders.find(candidate):
            return candidate
    return None


def region_asset(region_code: str, tail: str) -> str:
    """Full static URL for the best region asset, or "" if none exists."""
    from django.templatetags.static import static

    rel = region_asset_rel(region_code, tail)
    return static(rel) if rel else ""


def enabled_regions() -> list[dict]:
    """All regions currently switched on, in declaration order."""
    return [r for r in settings.REGIONS.values() if r.get("enabled")]


def is_enabled(code: str) -> bool:
    region = settings.REGIONS.get(code)
    return bool(region and region.get("enabled"))


def region_path(region_code: str, urlname: str, *args, **kwargs) -> str:
    """Reverse a URL name and prefix it with the region segment.

    The default region is served at the root (no prefix), so e.g. for the US
    default ``reverse('core:home')`` -> ``/`` stays ``/`` and ``/services/x/``
    stays ``/services/x/``; for the UAE it becomes ``/uae/`` and
    ``/uae/services/x/``.
    """
    base = reverse(urlname, args=args, kwargs=kwargs)
    return f"{region_prefix(region_code)}{base}"


def region_prefix(region_code: str) -> str:
    """URL prefix for a region: empty for the default region (served at the
    root), ``/<code>`` for every other region."""
    return "" if region_code == settings.DEFAULT_REGION else f"/{region_code}"


def region_absolute(region_code: str, urlname: str, *args, **kwargs) -> str:
    """Fully-qualified https URL for a region-prefixed route (for SEO tags)."""
    return f"https://{settings.SITE_DOMAIN}{region_path(region_code, urlname, *args, **kwargs)}"


def detect_region(request) -> str:
    """Best-effort detection of a visitor's region from edge/CDN headers.

    Falls back to the default region. Only returns regions that are enabled,
    so visitors are never sent to a region that is not live yet.
    """
    # Common country headers set by CDNs / proxies (Cloudflare, etc.).
    country = (
        request.META.get("HTTP_CF_IPCOUNTRY")
        or request.META.get("HTTP_X_VERCEL_IP_COUNTRY")
        or request.META.get("HTTP_X_COUNTRY_CODE")
        or ""
    ).lower()

    country_to_region = {"ae": "uae", "us": "us"}
    candidate = country_to_region.get(country)
    if candidate and is_enabled(candidate):
        return candidate
    return settings.DEFAULT_REGION
