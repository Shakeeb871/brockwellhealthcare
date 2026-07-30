"""Regression tests for whole-site rendering invariants.

These exist because each one has already shipped as a live bug once.
"""
import re
from pathlib import Path

from django.conf import settings
from django.test import SimpleTestCase, TestCase


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


class RootAssetRouteTests(SimpleTestCase):
    """Paths browsers fetch on their own must not 404.

    /favicon.ico is requested by every browser regardless of the <link rel="icon">
    tags, and it was unrouted — a 404 on essentially every visit. The manifest
    was likewise referenced by the CSP (`manifest-src 'self'`) and the
    theme-color meta but never served.
    """

    def test_favicon_ico_resolves(self):
        from django.test import Client

        response = Client().get("/favicon.ico")
        self.assertEqual(response.status_code, 301)
        self.assertIn("favicon", response["Location"])

    def test_webmanifest_is_served_and_valid(self):
        import json

        from django.test import Client

        response = Client().get("/site.webmanifest")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        for key in ("name", "short_name", "start_url", "icons", "theme_color"):
            self.assertIn(key, data)
        sizes = {icon["sizes"] for icon in data["icons"]}
        # 192 and 512 are what Android requires to treat the app as installable.
        self.assertTrue({"192x192", "512x512"} <= sizes, sizes)

    def test_webmanifest_is_not_region_redirected(self):
        """It is host-level: a UAE visitor must not be bounced to /uae/site.webmanifest."""
        from django.test import Client

        response = Client().get("/site.webmanifest", HTTP_CF_IPCOUNTRY="AE")
        self.assertEqual(response.status_code, 200)


class ResponseCompressionTests(TestCase):
    """HTML must go out compressed.

    WhiteNoise only compresses static files; without GZipMiddleware the pages
    themselves shipped raw, and the home page is ~192 kB of HTML.
    """

    def test_html_is_gzipped(self):
        from django.test import Client

        response = Client().get("/", HTTP_ACCEPT_ENCODING="gzip")
        self.assertEqual(response.get("Content-Encoding"), "gzip")
        self.assertIn("Accept-Encoding", response.get("Vary", ""))


class SelfHostedFontTests(SimpleTestCase):
    """Fonts must stay first-party.

    A third-party font stylesheet is render-blocking on a foreign origin, and
    it leaks visitor IPs to Google on every page view.
    """

    def test_no_third_party_font_requests(self):
        import re

        # Match an actual reference (href/src/url), not the word appearing in a
        # comment that explains why it is no longer used.
        ref = re.compile(r"""(?:href|src|url\()\s*=?\s*['"(]?[^'")]*fonts\.(?:googleapis|gstatic)\.com""")
        for path in TEMPLATE_DIRS[0].rglob("*.html"):
            hits = ref.findall(path.read_text())
            self.assertEqual(hits, [], f"{path} still loads Google Fonts: {hits}")

    def test_every_font_face_file_exists(self):
        import re

        from django.contrib.staticfiles import finders

        css = Path(settings.BASE_DIR) / "static" / "css" / "fonts.css"
        self.assertTrue(css.exists(), "static/css/fonts.css is missing")
        refs = re.findall(r"url\('\.\./(fonts/[^']+)'\)", css.read_text())
        self.assertTrue(refs, "fonts.css declares no font files")
        for rel in refs:
            self.assertTrue(finders.find(rel), f"missing font file: {rel}")


class ResponsiveCssTests(SimpleTestCase):
    """CSS invariants behind responsive bugs that reached production.

    A browser is needed to measure real overflow, so these assert the specific
    patterns that caused it — cheap to run and enough to catch a regression.
    """

    @property
    def css(self):
        return (Path(settings.BASE_DIR) / "static" / "css" / "styles.css").read_text()

    def test_auto_grid_tracks_cannot_exceed_container(self):
        """`minmax(300px, 1fr)` overflows a 320px phone; `minmax(min(300px,100%),1fr)` can't."""
        import re

        unguarded = re.findall(
            r"repeat\((?:auto-fill|auto-fit), ?minmax\(\d+px, ?1fr\)\)", self.css
        )
        self.assertEqual(
            unguarded, [],
            "Wrap the floor in min(<n>px, 100%) so the track can never be wider "
            f"than its container: {unguarded}",
        )

    def test_header_switches_before_desktop_layout_stops_fitting(self):
        """The brand + 8-link pill + search box need ~900px.

        They were only swapped for the hamburger below 720px, so at 768px (iPad
        portrait) the logo was pushed off the left edge and the page scrolled
        sideways by 128px.
        """
        import re

        css = self.css
        rule = ".mainbar__right .search { display: none; }"
        self.assertIn(rule, css, "could not find the rule hiding the desktop search")
        # Walk back to the @media that encloses it (a regex can't, because the
        # block contains nested rules with their own braces).
        before = css[: css.index(rule)]
        queries = re.findall(r"@media \(max-width: (\d+)px\) \{", before)
        self.assertTrue(queries, "the rule is not inside a max-width media query")
        self.assertGreaterEqual(
            int(queries[-1]), 900,
            "The desktop header must give way to the hamburger at 900px or wider — "
            f"found max-width: {queries[-1]}px.",
        )

    def test_catbar_clips_horizontally(self):
        """Its hidden dropdowns are laid out and made the document 15px wider."""
        block = self.css[self.css.index(".catbar {"):self.css.index(".catbar__inner")]
        self.assertIn("overflow-x: clip", block)
        # `clip` (not hidden/auto) so the panels can still escape downward.
        self.assertIn("overflow-y: visible", block)
