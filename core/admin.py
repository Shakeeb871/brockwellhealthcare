from django.conf import settings
from django.contrib import admin, messages
from django.contrib.contenttypes.admin import GenericStackedInline
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse
from django.utils.html import format_html
from tinymce.widgets import TinyMCE

from . import indexnow
from .models import ContactLead, FAQ, FAQItem, IndexSubmission, Page


class FAQItemInline(GenericStackedInline):
    """Per-object FAQ section — reusable on any content model's admin."""

    model = FAQItem
    extra = 1
    fields = ("question", "answer", "order", "is_published")
    ordering = ("order", "id")
    can_delete = True
    verbose_name = "FAQ"
    verbose_name_plural = "FAQs — shown below the content (with FAQ schema)"


@admin.register(ContactLead)
class ContactLeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "region", "handled", "created_at")
    list_filter = ("region", "handled", "created_at")
    search_fields = ("name", "email", "phone", "message")
    list_editable = ("handled",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at", "updated_at")


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "region", "order", "is_published")
    list_filter = ("region", "is_published")
    search_fields = ("question", "answer")
    list_editable = ("order", "is_published")


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "region", "is_published")
    list_filter = ("region", "is_published")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True
    inlines = [FAQItemInline]
    fieldsets = (
        (None, {"fields": ("region", "slug", "title", "body", "is_published")}),
        ("SEO (optional)", {"fields": ("seo_title", "seo_description"), "classes": ("collapse",)}),
        ("Custom code / schema", {"fields": ("custom_head",), "classes": ("collapse",)}),
    )

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "body":
            kwargs["widget"] = TinyMCE()
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(IndexSubmission)
class IndexSubmissionAdmin(admin.ModelAdmin):
    """History of URLs submitted to search engines.

    Adds a custom 'Submit URLs' page on top of the list so you can paste any
    number of URLs (one per line) and push them to IndexNow immediately.
    Everything submitted is logged as a row with its status.
    """

    change_list_template = "admin/core/indexsubmission/change_list.html"
    list_display = ("url", "engine", "status_badge", "http_code", "submitted_at", "submitted_by")
    list_filter = ("status", "engine", "submitted_at")
    search_fields = ("url", "response")
    date_hierarchy = "submitted_at"
    readonly_fields = ("url", "engine", "status", "http_code", "response",
                       "submitted_at", "submitted_by")

    def has_add_permission(self, request):
        return False               # rows are only created by the submit page

    @admin.display(description="Status", ordering="status")
    def status_badge(self, obj):
        colour = {"ok": "#2e7d46", "fail": "#c0392b", "skipped": "#7f8c8d"}.get(obj.status, "#333")
        return format_html(
            '<span style="background:{};color:#fff;padding:2px 8px;border-radius:10px;'
            'font-size:.78rem;font-weight:600;">{}</span>',
            colour, obj.get_status_display(),
        )

    # ---------- custom submit view ----------
    def get_urls(self):
        return [
            path(
                "submit/",
                self.admin_site.admin_view(self.submit_view),
                name="core_indexsubmission_submit",
            ),
        ] + super().get_urls()

    def submit_view(self, request):
        """Paste URLs → push to IndexNow → log every result."""
        domain = settings.SITE_DOMAIN
        key_configured = bool(getattr(settings, "INDEXNOW_KEY", ""))
        site_live = not getattr(settings, "SITE_NOINDEX", True)

        if request.method == "POST":
            raw = request.POST.get("urls", "")
            urls = _normalise_urls(raw, domain)

            if not urls:
                messages.error(request, "No valid URLs found. Paste one URL per line.")
            elif not key_configured:
                messages.error(request, "INDEXNOW_KEY is not set in the server .env — nothing was submitted.")
            elif not site_live:
                messages.error(request, "SITE_NOINDEX is True — the site is de-indexed so search engines would ignore this. Set SITE_NOINDEX=False first.")
            else:
                status, body = indexnow.submit(urls)
                ok = 200 <= status < 300
                for u in urls:
                    IndexSubmission.objects.create(
                        url=u, engine="indexnow",
                        status=IndexSubmission.STATUS_OK if ok else IndexSubmission.STATUS_FAIL,
                        http_code=status,
                        response=(body or "")[:200],
                        submitted_by=request.user if request.user.is_authenticated else None,
                    )
                if ok:
                    messages.success(request, f"Submitted {len(urls)} URL(s) to IndexNow (Bing, Yandex, Seznam, Naver). Google reads Bing signals too. Response: HTTP {status}.")
                else:
                    messages.warning(request, f"Submission accepted with warnings — HTTP {status}. Check the log below.")
                return HttpResponseRedirect(reverse("admin:core_indexsubmission_changelist"))

        # Sitemap URLs so the operator can copy the full set in one click.
        from .sitemaps import non_empty_sitemaps
        all_urls = []
        for cls in non_empty_sitemaps().values():
            sm = cls()
            for item in sm.items():
                loc = sm.location(item) if hasattr(sm, "location") else item.get_absolute_url()
                all_urls.append(f"https://{domain}{loc}")

        ctx = {
            **self.admin_site.each_context(request),
            "title": "Submit URLs for indexing",
            "opts": IndexSubmission._meta,
            "domain": domain,
            "key_configured": key_configured,
            "site_live": site_live,
            "all_urls": all_urls,
            "url_count": len(all_urls),
            "prefilled": request.POST.get("urls", ""),
        }
        return render(request, "admin/core/indexsubmission/submit.html", ctx)


def _normalise_urls(raw, domain):
    """Parse a textarea into a clean list of full https URLs.

    Accepts full URLs or paths ("/uae/services/..."), splits on any whitespace,
    de-duplicates while preserving order, and rejects anything off-domain.
    """
    out, seen = [], set()
    for line in raw.replace(",", "\n").split():
        u = line.strip()
        if not u:
            continue
        if u.startswith("/"):
            u = f"https://{domain}{u}"
        elif u.startswith("http://"):
            u = "https://" + u[len("http://"):]
        elif not u.startswith("https://"):
            u = f"https://{domain}/{u.lstrip('/')}"
        if f"//{domain}" not in u:              # off-domain — IndexNow rejects
            continue
        if u not in seen:
            seen.add(u); out.append(u)
    return out


admin.site.site_header = "Brockwell Healthcare — Site Administration"
admin.site.site_title = "Brockwell Admin"
admin.site.index_title = "Manage your website content"
