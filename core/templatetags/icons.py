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
    "search": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>',
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


# Filled brand/social glyphs (fill style, not stroke).
_SOCIAL = {
    "whatsapp": '<path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15l-1.3 4.7 4.8-1.3A10 10 0 1 0 12 2zm5.2 14c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-1.7-.1-.4-.1-1-.3-1.6-.6-2.8-1.2-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.8 0-1.3.7-2 .9-2.2.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 1.9c.1.2.1.4 0 .6l-.4.5c-.1.2-.3.3-.1.6.1.3.7 1.1 1.4 1.7.9.8 1.6 1.1 1.9 1.2.2.1.4.1.6-.1l.7-.8c.2-.2.4-.2.6-.1l1.7.9c.3.1.4.2.5.3.1.3.1.8-.1 1.3z"/>',
    "instagram": '<rect x="3" y="3" width="18" height="18" rx="5.4" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="12" r="3.8" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="17.3" cy="6.7" r="1.2" fill="currentColor"/>',
    "facebook": '<path fill="currentColor" d="M13.4 21v-7.4h2.5l.4-2.9h-2.9V8.8c0-.8.3-1.4 1.5-1.4H16V4.8c-.3 0-1.2-.1-2.2-.1-2.2 0-3.7 1.3-3.7 3.8v2.2H7.6v2.9h2.5V21z"/>',
    "x": '<path fill="currentColor" d="M17.5 3h3l-6.5 7.4L21.7 21h-5.9l-4.1-5.4L6.9 21H3.9l7-8L2.6 3h6l3.7 4.9zM16.4 19.2h1.7L7.7 4.7H5.9z"/>',
    "youtube": '<path fill="currentColor" d="M21.6 7.2a2.6 2.6 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.6 2.6 0 0 0 2.4 7.2 27 27 0 0 0 2 12a27 27 0 0 0 .4 4.8 2.6 2.6 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.6 2.6 0 0 0 1.8-1.8A27 27 0 0 0 22 12a27 27 0 0 0-.4-4.8zM10 14.7V9.3l4.7 2.7z"/>',
}


def _svg(body, cls):
    return mark_safe(
        f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" '
        f'aria-hidden="true" focusable="false">{body}</svg>'
    )


@register.simple_tag
def social(name, cls="soc"):
    body = _SOCIAL.get(name, "")
    return mark_safe(f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{body}</svg>')


@register.simple_tag
def icon(name, cls="ico"):
    return _svg(_ICONS.get(name, _ICONS["plus"]), cls)


@register.simple_tag
def category_icon(slug, cls="ico"):
    return _svg(_ICONS.get(_CATEGORY.get(slug, "plus"), _ICONS["plus"]), cls)
