"""Inline professional SVG icons (stroke style) — replaces emojis.

Usage:
    {% load icons %}
    {% icon 'calendar' %}
    {% category_icon category.slug %}
"""

from django import template
from django.contrib.staticfiles import finders
from django.templatetags.static import static
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def category_image(slug):
    """URL of a category's homepage image if a file exists at
    ``static/img/services/categories/<slug>.webp`` — else "" (safe, no crash).

    Lets category images be managed as repo files (like the per-service hero
    images) without touching the admin. Drop the file in and it appears."""
    rel = f"img/services/categories/{slug}.webp"
    return static(rel) if finders.find(rel) else ""

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
    "chevron-left": '<path d="M15 6l-6 6 6 6"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.6 2.7 2.6 15.3 0 18M12 3c-2.6 2.7-2.6 15.3 0 18"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7"/>',
    "shield": '<path d="M12 3l7.5 3v5.5c0 4.5-3.2 7.6-7.5 9.5-4.3-1.9-7.5-5-7.5-9.5V6z"/><path d="M9 12l2 2 4-4.5"/>',
    "users": '<circle cx="9" cy="8" r="3"/><path d="M3.5 20a5.5 6 0 0 1 11 0"/><path d="M16 5.5a3 3 0 0 1 0 6"/><path d="M20.5 20a5.5 6 0 0 0-3.5-5.4"/>',
    "award": '<circle cx="12" cy="9" r="5.5"/><path d="M8.5 13.5 7 22l5-2.5L17 22l-1.5-8.5"/>',
    "heart": '<path d="M12 20s-7-4.4-7-9.5A3.7 3.7 0 0 1 12 7a3.7 3.7 0 0 1 7 3.5C19 15.6 12 20 12 20Z"/>',
    "plus": '<circle cx="12" cy="12" r="9"/><path d="M12 8.2v7.6M8.2 12h7.6"/>',
    "stethoscope": '<path d="M6 3v5a4 4 0 0 0 8 0V3"/><path d="M10 16v1a4 4 0 0 0 8 0v-2"/><circle cx="18" cy="12" r="2"/><path d="M6 3H4M14 3h-2"/>',
    "bed": '<path d="M3 8v10"/><path d="M3 17h18v-3a3 3 0 0 0-3-3H9v3H3"/><circle cx="6.6" cy="10.6" r="1.6"/>',
    "pulse": '<path d="M2 12h3l2-6 3.5 12L14 9l1.5 3H22"/>',
    "user-plus": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20a6 6 0 0 1 11 0"/><path d="M18 13v6M15 16h6"/>',
    "scalpel": '<path d="M4 20l7-7"/><path d="M11 13l8-8v5l-5 5z"/>',
    "star": '<path d="M12 3.5l2.5 5.3 5.8.6-4.3 3.9 1.2 5.7L12 16.9 6.8 19l1.2-5.7L3.7 9.4l5.8-.6z"/>',
    "building": '<path d="M4 21V4h10v17"/><path d="M14 10h6v11"/><path d="M2.5 21h19"/><path d="M7 7.5h4M7 11h4M7 14.5h4M17 13.5h0M17 17h0"/>',
    "globe-pin": '<circle cx="12" cy="10" r="8"/><path d="M4 10h16M12 2c2.5 2.6 2.5 12.4 0 16M12 2c-2.5 2.6-2.5 12.4 0 16"/>',
    "chat": '<path d="M4 5.5h16a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H9l-4 3v-3H4a1 1 0 0 1-1-1v-9a1 1 0 0 1 1-1z"/>',
    # --- service-specific glyphs ---------------------------------------- #
    "droplet": '<path d="M12 3.2c3.2 3.6 5.3 6.6 5.3 9.6a5.3 5.3 0 0 1-10.6 0c0-3 2.1-6 5.3-9.6z"/>',
    "plasma": '<path d="M12 3.2c3.2 3.6 5.3 6.6 5.3 9.6a5.3 5.3 0 0 1-10.6 0c0-3 2.1-6 5.3-9.6z"/><path d="M12 10.5v4.5M9.7 12.7h4.6"/>',
    "syringe": '<path d="M15 3l6 6"/><path d="M18.5 5.5 8 16"/><path d="M13 7.5l3.5 3.5"/><path d="M10 10.5l3.5 3.5"/><path d="M8 16H5.5L3 18.5"/>',
    "brain": '<path d="M9.5 4a3 3 0 0 0-3 3 3 3 0 0 0-1 5.8V15a3 3 0 0 0 4 2.8"/><path d="M14.5 4a3 3 0 0 1 3 3 3 3 0 0 1 1 5.8V15a3 3 0 0 1-4 2.8"/><path d="M12 4.6v13.8"/>',
    "lungs": '<path d="M12 4v7"/><path d="M12 9c-1-1.6-3-1.4-3 .6 0 0-2 .6-3 3.1s-1 5.5 0 6.4 3 .4 3-1 .6-5.6 0-9.1z"/><path d="M12 9c1-1.6 3-1.4 3 .6 0 0 2 .6 3 3.1s1 5.5 0 6.4-3 .4-3-1-.6-5.6 0-9.1z"/>',
    "iv-bag": '<rect x="9" y="3" width="6" height="9" rx="1.6"/><path d="M11 6.2h2"/><path d="M12 12v5a2 2 0 0 0 2 2h1.5"/>',
    "male": '<circle cx="10" cy="14" r="5.5"/><path d="M14 10l6-6"/><path d="M15 4h5v5"/>',
    "apple": '<path d="M12 8.2c-1-2-3.4-2.4-5 0-1.4 2.2-.9 6 .9 8 1 1.1 2 1.6 4.1 1.6s3.1-.5 4.1-1.6c1.8-2 2.3-5.8.9-8-1.6-2.4-4-2-5 0z"/><path d="M12 8.2V5a3 3 0 0 1 3-3"/>',
    "magnet": '<path d="M6 4h4v8a2 2 0 0 0 4 0V4h4v8a6 6 0 0 1-12 0z"/><path d="M6 8.5h4M14 8.5h4"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2.4M12 19.6V22M2 12h2.4M19.6 12H22M4.9 4.9l1.7 1.7M17.4 17.4l1.7 1.7M19.1 4.9l-1.7 1.7M6.6 17.4l-1.7 1.7"/>',
    "waveform": '<circle cx="12" cy="12" r="1.4"/><path d="M8.2 8.2a6 6 0 0 0 0 7.6M5.8 5.8a9.4 9.4 0 0 0 0 12.4M15.8 8.2a6 6 0 0 1 0 7.6M18.2 5.8a9.4 9.4 0 0 1 0 12.4"/>',
    "spa": '<path d="M12 20c-2-1.5-3.2-3.8-3.2-6.2 0-2.6 1.4-4.9 3.2-6.3 1.8 1.4 3.2 3.7 3.2 6.3 0 2.4-1.2 4.7-3.2 6.2z"/><path d="M12 20c-3.8 0-6.6-2.4-6.8-6 2 0 3.6 1 4.7 2.3M12 20c3.8 0 6.6-2.4 6.8-6-2 0-3.6 1-4.7 2.3"/>',
    "kidney": '<path d="M10 4C6 4 4 7 4 12s2 8 6 8c2.2 0 3-1.6 3.6-3 .5-1.2 1-1.8 2-1.8 1.7 0 2.4-1.7 2.4-4.2C18 5.5 14 4 10 4z"/>',
    "bone": '<path d="M17.5 3.2a2.1 2.1 0 0 1 1.9 3.3 2.1 2.1 0 1 1-1.6 3.4l-7.7 7.7a2.1 2.1 0 1 1-3.4 1.6 2.1 2.1 0 1 1-1.6-3.4l7.7-7.7a2.1 2.1 0 0 1 3.3-1.9 2.1 2.1 0 0 1 1.4-3z"/>',
    "flask": '<path d="M9 3h6M10 3v5.5l-4.6 7.7A2 2 0 0 0 7.1 19h9.8a2 2 0 0 0 1.7-2.8L14 8.5V3"/><path d="M7.5 15h9"/>',
    "run": '<circle cx="15.5" cy="5" r="1.9"/><path d="M6 20.5l3-5 3 2 1.5 4.5M12 17.5l-1.2-6 4-2 2 3 3 1M8.5 9.5l2.5-1"/>',
    "molecule": '<circle cx="6" cy="7" r="2"/><circle cx="18" cy="9" r="2"/><circle cx="10" cy="18" r="2"/><circle cx="12.5" cy="11" r="2"/><path d="M7.7 8.3 10.7 9.8M16.2 9.9 14.4 10.4M11.4 12.9 10.6 16.1"/>',
    "clipboard": '<rect x="5" y="4.5" width="14" height="16.5" rx="2"/><path d="M9 4.5a3 3 0 0 1 6 0"/><path d="M12 10.5v5M9.5 13h5"/>',
    "hand": '<path d="M8 11V6.2a1.5 1.5 0 0 1 3 0V10M11 10V4.7a1.5 1.5 0 0 1 3 0V10M14 10.2V6.5a1.5 1.5 0 0 1 3 0V14c0 3.6-2.4 6.5-6 6.5-2.5 0-4.3-1.3-5.7-3.4L4 13.4a1.6 1.6 0 0 1 2.6-1.8L8 13.3"/>',
    "cells": '<circle cx="9" cy="10" r="4.2"/><circle cx="16.5" cy="15.5" r="3.4"/><circle cx="9" cy="10" r="1.3"/><circle cx="16.5" cy="15.5" r="1"/>',
    "refresh": '<path d="M4 11a8 8 0 0 1 13.7-4.7L20 8.5M20 13a8 8 0 0 1-13.7 4.7L4 15.5"/><path d="M20 3.5V8.5h-5M4 20.5V15.5h5"/>',
    "capsule": '<path d="M8.6 3.6a5 5 0 0 1 7 7l-5 5a5 5 0 0 1-7-7z"/><path d="M6.1 8.1l5 5"/>',
    "vial": '<path d="M8 3h8M9.5 3v13a2.5 2.5 0 0 0 5 0V3"/><path d="M9.5 11h5"/>',
    "chair": '<path d="M6.5 4v7.5h9V4"/><path d="M5 11.5h12"/><path d="M6.5 11.5 5.5 20M15.5 11.5l1 8.5"/><path d="M8 20h6"/>',
    "muscle": '<path d="M5 8.5c2.2-1.3 4.2-1 5.2 1 .8 1.5 2.1 2.1 3.8 2.1 2.1 0 3.5 1.6 3.5 4.1v1.8a1.5 1.5 0 0 1-1.5 1.5H8.2A3.2 3.2 0 0 1 5 16.8z"/><path d="M5 8.5C3.8 6.6 3.9 4.6 6 3.4"/>',
    "scan": '<rect x="3" y="4" width="18" height="12.5" rx="2"/><path d="M7.5 20.5h9M12 16.5v4"/><path d="M7.5 11a5 5 0 0 1 4.5-3 5 5 0 0 1 4.5 3"/><path d="M12 8v3.2"/>',
}

