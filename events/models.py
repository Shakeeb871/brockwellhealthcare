from django.db import models
from django.urls import reverse
from django.utils import timezone

from core.models import REGION_CHOICES, TimeStamped


class Event(TimeStamped):
    """A seminar / clinic event that visitors can register and pay for."""

    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="uae")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220)
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
        return f"/{self.region}" + reverse("events:detail", kwargs={"slug": self.slug})

    @property
    def is_upcoming(self):
        return self.start >= timezone.now()

    @property
    def is_free(self):
        return self.price <= 0

    @property
    def seats_left(self):
        if self.capacity == 0:
            return None
        taken = self.registrations.filter(paid=True).count()
        return max(self.capacity - taken, 0)

    @property
    def is_sold_out(self):
        left = self.seats_left
        return left is not None and left <= 0

    @property
    def paragraphs(self):
        return [p.strip() for p in self.description.split("\n\n") if p.strip()]


class EventRegistration(TimeStamped):
    """A booking for an event, optionally tied to a Stripe payment."""

    event = models.ForeignKey(
        Event, related_name="registrations", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=8, default="AED")
    stripe_session_id = models.CharField(max_length=255, blank=True, db_index=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        status = "paid" if self.paid else "pending"
        return f"{self.name} → {self.event.title} ({status})"
