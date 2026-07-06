"""Load the full Regenerative Wellness category content: SEO meta, keyword-rich
H1, styled rich-text sections (rendered through the site's `.prose` + `enhance`
pipeline so "Types" becomes a card grid and the process becomes a numbered
timeline) and the FAQ set."""

from django.db import migrations

SEO_TITLE = "Regenerative Wellness in Dubai | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led regenerative wellness in Dubai for fatigue, pain, inflammation, slow "
    "recovery and healthy ageing. Personalised, assessment-based treatment plans."
)
HERO_HEADING = "Regenerative Wellness in Dubai"
SUMMARY = (
    "Doctor-led regenerative wellness in Dubai for fatigue, pain, inflammation, slow "
    "recovery and healthy ageing."
)

DESCRIPTION = """
<p>Regenerative wellness is a doctor-led approach to recovery and long-term health that uses targeted therapies to support the body's own repair processes. Patients often choose regenerative wellness in Dubai when they want lasting results and real answers to why the body is not recovering the way it should.</p>

<h2>What Is Regenerative Wellness?</h2>
<p>Regenerative wellness is a structured medical approach that combines proper assessment, targeted treatment and follow-up to help the body work better over time. It takes a holistic view of your health, from energy, pain and inflammation to recovery, skin quality and general wellbeing.</p>
<p>At Brockwell Healthcare, regenerative wellness in Dubai draws on several clinical therapies, from PRP therapy and red light therapy to IV wellness infusions, ozone therapy, stem cell treatment and peptide therapy. Every plan starts with a proper clinical assessment of your symptoms, history and goals, so your care fits you from the very first session.</p>

<h2>How Does Regenerative Wellness Work?</h2>
<p>Your body already runs its own systems for healing, energy production, tissue repair and inflammation control. Age, stress, injury and the demands of daily life wear those systems down, and that is when fatigue, pain, slow recovery and dull skin start to surface.</p>
<p>Depending on your concern, treatment focuses on cellular energy, tissue repair, immune regulation, oxidative stress or hormonal and metabolic support. The aim is simple: give the body better conditions to do the work it is already built to do.</p>

<h2>Types of Regenerative Wellness Treatments</h2>
<p>Regenerative wellness is a framework, not a single treatment. It draws on several clinical therapies, and your doctor selects the right ones based on what your assessment shows.</p>
<h3>PRP Therapy</h3>
<p>Platelet-rich plasma therapy uses a concentrate from your own blood to support tissue repair, joint health, skin quality and hair concerns.</p>
<h3>Red Light Therapy</h3>
<p>Photobiomodulation therapy uses red and near-infrared wavelengths to support cellular energy, skin health, inflammation control and muscle recovery.</p>
<h3>Longevity IVs</h3>
<p>IV wellness infusions, sometimes called a longevity IV drip, deliver targeted nutrients such as NAD+, glutathione and vitamins straight into the bloodstream to support energy, recovery and healthy ageing.</p>
<h3>Ozone Therapy</h3>
<p>Medical ozone therapy uses a controlled oxygen and ozone mix to support circulation, immune regulation, tissue recovery and oxidative stress management.</p>
<h3>Peptide Therapy</h3>
<p>Regenerative peptide therapy uses short chains of amino acids to support tissue repair, hormonal signalling, metabolism, sleep and healthy ageing.</p>
<h3>Stem Cell Therapy</h3>
<p>Regenerative cell treatment may support tissue repair and inflammation control in joints and soft tissue. Your doctor considers it for selected patients where it is clinically appropriate.</p>

<h2>Benefits of Regenerative Wellness</h2>
<p>Delivered as part of a structured clinical plan, regenerative wellness therapy can offer several benefits. How much you notice depends on the concern, the treatments used, the number of sessions and how your body responds.</p>
<p>Reported benefits include:</p>
<ul>
<li>Steadier energy as cellular function gets better support</li>
<li>Less chronic pain and inflammation with targeted regenerative treatment</li>
<li>Better tissue repair after injury, surgery or physical strain</li>
<li>Improved skin quality, texture and cellular health</li>
<li>Greater joint comfort and mobility through regenerative joint therapy</li>
<li>Support for healthy ageing and long-term cellular function</li>
<li>Better sleep and recovery between sessions as repair systems strengthen</li>
<li>Support for metabolic health and body composition</li>
<li>The option to combine several therapies in one comprehensive plan</li>
</ul>
<p>Results are never guaranteed. A clinical assessment at Brockwell decides which options suit your health profile.</p>

<h2>The Regenerative Wellness Process at Brockwell Healthcare</h2>
<p>Every plan follows a structured clinical process, and nothing begins until your doctor has a clear picture of your condition, goals and suitability.</p>
<h3>Step 1: Booking</h3>
<p>Contact Brockwell Healthcare to schedule your consultation. The team matches you to the right appointment for your main concern, whether that is fatigue, pain, slow recovery, skin health, sports recovery or general wellness.</p>
<h3>Step 2: Consultation and Assessment</h3>
<p>Your doctor works through your symptoms, medical history, past treatments, current medications, lifestyle and goals. This is a proper, thorough clinical assessment: it pinpoints what is driving your symptoms, sorts which treatments may help from which to avoid, and takes any imaging, blood tests and past results into account.</p>
<h3>Step 3: Personalised Treatment Plan</h3>
<p>From your assessment, your doctor builds a plan around your specific concern, whether that means one therapy or several combined. You hear exactly what each treatment does, why it was chosen, what a session involves, how many sessions you are likely to need and what realistic outcomes look like. The cost is confirmed before anything begins.</p>
<h3>Step 4: Treatment Sessions</h3>
<p>A DHA-certified doctor or supervised clinical team delivers each session with medical-grade equipment and clean protocols. Whether your plan uses red light therapy, IV wellness infusions, PRP therapy, ozone therapy, peptide therapy or stem cell treatment, every session follows the protocol set during your assessment.</p>
<h3>Step 5: Aftercare and Follow-Up</h3>
<p>After each session, you receive clear aftercare instructions for the treatment delivered. Follow-up visits then review your progress, gauge your response and refine the plan, because regenerative wellness works best when it is monitored and adjusted over time.</p>

<h2>Why Patients Choose Brockwell Healthcare for Regenerative Wellness</h2>
<ul>
<li>A DHA-certified doctor builds and supervises every regenerative wellness plan personally.</li>
<li>A full clinical assessment comes before any treatment recommendation.</li>
<li>Multiple regenerative medicine therapies sit under one clinical framework in Dubai.</li>
<li>Each protocol is shaped around your specific concern and health profile.</li>
<li>A contraindication screen runs before every treatment session.</li>
<li>Clear, realistic outcomes are set out before any doctor-led regenerative care begins.</li>
<li>Upfront pricing is confirmed before your first session, with no surprises.</li>
</ul>

<h2>Book Regenerative Wellness in Dubai</h2>
<p>Book your regenerative wellness consultation at Brockwell Healthcare in Dubai. Your doctor talks through your goals, explains your treatment options, sets clear expectations and confirms the cost before anything starts.</p>
"""

