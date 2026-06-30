"""Region-aware XML sitemaps for every enabled region."""

from django.contrib.sitemaps import Sitemap

from events.models import Event
from services.models import Service

from .regions import enabled_regions, region_path


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        pages = ["core:home", "core:about", "core:contact", "services:list", "events:list"]
        return [
            (region["code"], name)
            for region in enabled_regions()
            for name in pages
        ]

    def location(self, item):
        region_code, name = item
        return region_path(region_code, name)

    def priority_for(self, name):
        return 1.0 if name.endswith("home") else 0.8


class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7
    protocol = "https"

    def items(self):
        codes = [r["code"] for r in enabled_regions()]
        return list(Service.objects.filter(region__in=codes, is_published=True))

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.updated_at


class EventSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    protocol = "https"

    def items(self):
        codes = [r["code"] for r in enabled_regions()]
        return list(Event.objects.filter(region__in=codes, is_published=True))

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.updated_at


sitemaps = {
    "static": StaticViewSitemap,
    "services": ServiceSitemap,
    "events": EventSitemap,
}
