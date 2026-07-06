"""Nest NAD+ IV Therapy under Longevity IVs (third-level sub-page), so the nav
reads Longevity | Healthspan → Longevity IVs → NAD+ IV Therapy."""

from django.db import migrations


def nest(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    parent = Service.objects.filter(region="uae", slug="longevity-ivs").first()
    child = Service.objects.filter(region="uae", slug="nad-iv-therapy").first()
    if parent and child:
        child.parent = parent
        child.category = parent.category
        child.save(update_fields=["parent", "category"])


def unnest(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    child = Service.objects.filter(region="uae", slug="nad-iv-therapy").first()
    if child:
        child.parent = None
        child.save(update_fields=["parent"])


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0039_service_parent"),
    ]

    operations = [migrations.RunPython(nest, unnest)]
