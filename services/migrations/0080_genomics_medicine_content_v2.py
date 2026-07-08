"""Update the existing Genomics Medicine service with the user's restructured, narrative,
interpretation-first copy. Prose-led with no card grid, timeline or lists, a reworked
section set and a 6-item FAQ. Supersedes the previous content (0045). Images added later."""

from django.db import migrations

SLUG = "genomics-medicine"

SEO_TITLE = "Genomics Medicine in Dubai | Genetic Insight | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Genomics medicine in Dubai at Brockwell Healthcare, using genetic testing to "
    "personalise prevention, medication choices and health planning, with honest "
    "interpretation and proper support."
)
HERO_HEADING = "Genomics medicine in Dubai"
SUMMARY = (
    "Doctor-interpreted genetic testing to personalise prevention, medication choices and "
    "health planning, where the reading matters as much as the test."
)

DESCRIPTION = """
<p>Your genome is the instruction set your body was built from, and reading parts of it can genuinely inform how you look after your health. Genomics medicine uses that information to make care more personal, from which medications suit you to which risks are worth watching. At Brockwell Healthcare our doctors offer genomics medicine in Dubai with one firm principle, which is that a genetic result is only as useful as the interpretation and support around it, so the reading matters as much as the test.</p>

<h2>What is genomics medicine?</h2>
<p>Genomics medicine is the use of information from your DNA to guide prevention, diagnosis and treatment. A test reads specific parts of your genetic code, often looking at common variations called SNPs, single letter differences in the sequence that can subtly influence how your body works. Those readings are then interpreted by a doctor against your health, family history and goals, which is the step that turns raw data into something useful.</p>

<h2>What your DNA can, and cannot, tell you</h2>
<p>This is the most important thing to understand before any test, so we lead with it. For a small number of conditions, a single gene carries a strong, clear effect, such as the well-known BRCA genes linked to certain cancers, and here a result really matters. But most common conditions, heart disease, type two diabetes and the like, are polygenic, meaning they are shaped by many genes each contributing a little, working together with lifestyle and environment. For these, a test gives you a probability, not a verdict. Your genes load the dice, and how you live still rolls them, which is exactly why the result is a starting point for action, not a fixed fate.</p>

<h2>Where genomic testing is genuinely useful</h2>
<p>Set against realistic expectations, a few uses stand out. Pharmacogenomics looks at how your genes affect the way you process medications, since variations in enzymes such as those in the cytochrome P450 family change how quickly some drugs are broken down, which can guide safer, more effective prescribing. Hereditary risk testing matters where a strong family history points to a single high-impact gene worth checking. Nutrigenomics, how your genes interact with diet, offers gentler, more general guidance. Each of these is handled by our doctor with the caveats it deserves, so the insight is used well, not overread.</p>

<h2>How it works in practice</h2>
<p>The process is calmer and more careful than the marketing suggests. It starts with a conversation about why you want testing and what you hope to learn, because the right test depends entirely on the question. A sample, usually blood or saliva, is analysed, and then the part that actually counts happens, which is a doctor sitting down to interpret the result in the context of your history and to translate it into a practical plan. Where a result carries real weight, proper genetic counselling is part of the process, since some findings deserve time and support to understand.</p>

<h2>Who it suits, and a word of caution</h2>
<p>Genomic testing suits people who want to personalise prevention, who are facing a medication decision where processing matters, or who have a family history that warrants a closer look. It rewards curiosity paired with a clear head. The caution is simple. A direct-to-consumer kit that emails you a spreadsheet of risks without interpretation can worry you needlessly or reassure you falsely, and the value of genomics lies almost entirely in the medical interpretation around the data. That interpretation is what we provide, and it is the part worth paying for.</p>
"""

FAQS = [
    ("What is genomic medicine?",
     "Genomic medicine uses information from your DNA to guide prevention, diagnosis and treatment. A test reads parts of your genetic code, and a doctor interprets it against your health and family history to personalise your care, from medication choices to which risks to monitor."),
    ("Do my genes determine my health?",
     "For most common conditions, no. Apart from a few strong single-gene conditions, illnesses like heart disease and diabetes are shaped by many genes together with lifestyle and environment, so a genetic result usually gives a probability you can act on, not a fixed outcome."),
    ("What is pharmacogenomics?",
     "Pharmacogenomics is the study of how your genes affect the way you respond to medications. Variations in drug-processing enzymes can change how quickly a medicine is broken down, which helps a doctor choose safer, more effective prescriptions for you."),
    ("Is genetic testing accurate?",
     "The laboratory reading of well-established variants is generally reliable, but accuracy is not the main issue. The harder part is interpretation, since a raw risk figure means little without a doctor placing it in the context of your whole health."),
    ("Should I just buy a home DNA kit?",
     "A home kit can be interesting, but without medical interpretation it can mislead, either alarming you over a minor risk or falsely reassuring you. The real value of genomics is the clinical reading around the data, which a kit does not provide."),
    ("Is my genetic data kept private?",
     "Genetic information is sensitive, and it is handled with strict confidentiality and proper consent. Our doctor explains how your data is stored and used before any test is done."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc:
        return

    svc.hero_heading = HERO_HEADING
    svc.summary = SUMMARY
    svc.description = DESCRIPTION.strip()
    svc.seo_title = SEO_TITLE
    svc.seo_description = SEO_DESCRIPTION
    svc.benefits = ""
    svc.is_published = True
    svc.save()

    ct, _ = ContentType.objects.get_or_create(app_label="services", model="service")
    FAQItem.objects.filter(content_type=ct, object_id=svc.id).delete()
    for i, (question, answer) in enumerate(FAQS):
        FAQItem.objects.create(
            content_type=ct, object_id=svc.id,
            question=question, answer=answer, order=i, is_published=True,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0079_iv_drips_inline_image"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
