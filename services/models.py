from django.db import models
from django.urls import reverse

from core.models import REGION_CHOICES, TimeStamped


class ServiceCategory(TimeStamped):
    """A main service area (e.g. Regenerative Wellness).

    May contain sub-services. A category with no sub-services (e.g. "Emsculpt
    For Pain") simply acts as its own service page using its description.
    """

    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="uae")
    name = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180)
    icon = models.CharField(max_length=8, default="🧬", help_text="Emoji shown on cards.")
    summary = models.CharField(max_length=255, help_text="One-line description for cards & meta.")
    description = models.TextField(
        blank=True, help_text="Full intro. Separate paragraphs with a blank line."
    )
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    seo_title = models.CharField(max_length=70, blank=True)
    seo_description = models.CharField(max_length=170, blank=True)

    class Meta:
        ordering = ["order", "name"]
        unique_together = ("region", "slug")
        verbose_name = "Service category"
        verbose_name_plural = "Service categories"

    def __str__(self):
        return f"{self.name} [{self.region}]"

    def get_absolute_url(self):
        return f"/{self.region}" + reverse("services:category", kwargs={"category": self.slug})

    @property
    def paragraphs(self):
        return [p.strip() for p in self.description.split("\n\n") if p.strip()]

    @property
    def published_services(self):
        return self.services.filter(is_published=True)


class Service(TimeStamped):
    """A sub-service belonging to a main category."""

    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="uae")
    category = models.ForeignKey(
        ServiceCategory, related_name="services", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180)
    icon = models.CharField(max_length=8, default="✦")
    summary = models.CharField(max_length=255, help_text="One-line description for cards & meta.")
    description = models.TextField(help_text="Full description. Blank line separates paragraphs.")
    benefits = models.TextField(blank=True, help_text="One benefit per line; shown as a checklist.")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        help_text="Optional starting price (region currency).",
    )
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    seo_title = models.CharField(max_length=70, blank=True)
    seo_description = models.CharField(max_length=170, blank=True)

    class Meta:
        ordering = ["order", "name"]
        unique_together = ("region", "slug")

    def __str__(self):
        return f"{self.name} [{self.region}]"

    def get_absolute_url(self):
        return f"/{self.region}" + reverse(
            "services:detail", kwargs={"category": self.category.slug, "slug": self.slug}
        )

    @property
    def benefit_list(self):
        return [line.strip() for line in self.benefits.splitlines() if line.strip()]

    @property
    def paragraphs(self):
        return [p.strip() for p in self.description.split("\n\n") if p.strip()]
