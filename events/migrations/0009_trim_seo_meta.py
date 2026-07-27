"""Trim over-length event SEO titles/descriptions (see services.0120)."""

from django.db import migrations

TITLE_MAX = 60
DESC_MAX = 158


def shorten_title(title):
    if not title or len(title) <= TITLE_MAX:
        return title
    parts = [p.strip() for p in title.split("|") if p.strip()]
    if len(parts) > 2:
        candidate = f"{parts[0]} | {parts[-1]}"
        if len(candidate) <= TITLE_MAX:
            return candidate
    if len(parts) >= 2:
        candidate = " | ".join(parts[:-1])
        if len(candidate) <= TITLE_MAX:
            return candidate
    return parts[0][:TITLE_MAX].rstrip(" -–|,") if parts else title


def shorten_description(desc):
    if not desc or len(desc) <= DESC_MAX:
        return desc
    window = desc[:DESC_MAX]
    cut = max(window.rfind(". "), window.rfind("! "), window.rfind("? "))
    if cut >= 90:
        return window[: cut + 1].strip()
    cut = window.rfind(" ")
    return (window[:cut].rstrip(" ,;:-–") + ".") if cut > 0 else window


def trim(apps, schema_editor):
    Event = apps.get_model("events", "Event")
    for obj in Event.objects.all():
        changed = False
        new_t = shorten_title(obj.seo_title)
        if new_t != obj.seo_title:
            obj.seo_title, changed = new_t, True
        new_d = shorten_description(obj.seo_description)
        if new_d != obj.seo_description:
            obj.seo_description, changed = new_d, True
        if changed:
            obj.save(update_fields=["seo_title", "seo_description"])


def noop(apps, schema_editor):
    """Irreversible: the trimmed copy is the desired state."""


class Migration(migrations.Migration):

    dependencies = [("events", "0008_backfill_online_source")]

    operations = [migrations.RunPython(trim, noop)]
