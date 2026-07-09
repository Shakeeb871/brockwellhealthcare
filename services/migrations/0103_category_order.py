"""Reorder the top-level service menu to the agreed sequence:
Regenerative Wellness, Regenerative Medicine, Longevity | Healthspan,
Anti-Aging Aesthetics, Chronic Pain, Advanced Diagnostics."""

from django.db import migrations

CATEGORY_ORDER = [
    "regenerative-wellness",
    "regenerative-medicine",
    "longevity-healthspan",
    "anti-aging-aesthetics",
    "chronic-pain",
    "advanced-diagnostics",
]


def reorder(apps, schema_editor):
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    for i, slug in enumerate(CATEGORY_ORDER):
        ServiceCategory.objects.filter(region="uae", slug=slug).update(order=i)


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0102_menu_restructure"),
    ]

    operations = [migrations.RunPython(reorder, migrations.RunPython.noop)]
