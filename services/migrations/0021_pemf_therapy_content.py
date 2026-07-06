"""Load the full PEMF Therapy content: keyword-rich H1, SEO meta, styled
rich-text sections (Types → card grid, process → numbered timeline via the
enhance pipeline) and the FAQ set. Images are added later."""

from django.db import migrations

SEO_TITLE = "PEMF Therapy in Dubai | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led PEMF therapy in Dubai for pain, inflammation, slow recovery, joint "
    "discomfort and cellular health. Non-invasive pulsed electromagnetic field treatment."
)
HERO_HEADING = "PEMF Therapy in Dubai"
SUMMARY = (
    "Non-invasive PEMF therapy using low-frequency electromagnetic pulses to support "
    "cellular function, reduce inflammation and aid recovery."
)

DESCRIPTION = """
<p>PEMF therapy is a non-invasive treatment that uses low-frequency electromagnetic pulses to support cellular function, reduce inflammation and encourage the body's natural recovery. It suits patients who want a gentle, drug-free electromagnetic therapy for recovery, pain relief and general wellness.</p>

<h2>What Is PEMF Therapy?</h2>
<p>PEMF, or pulsed electromagnetic field therapy, sends low-frequency electromagnetic pulses through the body using a medical device. The pulses pass through tissue and interact with your cells, all without any discomfort or damage.</p>
<p>At Brockwell Healthcare, we offer PEMF therapy as part of a personalised recovery and wellness plan. Your doctor may recommend it for pain, inflammation, slow tissue healing, joint discomfort, recovery setbacks or sleep-related concerns. Every plan starts with a clinical assessment to confirm suitability and set realistic expectations.</p>

<h2>How Does PEMF Therapy Work?</h2>
<p>Cells depend on electrical activity to work properly. Injury, inflammation and physical stress can disturb a cell's natural charge, which affects how well it produces energy and repairs itself. PEMF therapy sends low-frequency pulses through the tissue to the cell membrane, which may help restore that natural electrical potential and support normal cellular activity. Think of it as recharging a battery that has slowly run down.</p>
<p>By improving the environment cells work in, PEMF therapy may support natural repair, local circulation and a healthier inflammatory response. Benefits usually build gradually across a course of treatment, not after a single session.</p>

<h2>Types of PEMF Therapy</h2>
<p>PEMF therapy comes in different forms, depending on the area treated and the outcome you are after. After your assessment, your clinician recommends the approach that fits best.</p>
<h3>Whole-Body PEMF Therapy</h3>
<p>A treatment mat delivers electromagnetic pulses across the whole body. Patients often choose it to support recovery, sleep, circulation and overall wellbeing.</p>
<h3>Localised PEMF Therapy</h3>
<p>A dedicated applicator targets one area of the body. It works well for joints, muscles, tendons and soft-tissue injuries that need focused treatment.</p>
<h3>High-Intensity PEMF Therapy</h3>
<p>Higher-intensity settings push the pulses into deeper tissue, which can suit persistent musculoskeletal conditions or chronic pain.</p>
<h3>Low-Intensity PEMF Therapy</h3>
<p>Gentler settings suit more sensitive patients, post-procedure recovery, sleep support and general cellular wellness, often within a detox and wellness plan or alongside other regenerative treatments.</p>

<h2>Benefits of PEMF Therapy</h2>
<p>Used as part of a recovery and wellness plan, PEMF therapy can offer several benefits. How much you notice depends on the concern, the settings and how your body responds.</p>
<p>Reported benefits include:</p>
<ul>
<li>Better support for cellular energy production</li>
<li>Less localised pain and discomfort over a course of sessions</li>
<li>A calmer inflammatory response in treated areas</li>
<li>Improved recovery after injury or physical strain</li>
<li>Easier joint mobility and day-to-day comfort</li>
<li>Better sleep, especially when poor sleep links to pain or recovery strain</li>
<li>Stronger local circulation in the treatment area</li>
<li>Little to no downtime after treatment</li>
</ul>
<p>Results are never guaranteed. A clinical assessment at Brockwell decides whether pulsed electromagnetic field therapy in Dubai fits your condition.</p>

<h2>The PEMF Therapy Process at Brockwell Healthcare</h2>
<p>Every session follows a clear clinical process, and your doctor confirms the device settings, intensity and session plan before anything begins.</p>
<h3>Step 1: Booking</h3>
<p>Contact Brockwell Healthcare to arrange your consultation. The team matches you to the right appointment for your main concern, whether that is joint pain, inflammation, slow recovery, sleep support or general cellular wellness.</p>
<h3>Step 2: Consultation and Assessment</h3>
<p>Your doctor works through your symptoms, medical history, current medications, any implanted devices and wellness goals. This is where they screen for contraindications such as pacemakers, pregnancy, epilepsy and active cancer, then confirm the device type, intensity, treatment area and session frequency for your situation.</p>
<h3>Step 3: Preparation</h3>
<p>You remove any metal jewellery or accessories near the treatment area. For localised treatment, your clinician positions the applicator over the target; for whole-body sessions, you lie on or within the PEMF mat. The session needs no gel, needles or skin preparation, and it stays comfortable from the start.</p>
<h3>Step 4: Treatment</h3>
<p>The PEMF device delivers electromagnetic pulses at the settings set for your plan. Most patients feel little to nothing, though some notice mild warmth or a light tingling. The treatment is non-invasive and comfortable, and it leaves the skin and surrounding tissue untouched.</p>
<h3>Step 5: Aftercare and Follow-Up</h3>
<p>Afterwards, you receive clear aftercare guidance, and there is generally no downtime, so you return to normal activity straight away. Many patients complete a series of sessions within a wider recovery or wellness plan, with progress reviewed along the way.</p>

<h2>Why Patients Choose Brockwell Healthcare for PEMF Therapy</h2>
<ul>
<li>A DHA-certified doctor oversees every treatment plan.</li>
<li>Each protocol is tailored to your needs and treatment goals.</li>
<li>A thorough screening comes before treatment begins.</li>
<li>Medical-grade PEMF technology runs throughout.</li>
<li>Clear guidance sets out the outcomes you can expect.</li>
<li>Follow-up reviews track your progress and adjust the plan where needed.</li>
<li>Transparent pricing means no hidden fees.</li>
</ul>
"""

