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
from core.sitemaps import sitemaps
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path("admin/", admin.site.urls),
    # Serve user-uploaded media (e.g. service card images). Kept lightweight so
    # it works under cPanel/Passenger where WhiteNoise only handles static.
    re_path(
        r"^%s(?P<path>.*)$" % re.escape(settings.MEDIA_URL.lstrip("/")),
        media_serve,
        {"document_root": settings.MEDIA_ROOT},
    ),
    # Technical SEO endpoints (region-exempt).
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("robots.txt", core_views.robots_txt, name="robots"),
    path("llms.txt", core_views.llms_txt, name="llms"),
    path("healthz", core_views.healthz, name="healthz"),
    # Stripe calls this directly, without a region prefix.
    path("stripe/webhook/", include("payments.webhook_urls")),
    # Region-routed apps (top-level namespaces; the region prefix is stripped
    # by RegionMiddleware before resolution).
    path("services/", include("services.urls")),
    path("events/", include("events.urls")),
    path("team/", include("team.urls")),
    path("blog/", include("blog.urls")),
    path("checkout/", include("payments.urls")),
    path("", include("core.urls")),
]

handler404 = "core.views.error_404"
handler500 = "core.views.error_500"