_CATEGORY = {
    "regenerative-wellness": "leaf",
    "regenerative-medicine": "dna",
    "longevity-healthspan": "clock",
    "anti-aging-aesthetics": "sparkles",
    "advanced-diagnostics": "microscope",
    "emsculpt-for-pain": "zap",
}

# Unique, relevant glyph per sub-service (falls back to its category icon).
_SERVICE = {
    # regenerative-wellness
    "detox-therapy": "droplet",
    "hydrodissection-injections": "syringe",
    "exomind-tms-wellness": "brain",
    "hyperbaric-oxygen-therapy": "lungs",
    "iv-laser-therapy": "iv-bag",
    "male-wellness": "male",
    "sexual-health": "heart",
    "nutrition-weight-loss": "apple",
    "pemf-therapy": "magnet",
    "red-light-therapy": "sun",
    "shock-wave-therapy": "waveform",
    "stress-management": "spa",
    "urology-services": "kidney",
    "regenerative-iv-therapy": "iv-bag",
    "ozone-therapy": "lungs",
    "iv-drips": "droplet",
    # regenerative-medicine
    "regenerative-orthopedics": "bone",
    "biological-integrative-medicine": "flask",
    "sports-medicine": "run",
    "exosome-therapy": "molecule",
    "functional-medicine": "clipboard",
    "genomics-medicine": "dna",
    "physiotherapy": "hand",
    # longevity-healthspan
    "healthspan": "pulse",
    "longevity-medicine": "clock",
    "stem-cells": "cells",
    "stress-reset": "refresh",
    "ketamine-therapy": "capsule",
    "longevity-ivs": "vial",
    "nad-iv-therapy": "iv-bag",
    # anti-aging-aesthetics
    "pure-plasma": "plasma",
    "emsella": "chair",
    "emsculpt-neo": "muscle",
    # advanced-diagnostics
    "ultrasound-diagnostics": "scan",
}


