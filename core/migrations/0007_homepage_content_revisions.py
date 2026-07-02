"""Revised UAE homepage copy: refined category one-liners and FAQ answers."""

from django.db import migrations


CATEGORY_SUMMARIES = {
    "regenerative-wellness": "Improves energy, recovery and everyday function through natural, body-led healing.",
    "regenerative-medicine": "Repairs worn joints, tendons and nerves using biologic therapies, without surgery.",
    "longevity-healthspan": "Slows age-related decline so you stay active and well for longer.",
    "anti-aging-aesthetics": "Restores a natural, youthful look through regenerative treatments with little downtime.",
    "advanced-diagnostics": "Finds the real cause of your symptoms before we plan any treatment.",
    "emsculpt-for-pain": "Eases chronic pain and strengthens weak muscles through non-invasive stimulation.",
}

FAQS = [
    ("Is stem cell therapy legal and regulated in the UAE?",
     "Yes. DHA-licensed physicians carry out regenerative treatments at Brockwell within UAE medical "
     "regulations, and we confirm your suitability through an assessment first."),
    ("Are regenerative treatments painful, and is there downtime?",
     "Most treatments are minimally invasive and well tolerated. Any discomfort and recovery time depend "
     "on the therapy, and we explain both before you decide."),
    ("How soon might I notice results?",
     "It varies by treatment and condition. Some patients feel changes within weeks, while regenerative "
     "repair can keep building over several months."),
    ("How much do treatments cost?",
     "Cost depends on the treatment and your assessment. You receive a clear quote after your "
     "consultation, with no obligation to proceed."),
    ("What is the difference between stem cell therapy and PRP?",
     "PRP uses concentrated platelets from your own blood, while stem cell therapy uses regenerative "
     "cells. Your assessment determines which suits your case."),
    ("Can regenerative medicine help me avoid surgery?",
     "For some conditions, yes. We check whether a non-surgical option is realistic for you, and we refer "
     "you on when surgery is the better choice."),
    ("What happens at the first consultation?",
     "We review your history, symptoms and goals, discuss possible options and recommend any diagnostics "
     "needed before building a plan."),
    ("Do I need a doctor's referral to book?",
     "No referral is required. You can book a consultation directly and bring any past reports or scans "
     "you already have."),
]


def load(apps, schema_editor):
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    FAQ = apps.get_model("core", "FAQ")

    for slug, summary in CATEGORY_SUMMARIES.items():
        ServiceCategory.objects.filter(region="uae", slug=slug).update(summary=summary)

    FAQ.objects.filter(region="uae").delete()
    for i, (q, a) in enumerate(FAQS):
        FAQ.objects.create(region="uae", question=q, answer=a, order=i, is_published=True)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_homepage_final_content"),
        ("services", "0012_detox_therapy_content"),
    ]

    operations = [migrations.RunPython(load, migrations.RunPython.noop)]
