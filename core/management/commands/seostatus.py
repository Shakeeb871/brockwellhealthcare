"""Print the live search-engine indexing state.

Run this on the server to see exactly what search engines are being told:

    python manage.py seostatus

It reports the effective settings (as loaded from the environment/.env) and,
per region, whether pages are indexable and which robots directive they send.
"""

import os

from django.conf import settings
from django.core.management.base import BaseCommand

from core.regions import region_indexable, region_prefix


class Command(BaseCommand):
    help = "Show the current per-region search-engine indexing state."

    def handle(self, *args, **options):
        noindex = getattr(settings, "SITE_NOINDEX", True)
        allowed = getattr(settings, "SEO_INDEX_REGIONS", [])

        self.stdout.write("")
        self.stdout.write(self.style.MIGRATE_HEADING("Search-engine indexing status"))
        self.stdout.write(f"  SITE_NOINDEX        = {noindex}")
        self.stdout.write(f"  SEO_INDEX_REGIONS   = {allowed or '(none)'}")
        self.stdout.write(f"  SITE_DOMAIN         = {settings.SITE_DOMAIN}")
        self.stdout.write("")

        if noindex:
            self.stdout.write(self.style.WARNING(
                "  SITE_NOINDEX is True -> the WHOLE site is de-indexed.\n"
                "  Set SITE_NOINDEX=False in the server .env, then redeploy."
            ))
            self.stdout.write("")

        any_indexed = False
        for code, conf in settings.REGIONS.items():
            if not conf.get("enabled"):
                self.stdout.write(f"  {code:5} disabled")
                continue
            live = region_indexable(code)
            any_indexed = any_indexed or live
            url = f"https://{settings.SITE_DOMAIN}{region_prefix(code)}/"
            if live:
                self.stdout.write(self.style.SUCCESS(
                    f"  {code:5} INDEXED     robots: index, follow    {url}"
                ))
            else:
                self.stdout.write(
                    f"  {code:5} not indexed robots: noindex        {url}"
                )

        self.stdout.write("")
        if any_indexed:
            self.stdout.write(
                f"  Sitemap index: https://{settings.SITE_DOMAIN}/sitemap.xml"
            )
        else:
            self.stdout.write(self.style.WARNING(
                "  Nothing is indexable right now, so the sitemap index is empty."
            ))

        # --- Instant-indexing credentials -------------------------------- #
        from core import google_indexing, indexnow

        self.stdout.write("")
        self.stdout.write(self.style.MIGRATE_HEADING("Instant indexing"))

        raw = (getattr(settings, "GOOGLE_INDEXING_CREDENTIALS", "") or "").strip()
        if google_indexing.is_configured():
            self.stdout.write(self.style.SUCCESS(
                f"  Google Indexing API  READY   {google_indexing.service_account_email()}"
            ))
            self.stdout.write(
                "    Reminder: that email must be an OWNER of the property in Search Console."
            )
        elif not raw:
            self.stdout.write("  Google Indexing API  not set (GOOGLE_INDEXING_CREDENTIALS empty)")
        else:
            # A value is present but unusable — say exactly why.
            hint = "file not found" if not raw.startswith("{") and not os.path.exists(raw) else "unreadable or missing client_email/private_key"
            self.stdout.write(self.style.ERROR(
                f"  Google Indexing API  BROKEN  ({hint})"
            ))
            self.stdout.write(f"    value: {raw[:70]}{'…' if len(raw) > 70 else ''}")

        key = getattr(settings, "INDEXNOW_KEY", "")
        if key:
            state = "READY" if indexnow.is_enabled() else "key set, but site is de-indexed"
            style = self.style.SUCCESS if indexnow.is_enabled() else self.style.WARNING
            self.stdout.write(style(f"  IndexNow             {state}"))
            self.stdout.write(
                f"    verification file: https://{settings.SITE_DOMAIN}/{key}.txt"
            )
        else:
            self.stdout.write("  IndexNow             not set (INDEXNOW_KEY empty)")
        self.stdout.write("")
