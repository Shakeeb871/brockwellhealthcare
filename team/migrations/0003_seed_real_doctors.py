from django.db import migrations
from django.utils.text import slugify

# (name, photo path). Photo blank -> initials avatar (editable in admin).
DOCTORS = [
    ("Dr. Hasnain Haider-Shah", "/static/img/dr-shah-brockwell-health-care.webp"),
    ("Dr. Nigel Beejay", ""),
    ("Dr. Adeel Khan, MD", ""),
    ("Dr. Sabine Hazan, MD", ""),
    ("Dr. Salman Gilani", ""),
    ("Shirley D'Souza", ""),
    ("Jean-Francois Tremblay", ""),
    ("Shahnawaz Hussein Khan, PhD", ""),
    ("Dr. Nameer Haider", ""),
    ("Prof. Dato' Sri Dr. Mike Chan", ""),
    ("Dr. Rozina Badal Munir", ""),
    ("Dr. Summer Beattie", ""),
    ("Rachel Tan Garcia", ""),
    ("Oscar Tellez", ""),
    ("Dr Don Buford", ""),
]

# The initial placeholder doctors to remove.
PLACEHOLDERS = ["dr-sarah-al-mansoori", "dr-james-carter", "dr-layla-hassan"]


def seed(apps, schema_editor):
    Doctor = apps.get_model("team", "Doctor")
    Doctor.objects.filter(region="uae", slug__in=PLACEHOLDERS).delete()
    for order, (name, photo) in enumerate(DOCTORS, start=1):
        Doctor.objects.get_or_create(
            region="uae",
            slug=slugify(name),
            defaults={
                "name": name,
                "title": "Specialist",
                "photo": photo,
                "short_bio": "Part of the expert medical team at Brockwell Healthcare.",
                "full_bio": (
                    "Part of the expert medical team at Brockwell Healthcare. "
                    "(Add this specialist's full profile, specialties and photo in the admin.)"
                ),
                "order": order,
                "is_published": True,
            },
        )


def unseed(apps, schema_editor):
    Doctor = apps.get_model("team", "Doctor")
    Doctor.objects.filter(
        region="uae", slug__in=[slugify(n) for n, _ in DOCTORS]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("team", "0002_doctor_available_today_doctor_experience_and_more"),
    ]
    operations = [migrations.RunPython(seed, unseed)]
