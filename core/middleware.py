"""
RegionMiddleware — routes every request to the correct region.

Strategy
--------
* URLs are namespaced by region prefix: ``/uae/...`` (live) and ``/us/...``
  (reserved). The app URLconf itself is written WITHOUT the prefix; this
  middleware strips a valid region segment off ``path_info`` so the normal
  URL resolver matches clean paths, and records the active region on the
  request (``request.region`` / ``request.region_code``).
* A bare or un-prefixed path (e.g. ``/`` or ``/services/``) is redirected
  to the visitor's detected region so there is always exactly one canonical
  URL per page — important for SEO (no duplicate content).
* Infrastructure paths (admin, static, sitemap, robots, llms, webhooks) are
  exempt and pass straight through.
"""

from django.conf import settings
from django.shortcuts import redirect

from .regions import detect_region, get_region, is_enabled

# Paths that must never be region-prefixed.
EXEMPT_PREFIXES = ("/admin", "/static", "/media", "/stripe", "/__")
EXEMPT_EXACT = {
    "/sitemap.xml",
    "/robots.txt",
    "/llms.txt",
    "/favicon.ico",
    "/healthz",
}


def _is_exempt(path: str) -> bool:
    if path in EXEMPT_EXACT:
        return True
    return any(path.startswith(prefix) for prefix in EXEMPT_PREFIXES)


class RegionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info

        if _is_exempt(path):
            request.region_code = settings.DEFAULT_REGION
            request.region = get_region(settings.DEFAULT_REGION)
            return self.get_response(request)

        segments = [s for s in path.split("/") if s != ""]
        first = segments[0] if segments else ""

        if first in settings.REGIONS and is_enabled(first):
            # Valid, live region prefix: record it and strip for resolution.
            request.region_code = first
            request.region = get_region(first)
            stripped = "/" + "/".join(segments[1:])
            if not stripped.endswith("/"):
                stripped += "/"
            request.path_info = stripped
            return self.get_response(request)

        if first in settings.REGIONS and not is_enabled(first):
            # Region exists but is not live yet -> send to the live default.
            request.region_code = settings.DEFAULT_REGION
            request.region = get_region(settings.DEFAULT_REGION)
            return redirect(f"/{settings.DEFAULT_REGION}/")

        # No region prefix: redirect to the visitor's region (geo-aware).
        target_region = detect_region(request)
        return redirect(f"/{target_region}{path}")
