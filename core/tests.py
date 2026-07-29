"""Regression tests for whole-site rendering invariants.

These exist because each one has already shipped as a live bug once.
"""
import re
from pathlib import Path

from django.conf import settings
from django.test import SimpleTestCase


TEMPLATE_DIRS = [Path(settings.BASE_DIR) / "templates"]


class TemplateCommentTests(SimpleTestCase):
    """`{# ... #}` comments must stay on one line.

    Django only treats `{# #}` as a comment within a single line — a multi-line
    one is emitted as visible page text. That shipped twice: a note about the
    `noindex` directive printed at the top of every de-indexed page, and one
    about the reviews marquee printed on every page including it.
    Multi-line notes belong in `{% comment %}...{% endcomment %}`.
    """

    def test_no_multiline_hash_comments(self):
        offenders = []
        for root in TEMPLATE_DIRS:
            for path in sorted(root.rglob("*.html")):
                text = path.read_text()
                for match in re.finditer(r"\{#", text):
                    close = text.find("#}", match.start())
                    if close == -1:
                        continue
                    if "\n" in text[match.start():close]:
                        line = text[:match.start()].count("\n") + 1
                        offenders.append(f"{path.relative_to(root)}:{line}")
        self.assertEqual(
            offenders, [],
            "Multi-line {# #} comments render as visible text; use "
            "{% comment %}...{% endcomment %} instead:\n  " + "\n  ".join(offenders),
        )


class StaticAssetTests(SimpleTestCase):
    """Assets referenced by the templates must exist.

    `{% static %}` on a missing file raises "Missing staticfiles manifest entry"
    under ManifestStaticFilesStorage — a hard 500 in production, invisible in
    development. A stale reference to the deleted img/1.svg..6.svg logos sat in
    the service-section template exactly this way.
    """

    def test_referenced_static_images_exist(self):
        from django.contrib.staticfiles import finders

        literal = re.compile(r"\{%\s*static\s+['\"]([^'\"]+)['\"]\s*%\}")
        missing = []
        for root in TEMPLATE_DIRS:
            for path in sorted(root.rglob("*.html")):
                for rel in literal.findall(path.read_text()):
                    if not finders.find(rel):
                        missing.append(f"{path.relative_to(root)} -> {rel}")
        self.assertEqual(missing, [], "Missing static files:\n  " + "\n  ".join(missing))

    def test_page_weight_assets_stay_small(self):
        """The favicon and logo load on every page, so cap them tightly."""
        base = Path(settings.BASE_DIR) / "static" / "img"
        budgets = {
            "favicon-32.png": 8 * 1024,
            "favicon-192.png": 24 * 1024,
            "apple-touch-icon.png": 24 * 1024,
            "brockwell-healthcare-logo.png": 32 * 1024,
        }
        for name, budget in budgets.items():
            path = base / name
            self.assertTrue(path.exists(), f"{name} is missing")
            self.assertLessEqual(
                path.stat().st_size, budget,
                f"{name} is {path.stat().st_size // 1024}kb, budget "
                f"{budget // 1024}kb — it is fetched on every page.",
            )
