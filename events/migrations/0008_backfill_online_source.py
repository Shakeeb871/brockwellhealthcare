"""Backfill the new ``source`` field: any registration that already carries a
Stripe session id (i.e. it came through an online payment) is marked as an
online payment; everything else stays an enquiry-form lead (the default)."""

from django.db import migrations


def backfill(apps, schema_editor):
    EventRegistration = apps.get_model("events", "EventRegistration")
    EventRegistration.objects.exclude(stripe_session_id="").update(source="online")


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0007_onlinepayment_eventregistration_source"),
    ]

    operations = [migrations.RunPython(backfill, noop)]