FAQS = [
    ("What can doctor-led regenerative care support?",
     "Doctor-led regenerative care may support persistent fatigue, chronic pain, slow recovery, joint discomfort, skin health, sports injuries, healthy ageing and general cellular wellness. It does not suit every condition, so a clinical assessment confirms suitability first."),
    ("Is regenerative wellness the same as general wellness?",
     "No. Regenerative wellness in Dubai at Brockwell is a medically supervised approach built on a proper clinical assessment and clinically evaluated treatments, rather than lifestyle advice alone."),
    ("Can it help with fatigue and low energy?",
     "Yes. Regenerative wellness therapy may support patients with persistent fatigue through treatments that target cellular energy, nutrient delivery, oxidative stress and recovery."),
    ("Can it support joint pain and inflammation?",
     "Yes. Regenerative joint therapy options such as PRP therapy and stem cell treatment may ease joint discomfort, calm inflammation and improve mobility."),
    ("Is regenerative wellness safe?",
     "Yes, when qualified doctors deliver it with proper screening and clinical protocols. Not every treatment suits every patient, so a thorough assessment confirms which options are safe for your health profile."),
    ("Is it painful?",
     "Most treatments are minimally invasive and well tolerated. Injection-based options like PRP therapy or stem cell treatment may cause mild discomfort at the site, while red light therapy and IV wellness infusions are generally painless."),
    ("How many sessions will I need?",
     "It depends on the treatment, the concern and how your body responds. Some patients need a single procedure, while others follow a structured, multi-session plan."),
    ("When will I notice results?",
     "It varies by treatment. IV wellness infusions may show noticeable effects within hours, while stem cell treatment or PRP therapy build results gradually over weeks to months."),
    ("Can treatments be combined?",
     "Yes. A key strength of doctor-led regenerative care at Brockwell is combining treatments within one framework, so red light therapy, IV wellness infusions, PRP therapy, ozone therapy and others can work together around your goals."),
    ("What does regenerative wellness cost in Dubai?",
     "Cost depends on the treatments chosen, the number of sessions and the clinical protocol. You receive transparent pricing and a full estimate before any treatment begins."),
    ("Who should consider regenerative wellness?",
     "It may suit people with ongoing fatigue, chronic pain, stiffness, slow recovery, inflammation or healthy ageing goals, and anyone who wants a structured plan that combines therapies under medical guidance."),
    ("Who should avoid it?",
     "Regenerative wellness may not suit patients with an active infection, active cancer, pregnancy, breastfeeding, uncontrolled heart or kidney disease, medication risks or conditions needing urgent specialist care. A doctor assesses your case first."),
]


def load_content(apps, schema_editor):
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    cat = ServiceCategory.objects.filter(region="uae", slug="regenerative-wellness").first()
    if not cat:
        return

    cat.hero_heading = HERO_HEADING
    cat.summary = SUMMARY
    cat.description = DESCRIPTION.strip()
    cat.seo_title = SEO_TITLE
    cat.seo_description = SEO_DESCRIPTION
    cat.is_published = True
    cat.save()

    ct, _ = ContentType.objects.get_or_create(
        app_label="services", model="servicecategory"
    )
    FAQItem.objects.filter(content_type=ct, object_id=cat.id).delete()
    for i, (question, answer) in enumerate(FAQS):
        FAQItem.objects.create(
            content_type=ct, object_id=cat.id,
            question=question, answer=answer, order=i, is_published=True,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0018_servicecategory_hero_heading"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
