"""Add the inline content photo to the Longevity IVs page (the hero photo loads
automatically from the static file). Inserts the image after the 'How Do
Longevity IVs Work?' section, just before the 'Types of Longevity IVs' section."""

from django.db import migrations

IMG = (
    '<img src="/static/img/services/longevity-ivs-content.webp" '
    'alt="Longevity IV therapy session at Brockwell Healthcare in Dubai" '
    'loading="lazy" decoding="async">'
)
MARKER = "<h2>Types of Longevity IVs</h2>"


def add_image(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug="longevity-ivs").first()
    if not svc or not svc.description:
        return
    if "longevity-ivs-content.webp" in svc.description:
        return  # already present
    if MARKER in svc.description:
        svc.description = svc.description.replace(MARKER, IMG + "\n\n" + MARKER, 1)
        svc.save()


def remove_image(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug="longevity-ivs").first()
    if not svc or not svc.description:
        return
    svc.description = svc.description.replace(IMG + "\n\n", "").replace(IMG, "")
    svc.save()


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0036_longevity_medicine_content"),
    ]

    operations = [migrations.RunPython(add_image, remove_image)]
