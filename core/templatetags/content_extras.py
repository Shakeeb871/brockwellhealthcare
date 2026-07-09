"""Render-time content enhancers.

Editors write plain content in the WYSIWYG editor (headings, paragraphs, lists).
These filters turn simple, editor-friendly conventions into designed components
at render time — so the admin never has to build components by hand:

* Consecutive ``<h3>Step 1: Title</h3><p>…</p>`` blocks become a numbered
  treatment-process timeline (``|enhance``).
* A run of 3+ consecutive ``<h3>Title</h3><p>…</p>`` blocks (that are *not*
  steps) becomes a designed card grid — used e.g. for "Types of …" sections.
* Bullet lists are turned into professional icon lists purely via CSS
  (see ``.prose ul`` in styles.css) — no markup change needed.
"""

import html as html_lib
import re

from django import template
from django.conf import settings
from django.contrib.staticfiles import finders
from django.templatetags.static import static
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from core.regions import region_asset, region_asset_rel

from .icons import _ICONS, _svg

register = template.Library()

# Inline ``/static/img/<path>`` URLs (in editor content, doctor photos, etc.).
_STATIC_IMG = re.compile(r"/static/img/([^\"')\s]+)")


@register.filter
def region_media(value, region_code):
    """Rewrite ``/static/img/<path>`` URLs to a region's own override
    (``/static/img/<code>/<path>``) when that file exists, else keep the shared
    path. Works on a full HTML block or a single URL string."""
    if not value or not region_code:
        return value

    def repl(m):
        rel = region_asset_rel(region_code, m.group(1))
        return f"/static/{rel}" if rel else m.group(0)

    return mark_safe(_STATIC_IMG.sub(repl, value))

# Keyword → icon for content cards (first match on a whole word wins).
# Lets the card grid show a relevant glyph without any admin-side setup.
_ICON_KEYWORDS = [
    ("eboo", "refresh"), ("ozone", "lungs"), ("oxygen", "lungs"),
    ("glutathione", "iv-bag"), ("vitamin", "vial"), ("infusion", "iv-bag"),
    ("iv", "iv-bag"), ("pemf", "magnet"), ("magnet", "magnet"),
    ("laser", "zap"), ("light", "sun"), ("plasma", "plasma"), ("prp", "droplet"),
    ("stem", "cells"), ("exosome", "molecule"), ("detox", "droplet"),
    ("nutrition", "apple"), ("lifestyle", "apple"), ("diet", "apple"),
    ("stress", "spa"), ("massage", "spa"), ("shock", "waveform"),
    ("hyperbaric", "lungs"), ("genom", "dna"), ("dna", "dna"),
    ("physio", "hand"), ("sport", "run"), ("bone", "bone"), ("ortho", "bone"),
]
_ICON_DEFAULT = "sparkles"


def _pick_icon(title):
    text = title.lower()
    for kw, name in _ICON_KEYWORDS:
        if re.search(r"(?<![a-z])" + re.escape(kw) + r"(?![a-z])", text):
            return name
    return _ICON_DEFAULT

# One "Step N: Title" heading immediately followed by a paragraph.
_STEP = re.compile(
    r"<h3>\s*Step\s*(\d+)\s*[:.\-]?\s*(.*?)</h3>\s*<p>(.*?)</p>",
    re.S | re.I,
)
# A run of two or more consecutive step blocks.
_STEP_RUN = re.compile(
    r"((?:<h3>\s*Step\s*\d+\s*[:.\-]?.*?</h3>\s*<p>.*?</p>\s*){2,})",
    re.S | re.I,
)

# One plain "Title" heading + paragraph that is NOT a step.
_CARD = re.compile(
    r"<h3>\s*(?!\s*Step\s*\d)(.*?)</h3>\s*<p>(.*?)</p>",
    re.S | re.I,
)
# A run of three or more consecutive plain (non-step) heading+paragraph blocks.
_CARD_RUN = re.compile(
    r"((?:<h3>\s*(?!\s*Step\s*\d).*?</h3>\s*<p>.*?</p>\s*){3,})",
    re.S | re.I,
)


def _build_timeline(run_html):
    items = []
    for m in _STEP.finditer(run_html):
        num, title, body = m.group(1), m.group(2).strip(), m.group(3).strip()
        items.append(
            f'<li class="proc-step">'
            f'<span class="proc-step__num" aria-hidden="true">{num}</span>'
            f'<div class="proc-step__body"><h3>{title}</h3><p>{body}</p></div>'
            f"</li>"
        )
    return '<ol class="proc-steps">' + "".join(items) + "</ol>"


