"""Create the Regenerative IV Therapy sub-service (under Regenerative Wellness)
and load its full content: keyword-rich H1 (full, with tagline), SEO meta, styled
rich-text sections ('May Support' → card grid, process → numbered timeline via
the enhance pipeline) and the FAQ set. Photos are added later."""

from django.db import migrations

SEO_TITLE = "Regenerative IV Therapy in Dubai | Doctor-Led Infusion | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Book regenerative IV therapy in Dubai at Brockwell Healthcare for cellular repair, "
    "recovery, inflammation support and general wellness. Doctor-led IV infusion with "
    "personalised clinical plans."
)
HERO_HEADING = "Regenerative IV Therapy in Dubai | Doctor-Led IV Infusion"
NAME = "Regenerative IV Therapy"
SLUG = "regenerative-iv-therapy"
CATEGORY_SLUG = "regenerative-wellness"
ICON = "💧"
SUMMARY = (
    "Doctor-led regenerative IV therapy in Dubai for cellular repair, recovery, "
    "inflammation support and general wellness."
)

DESCRIPTION = """
<p>Regenerative IV therapy at Brockwell Healthcare delivers targeted combinations of nutrients, antioxidants and regenerative compounds directly into the bloodstream to support cellular repair, ease inflammation and help restore what chronic stress, illness or ageing has gradually depleted. It suits patients who feel their body is not recovering the way it should and want a clinically structured, doctor-led approach to replenishing what has been lost.</p>

<h2>What Is Regenerative IV Therapy?</h2>
<p>Regenerative IV therapy is an intravenous treatment that delivers a combination of fluids, vitamins, minerals, antioxidants and selected regenerative compounds directly into the bloodstream. Because it bypasses the digestive system entirely, nutrients reach the cells faster and at higher concentrations than oral supplementation usually allows, especially when the body is already under strain.</p>
<p>At Brockwell Healthcare, we tailor every regenerative IV treatment in Dubai to you. Your doctor selects the formulation around your symptoms, health history and what your clinical assessment identifies as the underlying concern. Whether the focus is cellular repair, inflammation management, recovery support or general depletion, the plan is built around what your body actually needs.</p>

<h2>How Does Regenerative IV Therapy Work?</h2>
<p>When the body is under sustained stress, recovering from illness or dealing with the gradual effects of ageing, two things tend to happen together. Cellular energy production becomes less efficient, and the body's antioxidant and repair capacity gets stretched. Oral supplementation can help to a degree, but its effect depends on how well the gut absorbs what you take, which is often reduced when the body is already under pressure.</p>
<p>Regenerative IV therapy delivers nutrients and regenerative compounds straight into circulation, available to cells immediately, at a bioavailability oral supplements rarely match. Depending on what the formulation includes, this may support mitochondrial energy production, reduce oxidative stress, support inflammatory regulation or deliver the building blocks the body needs for tissue repair. The combination in your session depends entirely on what your assessment indicates.</p>

<h2>What Regenerative IV Therapy May Support</h2>
<p>Where regenerative IV therapy fits depends on the concern and what your clinical assessment shows. It is not a treatment for every condition, and your doctor confirms formulation suitability before recommending any session.</p>
<h3>Cellular Repair and Recovery</h3>
<p>Where recovery from illness, physical exertion or chronic stress has been slow, a formulation targeting cellular energy and repair pathways may be considered as part of a wider recovery plan.</p>
<h3>Inflammation Support</h3>
<p>Chronic low-grade inflammation can affect energy, recovery and general function. Antioxidant-focused formulations may help manage the inflammatory and oxidative burden where your assessment identifies it as relevant.</p>
<h3>Energy and Fatigue Support</h3>
<p>Where persistent fatigue links to nutrient depletion or reduced cellular energy capacity, targeted IV delivery may be considered alongside a review of the underlying contributing factors.</p>
<h3>Immune and Wellness Support</h3>
<p>During periods of higher immune demand or general depletion, a targeted IV formulation may replenish the body more efficiently than oral intake alone.</p>
<h3>Longevity and Cellular Health</h3>
<p>Within a wider longevity medicine or healthspan plan, selected IV formulations may support cellular function, antioxidant capacity and tissue health over time.</p>

<h2>Benefits of Doctor-Led Regenerative IV Therapy</h2>
<p>Regenerative IV therapy may offer several potential benefits when the right formulation is matched to the right concern through proper clinical assessment. Results depend on the formulation used, the underlying cause and individual response.</p>
<p>Possible benefits include:</p>
<ul>
<li>Better-supported cellular repair when key nutrients are delivered directly</li>
<li>More complete recovery after illness or physical exertion over a course of sessions</li>
<li>Less fatigue where nutrient depletion is contributing to the concern</li>
<li>A lighter inflammatory burden when antioxidant-focused compounds are included</li>
<li>Better general wellbeing as depleted systems are replenished more directly</li>
<li>Nutrients that reach the bloodstream immediately, without relying on digestive absorption</li>
<li>A formulation chosen individually for your concern</li>
</ul>
<p>Results are not guaranteed and vary with the underlying cause and individual response. A clinical assessment at Brockwell Healthcare decides which regenerative IV treatment in Dubai is appropriate for your specific situation.</p>

<h2>The Regenerative IV Therapy Process at Brockwell Healthcare</h2>
<p>Every regenerative IV therapy session at Brockwell Healthcare follows a clear clinical process, and your doctor administers nothing until they understand what your body actually needs.</p>
<h3>Step 1: Booking</h3>
<p>Get in touch with Brockwell Healthcare to arrange your regenerative IV therapy Dubai consultation. The team helps you choose the right appointment for your main concern, whether that is cellular repair, recovery, inflammation support or general wellness.</p>
<h3>Step 2: Consultation and Assessment</h3>
<p>Your doctor reviews your symptoms, medical history, current medications and goals. This step identifies any contraindications and makes sure the formulation reflects what is actually contributing to your symptoms.</p>
<h3>Step 3: Formulation Preparation</h3>
<p>Your clinician prepares the specific formulation in a sterile clinical environment based on your assessment, confirming the ingredients, concentrations and delivery rate before the session begins.</p>
<h3>Step 4: Infusion</h3>
<p>A trained member of the clinical team places a small cannula in a vein, typically in the arm, under sterile conditions. The infusion runs at a controlled rate while you sit comfortably, and most sessions take 30 to 90 minutes, depending on the formulation and volume, while the clinical team monitors your comfort throughout.</p>
<h3>Step 5: Aftercare and Follow-Up</h3>
<p>Once the session finishes, your clinician removes the cannula and gives you any relevant aftercare guidance. Most patients return to normal activity the same day, and your doctor may recommend follow-up sessions depending on your assessment and how your body responds.</p>

<h2>Why Choose Brockwell Healthcare for Regenerative IV Therapy</h2>
<ul>
<li>A DHA-licensed doctor selects every formulation around your specific symptoms and assessment.</li>
<li>A contraindication screen comes before any infusion.</li>
<li>Trained staff deliver every session in a clean, monitored clinical setting using sterile protocols.</li>
<li>Realistic outcomes are discussed honestly before any regenerative IV treatment is recommended.</li>
<li>Follow-up reviews track your progress where ongoing sessions are part of your plan.</li>
<li>Upfront pricing is confirmed before your first session, with no surprises.</li>
</ul>
"""

