"""Admin for the clinic management system.

This gives staff a fully usable back-office out of the box (add patients,
book appointments, record encounters + prescriptions, raise invoices) before
the dedicated front-end dashboards land.
"""

from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Appointment,
    Encounter,
    Invoice,
    InvoiceItem,
    Patient,
    PrescriptionItem,
    StaffProfile,
)


@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "doctor", "region", "is_active")
    list_filter = ("role", "region", "is_active")
    search_fields = ("user__username", "user__first_name", "user__last_name", "user__email")
    autocomplete_fields = ("doctor",)
    raw_id_fields = ("user",)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "email", "gender", "age", "region", "is_active")
    list_filter = ("region", "gender", "blood_group", "is_active")
    search_fields = ("first_name", "last_name", "email", "phone")
    raw_id_fields = ("user",)
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Identity", {"fields": (("first_name", "last_name"), ("email", "phone"),
                                 ("gender", "date_of_birth", "blood_group"), "address")}),
        ("Portal & region", {"fields": ("user", "region", "is_active")}),
        ("Emergency contact", {"fields": ("emergency_contact_name", "emergency_contact_phone")}),
        ("Medical", {"fields": ("allergies", "medical_history", "notes")}),
        ("Meta", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )

    @admin.display(description="Age")
    def age(self, obj):
        return obj.age if obj.age is not None else "—"


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("start", "patient", "doctor", "status", "source", "region")
    list_filter = ("status", "region", "source", "doctor")
    search_fields = ("patient__first_name", "patient__last_name", "doctor__name", "reason")
    autocomplete_fields = ("patient", "doctor")
    date_hierarchy = "start"
    list_select_related = ("patient", "doctor")
    readonly_fields = ("created_at", "updated_at", "created_by")


class PrescriptionItemInline(admin.TabularInline):
    model = PrescriptionItem
    extra = 1


@admin.register(Encounter)
class EncounterAdmin(admin.ModelAdmin):
    list_display = ("date", "patient", "doctor", "diagnosis_short", "region")
    list_filter = ("region", "doctor")
    search_fields = ("patient__first_name", "patient__last_name", "diagnosis", "complaint")
    autocomplete_fields = ("patient", "doctor", "appointment")
    date_hierarchy = "date"
    inlines = [PrescriptionItemInline]
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (None, {"fields": (("patient", "doctor"), ("appointment", "date"), "region")}),
        ("Consultation", {"fields": ("complaint", "observations", "diagnosis", "advice")}),
        ("Vitals", {"fields": (("blood_pressure", "pulse", "temperature"),
                               ("weight_kg", "height_cm"))}),
        ("Follow-up", {"fields": ("follow_up_date",)}),
        ("Meta", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )

    @admin.display(description="Diagnosis")
    def diagnosis_short(self, obj):
        return (obj.diagnosis[:60] + "…") if len(obj.diagnosis) > 60 else (obj.diagnosis or "—")


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("number", "patient", "date", "status", "total_display", "region")
    list_filter = ("status", "region", "date")
    search_fields = ("number", "patient__first_name", "patient__last_name")
    autocomplete_fields = ("patient", "appointment", "encounter")
    date_hierarchy = "date"
    inlines = [InvoiceItemInline]
    readonly_fields = ("number", "stripe_session_id", "paid_at", "created_at", "updated_at",
                       "subtotal_display", "tax_display", "total_display")
    fieldsets = (
        (None, {"fields": ("number", ("patient", "date"), "status", "region")}),
        ("Links", {"fields": ("appointment", "encounter"), "classes": ("collapse",)}),
        ("Amounts", {"fields": (("currency", "tax_percent"),
                                ("subtotal_display", "tax_display", "total_display"))}),
        ("Payment", {"fields": ("stripe_session_id", "paid_at"), "classes": ("collapse",)}),
        ("Notes", {"fields": ("notes",)}),
    )

    @admin.display(description="Subtotal")
    def subtotal_display(self, obj):
        return f"{obj.currency} {obj.subtotal:,.2f}"

    @admin.display(description="Tax")
    def tax_display(self, obj):
        return f"{obj.currency} {obj.tax_amount:,.2f}"

    @admin.display(description="Total")
    def total_display(self, obj):
        return format_html("<b>{} {:,.2f}</b>", obj.currency, obj.total)