# Filled brand/social glyphs (fill style, not stroke).
_SOCIAL = {
    "whatsapp": '<path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15l-1.3 4.7 4.8-1.3A10 10 0 1 0 12 2zm5.2 14c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-1.7-.1-.4-.1-1-.3-1.6-.6-2.8-1.2-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.8 0-1.3.7-2 .9-2.2.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 1.9c.1.2.1.4 0 .6l-.4.5c-.1.2-.3.3-.1.6.1.3.7 1.1 1.4 1.7.9.8 1.6 1.1 1.9 1.2.2.1.4.1.6-.1l.7-.8c.2-.2.4-.2.6-.1l1.7.9c.3.1.4.2.5.3.1.3.1.8-.1 1.3z"/>',
    "instagram": '<rect x="3" y="3" width="18" height="18" rx="5.4" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="12" r="3.8" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="17.3" cy="6.7" r="1.2" fill="currentColor"/>',
    "facebook": '<path fill="currentColor" d="M13.4 21v-7.4h2.5l.4-2.9h-2.9V8.8c0-.8.3-1.4 1.5-1.4H16V4.8c-.3 0-1.2-.1-2.2-.1-2.2 0-3.7 1.3-3.7 3.8v2.2H7.6v2.9h2.5V21z"/>',
    "x": '<path fill="currentColor" d="M17.5 3h3l-6.5 7.4L21.7 21h-5.9l-4.1-5.4L6.9 21H3.9l7-8L2.6 3h6l3.7 4.9zM16.4 19.2h1.7L7.7 4.7H5.9z"/>',
    "youtube": '<path fill="currentColor" d="M21.6 7.2a2.6 2.6 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.6 2.6 0 0 0 2.4 7.2 27 27 0 0 0 2 12a27 27 0 0 0 .4 4.8 2.6 2.6 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.6 2.6 0 0 0 1.8-1.8A27 27 0 0 0 22 12a27 27 0 0 0-.4-4.8zM10 14.7V9.3l4.7 2.7z"/>',
    "tiktok": '<path fill="currentColor" d="M16.6 3h-2.7v11.9a2.4 2.4 0 1 1-2.4-2.4c.24 0 .47.04.7.1V9.8a5.3 5.3 0 1 0 4.4 5.2V8.9a6.3 6.3 0 0 0 3.6 1.15V7.3a3.6 3.6 0 0 1-3.6-3.6 3.7 3.7 0 0 1 0-.7z"/>',
    "linkedin": '<path fill="currentColor" d="M6.94 5a2 2 0 1 1-4.001-.001A2 2 0 0 1 6.94 5zM3.3 8.5h3.28V21H3.3zM9.4 8.5h3.14v1.7h.05c.44-.83 1.5-1.7 3.1-1.7 3.32 0 3.93 2.18 3.93 5V21h-3.28v-4.94c0-1.18-.02-2.7-1.64-2.7-1.65 0-1.9 1.28-1.9 2.6V21H9.4z"/>',
    # Official multi-colour Google "G" (brand asset — kept exact on purpose).
    "google": (
        '<path fill="#4285F4" d="M23.5 12.27c0-.79-.07-1.54-.2-2.27H12v4.51h6.47a5.54 5.54 0 0 1-2.4 3.63v3h3.88c2.27-2.09 3.55-5.17 3.55-8.87z"/>'
        '<path fill="#34A853" d="M12 24c3.24 0 5.96-1.08 7.95-2.91l-3.88-3.01c-1.08.72-2.45 1.15-4.07 1.15-3.13 0-5.78-2.11-6.73-4.96H1.26v3.11A12 12 0 0 0 12 24z"/>'
        '<path fill="#FBBC05" d="M5.27 14.27a7.2 7.2 0 0 1 0-4.55V6.61H1.26a12 12 0 0 0 0 10.77z"/>'
        '<path fill="#EA4335" d="M12 4.77c1.76 0 3.35.61 4.6 1.8l3.44-3.44C17.95 1.19 15.24 0 12 0A12 12 0 0 0 1.26 6.61l4.01 3.11C6.22 6.87 8.87 4.77 12 4.77z"/>'
    ),
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


@register.simple_tag
def service_icon(slug, cls="ico", category_slug=None):
    """Unique glyph for a sub-service; falls back to its category icon, then plus."""
    key = _SERVICE.get(slug) or _CATEGORY.get(category_slug, "plus")
    return _svg(_ICONS.get(key, _ICONS["plus"]), cls)
