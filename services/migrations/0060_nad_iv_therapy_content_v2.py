"""Update the existing NAD+ IV Therapy service (nested under Longevity IVs) with the
full refined content: SEO meta, H1, and styled rich-text sections. The 'Types' and
'Client Expectations & Timeline' sections become card grids, 'Your Patient Journey'
becomes a numbered timeline, and the benefit / why-choose lists become icon lists.
Supersedes the previous NAD+ content (0038). Images added later."""

from django.db import migrations

SLUG = "nad-iv-therapy"

SEO_TITLE = "NAD+ IV Therapy in Dubai | Doctor-Led Infusion | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "NAD+ IV therapy in Dubai at Brockwell Healthcare for cellular energy, recovery, "
    "cognitive support and healthy ageing. Doctor-led infusions built around your "
    "assessment."
)
HERO_HEADING = "NAD+ IV Therapy in Dubai"
SUMMARY = (
    "Doctor-led NAD+ infusions delivering the coenzyme straight into the bloodstream to "
    "support cellular energy, recovery, cognitive clarity and healthy ageing."
)

DESCRIPTION = """
<p>Every cell in the body runs on NAD+, a coenzyme at the centre of how energy is made and how repair happens, and those levels quietly fall with age, stress and illness. NAD+ IV therapy at Brockwell Healthcare delivers this coenzyme straight into the bloodstream, as a targeted, doctor-led way to support cellular energy, recovery and healthy ageing. Every plan begins with a proper assessment, because the right candidate and the right pace matter as much as the infusion itself.</p>

<h2>What Is NAD+ IV Therapy?</h2>
<p>NAD+, short for nicotinamide adenine dinucleotide, is a coenzyme present in every cell. It sits at the heart of how cells turn nutrients into usable energy and how they carry out repair, including the upkeep of DNA. Levels decline naturally over the years, and further under sustained stress, illness or poor recovery, which is associated with a drop in cellular performance across several systems.</p>
<p>At Brockwell Healthcare, our NAD+ IV therapy in Dubai delivers the coenzyme intravenously, straight into the bloodstream, so it reaches cells without relying on the uneven absorption of oral precursors through the gut. We offer it within a structured wellness or recovery plan, and only after an assessment confirms it suits your situation.</p>

<h2>How Does NAD+ IV Therapy Work?</h2>
<p>NAD+ sits at the centre of cellular energy metabolism. The mitochondria, the tiny power plants inside each cell, depend on it, and as NAD+ falls, mitochondrial efficiency tends to slip with it, which can show up as fatigue, slower recovery and foggier thinking.</p>
<p>Delivered by infusion, the coenzyme becomes available to cells directly. Inside them, it works as a key electron carrier in the cycle that produces ATP, the body's cellular fuel, and it activates a family of proteins called sirtuins while supporting PARP enzymes, both tied to DNA repair and cellular maintenance. How much of this translates into a felt difference varies from person to person and depends on what is driving the symptoms in the first place. The evidence around NAD+ is still developing, and responses are not guaranteed.</p>

<h2>Types of NAD+ IV Therapy</h2>
<p>The right format depends on your goal, your tolerance and what the assessment shows. Our doctor confirms which suits you.</p>
<h3>Standard NAD+ Infusion</h3>
<p>A full measured dose of NAD+ given as a slow intravenous drip over a longer session, the core format where cellular-energy support is the main aim.</p>
<h3>NAD+ with Co-factors</h3>
<p>NAD+ combined with supporting nutrients such as B-complex vitamins or an antioxidant like glutathione, chosen where the wider picture calls for added support.</p>
<h3>NAD+ Booster Sessions</h3>
<p>Lower-dose top-up infusions used for maintenance once an initial course is complete, spaced to suit your response and goals.</p>

<h2>Benefits of NAD+ IV Therapy</h2>
<p>For selected patients, within a properly assessed plan, NAD+ IV therapy is explored for several potential benefits. Responses differ considerably between individuals and depend on the underlying cause of the symptoms and the number of sessions completed.</p>
<p>Potential benefits it is studied and explored for include:</p>
<ul>
<li>Steadier energy where declining mitochondrial function is driving persistent fatigue</li>
<li>Support for mental clarity where cellular energy is a relevant factor</li>
<li>A role in the body's cellular repair once NAD+ availability improves</li>
<li>Recovery support after illness, exertion or sustained stress</li>
<li>Direct delivery that does not depend on the gut converting oral precursors</li>
<li>A place within a wider longevity or healthspan plan as levels decline with age</li>
</ul>
<p>Outcomes are not guaranteed, and the evidence base is still developing. Our assessment establishes whether NAD+ IV therapy is appropriate for you before anything begins.</p>

<h2>Who Is NAD+ IV Therapy For?</h2>
<p>The people who explore NAD+ IV therapy are often dealing with persistent fatigue, slower-than-expected recovery, brain fog, or a wish to support cellular health as they age, and many come to it after rest and standard measures have not been enough. It suits those who want a targeted, medically supervised approach and realistic expectations.</p>
<p>Fatigue and brain fog have many possible causes, so a proper assessment always comes first, both to look for other explanations and to confirm suitability. NAD+ IV therapy is generally set aside during pregnancy and breastfeeding and where a specific medical condition makes it unsuitable, all of which our doctor reviews beforehand.</p>

<h2>What to Expect from NAD+ IV Therapy in Dubai</h2>
<p>The starting point is a consultation, where our doctor reviews your symptoms, history and goals and looks into what might be driving how you feel. Where NAD+ fits, the plan, the dose and the number of sessions are set out clearly.</p>
<p>On the day, you settle comfortably while a clinician places a standard IV line and begins the infusion. NAD+ is given slowly and deliberately: a drip that runs too quickly can bring on nausea, flushing or a tight-chested feeling, so the pace is eased to keep you comfortable, which is why a session often runs from one to a few hours. Our clinician stays close throughout, adjusting the rate to how you feel.</p>

<h2>NAD+ IV Therapy: Client Expectations &amp; Timeline</h2>
<p>Realistic expectations are part of doing this properly, since responses vary and NAD+ is a support within a wider plan, not a quick fix.</p>
<h3>The Consultation</h3>
<p>Your first appointment looks for the real drivers of your symptoms and sets out whether NAD+ is a sensible fit and what it can reasonably offer.</p>
<h3>The Initial Course</h3>
<p>NAD+ is usually planned as a short series of infusions close together, with your response reviewed as you go.</p>
<h3>Ongoing Review</h3>
<p>Where it helps, spaced booster sessions and lifestyle support are folded into your broader wellness or longevity plan and adjusted over time.</p>

<h2>Tailored NAD+ IV Therapy Programs for Your Lifestyle</h2>
<p>We shape NAD+ care around the life you actually lead. For people running demanding schedules, sessions are arranged with enough calm, unhurried time for the slow infusion, often paired with practical guidance on sleep, stress and recovery that supports the same goals.</p>
<p>For those focused on healthy ageing, NAD+ is planned as one element within a longevity or healthspan programme, coordinated with diagnostics and other support. Whatever your focus, our team explains how each session fits your week and how it works with the rest of your care.</p>

<h2>Why Consider NAD+ IV Therapy?</h2>
<p>The appeal of NAD+ IV therapy is usually its directness: the coenzyme reaches cells straight away, without the uneven gut absorption of oral precursors, which draws people looking to support energy, recovery and cellular health with something targeted and supervised.</p>
<p>The honest counterpoint is just as important. The evidence is still developing, responses vary widely, fatigue has many causes worth investigating first, and NAD+ works best as one part of a broader plan. Our doctors talk this through openly, because a well-informed choice is the only sound one.</p>

<h2>Your Patient Journey</h2>
<h3>Step 1: Consultation &amp; Assessment</h3>
<p>Our doctor reviews your symptoms, history and goals, looks for other drivers of how you feel, and confirms whether NAD+ IV therapy is appropriate for you.</p>
<h3>Step 2: Your Personalised Plan</h3>
<p>We set out the format, dose, number of sessions and realistic expectations, so your decision is fully informed.</p>
<h3>Step 3: The Infusion</h3>
<p>A clinician places a standard IV line and runs the NAD+ drip slowly and comfortably, staying close and adjusting the pace to how you feel.</p>
<h3>Step 4: Review &amp; Maintenance</h3>
<p>We review your response, fold in any booster sessions and lifestyle support, and coordinate it all within your wider plan.</p>

<h2>Why Choose Brockwell Healthcare for NAD+ IV Therapy</h2>
<ul>
<li><strong>Doctor-Led &amp; Assessed.</strong> Experienced doctors plan every course from a proper assessment, looking for the real drivers of your symptoms first.</li>
<li><strong>Paced for Comfort.</strong> We run NAD+ slowly and attentively, adjusting the rate to keep each infusion comfortable.</li>
<li><strong>Considered Formats.</strong> From full infusions to co-factor blends and maintenance boosters, the format is matched to your goal.</li>
<li><strong>Part of a Wider Plan.</strong> We coordinate NAD+ with diagnostics, longevity care and lifestyle support, so it fits a bigger picture.</li>
<li><strong>Honest &amp; Transparent.</strong> We set realistic expectations, are open about the developing evidence, and confirm pricing before anything begins.</li>
</ul>
"""

