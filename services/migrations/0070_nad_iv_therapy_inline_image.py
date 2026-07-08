"""Add the inline content image to the NAD+ IV Therapy service description, placed
after the 'Why deliver it through a drip' section (before 'Why the drip has to be
slow'). The hero image (static/img/services/nad-iv-therapy-hero.webp) is resolved
automatically by the view; this migration only inserts the inline image and is
idempotent."""

from django.db import migrations

SLUG = "nad-iv-therapy"

IMG = (
    '<img src="/static/img/services/nad-iv-therapy-content.webp" '
    'alt="Patient receiving a slow, doctor-supervised NAD+ IV infusion '
    'at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">'
)
ANCHOR = "<h2>Why the drip has to be slow</h2>"


def add_image(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc or not svc.description:
        return
    if "nad-iv-therapy-content.webp" in svc.description:
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
        ("services", "0069_nad_iv_therapy_content_v3"),
    ]

    operations = [migrations.RunPython(add_image, remove_image)]
