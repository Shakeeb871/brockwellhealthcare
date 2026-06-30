"""Inline professional SVG icons (stroke style) — replaces emojis.

Usage:
    {% load icons %}
    {% icon 'calendar' %}
    {% category_icon category.slug %}
"""

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# 24x24 stroke icons (currentColor). Clean, professional line style.
_ICONS = {
    "leaf": '<path d="M4 20c8 0 15-5 16-17C9 3 4 9 4 20Z"/><path d="M4 20c3-7 8-10 13-12"/>',
    "dna": '<path d="M7 3c0 5 10 8 10 18M17 3c0 5-10 8-10 18"/><path d="M8.5 6.5h7M9 17.5h6M7.6 12h8.8"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7.5V12l3 1.8"/>',
    "sparkles": '<path d="M12 3l1.7 4.5L18 9l-4.3 1.5L12 15l-1.7-4.5L6 9l4.3-1.5z"/><path d="M18.5 14l.7 1.8 1.8.7-1.8.7-.7 1.8-.7-1.8-1.8-.7 1.8-.7z"/>',
    "microscope": '<path d="M5 21h12"/><path d="M9 21a7 7 0 0 0 7-7"/><path d="M11 5l3 3-2.5 2.5L8.5 7.5z"/><path d="M9 8l-2.5 2.5"/><path d="M11.5 3.5l1 1"/>',
    "zap": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    "calendar": '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 9.5h17M8 3v4M16 3v4"/>',
    "pin": '<path d="M12 21s7-5.6 7-11a7 7 0 0 0-14 0c0 5.4 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "ticket": '<path d="M3 8.5A2.5 2.5 0 0 1 5.5 6h13A2.5 2.5 0 0 1 21 8.5a2 2 0 0 0 0 4A2.5 2.5 0 0 1 18.5 15h-13A2.5 2.5 0 0 1 3 12.5a2 2 0 0 0 0-4z"/><path d="M14 6.5v11"/>',
    "phone": '<path d="M5 4h3.5l1.8 4.5-2.3 1.4a11.5 11.5 0 0 0 5.1 5.1l1.4-2.3L19 16v3.5a1.5 1.5 0 0 1-1.6 1.5A16.5 16.5 0 0 1 3 6.6 1.5 1.5 0 0 1 4.5 5z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3.5 7.5l8.5 6 8.5-6"/>',
    "arrow": '<path d="M5 12h13M13 6l6 6-6 6"/>',
    "chevron": '<path d="M9 6l6 6-6 6"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7"/>',
    "shield": '<path d="M12 3l7.5 3v5.5c0 4.5-3.2 7.6-7.5 9.5-4.3-1.9-7.5-5-7.5-9.5V6z"/><path d="M9 12l2 2 4-4.5"/>',
    "users": '<circle cx="9" cy="8" r="3"/><path d="M3.5 20a5.5 6 0 0 1 11 0"/><path d="M16 5.5a3 3 0 0 1 0 6"/><path d="M20.5 20a5.5 6 0 0 0-3.5-5.4"/>',
    "award": '<circle cx="12" cy="9" r="5.5"/><path d="M8.5 13.5 7 22l5-2.5L17 22l-1.5-8.5"/>',
    "heart": '<path d="M12 20s-7-4.4-7-9.5A3.7 3.7 0 0 1 12 7a3.7 3.7 0 0 1 7 3.5C19 15.6 12 20 12 20Z"/>',
    "plus": '<circle cx="12" cy="12" r="9"/><path d="M12 8.2v7.6M8.2 12h7.6"/>',
    "stethoscope": '<path d="M6 3v5a4 4 0 0 0 8 0V3"/><path d="M10 16v1a4 4 0 0 0 8 0v-2"/><circle cx="18" cy="12" r="2"/><path d="M6 3H4M14 3h-2"/>',
}

_CATEGORY = {
    "regenerative-wellness": "leaf",
    "regenerative-medicine": "dna",
    "longevity-healthspan": "clock",
    "anti-aging-aesthetics": "sparkles",
    "advanced-diagnostics": "microscope",
    "emsculpt-for-pain": "zap",
}


def _svg(body, cls):
    return mark_safe(
        f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" '
        f'aria-hidden="true" focusable="false">{body}</svg>'
    )


@register.simple_tag
def icon(name, cls="ico"):
    return _svg(_ICONS.get(name, _ICONS["plus"]), cls)


@register.simple_tag
def category_icon(slug, cls="ico"):
    return _svg(_ICONS.get(_CATEGORY.get(slug, "plus"), _ICONS["plus"]), cls)
