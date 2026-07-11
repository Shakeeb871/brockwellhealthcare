"""Restore the homepage FAQ list for the US region.

The FAQs were seeded for UAE only; when the US region was built by cloning
content, the FAQs were not carried over, so the US homepage FAQ list rendered
empty. This recreates the same eight FAQs for region="us" (idempotent), with
the one UAE/DHA-specific entry adapted to be location-neutral for the US site.
"""

from django.db import migrations

# (order, question, answer) — mirrors the UAE FAQs; entry 0 is de-localised.
FAQS = [
    (0, "Is regenerative medicine safe and properly regulated?",
     "Yes. Board-certified physicians carry out regenerative treatments at "
     "Brockwell under established medical standards, and we confirm your "
     "suitability through an assessment first."),
    (1, "Are regenerative treatments painful, and is there downtime?",
     "Most treatments are minimally invasive and well tolerated. Any discomfort "
     "and recovery time depend on the therapy, and we explain both before you decide."),
    (2, "How soon might I notice results?",
     "It varies by treatment and condition. Some patients feel changes within "
     "weeks, while regenerative repair can keep building over several months."),
    (3, "How much do treatments cost?",
     "Cost depends on the treatment and your assessment. You receive a clear "
     "quote after your consultation, with no obligation to proceed."),
    (4, "What is the difference between stem cell therapy and PRP?",
     "PRP uses concentrated platelets from your own blood, while stem cell "
     "therapy uses regenerative cells. Your assessment determines which suits your case."),
    (5, "Can regenerative medicine help me avoid surgery?",
     "For some conditions, yes. We check whether a non-surgical option is "
     "realistic for you, and we refer you on when surgery is the better choice."),
    (6, "What happens at the first consultation?",
     "We review your history, symptoms and goals, discuss possible options and "
     "recommend any diagnostics needed before building a plan."),
    (7, "Do I need a doctor's referral to book?",
     "No referral is required. You can book a consultation directly and bring "
     "any past reports or scans you already have."),
]


def add_us_faqs(apps, schema_editor):
    FAQ = apps.get_model("core", "FAQ")
    for order, question, answer in FAQS:
        FAQ.objects.update_or_create(
            region="us", question=question,
            defaults=dict(answer=answer, order=order, is_published=True),
        )


def remove_us_faqs(apps, schema_editor):
    FAQ = apps.get_model("core", "FAQ")
    FAQ.objects.filter(region="us", question__in=[q for _, q, _ in FAQS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_remove_oscar_tellez"),
    ]

    operations = [migrations.RunPython(add_us_faqs, remove_us_faqs)]
