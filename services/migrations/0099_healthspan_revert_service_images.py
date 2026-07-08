"""Revert the Healthspan *service* description to a single inline content image.

The four uploaded healthspan images belong on the Longevity | Healthspan *category*
(core-service) page, not on this sub-service. This strips the three inline images
added in 0098 and restores the single healthspan-content.webp image (as in 0092),
placed before the 'The gap, and compression of morbidity' section."""

import re

from django.db import migrations

SLUG = "healthspan"
IMG = (
    '<img src="/static/img/services/healthspan-content.webp" '
    'alt="Active, healthy ageing supported by a healthspan-focused plan at '
    'Brockwell Healthcare in Dubai" loading="lazy" decoding="async">'
)
ANCHOR = "<h2>The gap, and compression of morbidity</h2>"


def revert(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc or not svc.description:
        return
    desc = re.sub(r'<img[^>]*healthspan-content[^>]*>\s*', "", svc.description)
    if "healthspan-content.webp" not in desc and ANCHOR in desc:
        desc = desc.replace(ANCHOR, f"{IMG}\n\n{ANCHOR}", 1)
    svc.description = desc
    svc.save(update_fields=["description"])


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0098_healthspan_inline_images"),
    ]

    operations = [migrations.RunPython(revert, migrations.RunPython.noop)]
