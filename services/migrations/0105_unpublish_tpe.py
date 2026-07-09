"""Remove Therapeutic Plasma Exchange from the website by unpublishing it.

The service is taken off the navigation and its page returns 404, but the
record, content and images are retained so it can be re-enabled later. Reverse
re-publishes it."""

from django.db import migrations

SLUG = "therapeutic-plasma-exchange"


def unpublish(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    Service.objects.filter(region="uae", slug=SLUG).update(is_published=False)


def republish(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    Service.objects.filter(region="uae", slug=SLUG).update(is_published=True)


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0104_male_wellness_content_v2"),
    ]

    operations = [migrations.RunPython(unpublish, republish)]
