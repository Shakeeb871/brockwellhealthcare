from django.contrib import admin
from tinymce.widgets import TinyMCE

from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "region", "available_today", "order", "is_published")
    list_filter = ("region", "is_published", "available_today")
    search_fields = ("name", "title", "short_bio", "full_bio")
    list_editable = ("available_today", "order", "is_published")
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (None, {"fields": ("region", "name", "slug", "title", "credentials", "photo", "order", "is_published")}),
        ("Details", {"fields": ("experience", "languages", "available_today")}),
        ("Profile", {"fields": ("short_bio", "full_bio", "specialties")}),
        ("SEO (optional)", {"fields": ("seo_title", "seo_description"), "classes": ("collapse",)}),
    )

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "full_bio":
            kwargs["widget"] = TinyMCE()
        return super().formfield_for_dbfield(db_field, request, **kwargs)
