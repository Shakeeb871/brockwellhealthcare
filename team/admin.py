from django.contrib import admin

from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "region", "order", "is_published")
    list_filter = ("region", "is_published")
    search_fields = ("name", "title", "short_bio", "full_bio")
    list_editable = ("order", "is_published")
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (None, {"fields": ("region", "name", "slug", "title", "credentials", "photo", "order", "is_published")}),
        ("Profile", {"fields": ("short_bio", "full_bio", "specialties")}),
        ("SEO (optional)", {"fields": ("seo_title", "seo_description"), "classes": ("collapse",)}),
    )
