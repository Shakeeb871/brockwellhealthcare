from django.contrib import admin
from django.db.models import Count, Sum
from tinymce.widgets import TinyMCE

from .models import Event, EventPackage, EventRegistration, OnlinePayment


class RegistrationInline(admin.TabularInline):
    model = EventRegistration
    extra = 0
    fields = ("name", "email", "phone", "package", "amount", "currency", "paid", "source", "created_at")
    readonly_fields = fields
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
    """Enquiry-form leads — people who submitted a form (not online payments)."""

    list_display = ("name", "event", "email", "phone", "paid", "created_at")
    list_filter = ("paid", "event__region", "created_at")
    search_fields = ("name", "email", "phone")
    readonly_fields = ("created_at", "updated_at", "stripe_session_id", "source")
    date_hierarchy = "created_at"

    def get_queryset(self, request):
        return super().get_queryset(request).filter(source=EventRegistration.SOURCE_FORM)


@admin.register(OnlinePayment)
class OnlinePaymentAdmin(admin.ModelAdmin):
    """Online Payments dashboard — bookings paid through Stripe, with a revenue
    and tier-sales summary on top."""

    change_list_template = "admin/events/onlinepayment/change_list.html"
    list_display = ("created_at", "name", "email", "phone", "event", "tier", "amount_display", "paid")
    list_filter = ("paid", "event__region", "package", "created_at")
    search_fields = ("name", "email", "phone", "stripe_session_id")
    readonly_fields = (
        "event", "package", "name", "email", "phone", "amount", "currency",
        "paid", "source", "stripe_session_id", "created_at", "updated_at",
    )
    date_hierarchy = "created_at"

    def has_add_permission(self, request):
        return False  # created by the payment webhook, not by hand

    def get_queryset(self, request):
        return super().get_queryset(request).filter(source=EventRegistration.SOURCE_ONLINE)

    @admin.display(description="Tier")
    def tier(self, obj):
        return obj.package.name if obj.package else "—"

    @admin.display(description="Amount")
    def amount_display(self, obj):
        return f"{obj.currency} {obj.amount:,.0f}"

    def changelist_view(self, request, extra_context=None):
        qs = self.get_queryset(request)
        paid = qs.filter(paid=True)
        by_tier = list(
            paid.values("package__name")
            .annotate(n=Count("id"), total=Sum("amount"))
            .order_by("-total")
        )
        summary = {
            "total_revenue": paid.aggregate(s=Sum("amount"))["s"] or 0,
            "paid_count": paid.count(),
            "pending_count": qs.filter(paid=False).count(),
            "currency": paid.values_list("currency", flat=True).first() or "",
            "by_tier": by_tier,
        }
        extra_context = {**(extra_context or {}), "payment_summary": summary}
        return super().changelist_view(request, extra_context)
