from django.contrib import admin
from tinymce.widgets import TinyMCE

from core.admin import FAQItemInline
from .models import Service, ServiceCategory


# Shown above the content editor so editors always know how the plain text they
# type turns into the site's designed sections — no extra settings required.
CONTENT_HELP = (
    '<div style="max-width:74ch;line-height:1.6;background:#f4f8f2;'
    'border:1px solid #dbe7d6;border-radius:8px;padding:12px 14px">'
    '<p style="margin:0 0 .5rem"><strong>How this content becomes designed '
    'sections</strong> — just type in the editor below. The website styles it '
    'automatically; there are no separate section settings.</p>'
    '<ul style="margin:0;padding-left:1.15rem">'
    '<li><strong>Process timeline</strong> (numbered steps): make each step a '
    '<strong>Heading&nbsp;3</strong> written as <code>Step 1: Title</code>, then a '
    'normal paragraph under it. Two or more in a row become a numbered timeline.</li>'
    '<li><strong>Card grid</strong> (e.g. &ldquo;Types of&hellip;&rdquo;): write '
    'three or more items in a row, each a <strong>Heading&nbsp;3</strong> (the name) '
    'followed by a paragraph. They render as cards with an auto-picked icon.</li>'
    '<li><strong>Icon list</strong>: any bullet list becomes a professional '
    'check-circle list automatically.</li>'
    '<li>Everything else (Heading&nbsp;2, paragraphs, images, quotes) renders in the '
    'site&rsquo;s standard style.</li>'
    '</ul></div>'
)


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
    can_delete = True


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(RichDescriptionMixin, admin.ModelAdmin):
    list_display = ("name", "region", "order", "is_published")
    list_filter = ("region", "is_published")
    search_fields = ("name", "summary", "description")
    list_editable = ("order", "is_published")
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True
    inlines = [ServiceInline, FAQItemInline]
    fieldsets = (
        (None, {"fields": ("region", "name", "slug", "icon", "image", "summary", "order", "is_published")}),
        ("Content", {"fields": ("description",), "description": CONTENT_HELP}),
        ("SEO (optional)", {"fields": ("seo_title", "seo_description"), "classes": ("collapse",)}),
        ("Custom code / schema", {"fields": ("custom_head",), "classes": ("collapse",)}),
    )


@admin.register(Service)
class ServiceAdmin(RichDescriptionMixin, admin.ModelAdmin):
    list_display = ("name", "category", "region", "price", "order", "is_published")
    list_filter = ("region", "category", "is_published")
    search_fields = ("name", "summary", "description")
    list_editable = ("order", "is_published")
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True
    inlines = [FAQItemInline]
    fieldsets = (
        (None, {"fields": ("region", "category", "name", "slug", "icon", "image", "summary", "order", "is_published")}),
        ("Content", {"fields": ("description", "benefits", "price"), "description": CONTENT_HELP}),
        ("SEO (optional)", {"fields": ("seo_title", "seo_description"), "classes": ("collapse",)}),
        ("Custom code / schema", {"fields": ("custom_head",), "classes": ("collapse",)}),
    )
