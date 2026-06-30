from django.db import models
from django.urls import reverse

from core.models import REGION_CHOICES, TimeStamped


class Service(TimeStamped):
    """A stem-cell / regenerative service offered in a region.

    Fully editable from the admin so the client can manage content without
    touching code. SEO fields let each service rank independently.
    """

    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="uae")
    name = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180)
    icon = models.CharField(
        max_length=8,
        default="🧬",
        help_text="An emoji or short glyph shown on cards.",
    )
    summary = models.CharField(
        max_length=255, help_text="One-line description used on cards and meta tags."
    )
    description = models.TextField(
        help_text="Full description. Separate paragraphs with a blank line."
    )
    benefits = models.TextField(
        blank=True,
        help_text="One benefit per line; rendered as a checklist.",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Optional starting price (in the region's currency).",
    )
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    # Optional SEO overrides (fall back to name/summary when blank).
    seo_title = models.CharField(max_length=70, blank=True)
    seo_description = models.CharField(max_length=170, blank=True)

    class Meta:
        ordering = ["order", "name"]
        unique_together = ("region", "slug")

    def __str__(self):
        return f"{self.name} [{self.region}]"

    def get_absolute_url(self):
        return f"/{self.region}" + reverse("services:detail", kwargs={"slug": self.slug})

    @property
    def benefit_list(self):
        return [line.strip() for line in self.benefits.splitlines() if line.strip()]

    @property
    def paragraphs(self):
        return [p.strip() for p in self.description.split("\n\n") if p.strip()]
