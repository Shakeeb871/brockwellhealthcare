"""Update the existing Regenerative IV Therapy service with the user's restructured,
narrative, evidence-honest copy. Prose-led with no card grid, timeline or lists, a
reworked section set and a 6-item FAQ. Supersedes the previous content (0041). Images
added later."""

from django.db import migrations

SLUG = "regenerative-iv-therapy"

SEO_TITLE = "Regenerative IV Therapy in Dubai | Longevity Infusions | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Regenerative IV therapy in Dubai at Brockwell Healthcare, doctor-led infusions such as "
    "NAD+, glutathione and high-dose vitamin C aimed at cellular repair, with honest "
    "expectations."
)
HERO_HEADING = "Regenerative IV therapy in Dubai"
SUMMARY = (
    "Doctor-led infusions such as NAD+, glutathione and high-dose vitamin C aimed at "
    "cellular repair, energy and antioxidant defence, with honest expectations."
)

DESCRIPTION = """
<p>A basic vitamin drip is about topping you up. Regenerative IV therapy aims a step deeper, reaching the cellular machinery behind energy, repair and ageing, using specific compounds delivered straight into the bloodstream. It sits at the more serious end of intravenous medicine, and it is where drips overlap with longevity science. At Brockwell Healthcare our doctors offer regenerative IV therapy in Dubai as a supervised, assessment-led service, and a good part of that service is separating the infusions with a real rationale from those that are mostly marketing.</p>

<h2>What makes an IV regenerative, not routine</h2>
<p>The difference lies in what is in the bag and why. A routine drip carries fluid and common vitamins for hydration and general support. A regenerative infusion carries compounds chosen for their role in cellular repair, energy production and defence against oxidative stress. The delivery route is shared, since giving these directly into a vein bypasses the gut and its limited, variable absorption, which matters more for some of these molecules than for everyday vitamins. The intent, though, is different, and so is the honesty required, because the evidence behind these infusions is genuinely mixed.</p>

<h2>What goes into a regenerative infusion</h2>
<p>A few compounds do most of the work, and each has a real mechanism worth knowing. NAD+ is a coenzyme central to how cells make energy and run repair, and it is covered in depth on our dedicated NAD+ page. Glutathione is the body's master antioxidant, a small molecule built from three amino acids that helps neutralise oxidative stress and support the liver's own clearance work. High-dose vitamin C behaves differently by infusion than in a tablet, reaching levels that are being studied for their effects on oxidative balance and immune support. Alpha-lipoic acid is another antioxidant that works in both the watery and fatty parts of cells, and specific amino acid blends are used to support tissue repair. Our doctor selects from these around your goal, and explains the reasoning behind each.</p>

<h2>How it works, and the honest limits</h2>
<p>The shared logic is straightforward. These infusions supply, directly and at useful levels, the raw materials and antioxidants that cells use to produce energy, repair damage and manage oxidative stress. Where someone is genuinely depleted, or where a compound is poorly absorbed by mouth, that direct delivery can matter. The honest limits matter just as much. For a healthy, well-nourished person the added benefit of many of these is modest, the human evidence for the longevity claims is still developing, and no infusion substitutes for sleep, movement and nutrition, which remain the real drivers. We frame these as supportive, not transformative.</p>

<h2>Who it suits, and the safety side</h2>
<p>Regenerative IV therapy suits people recovering from a demanding period, those with genuine deficiencies or poor absorption, and those building a broader longevity plan who understand where the evidence stands. It is generally well tolerated in trained hands, though it is not for everyone. NAD+ must be infused slowly to avoid unpleasant effects, high-dose vitamin C is set aside in G6PD deficiency and certain kidney conditions, and the fluid and mineral load needs care in some heart and kidney problems. A proper assessment, sometimes with blood tests, is what makes the infusion appropriate for you.</p>
"""

FAQS = [
    ("What is regenerative IV therapy?",
     "Regenerative IV therapy delivers compounds aimed at cellular repair, energy and antioxidant defence, such as NAD+, glutathione and high-dose vitamin C, directly into the bloodstream. It targets the machinery behind ageing and recovery, and differs from a routine vitamin drip in its ingredients and intent."),
    ("How is it different from a normal vitamin drip?",
     "A normal drip focuses on hydration and everyday vitamins, while a regenerative infusion uses compounds chosen for their role in cellular repair and oxidative balance. The delivery is similar, but the ingredients, the intent and the evidence involved are different."),
    ("What is glutathione?",
     "Glutathione is the body's main antioxidant, a small molecule made from three amino acids that helps neutralise oxidative stress and supports the liver. It is a common addition to regenerative infusions, often for general antioxidant and skin support."),
    ("Do these infusions actually work?",
     "For correcting real deficiencies or poor absorption, they have a clear rationale. For a well-nourished person, the added benefit of many is modest and the longevity evidence is still developing, so we present them as supportive not a proven anti-ageing fix."),
    ("Are they safe?",
     "In trained hands and after assessment, they are generally well tolerated, with specific cautions such as slow NAD+ infusion and screening for G6PD deficiency before high-dose vitamin C. A brief assessment, sometimes with blood tests, is what keeps them appropriate."),
    ("How often would I have them?",
     "It depends on the goal and your response, often a short series followed by spaced maintenance, and your doctor sets the plan after assessment."),
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
        ("services", "0090_therapeutic_plasma_exchange_content"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
