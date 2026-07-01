from django.contrib import admin
from tinymce.widgets import TinyMCE

from core.admin import FAQItemInline
from .models import BlogCategory, BlogPost


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "region", "order", "is_published")
    list_filter = ("region", "is_published")
    search_fields = ("name", "description")
    list_editable = ("order", "is_published")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "region", "published_at", "is_published", "is_featured")
    list_filter = ("region", "category", "is_published", "is_featured")
    search_fields = ("title", "excerpt", "body", "author")
    list_editable = ("is_published", "is_featured")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"
    inlines = [FAQItemInline]
    fieldsets = (
        (None, {"fields": ("region", "category", "title", "slug", "image", "is_published", "is_featured")}),
        ("Content", {"fields": ("excerpt", "body", "author", "published_at")}),
        ("SEO (optional)", {"fields": ("seo_title", "seo_description"), "classes": ("collapse",)}),
        ("Custom code / schema", {"fields": ("custom_head",), "classes": ("collapse",)}),
    )

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "body":
            kwargs["widget"] = TinyMCE()
        return super().formfield_for_dbfield(db_field, request, **kwargs)
