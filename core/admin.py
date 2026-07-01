from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from tinymce.widgets import TinyMCE

from .models import ContactLead, FAQ, FAQItem, Page


class FAQItemInline(GenericStackedInline):
    """Per-object FAQ section — reusable on any content model's admin."""

    model = FAQItem
    extra = 1
    fields = ("question", "answer", "order", "is_published")
    ordering = ("order", "id")
    verbose_name = "FAQ"
    verbose_name_plural = "FAQs — shown below the content (with FAQ schema)"


@admin.register(ContactLead)
class ContactLeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "region", "handled", "created_at")
    list_filter = ("region", "handled", "created_at")
    search_fields = ("name", "email", "phone", "message")
    list_editable = ("handled",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "region", "order", "is_published")
    list_filter = ("region", "is_published")
    search_fields = ("question", "answer")
    list_editable = ("order", "is_published")


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "region", "is_published")
    list_filter = ("region", "is_published")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [FAQItemInline]
    fieldsets = (
        (None, {"fields": ("region", "slug", "title", "body", "is_published")}),
        ("SEO (optional)", {"fields": ("seo_title", "seo_description"), "classes": ("collapse",)}),
        ("Custom code / schema", {"fields": ("custom_head",), "classes": ("collapse",)}),
    )

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "body":
            kwargs["widget"] = TinyMCE()
        return super().formfield_for_dbfield(db_field, request, **kwargs)


admin.site.site_header = "Brockwell Healthcare — Site Administration"
admin.site.site_title = "Brockwell Admin"
admin.site.index_title = "Manage your website content"
