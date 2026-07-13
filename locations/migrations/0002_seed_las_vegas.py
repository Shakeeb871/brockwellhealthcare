"""Seed the first clinic location (Las Vegas) and link the US doctors.

Idempotent: safe to run on every environment. Uses the US address that already
lives in settings so there is a single source of truth.
"""

from django.conf import settings
from django.db import migrations


def seed(apps, schema_editor):
    Location = apps.get_model("locations", "Location")
    Doctor = apps.get_model("team", "Doctor")

    us = settings.REGIONS.get("us", {})
    loc, _ = Location.objects.get_or_create(
        region="us",
        slug="las-vegas",
        defaults={
            "name": f"{settings.BRAND_NAME} — Las Vegas",
            "city": "Las Vegas",
            "state": "Nevada",
            "state_code": "NV",
            "street_address": us.get("street", "8879 W Flamingo Rd, Ste 201"),
            "postal_code": us.get("postal", "89147"),
            "phone": us.get("phone", ""),
            "email": us.get("email", ""),
            "hours": "Mon – Fri: 9:00 AM – 5:00 PM\nSat: 9:00 AM – 1:00 PM\nSun: Closed",
            "intro": "Regenerative medicine, longevity and wellness care in Las Vegas, Nevada.",
            "is_primary": True,
            "is_active": True,
            "order": 0,
        },
    )

    # Link every published US doctor to the flagship clinic.
    us_doctors = Doctor.objects.filter(region="us", is_published=True)
    if us_doctors.exists():
        loc.doctors.add(*us_doctors)


def unseed(apps, schema_editor):
    Location = apps.get_model("locations", "Location")
    Location.objects.filter(region="us", slug="las-vegas").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("locations", "0001_initial"),
        ("team", "0003_seed_real_doctors"),
    ]

    operations = [migrations.RunPython(seed, unseed)]
