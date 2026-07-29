"""Search-engine indexing submissions log.

Every time you paste URLs into the admin submit page, we save a record of
what was submitted, when, where it went and what came back — so the whole
history is visible instead of a fire-and-forget ping.
"""

from django.db import models


class IndexSubmission(models.Model):
    """One row per URL sent to search engines for indexing."""

    STATUS_OK = "ok"
    STATUS_FAIL = "fail"
    STATUS_SKIP = "skipped"
    STATUS_CHOICES = [
        (STATUS_OK, "Submitted"),
        (STATUS_FAIL, "Failed"),
        (STATUS_SKIP, "Skipped (disabled)"),
    ]

    ENGINE_GOOGLE = "google"
    ENGINE_INDEXNOW = "indexnow"
    ENGINE_CHOICES = [
        (ENGINE_GOOGLE, "Google"),
        (ENGINE_INDEXNOW, "IndexNow (Bing/Yandex/…)"),
    ]

    SOURCE_ADMIN = "admin"
    SOURCE_CLI = "cli"
    SOURCE_CHOICES = [
        (SOURCE_ADMIN, "Admin page"),
        (SOURCE_CLI, "Command line / cron"),
    ]

    url = models.URLField(max_length=500, db_index=True)
    engine = models.CharField(
        max_length=32, choices=ENGINE_CHOICES, default=ENGINE_INDEXNOW,
        help_text="Which search endpoint the URL was sent to.",
    )
    source = models.CharField(
        max_length=10, choices=SOURCE_CHOICES, default=SOURCE_ADMIN, db_index=True,
        help_text="Where the submission was triggered from.",
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    http_code = models.PositiveSmallIntegerField(default=0)
    response = models.CharField(max_length=400, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True, db_index=True)
    submitted_by = models.ForeignKey(
        "auth.User", null=True, blank=True, on_delete=models.SET_NULL,
        related_name="index_submissions",
    )

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "Index submission"
        verbose_name_plural = "Index submissions"

    def __str__(self):
        return f"{self.url} → {self.get_status_display()}"
