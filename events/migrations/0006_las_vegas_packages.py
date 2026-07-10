"""Seed the four registration packages for the Las Vegas workshop so the
pricing cards drive real Stripe Checkout. Amounts are stored server-side and
are the authoritative price used at checkout."""

from decimal import Decimal

from django.db import migrations

SLUG = "regenerative-injection-training-las-vegas"

PACKAGES = [
    {
        "name": "Early Registration", "slug": "early", "amount": Decimal("1495.00"),
        "sort": 1, "is_featured": False, "badge": "",
        "features": "First 10 registrants only\n"
                    "Full access to all lectures and training sessions\n"
                    "Complete course materials\n"
                    "Certificate of attendance\n"
                    "Networking opportunities",
    },
    {
        "name": "Standard Registration", "slug": "standard", "amount": Decimal("1995.00"),
        "sort": 2, "is_featured": False, "badge": "",
        "features": "Full conference and training access\n"
                    "Hands-on training sessions\n"
                    "Educational materials\n"
                    "Certificate of attendance\n"
                    "Networking access",
    },
    {
        "name": "VIP Mentorship Package", "slug": "vip", "amount": Decimal("2995.00"),
        "sort": 3, "is_featured": True, "badge": "Most complete",
        "features": "Everything in Standard Registration\n"
                    "Priority seating\n"
                    "Small-group mentorship\n"
                    "Direct Q&A with faculty\n"
                    "Exclusive VIP resource materials\n"
                    "Post-event guidance and support",
    },
    {
        "name": "Observer Registration", "slug": "observer", "amount": Decimal("995.00"),
        "sort": 4, "is_featured": False, "badge": "",
        "features": "Lecture and observation only\n"
                    "Access to all didactic sessions\n"
                    "Live procedure demonstrations\n"
                    "Observation areas\n"
                    "General course materials\n"
                    "Hands-on participation not included",
    },
]


def seed(apps, schema_editor):
    Event = apps.get_model("events", "Event")
    EventPackage = apps.get_model("events", "EventPackage")
    event = Event.objects.filter(region="us", slug=SLUG).first()
    if not event:
        return
    for p in PACKAGES:
        EventPackage.objects.update_or_create(
            event=event, slug=p["slug"],
            defaults=dict(
                name=p["name"], amount=p["amount"], features=p["features"],
                badge=p["badge"], is_featured=p["is_featured"],
                is_active=True, sort=p["sort"],
            ),
        )


def unseed(apps, schema_editor):
    Event = apps.get_model("events", "Event")
    EventPackage = apps.get_model("events", "EventPackage")
    event = Event.objects.filter(region="us", slug=SLUG).first()
    if event:
        EventPackage.objects.filter(
            event=event, slug__in=[p["slug"] for p in PACKAGES]
        ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0005_eventpackage_eventregistration_package"),
    ]

    operations = [migrations.RunPython(seed, unseed)]