FAQS = [
    ("What can PEMF treatment support?",
     "PEMF treatment in Dubai may support joint pain, inflammation, slow tissue recovery, muscle soreness, sleep difficulties and general cellular wellness. It does not cure any condition, so a clinical assessment confirms the fit for your situation."),
    ("Can PEMF therapy help joint pain and inflammation?",
     "Yes. PEMF therapy for joint pain and inflammation may ease localised discomfort over a course of sessions, working by supporting cellular repair and circulation in the treatment area."),
    ("Can PEMF therapy support sleep and recovery?",
     "Yes. PEMF therapy for sleep may help patients whose poor sleep links to pain, stress or slow recovery. It does not treat sleep disorders, but it can sit within a wider wellness plan when sleep and recovery are goals."),
    ("Is cellular PEMF therapy safe?",
     "Yes, for most patients, when a qualified clinical team uses appropriate settings. It does not suit patients with pacemakers, cochlear implants, epilepsy, active cancer or pregnancy without clearance, so the consultation screens for these first."),
    ("Is PEMF therapy painful?",
     "No. Most patients feel nothing, or a faint warmth or tingling at higher intensities. There is no pain, no heat strong enough to bother you and nothing invasive to the skin or tissue."),
    ("How long does one session take?",
     "Sessions usually run 20 to 60 minutes, depending on the treatment area, device and protocol. Your clinician confirms the duration at your consultation."),
    ("Is there downtime after treatment?",
     "Usually none. Most patients return to normal activity straight after. Some feel relaxed or slightly tired, which passes within a few hours."),
    ("How many sessions will I need?",
     "Plans vary. Some patients attend a small number of sessions, while others benefit from ongoing treatment. Your doctor advises after the consultation."),
    ("When will I notice results?",
     "Some patients notice better pain or sleep after the first few sessions, while others see gradual change over a full course. The timeline depends on the concern, the intensity and how you respond."),
    ("Are the results permanent?",
     "Not always. PEMF therapy works best as part of an ongoing wellness or recovery plan, and maintenance sessions may help, depending on your condition and goals."),
    ("What should I do before a session?",
     "Remove metal jewellery and accessories near the treatment area, and tell your doctor about any implanted devices, recent health changes or new medications since your last visit. Follow any specific guidance from the team."),
    ("What should I do afterwards?",
     "Most sessions need no specific aftercare. Stay hydrated, rest if you feel relaxed, and follow your clinician's guidance. Contact the clinic if anything feels unexpected."),
    ("Who should avoid PEMF therapy?",
     "Patients with pacemakers, cochlear implants, epilepsy, active cancer without specialist clearance, pregnancy without clearance, or uncontrolled systemic disease should speak to a doctor first. The consultation checks all of this before anything is recommended."),
    ("Can PEMF therapy be combined with other treatments?",
     "Yes. It works well with red light therapy, longevity IVs, detox therapy, stem cell therapy, PRP therapy and other regenerative services at Brockwell. Your doctor advises on the best combination for your goals."),
    ("What does PEMF therapy cost in Dubai?",
     "Cost depends on the device, intensity, treatment area and number of sessions. You receive clear pricing and a full estimate before any session begins."),
    ("Do I need a consultation first?",
     "Yes. A consultation comes before any PEMF treatment in Dubai. It checks suitability, screens for contraindications and lets your doctor build the right plan, so nothing starts without it."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    svc = Service.objects.filter(region="uae", slug="pemf-therapy").first()
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
        ("services", "0020_hydrodissection_injections_content"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
