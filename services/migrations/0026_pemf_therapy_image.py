"""Add the inline content photo to the PEMF Therapy page (the hero photo loads
automatically from the static file). Inserts the image after the 'How Does PEMF
Therapy Work?' section, just before the 'Types of PEMF Therapy' section."""

from django.db import migrations

IMG = (
    '<img src="/static/img/services/pemf-therapy-content.webp" '
    'alt="PEMF therapy session at Brockwell Healthcare in Dubai" '
    'loading="lazy" decoding="async">'
)
MARKER = "<h2>Types of PEMF Therapy</h2>"


def add_image(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug="pemf-therapy").first()
    if not svc or not svc.description:
        return
    if "pemf-therapy-content.webp" in svc.description:
        return  # already present
    if MARKER in svc.description:
        svc.description = svc.description.replace(MARKER, IMG + "\n\n" + MARKER, 1)
        svc.save()


def remove_image(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug="pemf-therapy").first()
    if not svc or not svc.description:
        return
    svc.description = svc.description.replace(IMG + "\n\n", "").replace(IMG, "")
    svc.save()


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0025_iv_laser_therapy_content"),
    ]

    operations = [migrations.RunPython(add_image, remove_image)]
