"""Place a single inline content image in the Regenerative IV Therapy and
Physiotherapy service descriptions. Hero images (``<slug>-hero.webp``) are resolved
by the view and shown as the grid card thumbnail automatically. Stripping any
existing ``<slug>-content`` inline image first keeps this idempotent."""

import re

from django.db import migrations

# slug -> (content image file, anchor <h2> to sit before, alt text)
INLINE = {
    "regenerative-iv-therapy": (
        "regenerative-iv-therapy-content.webp",
        "<h2>How it works, and the honest limits</h2>",
        "Regenerative IV nutrient infusion prepared and administered at Brockwell Healthcare in Dubai",
    ),
    "physiotherapy": (
        "physiotherapy-content.webp",
        "<h2>What physiotherapy treats</h2>",
        "Doctor-led physiotherapy and rehabilitation session at Brockwell Healthcare in Dubai",
    ),
}


def _img(fname, alt):
    return (
        f'<img src="/static/img/services/{fname}" alt="{alt}" '
        f'loading="lazy" decoding="async">'
    )


def place(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    for slug, (fname, anchor, alt) in INLINE.items():
        svc = Service.objects.filter(region="uae", slug=slug).first()
        if not svc or not svc.description:
            continue
        stem = fname.replace(".webp", "")
        desc = re.sub(rf'<img[^>]*{re.escape(stem)}[^>]*>\s*', "", svc.description)
        if anchor in desc:
            desc = desc.replace(anchor, f"{_img(fname, alt)}\n\n{anchor}", 1)
        svc.description = desc
        svc.save(update_fields=["description"])


def remove(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    for slug, (fname, _anchor, _alt) in INLINE.items():
        svc = Service.objects.filter(region="uae", slug=slug).first()
        if not svc or not svc.description:
            continue
        stem = fname.replace(".webp", "")
        svc.description = re.sub(
            rf'<img[^>]*{re.escape(stem)}[^>]*>\s*', "", svc.description
        )
        svc.save(update_fields=["description"])


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0107_functional_medicine_content_v2"),
    ]

    operations = [migrations.RunPython(place, remove)]
