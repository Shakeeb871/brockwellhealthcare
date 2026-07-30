"""Root URL configuration.

Region prefixes (``/uae/``, ``/us/``) are handled by ``RegionMiddleware``,
which strips the prefix before resolution — so the app URLconfs below are
written WITHOUT the region segment. Infrastructure routes (admin, sitemap,
robots, llms, the Stripe webhook) are region-exempt.
"""

import re

from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve as media_serve

from core import views as core_views
from core.region_admin import build_region_admin_sites
from core.sitemaps import non_empty_sitemaps, sitemaps, sitemaps_for_region
from django.contrib.sitemaps.views import index as sitemap_index, sitemap
from django.http import Http404


def sitemap_index_view(request):
    """Master sitemap index — every populated section, across all countries."""
    return sitemap_index(
        request, non_empty_sitemaps(), sitemap_url_name="sitemap-section"
    )


def sitemap_country_view(request, country):
    """Per-country sitemap index, e.g. /sitemap-uae.xml.

    Lists only that market's section sitemaps, so each country can be
    submitted and tracked separately in Search Console. Still a single level
    of nesting (index -> sitemaps), which is what search engines support.
    """
    live = sitemaps_for_region(country)
    if not live:
        raise Http404("No indexable sitemaps for this region")
    return sitemap_index(request, live, sitemap_url_name="sitemap-section")


# Country codes for the per-country index route, e.g. "uae|us". Kept ahead of
# the generic section route so /sitemap-uae.xml resolves to the country index
# while /sitemap-uae-services.xml resolves to the section sitemap.
_COUNTRY_RE = "|".join(re.escape(code) for code in settings.REGIONS)

# Per-region admin panels at /admin/<code>/ (generated from settings.REGIONS).
# Must be listed BEFORE the master /admin/ so the more specific paths win.
region_admin_sites = build_region_admin_sites()

urlpatterns = [
    *[path(f"admin/{code}/", site.urls) for code, site in region_admin_sites.items()],
    path("admin/", admin.site.urls),
    # Rich-text editor assets/config (region-exempt).
    path("tinymce/", include("tinymce.urls")),
    # Serve user-uploaded media (e.g. service card images). Kept lightweight so
    # it works under cPanel/Passenger where WhiteNoise only handles static.
    re_path(
        r"^%s(?P<path>.*)$" % re.escape(settings.MEDIA_URL.lstrip("/")),
        media_serve,
        {"document_root": settings.MEDIA_ROOT},
    ),
    # Technical SEO endpoints (region-exempt).
    # /sitemap.xml            master index — every populated section
    # /sitemap-<country>.xml  per-country index (submit these per market)
    # /sitemap-<country>-<section>.xml  the actual URL sitemaps
    path("sitemap.xml", sitemap_index_view, name="sitemap"),
    re_path(
        rf"^sitemap-(?P<country>{_COUNTRY_RE})\.xml$",
        sitemap_country_view, name="sitemap-country",
    ),
    path(
        "sitemap-<section>.xml", sitemap,
        {"sitemaps": sitemaps}, name="sitemap-section",
    ),
    path("robots.txt", core_views.robots_txt, name="robots"),
    path("llms.txt", core_views.llms_txt, name="llms"),
    path("healthz", core_views.healthz, name="healthz"),
    # Browsers request /favicon.ico on their own, whatever the <link> tags say,
    # so without this every visit logged a 404. RegionMiddleware already treats
    # the path as region-exempt; only the route was missing.
    path("favicon.ico", core_views.favicon_ico, name="favicon"),
    # Web app manifest. The CSP already allows `manifest-src 'self'`, and the
    # theme-color meta and 192px icon were both in place — this was the only
    # missing piece.
    path("site.webmanifest", core_views.site_webmanifest, name="webmanifest"),
    # IndexNow verification file — must be reachable at /<key>.txt.
    re_path(r"^(?P<key>[A-Za-z0-9-]{8,128})\.txt$", core_views.indexnow_key, name="indexnow-key"),
    # Stripe calls this directly, without a region prefix.
    path("stripe/webhook/", include("payments.webhook_urls")),
    # Region-routed apps (top-level namespaces; the region prefix is stripped
    # by RegionMiddleware before resolution).
    path("services/", include("services.urls")),
    path("events/", include("events.urls")),
    path("locations/", include("locations.urls")),
    path("team/", include("team.urls")),
    path("blog/", include("blog.urls")),
    path("checkout/", include("payments.urls")),
    path("", include("core.urls")),
]

handler404 = "core.views.error_404"
handler500 = "core.views.error_500"
