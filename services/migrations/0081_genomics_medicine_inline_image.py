"""Add the inline content image to the Genomics Medicine service description, placed
after the 'What your DNA can, and cannot, tell you' section (before 'Where genomic
testing is genuinely useful'). The hero image
(static/img/services/genomics-medicine-hero.webp) is resolved automatically by the
view; this migration only inserts the inline image and is idempotent."""

from django.db import migrations

SLUG = "genomics-medicine"

IMG = (
    '<img src="/static/img/services/genomics-medicine-content.webp" '
    'alt="Doctor interpreting genetic testing results as part of a genomics medicine '
    'plan at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">'
)
ANCHOR = "<h2>Where genomic testing is genuinely useful</h2>"


def add_image(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc or not svc.description:
        return
    if "genomics-medicine-content.webp" in svc.description:
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
        ("services", "0080_genomics_medicine_content_v2"),
    ]

    operations = [migrations.RunPython(add_image, remove_image)]
