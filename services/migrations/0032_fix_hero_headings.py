"""Restore the full hero H1 headings exactly as provided for the Urology and
Regenerative Orthopedics pages (the tagline after the '|' was previously
trimmed). Stored with a literal '&' so template auto-escaping renders it once."""

from django.db import migrations

HEADINGS = {
    "urology-services": "Urology Clinic in Dubai | Expert, Doctor-Led Urologists",
    "regenerative-orthopedics": (
        "Regenerative Orthopedic Treatment in Dubai | Non-Surgical Joint & Tissue Repair"
    ),
}


def set_headings(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    for slug, heading in HEADINGS.items():
        Service.objects.filter(region="uae", slug=slug).update(hero_heading=heading)


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0031_regenerative_orthopedics_content"),
    ]

    operations = [migrations.RunPython(set_headings, migrations.RunPython.noop)]
