"""Place three inline content images across the Healthspan service description, one
before each of the middle sections, and rely on the hero image
(static/img/services/healthspan-hero.webp) resolved by the view. Any pre-existing
healthspan-content* inline image is stripped first, so the migration is idempotent."""

import re

from django.db import migrations

SLUG = "healthspan"

# (image file, anchor heading it should sit before)
INLINE = [
    ("healthspan-content.webp",
     "Older adults staying active and independent, the goal of a healthspan-focused plan at Brockwell Healthcare in Dubai",
     "<h2>What healthspan means</h2>"),
    ("healthspan-content-2.webp",
     "Compression of morbidity illustrated: keeping the healthy years long and the decline short",
     "<h2>The gap, and compression of morbidity</h2>"),
    ("healthspan-content-3.webp",
     "The everyday fundamentals, exercise, nutrition and sleep, that extend healthspan at Brockwell Healthcare in Dubai",
     "<h2>How healthspan is actually extended</h2>"),
]


def _img(fname, alt):
    return (
        f'<img src="/static/img/services/{fname}" alt="{alt}" '
        f'loading="lazy" decoding="async">'
    )


def place_images(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc or not svc.description:
        return
    desc = svc.description
    # Strip any existing healthspan-content* inline images so this is idempotent.
    desc = re.sub(r'<img[^>]*healthspan-content[^>]*>\s*', "", desc)
    for fname, alt, anchor in INLINE:
        if anchor in desc:
            desc = desc.replace(anchor, f"{_img(fname, alt)}\n\n{anchor}", 1)
    svc.description = desc
    svc.save(update_fields=["description"])


def remove_images(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc or not svc.description:
        return
    svc.description = re.sub(r'<img[^>]*healthspan-content[^>]*>\s*', "", svc.description)
    svc.save(update_fields=["description"])


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0097_hydrodissection_content_v2"),
    ]

    operations = [migrations.RunPython(place_images, remove_images)]
