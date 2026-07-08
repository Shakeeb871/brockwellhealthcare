"""Add the inline content image to the Ozone Therapy service description, placed
after the 'How a small, controlled dose works' section (before 'The methods, from
gentle to intensive'). The hero image (static/img/services/ozone-therapy-hero.webp)
is resolved automatically by the view; this migration only inserts the inline image
and is idempotent."""

from django.db import migrations

SLUG = "ozone-therapy"

IMG = (
    '<img src="/static/img/services/ozone-therapy-content.webp" '
    'alt="Doctor delivering a sterile, closed-system medical ozone treatment '
    'at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">'
)
ANCHOR = "<h2>The methods, from gentle to intensive</h2>"


def add_image(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc or not svc.description:
        return
    if "ozone-therapy-content.webp" in svc.description:
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
        ("services", "0067_ketamine_therapy_content_v3"),
    ]

    operations = [migrations.RunPython(add_image, remove_image)]
