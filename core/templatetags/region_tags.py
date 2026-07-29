"""Template helpers for region-aware URLs and hreflang generation."""

import os

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

from core.regions import region_path

register = template.Library()


@register.simple_tag(takes_context=True)
def rurl(context, urlname, *args, **kwargs):
    """Region-prefixed URL for the current request's region.

    Usage: ``{% rurl 'services:list' %}`` -> ``/uae/services/``.
    """
    request = context.get("request")
    code = getattr(request, "region_code", settings.DEFAULT_REGION)
    return region_path(code, urlname, *args, **kwargs)


@register.simple_tag(takes_context=True)
def rurl_for(context, region_code, urlname, *args, **kwargs):
    """Region-prefixed URL for a specific region (for hreflang / switchers)."""
    return region_path(region_code, urlname, *args, **kwargs)


@register.simple_tag
def region_home(region_code):
    return f"/{region_code}/"


@register.filter
def digits(value):
    """Strip everything but digits — for tel:/wa.me links.

    Phone numbers are stored for display ("+1 (262) 302-1216"), but wa.me and
    tel: need bare digits, so "+1 (262) 302-1216" -> "12623021216".
    """
    return "".join(ch for ch in str(value or "") if ch.isdigit())


# --------------------------------------------------------------------------- #
# Intrinsic image dimensions
# --------------------------------------------------------------------------- #
# Every <img> needs width/height so the browser can reserve the right box
# before the file arrives — without them the page reflows as images load
# (Cumulative Layout Shift, a Core Web Vitals metric and a Screaming Frog
# "missing size attributes" finding).
#
# Rather than hard-code numbers next to each tag — which silently rot the
# moment an image is replaced — this resolves the URL already in the template
# back to the file on disk and reads its real size. The result is cached per
# process, so each image is opened at most once per worker.

_DIMS_CACHE: dict[str, tuple[int, int] | None] = {}


def _local_path(url: str) -> str | None:
    """Map a static/media URL back to the file on disk, or None if it isn't ours."""
    static_url = getattr(settings, "STATIC_URL", "") or ""
    media_url = getattr(settings, "MEDIA_URL", "") or ""

    if static_url and url.startswith(static_url):
        rel = url[len(static_url):]
        # Ask the finders first: they see the *source* file, so a stale
        # STATIC_ROOT left over from an older collectstatic can't feed us the
        # wrong dimensions. In production the name is hashed
        # ("img/x.abc123.webp") which the finders won't match, so fall through
        # to STATIC_ROOT where collectstatic put it.
        from django.contrib.staticfiles import finders

        found = finders.find(rel)
        if found:
            return found
        root = getattr(settings, "STATIC_ROOT", None)
        if root:
            candidate = os.path.join(root, rel)
            if os.path.exists(candidate):
                return candidate
        return None

    if media_url and url.startswith(media_url):
        root = getattr(settings, "MEDIA_ROOT", None)
        if not root:
            return None
        candidate = os.path.join(root, url[len(media_url):])
        return candidate if os.path.exists(candidate) else None

    if url.startswith(("http://", "https://", "//", "data:")):
        return None

    # Not a URL: treat it as a static-relative path, so a template can pass the
    # same expression it hands to {% static %} instead of duplicating the URL.
    from django.contrib.staticfiles import finders

    return finders.find(url.lstrip("/"))


def _dimensions(url: str) -> tuple[int, int] | None:
    if url in _DIMS_CACHE:
        return _DIMS_CACHE[url]

    dims = None
    path = _local_path(url)
    if path:
        try:
            if path.lower().endswith(".svg"):
                dims = _svg_dimensions(path)
            else:
                from PIL import Image

                with Image.open(path) as im:
                    dims = im.size
        except Exception:
            # A missing or unreadable file must never break page rendering —
            # the <img> just goes out without size hints, as it did before.
            dims = None
    _DIMS_CACHE[url] = dims
    return dims


def _svg_dimensions(path: str) -> tuple[int, int] | None:
    """Read an SVG's pixel box from width/height, falling back to viewBox.

    Pillow can't open SVG, but an <img> pointing at one still needs size hints.
    """
    import re

    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        head = fh.read(2048)

    def px(name):
        m = re.search(rf'\b{name}\s*=\s*"([\d.]+)(px)?"', head)
        return float(m.group(1)) if m else None

    w, h = px("width"), px("height")
    if not (w and h):
        m = re.search(r'\bviewBox\s*=\s*"([-\d.\s,]+)"', head)
        if m:
            parts = [p for p in re.split(r"[\s,]+", m.group(1).strip()) if p]
            if len(parts) == 4:
                w, h = float(parts[2]), float(parts[3])
    return (round(w), round(h)) if w and h else None


@register.simple_tag
def img_dims(src):
    """Emit ``width="W" height="H"`` for an image URL.

    Usage: ``<img src="{{ p.image.url }}" {% img_dims p.image.url %}>``

    Renders nothing when the file can't be found, so a broken or remote src
    degrades to exactly the old markup instead of an exception.
    """
    url = str(src or "").strip()
    if not url:
        return ""
    dims = _dimensions(url)
    if not dims:
        return ""
    return mark_safe(f'width="{dims[0]}" height="{dims[1]}"')
