"""Patient & Clinic Management System.

A KiviCare-style back-office layered on top of the existing site: patients,
appointments, clinical encounters (notes + prescriptions) and billing. It
reuses the project's built-in Django auth for roles and the public
``team.Doctor`` records for clinicians.

Roles
-----
* **Patient**   — a ``Patient`` row, optionally linked to a ``User`` for the
  self-service portal (book, view history, pay invoices).
* **Staff**     — a ``StaffProfile`` linking a ``User`` to a role
  (doctor / receptionist / clinic admin). Doctors also link to their public
  ``team.Doctor`` profile.
"""

from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from core.models import REGION_CHOICES, TimeStamped
from team.models import Doctor


# --------------------------------------------------------------------------- #
# Shared choices
# --------------------------------------------------------------------------- #
GENDER_CHOICES = [("male", "Male"), ("female", "Female"), ("other", "Other")]
BLOOD_GROUPS = [(g, g) for g in ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")]


# --------------------------------------------------------------------------- #
# People & roles
# --------------------------------------------------------------------------- #
class StaffProfile(TimeStamped):
    """Marks a ``User`` as clinic staff and records their role."""

    ROLE_DOCTOR = "doctor"
    ROLE_RECEPTION = "reception"
    ROLE_ADMIN = "admin"
    ROLE_CHOICES = [
        (ROLE_DOCTOR, "Doctor"),
        (ROLE_RECEPTION, "Receptionist"),
        (ROLE_ADMIN, "Clinic Admin"),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="clinic_staff"
    )
    role = models.CharField(max_length=16, choices=ROLE_CHOICES, default=ROLE_RECEPTION)
    doctor = models.ForeignKey(
        Doctor, null=True, blank=True, on_delete=models.SET_NULL,
        related_name="staff_profiles",
        help_text="For doctors — link to the public Doctor profile.",
    )
    phone = models.CharField(max_length=40, blank=True)
    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="us")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["role", "user__first_name"]

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} ({self.get_role_display()})"


class Patient(TimeStamped):
    """A patient record (EHR). May optionally own a ``User`` for portal login."""

    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.SET_NULL,
        related_name="patient_profile",
        help_text="Optional — link a login account so the patient can use the portal.",
    )
    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="us")

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=40, blank=True)

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=4, choices=BLOOD_GROUPS, blank=True)
    address = models.CharField(max_length=255, blank=True)

    emergency_contact_name = models.CharField(max_length=120, blank=True)
    emergency_contact_phone = models.CharField(max_length=40, blank=True)

    allergies = models.TextField(blank=True, help_text="Known allergies, one per line.")
    medical_history = models.TextField(blank=True, help_text="Chronic conditions, past history.")
    notes = models.TextField(blank=True, help_text="Internal staff notes.")

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["first_name", "last_name"]
        indexes = [models.Index(fields=["region", "is_active"])]

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def age(self):
        if not self.date_of_birth:
            return None
        today = timezone.localdate()
        born = self.date_of_birth
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


# --------------------------------------------------------------------------- #
# Appointments
# --------------------------------------------------------------------------- #
class Appointment(TimeStamped):
    """A scheduled visit between a patient and a doctor."""

    STATUS_REQUESTED = "requested"
    STATUS_CONFIRMED = "confirmed"
    STATUS_COMPLETED = "completed"
    STATUS_CANCELLED = "cancelled"
    STATUS_NO_SHOW = "no_show"
    STATUS_CHOICES = [
        (STATUS_REQUESTED, "Requested"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_CANCELLED, "Cancelled"),
        (STATUS_NO_SHOW, "No-show"),
    ]

    SOURCE_ONLINE = "online"
    SOURCE_PHONE = "phone"
    SOURCE_WALK_IN = "walk_in"
    SOURCE_CHOICES = [
        (SOURCE_ONLINE, "Online (portal)"),
        (SOURCE_PHONE, "Phone"),
        (SOURCE_WALK_IN, "Walk-in"),
    ]

    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="us")
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="appointments"
    )
    doctor = models.ForeignKey(
        Doctor, on_delete=models.PROTECT, related_name="appointments"
    )

    start = models.DateTimeField(db_index=True)
    duration_minutes = models.PositiveIntegerField(default=30)
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_REQUESTED, db_index=True
    )
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES, default=SOURCE_WALK_IN)

    reason = models.CharField(max_length=200, blank=True, help_text="Reason for visit / service.")
    notes = models.TextField(blank=True)

    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL,
        related_name="appointments_created",
    )

    class Meta:
        ordering = ["-start"]
        indexes = [models.Index(fields=["region", "status", "start"])]

    def __str__(self):
        when = timezone.localtime(self.start).strftime("%d %b %Y %H:%M") if self.start else "—"
        return f"{self.patient.full_name} · Dr {self.doctor.name} · {when}"

    @property
    def end(self):
        if not self.start:
            return None
        return self.start + timezone.timedelta(minutes=self.duration_minutes)

    @property
    def is_upcoming(self):
        return bool(self.start and self.start >= timezone.now()
                    and self.status in (self.STATUS_REQUESTED, self.STATUS_CONFIRMED))


