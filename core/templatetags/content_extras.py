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
from django.contrib.staticfiles import finders
from django.templatetags.static import static
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from .icons import _ICONS, _svg

register = template.Library()

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


def _section_image(cat_slug, name):
    """Static URL for an optional per-section image, or "" if the file is
    absent — so image slots are placeholders until a file is dropped in at
    ``static/img/services/categories/<cat_slug>/<name>.webp``."""
    if not cat_slug:
        return ""
    rel = f"img/services/categories/{cat_slug}/{name}.webp"
    return static(rel) if finders.find(rel) else ""


@register.simple_tag
def service_thumb(slug):
    """Static thumbnail for a sub-service card: ``img/services/<slug>-hero.webp``
    if that file exists, else "" so the card falls back to its icon."""
    if not slug:
        return ""
    rel = f"img/services/{slug}-hero.webp"
    return static(rel) if finders.find(rel) else ""


@register.simple_tag
def content_sections(html, cat_slug=""):
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
        body = enhance(m.group(2).strip())
        if "info-cards" in body:
            kind = "cards"
        elif "proc-steps" in body:
            kind = "steps"
        elif "<ul" in body:
            kind = "list"
        else:
            kind = "plain"
        img_slug = slugify(heading)
        image = _section_image(cat_slug, img_slug) if kind in ("plain", "list") else ""
        sections.append(
            {"heading": heading, "body": body, "kind": kind,
             "img_slug": img_slug, "image": image}
        )

    if sections:
        lm = _LEAD.match(html)
        lead_html = lm.group(1).strip() if lm else ""
        lead = enhance(lead_html) if lead_html else ""
    else:
        lead = enhance(html.strip())

    return {"lead": lead, "lead_image": _section_image(cat_slug, "intro"),
            "sections": sections}
