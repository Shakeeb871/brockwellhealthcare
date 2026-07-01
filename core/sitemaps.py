"""Region-aware XML sitemaps for every enabled region."""

from django.contrib.sitemaps import Sitemap

from blog.models import BlogCategory, BlogPost
from events.models import Event
from services.models import Service, ServiceCategory
from team.models import Doctor

from .models import Page
from .regions import enabled_regions, region_path


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        pages = [
            "core:home", "core:about", "core:contact",
            "services:list", "events:list", "team:list", "blog:list",
        ]
        return [
            (region["code"], name)
            for region in enabled_regions()
            for name in pages
        ]

    def location(self, item):
        region_code, name = item
        return region_path(region_code, name)


def _codes():
    return [r["code"] for r in enabled_regions()]


class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return list(ServiceCategory.objects.filter(region__in=_codes(), is_published=True))

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.updated_at


class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7
    protocol = "https"

    def items(self):
        return list(Service.objects.filter(region__in=_codes(), is_published=True))

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.updated_at


class DoctorSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6
    protocol = "https"

    def items(self):
        return list(Doctor.objects.filter(region__in=_codes(), is_published=True))

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.updated_at


class EventSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    protocol = "https"

    def items(self):
        return list(Event.objects.filter(region__in=_codes(), is_published=True))

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.updated_at


class PageSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.3
    protocol = "https"

    def items(self):
        return list(Page.objects.filter(region__in=_codes(), is_published=True))

    def location(self, obj):
        return f"/{obj.region}/{obj.slug}/"

    def lastmod(self, obj):
        return obj.updated_at


class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    protocol = "https"

    def items(self):
        return list(BlogPost.objects.filter(region__in=_codes(), is_published=True))

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.updated_at


class BlogCategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    protocol = "https"

    def items(self):
        return list(BlogCategory.objects.filter(region__in=_codes(), is_published=True))

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.updated_at


sitemaps = {
    "static": StaticViewSitemap,
    "categories": CategorySitemap,
    "services": ServiceSitemap,
    "team": DoctorSitemap,
    "events": EventSitemap,
    "pages": PageSitemap,
    "blog": BlogPostSitemap,
    "blog_categories": BlogCategorySitemap,
}
