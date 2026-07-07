"""Add the inline content image to the Stem Cells service description, placed
after the 'How Does Stem Cell Therapy Work?' section (before 'Types of Stem Cell
Therapy'). The hero image (static/img/services/stem-cells-hero.webp) is resolved
automatically by the view; this migration only inserts the inline image so it is
idempotent and safe to re-run."""

from django.db import migrations

SLUG = "stem-cells"

IMG = (
    '<img src="/static/img/services/stem-cells-content.webp" '
    'alt="Doctor preparing a stem cell therapy treatment under ultrasound guidance '
    'at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">'
)
ANCHOR = "<h2>Types of Stem Cell Therapy</h2>"


def add_image(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc or not svc.description:
        return
    # Idempotent: do nothing if the inline image is already present.
    if "stem-cells-content.webp" in svc.description:
        return
    if ANCHOR in svc.description:
        svc.description = svc.description.replace(ANCHOR, f"{IMG}\n\n{ANCHOR}", 1)
        svc.save(update_fields=["description"])


def remove_image(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc or not svc.description:
        return
    svc.description = svc.description.replace(f"{IMG}\n\n", "").replace(IMG, "")
    svc.save(update_fields=["description"])


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0052_stem_cells_content"),
    ]

    operations = [migrations.RunPython(add_image, remove_image)]
