"""Keyword-rich page H1s (hero_heading) for the service pages built so far."""

from django.db import migrations

HEADINGS = {
    "detox-therapy": "Detox Therapy in Dubai",
    "red-light-therapy": "Red Light Therapy in Dubai",
    "stem-cells": "Stem Cell Therapy in Dubai",
    "longevity-ivs": "Longevity IVs in Dubai",
}


def load(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    for slug, heading in HEADINGS.items():
        Service.objects.filter(region="uae", slug=slug).update(hero_heading=heading)


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0016_service_hero_heading"),
    ]

    operations = [migrations.RunPython(load, migrations.RunPython.noop)]
