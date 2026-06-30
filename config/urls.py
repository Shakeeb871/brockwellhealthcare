"""Root URL configuration.

Region prefixes (``/uae/``, ``/us/``) are handled by ``RegionMiddleware``,
which strips the prefix before resolution — so the app URLconfs below are
written WITHOUT the region segment. Infrastructure routes (admin, sitemap,
robots, llms, the Stripe webhook) are region-exempt.
"""

from django.contrib import admin
from django.urls import include, path

from core import views as core_views
from core.sitemaps import sitemaps
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path("admin/", admin.site.urls),
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
    path("checkout/", include("payments.urls")),
    path("", include("core.urls")),
]

handler404 = "core.views.error_404"
handler500 = "core.views.error_500"
