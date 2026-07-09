"""Add ONE inline content image to the Emsculpt NEO service description without
changing any of the existing copy. The image tag is inserted before the
'What it does to muscle and fat' section; the hero image (emsculpt-neo-hero.webp)
is resolved by the view and shown as the grid card thumbnail automatically.
Stripping any existing emsculpt-neo-content image first keeps this idempotent, and
reversing removes only the inserted image."""

import re

from django.db import migrations

SLUG = "emsculpt-neo"
ANCHOR = "<h2>What it does to muscle and fat</h2>"
IMG = (
    '<img src="/static/img/services/emsculpt-neo-content.webp" '
    'alt="Emsculpt NEO body-contouring and muscle-strengthening session at '
    'Brockwell Healthcare in Dubai" loading="lazy" decoding="async">'
)


def place(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc or not svc.description:
        return
    desc = re.sub(r'<img[^>]*emsculpt-neo-content[^>]*>\s*', "", svc.description)
    if ANCHOR in desc:
        desc = desc.replace(ANCHOR, f"{IMG}\n\n{ANCHOR}", 1)
    svc.description = desc
    svc.save(update_fields=["description"])


def remove(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc or not svc.description:
        return
    svc.description = re.sub(
        r'<img[^>]*emsculpt-neo-content[^>]*>\s*', "", svc.description
    )
    svc.save(update_fields=["description"])


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0108_regeniv_physio_inline_images"),
    ]

    operations = [migrations.RunPython(place, remove)]
