from django.db import models
from django.urls import reverse

from core.regions import region_prefix
from django.utils import timezone

from core.models import REGION_CHOICES, TimeStamped


class Event(TimeStamped):
    """A seminar / clinic event that visitors can register and pay for."""

    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="uae")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220)
    image = models.ImageField(
        upload_to="events/", blank=True, null=True,
        help_text="Optional event image shown on event cards.",
    )
    summary = models.CharField(max_length=255)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text="Ticket price in the region's currency. 0 = free.",
    )
    capacity = models.PositiveIntegerField(default=0, help_text="0 = unlimited.")
    is_published = models.BooleanField(default=True)

    seo_title = models.CharField(max_length=70, blank=True)
    seo_description = models.CharField(max_length=170, blank=True)

    class Meta:
        ordering = ["start"]
        unique_together = ("region", "slug")

    def __str__(self):
        return f"{self.title} [{self.region}]"

    def get_absolute_url(self):
        return region_prefix(self.region) + reverse("events:detail", kwargs={"slug": self.slug})

    @property
    def is_upcoming(self):
        return self.start >= timezone.now()

    @property
    def is_free(self):
        return self.price <= 0

    @property
    def paragraphs(self):
        return [p.strip() for p in self.description.split("\n\n") if p.strip()]


class EventPackage(TimeStamped):
    """A purchasable registration tier for an event (e.g. Early / Standard /
    VIP / Observer). The amount is the authoritative, server-side price used
    when creating the Stripe Checkout session — the browser never sends it."""

    event = models.ForeignKey(
        Event, related_name="packages", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2,
        help_text="Price in the event region's currency.",
    )
    features = models.TextField(
        blank=True, help_text="One inclusion per line — shown as a checklist.",
    )
    badge = models.CharField(
        max_length=40, blank=True,
        help_text="Optional ribbon label, e.g. 'Most complete'.",
    )
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    sort = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort", "amount"]
        unique_together = ("event", "slug")

    def __str__(self):
        return f"{self.name} — {self.event.title}"

    @property
    def feature_list(self):
        return [ln.strip() for ln in self.features.splitlines() if ln.strip()]


class EventRegistration(TimeStamped):
    """A booking for an event, optionally tied to a Stripe payment."""

    event = models.ForeignKey(
        Event, related_name="registrations", on_delete=models.CASCADE
    )
    package = models.ForeignKey(
        "EventPackage", related_name="registrations", on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=8, default="AED")
    stripe_session_id = models.CharField(max_length=255, blank=True, db_index=True)
    paid = models.BooleanField(default=False)

    SOURCE_FORM = "form"
    SOURCE_ONLINE = "online"
    SOURCE_CHOICES = [
        (SOURCE_FORM, "Enquiry form"),
        (SOURCE_ONLINE, "Online payment"),
    ]
    source = models.CharField(
        max_length=10, choices=SOURCE_CHOICES, default=SOURCE_FORM, db_index=True,
        help_text="How the booking came in — a form enquiry or a completed online payment.",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        status = "paid" if self.paid else "pending"
        return f"{self.name} → {self.event.title} ({status})"


class OnlinePayment(EventRegistration):
    """Proxy over EventRegistration for the Online Payments dashboard — the
    same rows, but the admin filters to bookings that came through a completed
    Stripe payment (source='online'), kept separate from enquiry-form leads."""

    class Meta:
        proxy = True
        verbose_name = "Online payment"
        verbose_name_plural = "Online Payments"
