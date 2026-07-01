"""Convert existing plain-text content fields to HTML.

The admin now uses a TinyMCE rich-text editor for the long-form content fields,
which store HTML. Existing rows hold the old plain-text / lightweight-markdown
format, so this one-off data migration converts them using the same rules the
old template parsers used — preserving how the current content looks.
"""

import html

from django.db import migrations


def _p(text):
    return "<p>" + html.escape(text).replace("\n", "<br>") + "</p>"


def _paras_to_html(text):
    return "\n".join(_p(c.strip()) for c in text.split("\n\n") if c.strip())


def _page_to_html(text):
    out = []
    for chunk in text.split("\n\n"):
        chunk = chunk.strip()
        if not chunk:
            continue
        if chunk.endswith(":") and len(chunk) < 80:
            out.append("<h2>" + html.escape(chunk.rstrip(":")) + "</h2>")
        else:
            out.append(_p(chunk))
    return "\n".join(out)


def _blog_to_html(text):
    out = []
    for raw in text.split("\n\n"):
        raw = raw.strip()
        if not raw:
            continue
        lines = raw.splitlines()
        if raw.startswith("## "):
            out.append("<h2>" + html.escape(raw[3:].strip()) + "</h2>")
        elif all(line.strip().startswith("- ") for line in lines):
            items = "".join(
                "<li>" + html.escape(line.strip()[2:].strip()) + "</li>" for line in lines
            )
            out.append("<ul>" + items + "</ul>")
        else:
            out.append(_p(raw))
    return "\n".join(out)


_CONVERSIONS = [
    ("core", "Page", "body", _page_to_html),
    ("blog", "BlogPost", "body", _blog_to_html),
    ("services", "Service", "description", _paras_to_html),
    ("services", "ServiceCategory", "description", _paras_to_html),
    ("team", "Doctor", "full_bio", _paras_to_html),
    ("events", "Event", "description", _paras_to_html),
]


def forwards(apps, schema_editor):
    for app_label, model_name, field, convert in _CONVERSIONS:
        Model = apps.get_model(app_label, model_name)
        for obj in Model.objects.all():
            value = getattr(obj, field) or ""
            # Skip empty or already-HTML content (idempotent / safe to re-run).
            if not value.strip() or value.lstrip().startswith("<"):
                continue
            setattr(obj, field, convert(value))
            obj.save(update_fields=[field])


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_page"),
        ("blog", "0002_seed_blog"),
        ("services", "0003_service_image"),
        ("team", "0003_seed_real_doctors"),
        ("events", "0002_event_image"),
    ]

    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
