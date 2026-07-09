"""Add the inline content image to the Stress Reset service description now that its
file has been supplied. The image is inserted before the 'What we address' section; the
hero (stress-reset-hero.webp) is resolved by the view and shown as the grid card
thumbnail automatically. Stripping any existing stress-reset-content image first keeps
this idempotent."""

import re

from django.db import migrations

SLUG = "stress-reset"
ANCHOR = "<h2>What we address</h2>"
IMG = (
    '<img src="/static/img/services/stress-reset-content.webp" '
    'alt="Doctor-led Stress Reset assessment and burnout recovery at '
    'Brockwell Healthcare in Dubai" loading="lazy" decoding="async">'
)


def place(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc or not svc.description:
        return
    desc = re.sub(r'<img[^>]*stress-reset-content[^>]*>\s*', "", svc.description)
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
        r'<img[^>]*stress-reset-content[^>]*>\s*', "", svc.description
    )
    svc.save(update_fields=["description"])


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0113_stress_reset_content_v2"),
    ]

    operations = [migrations.RunPython(place, remove)]
