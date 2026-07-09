from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse

from core.regions import region_prefix

from core.models import CUSTOM_HEAD_HELP, REGION_CHOICES, TimeStamped


class ServiceCategory(TimeStamped):
    """A main service area (e.g. Regenerative Wellness).

    May contain sub-services. A category with no sub-services (e.g. "Emsculpt
    For Pain") simply acts as its own service page using its description.
    """

    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="uae")
    name = models.CharField(max_length=160)
    hero_heading = models.CharField(
        max_length=200, blank=True,
        help_text="Keyword-rich H1 for the page hero, e.g. 'Regenerative Wellness in Dubai'. "
        "Falls back to the category name if left blank.",
    )
    slug = models.SlugField(max_length=180)
    icon = models.CharField(max_length=8, default="🧬", help_text="Emoji shown on cards.")
    image = models.ImageField(
        upload_to="services/", blank=True, null=True,
        help_text="Optional card image. If set, it is shown on the home 'Our Services' "
        "slider instead of the icon.",
    )
    summary = models.CharField(max_length=255, help_text="One-line description for cards & meta.")
    description = models.TextField(
        blank=True, help_text="Full intro. Separate paragraphs with a blank line."
    )
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    seo_title = models.CharField(max_length=70, blank=True)
    seo_description = models.CharField(max_length=170, blank=True)
    custom_head = models.TextField(blank=True, help_text=CUSTOM_HEAD_HELP)

    faqs = GenericRelation("core.FAQItem")

    class Meta:
        ordering = ["order", "name"]
        unique_together = ("region", "slug")
        verbose_name = "Service category"
        verbose_name_plural = "Service categories"

    def __str__(self):
        return f"{self.name} [{self.region}]"

    def get_absolute_url(self):
        return region_prefix(self.region) + reverse("services:category", kwargs={"category": self.slug})

    @property
    def paragraphs(self):
        return [p.strip() for p in self.description.split("\n\n") if p.strip()]

    @property
    def published_services(self):
        # Only top-level services (a nested child is reached via its parent).
        return self.services.filter(is_published=True, parent__isnull=True)

    @property
    def has_nested_services(self):
        # True if any top-level service in this category has published sub-pages
        # (so its dropdown needs to allow a third-level flyout to escape).
        return self.services.filter(
            is_published=True, parent__isnull=True, children__is_published=True
        ).exists()


class Service(TimeStamped):
    """A sub-service belonging to a main category.

    A service may optionally nest under another service (``parent``), giving a
    third navigation level: Category → Service (hub) → Service (sub-page).
    """

    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="uae")
    category = models.ForeignKey(
        ServiceCategory, related_name="services", on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children",
        on_delete=models.CASCADE, limit_choices_to={"parent__isnull": True},
        help_text="Optional. Nest this service under another service to create a "
        "third-level sub-page (e.g. NAD+ IV Therapy under Longevity IVs). Leave "
        "blank for a normal top-level service.",
    )
    name = models.CharField(max_length=160)
    hero_heading = models.CharField(
        max_length=200, blank=True,
        help_text="Keyword-rich H1 for the page hero, e.g. 'Stem Cell Therapy in Dubai'. "
        "Falls back to the service name if left blank.",
    )
    slug = models.SlugField(max_length=180)
    icon = models.CharField(max_length=8, default="✦")
    image = models.ImageField(
        upload_to="services/", blank=True, null=True,
        help_text="Card image shown on the category page. Recommended 16:10 ratio.",
    )
    summary = models.CharField(max_length=255, help_text="One-line description for cards & meta.")
    description = models.TextField(help_text="Full description. Blank line separates paragraphs.")
    benefits = models.TextField(blank=True, help_text="One benefit per line; shown as a checklist.")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        help_text="Optional starting price (region currency).",
    )
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    seo_title = models.CharField(max_length=200, blank=True)
    seo_description = models.CharField(max_length=320, blank=True)
    custom_head = models.TextField(blank=True, help_text=CUSTOM_HEAD_HELP)

    faqs = GenericRelation("core.FAQItem")

    class Meta:
        ordering = ["order", "name"]
        unique_together = ("region", "slug")

    def __str__(self):
        return f"{self.name} [{self.region}]"

    def get_absolute_url(self):
        if self.parent_id:
            return region_prefix(self.region) + reverse(
                "services:subdetail",
                kwargs={
                    "category": self.category.slug,
                    "parent": self.parent.slug,
                    "slug": self.slug,
                },
            )
        return region_prefix(self.region) + reverse(
            "services:detail", kwargs={"category": self.category.slug, "slug": self.slug}
        )

    @property
    def published_children(self):
        return self.children.filter(is_published=True)

    @property
    def benefit_list(self):
        return [line.strip() for line in self.benefits.splitlines() if line.strip()]

    @property
    def paragraphs(self):
        return [p.strip() for p in self.description.split("\n\n") if p.strip()]


class PageSection(TimeStamped):
    """A reorderable, pre-designed content block added to a service page.

    Editors pick a `kind`, fill a few fields, and the front-end renders the
    matching designed section (counters, why-choose-us, treatments, etc.).
    Order is managed with drag-and-drop in the admin.
    """

    KIND_CHOICES = [
        ("text", "Rich text / content"),
        ("benefits", "Key benefits (checklist)"),
        ("journey", "Treatment journey / process steps"),
        ("treatments", "Our treatments (cards from this category)"),
        ("counters", "Counters / statistics"),
        ("why", "Why choose us"),
        ("faq", "FAQ (uses this service's FAQs)"),
        ("reviews", "Patient reviews slider"),
        ("brands", "Accreditations / brand logos"),
        ("cta", "Call-to-action band"),
        ("booking", "Booking / consultation form"),
    ]
    BACKGROUND_CHOICES = [
        ("light", "White"),
        ("soft", "Soft grey"),
        ("dark", "Dark green"),
    ]

    service = models.ForeignKey(Service, related_name="sections", on_delete=models.CASCADE)
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default="text")
    eyebrow = models.CharField(max_length=80, blank=True, help_text="Small label above the heading.")
    heading = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True, help_text="Intro / paragraph text. Blank line = new paragraph.")
    image = models.ImageField(upload_to="sections/", blank=True, null=True)
    items = models.TextField(
        blank=True,
        help_text=(
            "One item per line. • Key benefits: just the benefit text. • Journey steps: "
            "'title | description' (auto-numbered). • Counters: 'value | suffix | label' "
            "(e.g. 500 | + | Patients Treated). • Why choose us: 'title | description'. "
            "Not needed for other types."
        ),
    )
    button_text = models.CharField(max_length=60, blank=True)
    button_url = models.CharField(max_length=300, blank=True)
    background = models.CharField(max_length=10, choices=BACKGROUND_CHOICES, default="light")
    order = models.PositiveIntegerField(default=0, db_index=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Page section"

    def __str__(self):
        return f"{self.get_kind_display()} — {self.heading or self.service.name}"

    @property
    def item_rows(self):
        """Parse `items` into a list of pipe-split rows."""
        rows = []
        for line in self.items.splitlines():
            line = line.strip()
            if line:
                rows.append([p.strip() for p in line.split("|")])
        return rows
