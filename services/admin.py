from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from tinymce.widgets import TinyMCE

from core.admin import FAQItemInline
from .models import PageSection, Service, ServiceCategory


class PageSectionInline(SortableStackedInline):
    """Drag-and-drop reorderable, pre-designed content blocks for a service."""

    model = PageSection
    extra = 0
    fields = (
        "kind", "background", "eyebrow", "heading", "body", "items",
        "image", "button_text", "button_url", "is_published",
    )
    verbose_name = "Content block"
    verbose_name_plural = "Content blocks — drag to reorder (this IS the page content)"

    class Media:
        js = ("admin/js/pagesection_fields.js",)

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "body":
            kwargs["widget"] = TinyMCE()
        return super().formfield_for_dbfield(db_field, request, **kwargs)


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
    inlines = [ServiceInline, FAQItemInline]
    fieldsets = (
        (None, {"fields": ("region", "name", "slug", "icon", "image", "summary", "order", "is_published")}),
        ("Content", {"fields": ("description",)}),
        ("SEO (optional)", {"fields": ("seo_title", "seo_description"), "classes": ("collapse",)}),
        ("Custom code / schema", {"fields": ("custom_head",), "classes": ("collapse",)}),
    )


@admin.register(Service)
class ServiceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ("name", "category", "region", "price", "order", "is_published")
    list_filter = ("region", "category", "is_published")
    search_fields = ("name", "summary", "description")
    list_editable = ("order", "is_published")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [PageSectionInline, FAQItemInline]
    fieldsets = (
        (None, {"fields": ("region", "category", "name", "slug", "icon", "image", "summary", "price", "order", "is_published")}),
        ("SEO (optional)", {"fields": ("seo_title", "seo_description"), "classes": ("collapse",)}),
        ("Custom code / schema", {"fields": ("custom_head",), "classes": ("collapse",)}),
    )
