from django.db import models
from django.urls import reverse

from core.models import REGION_CHOICES, TimeStamped


class Doctor(TimeStamped):
    """A clinician shown on the Our Team page, with an individual profile page."""

    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="uae")
    name = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180)
    title = models.CharField(
        max_length=160, help_text="Role / specialty, e.g. 'Regenerative Medicine Specialist'."
    )
    credentials = models.CharField(
        max_length=160, blank=True, help_text="e.g. 'MD, PhD, FRCS'."
    )
    experience = models.CharField(
        max_length=60, blank=True, help_text="e.g. '15+ years'."
    )
    languages = models.CharField(
        max_length=120, blank=True, help_text="e.g. 'English, Arabic'."
    )
    available_today = models.BooleanField(
        default=False, help_text="Show an 'Available Today' badge."
    )
    photo = models.CharField(
        max_length=300, blank=True,
        help_text="Optional image URL/path. Leave blank to show initials avatar.",
    )
    short_bio = models.CharField(max_length=255, help_text="One/two-line summary for the team grid.")
    full_bio = models.TextField(help_text="Full biography. Blank line separates paragraphs.")
    specialties = models.TextField(blank=True, help_text="One specialty per line.")
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
        return f"/{self.region}" + reverse("team:detail", kwargs={"slug": self.slug})

    @property
    def initials(self):
        parts = [p for p in self.name.replace("Dr.", "").replace("Dr ", "").split() if p]
        return "".join(p[0].upper() for p in parts[:2]) or "Dr"

    @property
    def specialty_list(self):
        return [line.strip() for line in self.specialties.splitlines() if line.strip()]

    @property
    def bio_paragraphs(self):
        return [p.strip() for p in self.full_bio.split("\n\n") if p.strip()]
