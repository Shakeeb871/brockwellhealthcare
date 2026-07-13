"""Clinic locations — the flexible, multi-location layer.

The site is organised in two levels so any number of clinics can be added
without code changes:

* **Region / country** (``us``, ``uae``, …) — configured in settings; controls
  currency, language and the URL prefix.
* **Location** (this model) — a physical clinic branch under a region. Unlimited
  per region, each with its own address, hours, doctors, hero image and local
  SEO. States/areas are derived by grouping locations on their ``state`` field,
  so state landing pages need no separate records.

Nothing here is hard-coded: staff add a Location in the admin and its public
page, listings and schema are generated automatically.
"""

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from core.models import REGION_CHOICES, TimeStamped
from core.regions import region_prefix


class Location(TimeStamped):
    """A single clinic branch (e.g. Las Vegas, NV) under a region/country."""

    region = models.CharField(
        max_length=8, choices=REGION_CHOICES, default="us", db_index=True,
        help_text="Country/region this clinic belongs to.",
    )
    name = models.CharField(
        max_length=160,
        help_text="Public name, e.g. 'Brockwell Healthcare — Las Vegas'.",
    )
    slug = models.SlugField(
        max_length=180,
        help_text="URL segment, e.g. 'las-vegas'. Unique within the region.",
    )

    # --- Geography (state powers automatic grouping / state pages) ---------- #
    city = models.CharField(max_length=120, help_text="e.g. 'Las Vegas'.")
    state = models.CharField(
        max_length=120, blank=True, help_text="e.g. 'Nevada'. Used to group locations."
    )
    state_code = models.CharField(
        max_length=8, blank=True, help_text="e.g. 'NV'."
    )

    # --- Contact & address -------------------------------------------------- #
    street_address = models.CharField(
        max_length=200, help_text="e.g. '8879 W Flamingo Rd, Ste 201'."
    )
    postal_code = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    hours = models.TextField(
        blank=True, help_text="One line per row, e.g. 'Mon–Fri: 9:00 AM – 5:00 PM'.",
    )

    # --- Map / geo ---------------------------------------------------------- #
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    map_url = models.URLField(
        blank=True, help_text="Google Maps link for the 'Get directions' button.",
    )

    # --- Presentation ------------------------------------------------------- #
    hero = models.ImageField(
        upload_to="locations/", blank=True, null=True,
        help_text="Hero/photo for the location page and listing card.",
    )
    intro = models.CharField(
        max_length=255, blank=True, help_text="One-line summary for cards & hero.",
    )
    about = models.TextField(
        blank=True, help_text="Full description for the location page (blank line = new paragraph).",
    )

    doctors = models.ManyToManyField(
        "team.Doctor", related_name="locations", blank=True,
        help_text="Clinicians who practise at this location.",
    )

    # --- SEO / status ------------------------------------------------------- #
    seo_title = models.CharField(max_length=70, blank=True)
    seo_description = models.CharField(max_length=170, blank=True)
    is_primary = models.BooleanField(
        default=False, help_text="The main/HQ clinic for this region (shown first).",
    )
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-is_primary", "order", "city"]
        unique_together = ("region", "slug")
        indexes = [models.Index(fields=["region", "is_active"])]

    def __str__(self):
        return f"{self.name} [{self.region}]"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.city or self.name)[:180]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return region_prefix(self.region) + reverse(
            "locations:detail", kwargs={"slug": self.slug}
        )

    @property
    def state_slug(self):
        return slugify(self.state) if self.state else ""

    @property
    def full_address(self):
        bits = [self.street_address, self.city]
        tail = " ".join(b for b in (self.state_code or self.state, self.postal_code) if b)
        if tail:
            bits.append(tail)
        return ", ".join(b for b in bits if b)

    @property
    def region_label(self):
        from django.conf import settings
        conf = settings.REGIONS.get(self.region, {})
        return conf.get("short") or conf.get("name") or self.region.upper()

    @property
    def hours_list(self):
        return [ln.strip() for ln in self.hours.splitlines() if ln.strip()]

    @property
    def about_paragraphs(self):
        return [p.strip() for p in self.about.split("\n\n") if p.strip()]

    @property
    def published_doctors(self):
        return self.doctors.filter(is_published=True)