def _build_cards(run_html):
    cards = []
    for m in _CARD.finditer(run_html):
        title, body = m.group(1).strip(), m.group(2).strip()
        glyph = _svg(_ICONS.get(_pick_icon(title), _ICONS["sparkles"]), "ico")
        cards.append(
            f'<div class="info-card">'
            f'<span class="info-card__ico" aria-hidden="true">{glyph}</span>'
            f'<h3 class="info-card__title">{title}</h3>'
            f'<p class="info-card__body">{body}</p>'
            f"</div>"
        )
    return '<div class="info-cards">' + "".join(cards) + "</div>"


# A trailing "Book …" call-to-action heading and its paragraph(s). We drop these
# everywhere — booking prompts live in the page's own CTA/booking widgets, so an
# inline "Book …" section is redundant on every page.
_BOOK_CTA = re.compile(
    r"<h2[^>]*>\s*Book\b.*?</h2>(?:\s*<p>.*?</p>)*",
    re.S | re.I,
)


@register.filter
def enhance(html):
    """Transform editor conventions into designed components."""
    if not html:
        return ""
    # Remove any inline "Book …" CTA section first.
    out = _BOOK_CTA.sub("", html)
    # Steps first — so their headings are consumed before the card pass runs.
    out = _STEP_RUN.sub(lambda m: _build_timeline(m.group(1)), out)
    out = _CARD_RUN.sub(lambda m: _build_cards(m.group(1)), out)
    return mark_safe(out)


# --- Section splitter for the professional (homepage-style) category page ----

# One <h2> heading and everything up to the next <h2> (or end of string).
_H2_SECTION = re.compile(r"<h2[^>]*>(.*?)</h2>(.*?)(?=<h2[^>]*>|$)", re.S | re.I)
# Everything before the first <h2> (the intro / lead paragraphs).
_LEAD = re.compile(r"^(.*?)(?=<h2[^>]*>)", re.S | re.I)
_TAGS = re.compile(r"<[^>]+>")


def _section_image(cat_slug, name, region_code=""):
    """Region-aware static URL for an optional per-section image, or "" if absent
    — the region's ``img/<code>/services/categories/<cat>/<name>.webp`` if present,
    else the shared file, else a placeholder slot."""
    if not cat_slug:
        return ""
    return region_asset(region_code, f"services/categories/{cat_slug}/{name}.webp")


@register.simple_tag(takes_context=True)
def region_img(context, tail):
    """Region-aware static URL for any image under ``img/`` (region override →
    shared → ""). ``tail`` is the path under ``img/``, e.g. ``brockwell-healthcare.webp``."""
    region_code = context.get("region_code") or settings.DEFAULT_REGION
    return region_asset(region_code, tail)


@register.simple_tag(takes_context=True)
def service_thumb(context, slug):
    """Region-aware thumbnail for a sub-service card. Prefers a dedicated card
    image, then the service hero; region override wins over the shared file.
    Returns "" so the card falls back to its icon when neither exists."""
    if not slug:
        return ""
    region_code = context.get("region_code") or settings.DEFAULT_REGION
    for tail in (f"services/{slug}-card.webp", f"services/{slug}-hero.webp"):
        url = region_asset(region_code, tail)
        if url:
            return url
    return ""


@register.simple_tag
def content_sections(html, cat_slug="", region_code=""):
    """Split rich category content into a designed, homepage-style layout.

    Returns ``{lead, lead_image, sections}`` where each section is
    ``{heading, body, kind, img_slug, image}``. ``kind`` picks the layout:
    ``cards`` (Types → card grid), ``steps`` (process timeline), ``list``
    (benefits / why-choose), or ``plain`` (text + image split). Body HTML is
    run through ``enhance``. Inline "Book …" CTA sections are dropped."""
    if not html:
        return {"lead": "", "lead_image": "", "sections": []}

    sections = []
    for m in _H2_SECTION.finditer(html):
        # Strip tags, then unescape entities (e.g. &amp; → &) so the plain-text
        # heading isn't double-escaped when re-rendered via {{ }}.
        heading = html_lib.unescape(_TAGS.sub("", m.group(1)).strip())
        # Drop inline "Book …" call-to-action sections everywhere.
        if heading.lower().startswith("book"):
            continue
        body = region_media(enhance(m.group(2).strip()), region_code)
        if "info-cards" in body:
            kind = "cards"
        elif "proc-steps" in body:
            kind = "steps"
        elif "<ul" in body:
            kind = "list"
        else:
            kind = "plain"
        img_slug = slugify(heading)
        image = (_section_image(cat_slug, img_slug, region_code)
                 if kind in ("plain", "list") else "")
        sections.append(
            {"heading": heading, "body": body, "kind": kind,
             "img_slug": img_slug, "image": image}
        )

    if sections:
        lm = _LEAD.match(html)
        lead_html = lm.group(1).strip() if lm else ""
        lead = region_media(enhance(lead_html), region_code) if lead_html else ""
    else:
        lead = region_media(enhance(html.strip()), region_code)

    return {"lead": lead,
            "lead_image": _section_image(cat_slug, "intro", region_code),
            "sections": sections}