FAQS = [
    ("What can regenerative IV therapy support?",
     "Cellular repair IV therapy Dubai programmes may support recovery, tissue repair, fatigue related to nutrient depletion and overall cellular function, depending on the formulation selected after assessment. It does not replace addressing the root cause of ongoing symptoms, and suitability depends on your individual assessment."),
    ("How is regenerative IV therapy different from a standard IV drip?",
     "A standard IV drip usually focuses on hydration and basic electrolyte replacement. Regenerative IV therapy uses more targeted formulations built to support cellular repair, antioxidant capacity and recovery at a deeper level. The difference lies in what the formulation contains and why your doctor selected it, which depends on the clinical assessment."),
    ("What ingredients might be included in a regenerative IV formulation?",
     "The specific ingredients depend on your assessment. Common components in regenerative formulations include glutathione, Vitamin C, B vitamins, magnesium, amino acids and other antioxidant or repair-focused compounds. Your doctor explains exactly what your formulation includes, and why, before your session begins."),
    ("What is the difference between IV infusion therapy and regenerative IV therapy?",
     "IV infusion therapy Dubai services can include hydration, vitamin replacement and general wellness drips. Regenerative IV therapy focuses on personalised formulations built to support cellular repair, recovery and overall wellness after a clinical assessment."),
    ("Is regenerative IV therapy safe?",
     "Doctor-led regenerative IV therapy can be safe when trained staff administer it with proper screening and clinical protocols. It does not suit every patient, particularly those with kidney disease, heart failure or known allergies to IV components, so a thorough assessment confirms suitability first."),
    ("Does regenerative IV therapy hurt?",
     "Most patients feel only mild discomfort when the cannula first goes in. The infusion itself is not painful, though some mild sensitivity at the site can occur depending on the formulation and the individual."),
    ("How long does one regenerative IV therapy session take?",
     "Sessions typically take 30 to 90 minutes, depending on the formulation and volume. Your clinician confirms the expected duration during your regenerative IV therapy Dubai consultation."),
    ("How quickly will I notice an effect?",
     "It varies with your health, the formulation and your goals. Some patients notice changes in energy or general wellbeing within hours, while others, especially those on a recovery IV therapy Dubai plan aimed at cellular repair or inflammation over time, experience more gradual change across a course of sessions."),
    ("How often can I have regenerative IV therapy?",
     "Frequency depends on your goals and what your doctor recommends after assessment. Some patients have sessions around specific recovery demands, while others follow a structured plan within a wider wellness or longevity approach."),
    ("Can regenerative IV therapy be combined with other treatments?",
     "Yes. Regenerative IV therapy may be combined with other treatments at Brockwell Healthcare, including red light therapy, PEMF therapy, ozone therapy or other regenerative approaches, depending on your goals. Your doctor advises on the most appropriate combination for your assessment."),
    ("What is the cost of regenerative IV therapy in Dubai?",
     "The cost depends on the specific formulation, volume and number of sessions. Brockwell Healthcare provides clear pricing and a full cost estimate before any session begins."),
    ("Who should avoid regenerative IV therapy?",
     "Patients with kidney disease, heart failure, fluid-balance conditions, known allergies to IV components, bleeding or clotting disorders, or active cancer without specialist clearance should speak to a doctor before considering regenerative IV therapy. All of this is reviewed during the consultation before anything is recommended."),
    ("Do I need a consultation before regenerative IV therapy in Dubai?",
     "Yes. A clinical assessment is required before any regenerative IV therapy in Dubai begins. It makes sure the formulation genuinely addresses what is contributing to your symptoms, so nothing begins without it."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    cat = ServiceCategory.objects.filter(region="uae", slug=CATEGORY_SLUG).first()
    if not cat:
        return

    last = cat.services.filter(parent__isnull=True).order_by("-order").first()
    next_order = (last.order + 1) if last else 0

    svc, _ = Service.objects.update_or_create(
        region="uae", slug=SLUG,
        defaults=dict(
            category=cat,
            parent=None,
            name=NAME,
            hero_heading=HERO_HEADING,
            icon=ICON,
            summary=SUMMARY,
            description=DESCRIPTION.strip(),
            benefits="",
            seo_title=SEO_TITLE,
            seo_description=SEO_DESCRIPTION,
            order=next_order,
            is_published=True,
        ),
    )

    ct, _ = ContentType.objects.get_or_create(app_label="services", model="service")
    FAQItem.objects.filter(content_type=ct, object_id=svc.id).delete()
    for i, (question, answer) in enumerate(FAQS):
        FAQItem.objects.create(
            content_type=ct, object_id=svc.id,
            question=question, answer=answer, order=i, is_published=True,
        )


def remove_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if svc:
        ct, _ = ContentType.objects.get_or_create(app_label="services", model="service")
        FAQItem.objects.filter(content_type=ct, object_id=svc.id).delete()
        svc.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0040_nest_nad_under_longevity_ivs"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, remove_content)]
