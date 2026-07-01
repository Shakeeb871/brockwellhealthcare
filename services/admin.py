from django.contrib import admin
from tinymce.widgets import TinyMCE

from .models import Service, ServiceCategory


class RichDescriptionMixin:
    """Render the model's ``description`` field with the TinyMCE editor."""

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "description":
            kwargs["widget"] = TinyMCE()
        return super().formfield_for_dbfield(db_field, request, **kwargs)


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 0
    fields = ("name", "slug", "order", "is_published")
    prepopulated_fields = {"slug": ("name",)}
    show_change_link = True


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(RichDescriptionMixin, admin.ModelAdmin):
    list_display = ("name", "region", "order", "is_published")
    list_filter = ("region", "is_published")
    search_fields = ("name", "summary", "description")
    list_editable = ("order", "is_published")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ServiceInline]
    fieldsets = (
        (None, {"fields": ("region", "name", "slug", "icon", "image", "summary", "order", "is_published")}),
        ("Content", {"fields": ("description",)}),
        ("SEO (optional)", {"fields": ("seo_title", "seo_description"), "classes": ("collapse",)}),
    )


@admin.register(Service)
class ServiceAdmin(RichDescriptionMixin, admin.ModelAdmin):
    list_display = ("name", "category", "region", "price", "order", "is_published")
    list_filter = ("region", "category", "is_published")
    search_fields = ("name", "summary", "description")
    list_editable = ("order", "is_published")
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (None, {"fields": ("region", "category", "name", "slug", "icon", "image", "summary", "order", "is_published")}),
        ("Content", {"fields": ("description", "benefits", "price")}),
        ("SEO (optional)", {"fields": ("seo_title", "seo_description"), "classes": ("collapse",)}),
    )
