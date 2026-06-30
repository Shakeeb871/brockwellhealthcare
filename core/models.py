from django.db import models

# Region choices shared across apps. Keep in sync with settings.REGIONS.
REGION_CHOICES = [
    ("uae", "United Arab Emirates"),
    ("us", "United States"),
]


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ContactLead(TimeStamped):
    """An enquiry submitted through the contact form."""

    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="uae")
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    subject = models.CharField(max_length=160, blank=True)
    message = models.TextField()
    handled = models.BooleanField(default=False, help_text="Mark once followed up.")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact lead"

    def __str__(self):
        return f"{self.name} ({self.get_region_display()})"


class FAQ(TimeStamped):
    """Question/answer pairs rendered with FAQPage structured data.

    Strong for AEO/GEO: answer engines and LLMs surface these directly.
    """

    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="uae")
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question


class Page(TimeStamped):
    """A simple content page (Privacy Policy, Terms, Cookies), editable in admin."""

    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="uae")
    slug = models.SlugField(max_length=80, help_text="e.g. privacy-policy, terms, cookies")
    title = models.CharField(max_length=160)
    body = models.TextField(help_text="Use a blank line between paragraphs. Lines ending with ':' render as headings.")
    is_published = models.BooleanField(default=True)

    seo_title = models.CharField(max_length=70, blank=True)
    seo_description = models.CharField(max_length=170, blank=True)

    class Meta:
        ordering = ["title"]
        unique_together = ("region", "slug")

    def __str__(self):
        return f"{self.title} [{self.region}]"

    @property
    def blocks(self):
        """Split body into (kind, text) blocks: 'heading' or 'para'."""
        out = []
        for chunk in self.body.split("\n\n"):
            chunk = chunk.strip()
            if not chunk:
                continue
            if chunk.endswith(":") and len(chunk) < 80:
                out.append(("heading", chunk.rstrip(":")))
            else:
                out.append(("para", chunk))
        return out
