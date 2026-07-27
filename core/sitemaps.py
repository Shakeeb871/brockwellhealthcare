"""Region-aware XML sitemaps — split per country AND per content type.

Served as a **sitemap index** at ``/sitemap.xml`` pointing at one sitemap per
country/content-type pair::

    /sitemap-uae-main.xml       /sitemap-us-main.xml
    /sitemap-uae-services.xml   /sitemap-us-services.xml
    /sitemap-uae-blog.xml       /sitemap-us-blog.xml
    …

Country-first is the right structure for an international site: Search Console
reports coverage per country *and* per section, so "UAE blog isn't indexing"
is visible immediately, and each market can be diagnosed on its own. Sections
are generated from ``settings.REGIONS``, so adding a country adds its sitemaps
automatically — no code changes.

A region that isn't indexable yields empty sitemaps and is left out of the
index entirely, so a de-indexed market is never advertised.
"""

from django.conf import settings
from django.contrib.sitemaps import Sitemap

from blog.models import BlogCategory, BlogPost
from events.models import Event
from locations.models import Location
from services.models import Service, ServiceCategory
from team.models import Doctor

from .models import Page
from .regions import region_indexable, region_path, region_prefix


class _RegionSitemap(Sitemap):
    """Base: every sitemap is scoped to a single region (country).

    ``region_code`` is set by the factory below. When that region isn't
    indexable the sitemap is empty, so nothing de-indexed is ever listed.
    """

    protocol = "https"
    region_code = None

    @property
    def _live(self):
        return region_indexable(self.region_code)

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return getattr(obj, "updated_at", None)


# --------------------------------------------------------------------------- #
# 1. Main pages — home, about, contact, section landing pages and legal
# --------------------------------------------------------------------------- #
class MainSitemap(_RegionSitemap):
    """Items are either ``url_name`` strings (routed views) or ``Page`` rows,
    so ``location``/``lastmod``/``priority`` dispatch on the type."""

    changefreq = "weekly"

    ROUTES = [
        "core:home", "core:about", "core:contact",
        "services:list", "events:list", "team:list", "blog:list",
        "locations:list",
    ]

    def items(self):
        if not self._live:
            return []
        legal = list(
            Page.objects.filter(region=self.region_code, is_published=True)
        )
        return list(self.ROUTES) + legal

    def location(self, item):
        if isinstance(item, str):
            return region_path(self.region_code, item)
        return f"{region_prefix(item.region)}/{item.slug}/"

    def lastmod(self, item):
        return None if isinstance(item, str) else item.updated_at

    def priority(self, item):
        if isinstance(item, str):
            return 1.0 if item == "core:home" else 0.9
        return 0.3


# --------------------------------------------------------------------------- #
# 2. Services — categories and every published service/sub-service
# --------------------------------------------------------------------------- #
class ServicesSitemap(_RegionSitemap):
    changefreq = "monthly"

    def items(self):
        if not self._live:
            return []
        cats = list(
            ServiceCategory.objects.filter(region=self.region_code, is_published=True)
        )
        svcs = list(
            Service.objects.filter(region=self.region_code, is_published=True)
        )
        return cats + svcs

    def priority(self, obj):
        # Category hubs carry more weight than individual services.
        return 0.8 if isinstance(obj, ServiceCategory) else 0.7


# --------------------------------------------------------------------------- #
# 3. Events
# --------------------------------------------------------------------------- #
class EventsSitemap(_RegionSitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        if not self._live:
            return []
        return list(Event.objects.filter(region=self.region_code, is_published=True))


# --------------------------------------------------------------------------- #
# 4. Blog — posts and category archives
# --------------------------------------------------------------------------- #
class BlogSitemap(_RegionSitemap):
    changefreq = "weekly"

    def items(self):
        if not self._live:
            return []
        posts = list(
            BlogPost.objects.filter(region=self.region_code, is_published=True)
        )
        cats = list(
            BlogCategory.objects.filter(region=self.region_code, is_published=True)
        )
        return posts + cats

    def priority(self, obj):
        return 0.7 if isinstance(obj, BlogPost) else 0.5


# --------------------------------------------------------------------------- #
# 5. Team
# --------------------------------------------------------------------------- #
class TeamSitemap(_RegionSitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        if not self._live:
            return []
        return list(Doctor.objects.filter(region=self.region_code, is_published=True))


# --------------------------------------------------------------------------- #
# 6. Locations (local SEO)
# --------------------------------------------------------------------------- #
class LocationsSitemap(_RegionSitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        if not self._live:
            return []
        return list(Location.objects.filter(region=self.region_code, is_active=True))


# --------------------------------------------------------------------------- #
# Build "<country>-<section>" sitemaps for every configured region
# --------------------------------------------------------------------------- #
SECTIONS = {
    "main": MainSitemap,
    "services": ServicesSitemap,
    "events": EventsSitemap,
    "blog": BlogSitemap,
    "team": TeamSitemap,
    "locations": LocationsSitemap,
}


def _build_sitemaps():
    """One sitemap per (region, section) — e.g. ``uae-services``.

    Generated from ``settings.REGIONS`` so a new country automatically gets its
    own full set of sitemaps with no code change.
    """
    built = {}
    for code in settings.REGIONS:
        for name, base in SECTIONS.items():
            built[f"{code}-{name}"] = type(
                f"{code.title()}{base.__name__}", (base,), {"region_code": code}
            )
    return built


sitemaps = _build_sitemaps()


def non_empty_sitemaps():
    """The sections that currently have URLs.

    Keeps de-indexed countries and empty sections out of the index (Search
    Console flags empty child sitemaps). The child URLs stay routable, so a
    section simply isn't listed until it has content.
    """
    live = {}
    for name, cls in sitemaps.items():
        try:
            if cls().items():
                live[name] = cls
        except Exception:
            live[name] = cls
    return live
