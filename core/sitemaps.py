"""Region-aware XML sitemaps for every enabled region.

These are served as a **sitemap index** (``/sitemap.xml``) that points at one
sitemap per content type (``/sitemap-main.xml``, ``/sitemap-services.xml``,
``/sitemap-blog.xml``, …). Splitting by type is the recommended structure: it
lets Search Console report indexing coverage per section, so you can see at a
glance which content type has a problem, and it scales as the site grows.
"""

from django.contrib.sitemaps import Sitemap

from blog.models import BlogCategory, BlogPost
from events.models import Event
from locations.models import Location
from services.models import Service, ServiceCategory
from team.models import Doctor

from .models import Page
from .regions import indexable_regions, region_path, region_prefix


def _codes():
    # Only list URLs for regions that are actually indexable, so the sitemap
    # never advertises de-indexed (noindex) pages.
    return [r["code"] for r in indexable_regions()]


class _ModelSitemap(Sitemap):
    """Base for sitemaps built from published, region-scoped models."""

    protocol = "https"

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return getattr(obj, "updated_at", None)


# --------------------------------------------------------------------------- #
# 1. Main pages — home, about, contact, the section landing pages and legal
# --------------------------------------------------------------------------- #
class MainSitemap(Sitemap):
    """Home + key landing pages, plus the editable legal pages.

    Items are either ``(region_code, url_name)`` tuples for routed views or
    ``Page`` instances, so ``location``/``lastmod`` dispatch on the type.
    """

    changefreq = "weekly"
    priority = 0.9
    protocol = "https"

    ROUTES = [
        "core:home", "core:about", "core:contact",
        "services:list", "events:list", "team:list", "blog:list",
        "locations:list",
    ]

    def items(self):
        routed = [
            (region["code"], name)
            for region in indexable_regions()
            for name in self.ROUTES
        ]
        legal = list(Page.objects.filter(region__in=_codes(), is_published=True))
        return routed + legal

    def location(self, item):
        if isinstance(item, tuple):
            region_code, name = item
            return region_path(region_code, name)
        return f"{region_prefix(item.region)}/{item.slug}/"

    def lastmod(self, item):
        return None if isinstance(item, tuple) else item.updated_at

    def priority(self, item):  # noqa: D401 - Django calls this per item
        """Home ranks highest, landing pages next, legal pages lowest."""
        if isinstance(item, tuple):
            return 1.0 if item[1] == "core:home" else 0.9
        return 0.3


# --------------------------------------------------------------------------- #
# 2. Services — categories and every published service/sub-service
# --------------------------------------------------------------------------- #
class ServicesSitemap(_ModelSitemap):
    changefreq = "monthly"

    def items(self):
        codes = _codes()
        cats = list(ServiceCategory.objects.filter(region__in=codes, is_published=True))
        svcs = list(Service.objects.filter(region__in=codes, is_published=True))
        return cats + svcs

    def priority(self, obj):
        # Category hubs carry more weight than individual services.
        return 0.8 if isinstance(obj, ServiceCategory) else 0.7


# --------------------------------------------------------------------------- #
# 3. Events
# --------------------------------------------------------------------------- #
class EventsSitemap(_ModelSitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return list(Event.objects.filter(region__in=_codes(), is_published=True))


# --------------------------------------------------------------------------- #
# 4. Blog — posts and category archives
# --------------------------------------------------------------------------- #
class BlogSitemap(_ModelSitemap):
    changefreq = "weekly"

    def items(self):
        codes = _codes()
        posts = list(BlogPost.objects.filter(region__in=codes, is_published=True))
        cats = list(BlogCategory.objects.filter(region__in=codes, is_published=True))
        return posts + cats

    def priority(self, obj):
        return 0.7 if isinstance(obj, BlogPost) else 0.5


# --------------------------------------------------------------------------- #
# 5. Team
# --------------------------------------------------------------------------- #
class TeamSitemap(_ModelSitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return list(Doctor.objects.filter(region__in=_codes(), is_published=True))


# --------------------------------------------------------------------------- #
# 6. Locations (local SEO)
# --------------------------------------------------------------------------- #
class LocationsSitemap(_ModelSitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return list(Location.objects.filter(region__in=_codes(), is_active=True))


# Section name -> sitemap. The keys become the child sitemap filenames, e.g.
# "services" -> /sitemap-services.xml, and are what Search Console reports on.
sitemaps = {
    "main": MainSitemap,
    "services": ServicesSitemap,
    "events": EventsSitemap,
    "blog": BlogSitemap,
    "team": TeamSitemap,
    "locations": LocationsSitemap,
}


def non_empty_sitemaps():
    """The sections that currently have URLs.

    Used for the index so it never advertises an empty child sitemap (Search
    Console flags those as "sitemap is empty"). The child URLs themselves stay
    routable, so an empty section simply isn't listed until it has content.
    """
    live = {}
    for name, cls in sitemaps.items():
        try:
            if cls().items():
                live[name] = cls
        except Exception:
            live[name] = cls
    return live