# --------------------------------------------------------------------------- #
# Clinical encounters (consultation notes + prescription)
# --------------------------------------------------------------------------- #
class Encounter(TimeStamped):
    """A consultation record: complaint, vitals, diagnosis and notes.

    A prescription (if any) hangs off this via ``PrescriptionItem`` rows.
    """

    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="us")
    appointment = models.OneToOneField(
        Appointment, null=True, blank=True, on_delete=models.SET_NULL,
        related_name="encounter",
    )
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="encounters"
    )
    doctor = models.ForeignKey(
        Doctor, on_delete=models.PROTECT, related_name="encounters"
    )
    date = models.DateTimeField(default=timezone.now, db_index=True)

    complaint = models.TextField(blank=True, help_text="Presenting complaint / symptoms.")
    observations = models.TextField(blank=True, help_text="Examination findings.")
    diagnosis = models.TextField(blank=True)
    advice = models.TextField(blank=True, help_text="Advice / plan.")

    # Vitals
    blood_pressure = models.CharField(max_length=20, blank=True, help_text="e.g. 120/80")
    pulse = models.CharField(max_length=20, blank=True, help_text="bpm")
    temperature = models.CharField(max_length=20, blank=True, help_text="°C / °F")
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    follow_up_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"Encounter · {self.patient.full_name} · {timezone.localtime(self.date).strftime('%d %b %Y')}"


class PrescriptionItem(models.Model):
    """A single prescribed medicine on an encounter."""

    encounter = models.ForeignKey(
        Encounter, on_delete=models.CASCADE, related_name="prescription_items"
    )
    drug_name = models.CharField(max_length=160)
    dosage = models.CharField(max_length=80, blank=True, help_text="e.g. 500 mg")
    frequency = models.CharField(max_length=80, blank=True, help_text="e.g. Twice daily")
    duration = models.CharField(max_length=80, blank=True, help_text="e.g. 7 days")
    instructions = models.CharField(max_length=200, blank=True, help_text="e.g. After food")
    sort = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort", "id"]

    def __str__(self):
        return self.drug_name


# --------------------------------------------------------------------------- #
# Billing
# --------------------------------------------------------------------------- #
class Invoice(TimeStamped):
    """A patient invoice. Payable online via Stripe or marked paid by staff."""

    STATUS_DRAFT = "draft"
    STATUS_UNPAID = "unpaid"
    STATUS_PAID = "paid"
    STATUS_CANCELLED = "cancelled"
    STATUS_CHOICES = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_UNPAID, "Unpaid"),
        (STATUS_PAID, "Paid"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="us")
    number = models.CharField(max_length=24, unique=True, blank=True, db_index=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.PROTECT, related_name="invoices"
    )
    appointment = models.ForeignKey(
        Appointment, null=True, blank=True, on_delete=models.SET_NULL,
        related_name="invoices",
    )
    encounter = models.ForeignKey(
        Encounter, null=True, blank=True, on_delete=models.SET_NULL,
        related_name="invoices",
    )

    date = models.DateField(default=timezone.localdate)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STATUS_DRAFT, db_index=True
    )
    currency = models.CharField(max_length=8, default="USD")
    tax_percent = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal("0"))
    notes = models.TextField(blank=True)

    stripe_session_id = models.CharField(max_length=200, blank=True)
    paid_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-date", "-id"]
        indexes = [models.Index(fields=["region", "status"])]

    def __str__(self):
        return f"{self.number or 'INV'} · {self.patient.full_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.number:
            # Assign a stable, human-friendly number once we have a PK.
            Invoice.objects.filter(pk=self.pk).update(number=f"INV-{self.pk:05d}")
            self.number = f"INV-{self.pk:05d}"

    @property
    def subtotal(self):
        return sum((i.amount for i in self.items.all()), Decimal("0"))

    @property
    def tax_amount(self):
        return (self.subtotal * self.tax_percent / Decimal("100")).quantize(Decimal("0.01"))

    @property
    def total(self):
        return (self.subtotal + self.tax_amount).quantize(Decimal("0.01"))


class InvoiceItem(models.Model):
    """A line on an invoice."""

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="items")
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0"))
    sort = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort", "id"]

    def __str__(self):
        return self.description

    @property
    def amount(self):
        return (Decimal(self.quantity) * self.unit_price).quantize(Decimal("0.01"))
