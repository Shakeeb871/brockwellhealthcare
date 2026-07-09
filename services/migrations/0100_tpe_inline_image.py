"""Place a single inline content image in the Therapeutic Plasma Exchange service
description, before the 'The longevity idea, and where it comes from' section. The
hero image (static/img/services/therapeutic-plasma-exchange-hero.webp) is resolved
by the view. Stripping any existing tpe content image first keeps this idempotent."""

import re

from django.db import migrations

SLUG = "therapeutic-plasma-exchange"
ANCHOR = "<h2>The longevity idea, and where it comes from</h2>"
IMG = (
    '<img src="/static/img/services/therapeutic-plasma-exchange-content.webp" '
    'alt="Therapeutic plasma exchange being carried out under medical supervision at '
    'Brockwell Healthcare in Dubai" loading="lazy" decoding="async">'
)


def place_image(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc or not svc.description:
        return
    desc = re.sub(
        r'<img[^>]*therapeutic-plasma-exchange-content[^>]*>\s*', "", svc.description
    )
    if ANCHOR in desc:
        desc = desc.replace(ANCHOR, f"{IMG}\n\n{ANCHOR}", 1)
    svc.description = desc
    svc.save(update_fields=["description"])


def remove_image(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc or not svc.description:
        return
    svc.description = re.sub(
        r'<img[^>]*therapeutic-plasma-exchange-content[^>]*>\s*', "", svc.description
    )
    svc.save(update_fields=["description"])


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0099_healthspan_revert_service_images"),
    ]

    operations = [migrations.RunPython(place_image, remove_image)]
