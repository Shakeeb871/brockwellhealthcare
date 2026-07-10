from django.contrib import admin
from tinymce.widgets import TinyMCE

from .models import Event, EventPackage, EventRegistration


class RegistrationInline(admin.TabularInline):
    model = EventRegistration
    extra = 0
    readonly_fields = ("name", "email", "phone", "amount", "currency", "paid", "created_at")
    can_delete = False


class PackageInline(admin.StackedInline):
    model = EventPackage
    extra = 0
    prepopulated_fields = {"slug": ("name",)}
    fields = ("name", "slug", "amount", "features", "badge", "is_featured", "is_active", "sort")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "region", "start", "location", "price", "is_published")
    list_filter = ("region", "is_published", "start")
    search_fields = ("title", "summary", "description", "location")
    list_editable = ("is_published",)
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "start"
    inlines = [PackageInline, RegistrationInline]
    fieldsets = (
        (None, {"fields": ("region", "title", "slug", "image", "summary", "is_published")}),
        ("Schedule & Venue", {"fields": ("start", "end", "location", "capacity")}),
        ("Content & Pricing", {"fields": ("description", "price")}),
        ("SEO (optional)", {"fields": ("seo_title", "seo_description"), "classes": ("collapse",)}),
    )

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "description":
            kwargs["widget"] = TinyMCE()
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ("name", "event", "amount", "currency", "paid", "created_at")
    list_filter = ("paid", "event__region", "created_at")
    search_fields = ("name", "email", "phone")
    readonly_fields = ("created_at", "updated_at", "stripe_session_id")
