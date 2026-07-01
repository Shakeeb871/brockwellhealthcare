from django.db import models
from django.urls import reverse
from django.utils import timezone

from core.models import REGION_CHOICES, TimeStamped


class BlogCategory(TimeStamped):
    """A blog category (e.g. Regenerative Medicine, Longevity)."""

    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="uae")
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140)
    description = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]
        unique_together = ("region", "slug")
        verbose_name = "Blog category"
        verbose_name_plural = "Blog categories"

    def __str__(self):
        return f"{self.name} [{self.region}]"

    def get_absolute_url(self):
        return f"/{self.region}" + reverse("blog:entry", kwargs={"slug": self.slug})

    @property
    def published_posts(self):
        return self.posts.filter(is_published=True)


class BlogPost(TimeStamped):
    """A blog article."""

    region = models.CharField(max_length=8, choices=REGION_CHOICES, default="uae")
    category = models.ForeignKey(
        BlogCategory, related_name="posts", on_delete=models.SET_NULL, null=True, blank=True
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220)
    image = models.ImageField(
        upload_to="blog/", blank=True, null=True, help_text="Featured image."
    )
    excerpt = models.CharField(
        max_length=300, help_text="Short summary shown on cards & meta."
    )
    body = models.TextField(
        help_text="Article body. Separate paragraphs with a blank line. "
        "Start a line with '## ' for a subheading, or '- ' for list items."
    )
    author = models.CharField(max_length=120, default="Brockwell Healthcare")
    published_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    seo_title = models.CharField(max_length=70, blank=True)
    seo_description = models.CharField(max_length=170, blank=True)

    class Meta:
        ordering = ["-published_at"]
        unique_together = ("region", "slug")
        verbose_name = "Blog post"
        verbose_name_plural = "Blog posts"

    def __str__(self):
        return f"{self.title} [{self.region}]"

    def get_absolute_url(self):
        return f"/{self.region}" + reverse("blog:entry", kwargs={"slug": self.slug})

    @property
    def reading_time(self):
        words = len(self.body.split())
        return max(1, round(words / 200))

    @property
    def body_blocks(self):
        """Parse the body into structured blocks (heading / list / paragraph)."""
        blocks = []
        for raw in self.body.split("\n\n"):
            raw = raw.strip()
            if not raw:
                continue
            lines = raw.splitlines()
            if raw.startswith("## "):
                blocks.append({"type": "h", "text": raw[3:].strip()})
            elif all(line.strip().startswith("- ") for line in lines):
                blocks.append({"type": "ul", "items": [ln.strip()[2:].strip() for ln in lines]})
            else:
                blocks.append({"type": "p", "text": raw})
        return blocks
