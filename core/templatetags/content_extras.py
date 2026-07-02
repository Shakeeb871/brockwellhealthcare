"""Render-time content enhancers.

Editors write plain content in the WYSIWYG editor (headings, paragraphs, lists).
These filters turn simple, editor-friendly conventions into designed components
at render time — so the admin never has to build components by hand:

* Consecutive ``<h3>Step 1: Title</h3><p>…</p>`` blocks become a numbered
  treatment-process timeline (``|enhance``).
* Bullet lists are turned into professional icon lists purely via CSS
  (see ``.prose ul`` in styles.css) — no markup change needed.
"""

import re

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

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


@register.filter
def enhance(html):
    """Transform editor conventions into designed components."""
    if not html:
        return ""
    out = _STEP_RUN.sub(lambda m: _build_timeline(m.group(1)), html)
    return mark_safe(out)
