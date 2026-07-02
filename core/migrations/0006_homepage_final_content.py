"""Final UAE homepage content: category one-liners, the 8 homepage FAQs, and
per-doctor titles + short bios to match the approved copy."""

from django.db import migrations


CATEGORY_SUMMARIES = {
    "regenerative-wellness": "Rebuilds energy, recovery and daily function through natural, body-led healing.",
    "regenerative-medicine": "Repairs worn joints, tendons and nerves using biologic therapies, not surgery.",
    "longevity-healthspan": "Slows age-related decline so you stay active and well for longer.",
    "anti-aging-aesthetics": "Restores a natural, youthful look through regenerative treatments with little downtime.",
    "advanced-diagnostics": "Finds the real cause of your symptoms before any treatment is planned.",
    "emsculpt-for-pain": "Non-invasive muscle stimulation that eases chronic pain and strengthens weak areas.",
}

FAQS = [
    ("Is stem cell therapy legal and regulated in the UAE?",
     "Yes. DHA-licensed physicians carry out regenerative treatments at Brockwell within UAE medical "
     "regulations, and we confirm your suitability by assessment first."),
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
     "cells. Your assessment decides which suits your case."),
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

# slug -> (title, short_bio)
DOCTORS = {
    "dr-hasnain-haider-shah": (
        "Founder & Lead Specialist",
        "DHA-licensed and American Board-trained in neurointerventional surgery and regenerative medicine."),
    "dr-nigel-beejay": (
        "Gastroenterologist (UK & UAE)",
        "20+ years in gastrointestinal care, endoscopy and colon cancer screening."),
    "dr-adeel-khan-md": (
        "Regenerative Medicine & Longevity",
        "Specialist in advanced biologics, stem cell and Muse cell therapy."),
    "dr-sabine-hazan-md": (
        "Gastroenterology & Microbiome",
        "Researcher and clinical-trials leader in gut health and digestive care."),
    "dr-salman-gilani": (
        "Regenerative Medicine",
        "Expert in stem cell therapy and precision diagnostics for proactive care."),
    "shirley-dsouza": (
        "Functional Nutritionist",
        "Focuses on root-cause healing through nutrition, peptides and gut-health support."),
    "shahnawaz-hussein-khan-phd": (
        "Regenerative & Nutritional Science",
        "Builds individualised protocols combining diagnostics, nutrition and regenerative therapy."),
    "dr-nameer-haider": (
        "Pain & Interventional Specialist",
        "25+ years in minimally invasive pain management and neuromodulation."),
    "prof-dato-sri-dr-mike-chan": (
        "Biotechnology & Regenerative Medicine",
        "Four decades in stem cell research and peptide therapeutics."),
    "dr-rozina-badal-munir": (
        "Ultrasound Diagnostics",
        "Leads regenerative-medicine education across 25+ countries, specialising in diagnostic imaging."),
    "dr-summer-beattie": (
        "Photobiomodulation",
        "Naturopathic doctor specialising in laser and light-based regenerative therapies."),
    "rachel-tan-garcia": (
        "Acute Care Nurse Practitioner",
        "ICU-trained in IV infusion and peptide-based recovery protocols."),
    "dr-don-buford": (
        "Orthopedic Surgeon & Regenerative Medicine",
        "26 years using PRP and bone marrow concentrate for joint pain."),
    "jean-francois-tremblay": (
        "Founder, Canlab",
        "Leads diagnostics and lab innovation behind precise, evidence-based treatment."),
}


def load(apps, schema_editor):
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    FAQ = apps.get_model("core", "FAQ")
    Doctor = apps.get_model("team", "Doctor")

    for slug, summary in CATEGORY_SUMMARIES.items():
        ServiceCategory.objects.filter(region="uae", slug=slug).update(summary=summary)

    FAQ.objects.filter(region="uae").delete()
    for i, (q, a) in enumerate(FAQS):
        FAQ.objects.create(region="uae", question=q, answer=a, order=i, is_published=True)

    for slug, (title, bio) in DOCTORS.items():
        Doctor.objects.filter(region="uae", slug=slug).update(title=title, short_bio=bio)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_page_custom_head"),
        ("services", "0012_detox_therapy_content"),
        ("team", "0003_seed_real_doctors"),
    ]

    operations = [migrations.RunPython(load, migrations.RunPython.noop)]
