"""Create the NAD+ IV Therapy sub-service (under Longevity | Healthspan) and load
its full content: keyword-rich H1 (full, with tagline), SEO meta, styled
rich-text sections ('May Support' → card grid, process → numbered timeline via
the enhance pipeline) and the FAQ set. Photos are added later."""

from django.db import migrations

SEO_TITLE = "NAD+ IV Therapy in Dubai | Doctor-Led Infusion | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Book NAD+ IV therapy in Dubai at Brockwell Healthcare for cellular energy, recovery, "
    "cognitive support and healthy ageing. Doctor-led NAD+ infusion with personalised "
    "clinical plans."
)
HERO_HEADING = "NAD+ IV Therapy in Dubai | Doctor-Led NAD+ Infusion"
NAME = "NAD+ IV Therapy"
SLUG = "nad-iv-therapy"
CATEGORY_SLUG = "longevity-healthspan"
ICON = "⚡"  # ⚡ energy
SUMMARY = (
    "Doctor-led NAD+ IV therapy in Dubai for cellular energy, recovery, cognitive support "
    "and healthy ageing."
)

DESCRIPTION = """
<p>NAD+ IV therapy at Brockwell Healthcare delivers nicotinamide adenine dinucleotide directly into the bloodstream to support cellular energy production, recovery and healthy biological ageing. Patients often consider it for persistent fatigue, slow recovery or cognitive decline, when they want a targeted, doctor-led clinical approach to supporting NAD+ levels.</p>

<h2>What Is NAD+ IV Therapy?</h2>
<p>NAD+, or nicotinamide adenine dinucleotide, is a coenzyme found in every cell in the body. It plays a central role in how cells produce energy and how they run repair processes, including DNA maintenance. NAD+ levels decline naturally with age, and further under sustained stress, illness or poor recovery, which is associated with reduced cellular function across multiple systems.</p>
<p>NAD+ infusion therapy delivers this coenzyme straight into the bloodstream intravenously, bypassing the digestive system, where the absorption of oral NAD+ precursors can be inconsistent and limited. At Brockwell Healthcare, we offer NAD+ IV therapy in Dubai as part of a structured wellness or recovery plan, and recommend it only after a proper clinical assessment confirms it is appropriate for your specific situation.</p>

<h2>How Does NAD+ IV Therapy Work?</h2>
<p>NAD+ sits at the centre of cellular energy metabolism. Mitochondria, the structures inside cells that produce energy, depend on it to function properly. When NAD+ levels fall, mitochondrial efficiency tends to decline alongside them, which can contribute to fatigue, slower recovery and reduced cognitive performance.</p>
<p>Delivering NAD+ intravenously puts the coenzyme straight into the bloodstream, available to cells without depending on the digestive conversion of precursors. Inside the cell, NAD+ acts as a central electron carrier in the energy cycle that generates ATP, the body's cellular fuel. It also activates a family of proteins called sirtuins and supports PARP enzymes, both linked to DNA repair, cellular maintenance and healthy ageing. How much this translates into a noticeable clinical benefit varies between individuals and depends on the underlying causes of their symptoms. The evidence base around NAD+ therapy is still developing, and results are not guaranteed.</p>

<h2>What NAD+ IV Therapy May Support</h2>
<p>Where NAD+ IV drip Dubai fits depends on the concern and what your clinical assessment shows. It is not a treatment for every condition, and suitability is confirmed before any session is recommended.</p>
<h3>Cellular Energy and Fatigue</h3>
<p>Where persistent fatigue links to declining cellular energy production, NAD+ therapy for energy may be considered as part of a wider plan to support mitochondrial function. Fatigue has many possible causes, and your doctor assesses these properly before recommending NAD+.</p>
<h3>Cognitive Function and Clarity</h3>
<p>Some patients with brain fog or reduced cognitive performance tied to energy-related factors may find it relevant. It is not a treatment for neurological conditions, and your doctor considers it only where the clinical picture supports it.</p>
<h3>Recovery Support</h3>
<p>Where recovery from illness, physical exertion or stress has been slower than expected and cellular energy is a likely contributor, NAD+ therapy for recovery may be discussed within a broader recovery plan.</p>
<h3>Healthy Ageing and Longevity Support</h3>
<p>As NAD+ levels decline with age, supporting them with NAD+ therapy for healthy ageing is sometimes considered within a wider longevity medicine or healthspan plan at Brockwell Healthcare. Your doctor assesses suitability individually.</p>

<h2>Benefits of Doctor-Led NAD+ IV Therapy</h2>
<p>For selected patients, delivered within a properly assessed clinical plan, NAD+ IV therapy may offer several potential benefits. Results vary considerably between individuals and depend on the underlying cause of symptoms and the number of sessions completed.</p>
<p>Possible benefits include:</p>
<ul>
<li>Better energy where mitochondrial decline is driving persistent fatigue</li>
<li>Support for cognitive clarity where cellular energy is a relevant factor</li>
<li>Improved physical recovery after exertion over a course of sessions</li>
<li>Better-supported cellular repair once NAD+ availability is restored</li>
<li>Better sleep for some patients as cellular function and recovery capacity improve</li>
<li>Direct NAD+ delivery that does not depend on digestive conversion of precursors</li>
</ul>
<p>Results are not guaranteed. The evidence base for NAD+ therapy is still developing, and a clinical assessment at Brockwell Healthcare decides whether it is appropriate for your specific situation.</p>

<h2>The NAD+ IV Therapy Process at Brockwell Healthcare</h2>
<p>Every NAD+ IV therapy session at Brockwell Healthcare follows a clear clinical process, and nothing begins until your doctor understands your symptoms, history and goals.</p>
<h3>Step 1: Booking</h3>
<p>Get in touch with Brockwell Healthcare to arrange your NAD+ therapy Dubai consultation. The team helps you choose the right appointment for your main concern, whether that is energy, cognitive performance, recovery or longevity support.</p>
<h3>Step 2: Consultation and Assessment</h3>
<p>Your doctor reviews your symptoms, medical history, current medications and goals, and may include relevant blood work depending on your case. This step confirms whether NAD+ IV therapy is appropriate and realistic for your situation, and what a sensible session plan looks like.</p>
<h3>Step 3: Preparation</h3>
<p>On arrival, the team runs a brief pre-session check, covering blood pressure and any changes since your last visit. Your clinician then places a small cannula in a vein, typically in the arm, under sterile conditions.</p>
<h3>Step 4: Infusion</h3>
<p>Your clinician administers the NAD+ infusion at a carefully controlled rate. Most patients feel mild warmth or flushing during the session, a common response that usually settles as the infusion continues, and slowing the rate generally manages it. Sessions typically take 60 to 180 minutes, depending on the dose and how well the infusion is tolerated, while the clinical team monitors your comfort throughout.</p>
<h3>Step 5: Aftercare and Follow-Up</h3>
<p>Once the infusion finishes, your clinician removes the cannula and gives you brief aftercare guidance. Most patients return to normal activity the same day, and follow-up appointments review your response and whether further sessions are appropriate.</p>

<h2>Why Choose Brockwell Healthcare for NAD+ IV Therapy</h2>
<ul>
<li>A DHA-licensed doctor prescribes and supervises every NAD+ IV therapy session.</li>
<li>A proper clinical assessment confirms suitability before any session is recommended.</li>
<li>Careful infusion-rate management minimises the flushing and discomfort NAD+ can cause.</li>
<li>Realistic outcomes are discussed honestly, including where the evidence currently stands.</li>
<li>Follow-up reviews track your response and adjust the plan over time.</li>
<li>Upfront pricing is confirmed before your first session, with no surprises.</li>
</ul>
"""

