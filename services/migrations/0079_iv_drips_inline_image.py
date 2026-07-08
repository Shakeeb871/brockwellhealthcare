"""Add the inline content image to the IV Drips service description, placed after the
'What is an IV drip?' section (before 'Why give nutrients by vein at all'). The hero
image (static/img/services/iv-drips-hero.webp) is resolved automatically by the view;
this migration only inserts the inline image and is idempotent."""

from django.db import migrations

SLUG = "iv-drips"

IMG = (
    '<img src="/static/img/services/iv-drips-content.webp" '
    'alt="Patient receiving a doctor-supervised IV drip at Brockwell Healthcare in Dubai" '
    'loading="lazy" decoding="async">'
)
ANCHOR = "<h2>Why give nutrients by vein at all</h2>"


def add_image(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc or not svc.description:
        return
    if "iv-drips-content.webp" in svc.description:
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
        ("services", "0078_longevity_medicine_content_v2"),
    ]

    operations = [migrations.RunPython(add_image, remove_image)]
