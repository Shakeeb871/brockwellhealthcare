"""Clear the legacy emoji values from Service.icon and ServiceCategory.icon.

These fields are no longer rendered anywhere: the nav and every card now draw
SVG glyphs via the {% category_icon %} / {% service_icon %} template tags, which
map from the slug, not from this field. Blanking the field removes the last
emoji from the project so nothing emoji-based can leak onto the site."""

import re

from django.db import migrations

_EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\U00002190-\U000021FF\U00002300-\U000027BF"
    "\U00002B00-\U00002BFF\U0000FE00-\U0000FE0F\U00002600-\U000026FF]"
)


def clear_icons(apps, schema_editor):
    for model_name in ("Service", "ServiceCategory"):
        Model = apps.get_model("services", model_name)
        for obj in Model.objects.all():
            if obj.icon and _EMOJI.search(obj.icon):
                obj.icon = ""
                obj.save(update_fields=["icon"])


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0086_emsculpt_neo_content"),
    ]

    operations = [migrations.RunPython(clear_icons, migrations.RunPython.noop)]
