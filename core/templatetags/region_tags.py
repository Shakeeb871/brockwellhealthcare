"""Template helpers for region-aware URLs and hreflang generation."""

from django import template
from django.conf import settings

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
