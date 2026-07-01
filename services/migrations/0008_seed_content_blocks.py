"""Convert each service's existing description / benefits / FAQs into ordered
content blocks, so the new fully block-based service page keeps all content.

Runs once; skips any service that already has blocks (idempotent-safe).
"""

from django.db import migrations


def create_blocks(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    PageSection = apps.get_model("services", "PageSection")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    try:
        service_ct = ContentType.objects.get(app_label="services", model="service")
    except ContentType.DoesNotExist:
        service_ct = None

    for svc in Service.objects.all():
        if PageSection.objects.filter(service=svc).exists():
            continue

        order = 0
        if (svc.description or "").strip():
            PageSection.objects.create(service=svc, kind="text", body=svc.description, order=order)
            order += 1

        benefits = [ln.strip() for ln in (svc.benefits or "").splitlines() if ln.strip()]
        if benefits:
            PageSection.objects.create(
                service=svc, kind="benefits", heading="Key Benefits",
                items="\n".join(benefits), order=order,
            )
            order += 1

        has_faq = service_ct and FAQItem.objects.filter(
            content_type=service_ct, object_id=svc.id, is_published=True
        ).exists()
        if has_faq:
            PageSection.objects.create(service=svc, kind="faq", heading="Frequently Asked Questions", order=order)
            order += 1

        PageSection.objects.create(service=svc, kind="booking", heading="Book A Consultation", order=order)


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0007_pagesection"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(create_blocks, migrations.RunPython.noop)]
