from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "region", "price", "order", "is_published")
    list_filter = ("region", "is_published")
    search_fields = ("name", "summary", "description")
    list_editable = ("order", "is_published")
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (None, {"fields": ("region", "name", "slug", "icon", "summary", "order", "is_published")}),
        ("Content", {"fields": ("description", "benefits", "price")}),
        ("SEO (optional)", {"fields": ("seo_title", "seo_description"), "classes": ("collapse",)}),
    )
