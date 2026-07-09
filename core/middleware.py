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
EXEMPT_PREFIXES = ("/admin", "/static", "/media", "/stripe", "/tinymce", "/__")
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

        default = settings.DEFAULT_REGION
        segments = [s for s in path.split("/") if s != ""]
        first = segments[0] if segments else ""

        # A non-default, live region prefix (e.g. /uae/...): record it and strip.
        if first in settings.REGIONS and first != default and is_enabled(first):
            request.region_code = first
            request.region = get_region(first)
            stripped = "/" + "/".join(segments[1:])
            if not stripped.endswith("/"):
                stripped += "/"
            request.path_info = stripped
            return self.get_response(request)

        # The default region is served at the root, so its own prefix (/us/...)
        # is redundant -> 301 to the clean, prefix-less URL.
        if first == default:
            rest = "/" + "/".join(segments[1:])
            if not rest.endswith("/"):
                rest += "/"
            return redirect(rest, permanent=True)

        # A reserved/disabled region prefix -> the default root.
        if first in settings.REGIONS and not is_enabled(first):
            return redirect("/")

        # No region prefix: this is the default region, served at the root.
        # Geo-route visitors from a non-default live region (e.g. the UAE) to
        # their prefix; everyone else stays on the root (default) site.
        detected = detect_region(request)
        if detected != default and is_enabled(detected):
            return redirect(f"/{detected}{path}")
        request.region_code = default
        request.region = get_region(default)
        return self.get_response(request)


class SecurityHeadersMiddleware:
    """Add defence-in-depth response headers that Django core does not set.

    Covers the gaps SEO can't be harmed by:

    * ``Content-Security-Policy`` — blocks injected/external scripts, framing,
      plugins, ``<base>`` hijacking and off-site form posts. Inline first-party
      scripts, JSON-LD structured data (SEO), inline styles and image ``onerror``
      fallbacks are kept working via ``'unsafe-inline'``; no external script host
      is allowed, so an injected ``<script src=evil>`` cannot load.
    * ``Permissions-Policy`` — switches off device APIs the site never uses and
      opts out of FLoC/Topics.
    * ``Cross-Origin-Opener-Policy`` — isolates the browsing context.
    * ``Referrer-Policy`` — set here too so it applies in every environment.
    * ``Server`` header — overwritten so the response does not advertise the web
      server / framework to anyone inspecting requests.

    Crawlers ignore these headers, so indexing and rich results are unaffected.
    """

    CSP = (
        "default-src 'self'; "
        "base-uri 'self'; "
        "object-src 'none'; "
        "frame-ancestors 'none'; "
        "form-action 'self'; "
        "img-src 'self' data:; "
        "font-src 'self' https://fonts.gstatic.com; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        "script-src 'self' 'unsafe-inline' https://analytics.ahrefs.com; "
        "connect-src 'self' https://analytics.ahrefs.com; "
        "manifest-src 'self'; "
        "frame-src 'self'; "
        "upgrade-insecure-requests"
    )
    PERMISSIONS_POLICY = (
        "geolocation=(), microphone=(), camera=(), payment=(), usb=(), "
        "magnetometer=(), gyroscope=(), accelerometer=(), browsing-topics=()"
    )

    def __init__(self, get_response):
        self.get_response = get_response
        self.csp = getattr(settings, "CONTENT_SECURITY_POLICY", self.CSP)

    def __call__(self, request):
        response = self.get_response(request)
        response.setdefault("Content-Security-Policy", self.csp)
        response.setdefault("Permissions-Policy", self.PERMISSIONS_POLICY)
        response.setdefault("Cross-Origin-Opener-Policy", "same-origin")
        response.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        response.setdefault("X-Content-Type-Options", "nosniff")
        # Do not advertise the server / framework.
        response["Server"] = settings.BRAND_NAME.replace(" ", "")
        return response


class NoIndexMiddleware:
    """Emit ``X-Robots-Tag: noindex`` on every response when ``SITE_NOINDEX``.

    A response header is the most reliable way to de-index a whole site: it
    covers HTML pages, files, redirects and error responses alike, and search
    engines honour it even where they wouldn't parse a ``<meta>`` tag. Set
    ``SITE_NOINDEX=False`` in the environment to lift it and allow indexing.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if getattr(settings, "SITE_NOINDEX", False):
            response["X-Robots-Tag"] = "noindex, nofollow, noarchive, nosnippet"
        return response
