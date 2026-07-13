from django.contrib import admin

from .models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "state", "region", "is_primary", "is_active", "order")
    list_filter = ("region", "state", "is_active", "is_primary")
    search_fields = ("name", "city", "state", "street_address")
    prepopulated_fields = {"slug": ("city",)}
    filter_horizontal = ("doctors",)
    list_editable = ("order", "is_primary", "is_active")
    fieldsets = (
        (None, {"fields": ("name", "slug", ("region", "is_primary", "is_active"), "order")}),
        ("Location", {"fields": (("city", "state", "state_code"), "street_address",
                                 "postal_code")}),
        ("Contact", {"fields": (("phone", "email"), "hours")}),
        ("Map", {"fields": (("latitude", "longitude"), "map_url"), "classes": ("collapse",)}),
        ("Content", {"fields": ("hero", "intro", "about", "doctors")}),
        ("SEO", {"fields": ("seo_title", "seo_description"), "classes": ("collapse",)}),
    )
