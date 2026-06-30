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
