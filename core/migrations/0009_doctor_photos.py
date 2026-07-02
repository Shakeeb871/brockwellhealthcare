"""Wire each doctor's uploaded photo (static/img/doctors/<slug>.jpg) to the
`photo` field so it shows in the home 'Our Doctors' spotlight and profiles."""

from django.db import migrations

SLUGS = [
    "dr-hasnain-haider-shah", "dr-nigel-beejay", "dr-adeel-khan-md",
    "dr-sabine-hazan-md", "dr-salman-gilani", "shirley-dsouza",
    "shahnawaz-hussein-khan-phd", "dr-nameer-haider", "prof-dato-sri-dr-mike-chan",
    "dr-rozina-badal-munir", "dr-summer-beattie", "rachel-tan-garcia",
    "dr-don-buford", "jean-francois-tremblay", "oscar-tellez",
]


def load(apps, schema_editor):
    Doctor = apps.get_model("team", "Doctor")
    for slug in SLUGS:
        Doctor.objects.filter(region="uae", slug=slug).update(
            photo=f"/static/img/doctors/{slug}.jpg"
        )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_doctor_full_bios"),
        ("team", "0003_seed_real_doctors"),
    ]

    operations = [migrations.RunPython(load, migrations.RunPython.noop)]