FAQS = [
    ("Is NAD+ IV better than oral NAD+ supplements?",
     "They work differently. Oral products usually supply precursors that the body must absorb and convert, which can be uneven, whereas an infusion delivers NAD+ directly into the bloodstream. Our doctor explains where each fits and what is realistic for your goals."),
    ("What does NAD+ IV therapy feel like?",
     "Most people simply rest during the drip. Because a fast infusion can cause nausea, flushing or a tight-chested feeling, it is run slowly, and any such sensations usually ease when the pace is reduced. Our clinician adjusts the rate to your comfort throughout."),
    ("How long does a session take?",
     "NAD+ is given slowly, so a session commonly runs from one to a few hours depending on the dose and your tolerance. Our doctor confirms the expected length when your plan is set."),
    ("How many sessions might I need?",
     "It varies with your goal and response. Many people begin with a short series of infusions close together, followed by spaced boosters where helpful. Your doctor recommends a plan after the assessment."),
    ("When might I notice a difference?",
     "Some people notice a shift in energy or clarity within a course of sessions, while for others any change is subtler and gradual. Responses depend heavily on what is driving the symptoms, and our doctor keeps expectations realistic."),
    ("Is NAD+ IV therapy safe?",
     "Given slowly by trained clinicians, NAD+ infusions are generally well tolerated, with the main sensations linked to infusing too quickly. It is not suitable for everyone, and assessment and monitoring exist to manage that."),
    ("Can NAD+ IV be combined with other treatments?",
     "Yes. It is often coordinated with vitamin infusions, longevity care and diagnostics, where clinically appropriate. Our doctor advises on the right combination for your goals."),
    ("Who should avoid NAD+ IV therapy?",
     "It is generally set aside during pregnancy and breastfeeding and where a specific medical condition makes it unsuitable. Our doctor reviews your history and confirms suitability first."),
    ("How much does NAD+ IV therapy cost in Dubai?",
     "The cost depends on the dose, the format and the number of sessions. We explain your pricing clearly before anything begins."),
    ("Do I need a consultation first?",
     "Yes. An assessment comes before any NAD+ infusion, both to look for other causes of your symptoms and to build a plan that genuinely suits you."),
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
    svc.benefits = ""  # benefits are a styled section inside the content above
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
        ("services", "0059_ketamine_therapy_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
