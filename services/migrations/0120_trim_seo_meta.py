"""Trim over-length SEO titles and descriptions.

Google renders roughly 60 characters of a <title> and ~155-160 of a meta
description; anything beyond that is truncated with an ellipsis, which wastes
the space and can cut a sentence mid-word.

Titles keep the primary keyword phrase and the brand, dropping the middle
descriptor when the whole thing doesn't fit. Descriptions are trimmed back to
the last complete sentence (or, failing that, the last whole word) so they
still read as finished copy. Nothing is invented and nothing already within
budget is touched.
"""

from django.db import migrations

TITLE_MAX = 60
DESC_MAX = 158


def shorten_title(title):
    """Keep "<primary keyword> | <brand>", dropping middle descriptors."""
    if not title or len(title) <= TITLE_MAX:
        return title
    parts = [p.strip() for p in title.split("|") if p.strip()]
    if len(parts) > 2:
        # primary keyword + brand (drops the middle "nice to have" phrases)
        candidate = f"{parts[0]} | {parts[-1]}"
        if len(candidate) <= TITLE_MAX:
            return candidate
    if len(parts) >= 2:
        # Still too long — try dropping the brand instead of the keyword.
        candidate = " | ".join(parts[:-1])
        if len(candidate) <= TITLE_MAX:
            return candidate
    # Last resort: the primary phrase on its own.
    return parts[0][:TITLE_MAX].rstrip(" -–|,") if parts else title


def shorten_description(desc):
    """Cut back to the last complete sentence, else the last whole word."""
    if not desc or len(desc) <= DESC_MAX:
        return desc
    window = desc[:DESC_MAX]
    cut = max(window.rfind(". "), window.rfind("! "), window.rfind("? "))
    if cut >= 90:                       # a sentence break we can use
        return window[: cut + 1].strip()
    cut = window.rfind(" ")
    return (window[:cut].rstrip(" ,;:-–") + ".") if cut > 0 else window


def trim(apps, schema_editor):
    for label in ("ServiceCategory", "Service"):
        Model = apps.get_model("services", label)
        for obj in Model.objects.all():
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

    dependencies = [("services", "0118_us_titles_location_light")]

    operations = [migrations.RunPython(trim, noop)]
