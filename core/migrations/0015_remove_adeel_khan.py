"""Remove Dr. Adeel Khan from the team, on request.

Unpublishing is what takes him off the site: the Our Team grid, the home-page
doctor spotlight, his own profile page and the team sitemap all read published
Doctor records, so this removes him from every one of them at once. It is also
reversible, which a delete would not be.

Not filtered by region, unlike 0010 — the request was to remove him from the
whole site, so this covers the US and UAE records together and any market added
later.

The About page lists its specialists from a hard-coded slug list in
core/views.py that does not check is_published, so his entry is removed there in
the same change.
"""

from django.db import migrations

SLUG = "dr-adeel-khan-md"


def load(apps, schema_editor):
    Doctor = apps.get_model("team", "Doctor")
    Doctor.objects.filter(slug=SLUG).update(is_published=False)


def unload(apps, schema_editor):
    Doctor = apps.get_model("team", "Doctor")
    Doctor.objects.filter(slug=SLUG).update(is_published=True)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_indexsubmission_source_alter_indexsubmission_engine"),
        ("team", "0003_seed_real_doctors"),
    ]

    operations = [migrations.RunPython(load, unload)]