FAQS = [
    ("What can NAD+ therapy support?",
     "NAD+ infusion therapy may support cellular energy, cognitive clarity, physical recovery and healthy-ageing processes, depending on the underlying cause of your symptoms and the clinical assessment. It is not appropriate for every condition, and suitability is confirmed before any session is recommended."),
    ("Is NAD+ therapy for energy the same as taking NAD+ supplements?",
     "No. Oral NAD+ precursors such as NR and NMN pass through the digestive system, and their conversion and absorption can be inconsistent. NAD+ IV therapy delivers the coenzyme straight into the bloodstream, which may allow higher concentrations to reach cells than oral supplementation usually achieves. Whether that produces a meaningful clinical difference depends on the individual and the underlying concern."),
    ("Is NAD+ IV therapy safe?",
     "NAD+ IV therapy is generally well tolerated when a qualified doctor administers it after proper screening and at a carefully managed infusion rate. Not every patient is suitable, and your doctor reviews contraindications, including active cancer, pregnancy and serious cardiovascular or kidney disease, before recommending any session."),
    ("Does doctor-led NAD+ therapy cause side effects?",
     "Mild flushing, warmth, nausea or a tight feeling in the chest can occur during the infusion, particularly if the rate is too fast. Slowing the infusion usually resolves these. Serious adverse effects are uncommon when the session is properly supervised and the rate is managed appropriately."),
    ("How long does one NAD+ IV therapy session take?",
     "Sessions typically take 60 to 180 minutes, depending on the dose and how well the infusion is tolerated. A slower rate is sometimes needed for comfort, which extends the time. Your doctor confirms the expected duration at your consultation."),
    ("Is there downtime after NAD+ therapy for recovery?",
     "Most patients return to normal activity the same day. Some feel tired or relaxed afterwards, which tends to settle within a few hours. No formal recovery period is required."),
    ("How many NAD+ IV therapy sessions are usually needed?",
     "It depends on the concern and your individual response. Some patients complete a short initial course, while others include NAD+ therapy as a regular part of a wider longevity or recovery plan. Your doctor confirms the recommended approach after the assessment."),
    ("When can results from NAD+ therapy be noticed?",
     "Some patients notice changes in energy or clarity within a few days of the first session, while others improve more gradually over a course of treatment. The timeline varies considerably and is not guaranteed."),
    ("Can NAD+ IV therapy be combined with other treatments?",
     "Yes. NAD+ infusion therapy may be combined with other regenerative or wellness treatments at Brockwell Healthcare, depending on your goals. Your doctor advises on the most appropriate combination for your assessment."),
    ("What is the cost of NAD+ IV therapy in Dubai?",
     "The cost depends on the dose, session duration and number of sessions. Brockwell Healthcare provides clear pricing and a full cost estimate before any treatment begins."),
    ("Who should avoid NAD+ therapy for healthy ageing?",
     "Patients with active cancer, pregnancy without clearance, serious kidney or cardiovascular disease, or known sensitivity to NAD+ compounds should speak to a doctor before considering NAD+ IV therapy in Dubai. All of this is reviewed during the consultation before anything is recommended."),
    ("Do I need a consultation before NAD+ IV therapy in Dubai?",
     "Yes. A proper clinical assessment is required before any NAD+ infusion therapy begins. It confirms suitability, identifies any contraindications and lets your doctor build a plan that fits your situation, so nothing begins without it."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    cat = ServiceCategory.objects.filter(region="uae", slug=CATEGORY_SLUG).first()
    if not cat:
        return

    last = cat.services.order_by("-order").first()
    next_order = (last.order + 1) if last else 0

    svc, _ = Service.objects.update_or_create(
        region="uae", slug=SLUG,
        defaults=dict(
            category=cat,
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
        ("services", "0037_longevity_ivs_image"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, remove_content)]
