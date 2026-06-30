"""Render Python dicts as safe JSON-LD inside <script> tags."""

import json

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def as_jsonld(value):
    """Serialise a schema dict/list to JSON-LD, safe for inline <script>.

    ``</`` is escaped so the payload can never break out of the script tag.
    """
    text = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    text = text.replace("</", "<\\/")
    return mark_safe(text)


@register.filter
def og_locale(locale):
    """``en-AE`` -> ``en_AE`` for Open Graph."""
    return (locale or "en").replace("-", "_")
