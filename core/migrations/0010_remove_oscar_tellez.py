"""Oscar Tellez is not a doctor — hide him from the Our Doctors section
(and every doctor listing) by unpublishing the record."""

from django.db import migrations


def load(apps, schema_editor):
    Doctor = apps.get_model("team", "Doctor")
    Doctor.objects.filter(region="uae", slug="oscar-tellez").update(is_published=False)


def unload(apps, schema_editor):
    Doctor = apps.get_model("team", "Doctor")
    Doctor.objects.filter(region="uae", slug="oscar-tellez").update(is_published=True)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_doctor_photos"),
        ("team", "0003_seed_real_doctors"),
    ]

    operations = [migrations.RunPython(load, unload)]
