"""Submit URLs to Google's Indexing API and IndexNow from the command line.

Useful for cron ("keep pushing the sitemap"), for bulk work beyond the admin
form, and for a first push after launch.

    # every indexable sitemap URL (respects Google's 200/day quota)
    python manage.py submiturls --all

    # only URLs never successfully submitted to Google before
    python manage.py submiturls --all --new-only

    # specific URLs
    python manage.py submiturls https://example.com/a/ /uae/services/

    # see what would happen, send nothing
    python manage.py submiturls --all --dry-run
"""

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from core import google_indexing, indexnow
from core.models import IndexSubmission
from core.sitemaps import non_empty_sitemaps


class Command(BaseCommand):
    help = "Submit URLs to the Google Indexing API and/or IndexNow."

    def add_arguments(self, parser):
        parser.add_argument("urls", nargs="*", help="URLs or paths to submit.")
        parser.add_argument("--all", action="store_true",
                            help="Submit every URL from the indexable sitemaps.")
        parser.add_argument("--new-only", action="store_true",
                            help="Skip URLs already submitted to Google successfully.")
        parser.add_argument("--limit", type=int, default=google_indexing.DAILY_QUOTA,
                            help=f"Max URLs to send to Google (default {google_indexing.DAILY_QUOTA}).")
        parser.add_argument("--no-google", action="store_true", help="Skip the Google Indexing API.")
        parser.add_argument("--no-indexnow", action="store_true", help="Skip IndexNow.")
        parser.add_argument("--dry-run", action="store_true", help="Show the plan, send nothing.")

    # ------------------------------------------------------------------ #
    def handle(self, *args, **o):
        domain = settings.SITE_DOMAIN

        if getattr(settings, "SITE_NOINDEX", True):
            raise CommandError(
                "SITE_NOINDEX is True — the site is de-indexed, so submitting is "
                "pointless. Set SITE_NOINDEX=False first."
            )

        urls = [self._absolute(u, domain) for u in o["urls"]]
        if o["all"]:
            urls += self._sitemap_urls(domain)
        urls = list(dict.fromkeys(u for u in urls if u))          # dedupe, keep order
        if not urls:
            raise CommandError("No URLs given. Pass URLs or use --all.")

        if o["new_only"]:
            done = set(
                IndexSubmission.objects.filter(
                    engine="google", status=IndexSubmission.STATUS_OK
                ).values_list("url", flat=True)
            )
            before = len(urls)
            urls = [u for u in urls if u not in done]
            self.stdout.write(f"--new-only: skipped {before - len(urls)} already-submitted URL(s)")

        use_google = not o["no_google"] and google_indexing.is_configured()
        use_indexnow = not o["no_indexnow"] and indexnow.is_enabled()

        if not use_google:
            reason = "disabled" if o["no_google"] else "not configured (GOOGLE_INDEXING_CREDENTIALS)"
            self.stdout.write(self.style.WARNING(f"Google Indexing API: {reason}"))
        if not use_indexnow:
            reason = "disabled" if o["no_indexnow"] else "not configured (INDEXNOW_KEY)"
            self.stdout.write(self.style.WARNING(f"IndexNow: {reason}"))
        if not (use_google or use_indexnow):
            raise CommandError("Nothing to submit to — configure credentials first.")

        google_urls = urls[: o["limit"]] if use_google else []
        if use_google and len(urls) > o["limit"]:
            self.stdout.write(self.style.WARNING(
                f"Google: sending the first {o['limit']} of {len(urls)} URLs "
                f"(daily quota). Re-run tomorrow, or use --new-only."
            ))

        self.stdout.write("")
        self.stdout.write(f"URLs: {len(urls)} | Google: {len(google_urls)} | IndexNow: {len(urls) if use_indexnow else 0}")
        if o["dry_run"]:
            for u in urls[:20]:
                self.stdout.write(f"  would submit  {u}")
            if len(urls) > 20:
                self.stdout.write(f"  … +{len(urls) - 20} more")
            self.stdout.write(self.style.WARNING("\nDry run — nothing was sent."))
            return

        rows, ok, fail = [], 0, 0

        if use_google:
            self.stdout.write("\nGoogle Indexing API:")
            for url, status, msg in google_indexing.publish_many(google_urls):
                good = 200 <= status < 300
                ok, fail = ok + good, fail + (not good)
                mark = self.style.SUCCESS("ok  ") if good else self.style.ERROR("fail")
                self.stdout.write(f"  {mark} {status:3} {url}")
                if not good:
                    self.stdout.write(f"        {msg}")
                rows.append(IndexSubmission(
                    url=url, engine="google", http_code=status, response=msg,
                    status=IndexSubmission.STATUS_OK if good else IndexSubmission.STATUS_FAIL,
                ))

        if use_indexnow:
            status, body = indexnow.submit(urls)
            good = 200 <= status < 300
            style = self.style.SUCCESS if good else self.style.ERROR
            self.stdout.write("\nIndexNow: " + style(f"HTTP {status}") + f" for {len(urls)} URL(s)")
            if not good:
                self.stdout.write(f"  {body}")
            for url in urls:
                rows.append(IndexSubmission(
                    url=url, engine="indexnow", http_code=status, response=(body or "")[:400],
                    status=IndexSubmission.STATUS_OK if good else IndexSubmission.STATUS_FAIL,
                ))

        IndexSubmission.objects.bulk_create(rows)
        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(
            f"Logged {len(rows)} submission(s). Google accepted {ok}, rejected {fail}."
        ))
        self.stdout.write("Review them in the admin under Core → Index submissions.")

    # ------------------------------------------------------------------ #
    @staticmethod
    def _absolute(u, domain):
        u = (u or "").strip()
        if not u:
            return ""
        if u.startswith("/"):
            return f"https://{domain}{u}"
        if u.startswith("http://"):
            return "https://" + u[len("http://"):]
        if not u.startswith("https://"):
            return f"https://{domain}/{u.lstrip('/')}"
        return u

    @staticmethod
    def _sitemap_urls(domain):
        out = []
        for cls in non_empty_sitemaps().values():
            sm = cls()
            for item in sm.items():
                out.append(f"https://{domain}{sm.location(item)}")
        return out
