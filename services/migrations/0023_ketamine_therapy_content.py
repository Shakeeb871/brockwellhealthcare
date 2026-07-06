"""Load the full Ketamine Therapy content: keyword-rich H1, SEO meta, styled
rich-text sections (Types → card grid, process → numbered timeline via the
enhance pipeline), two clinical photos and the FAQ set."""

from django.db import migrations

SEO_TITLE = "Ketamine Therapy in Dubai | Doctor-Led Treatment | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led ketamine therapy in Dubai for treatment-resistant depression, anxiety, "
    "PTSD, trauma and chronic pain. Supervised, assessment-first clinical care."
)
HERO_HEADING = "Ketamine Therapy in Dubai"
SUMMARY = (
    "Doctor-led, medically supervised ketamine therapy for treatment-resistant depression, "
    "anxiety, PTSD, trauma and certain chronic pain."
)

DESCRIPTION = """
<p>Ketamine therapy is a medically supervised treatment for selected patients with treatment-resistant mental health conditions or certain chronic pain concerns. Doctors usually consider it when standard treatments have not brought enough relief and a full assessment confirms it is clinically appropriate.</p>

<h2>What Is Ketamine Therapy?</h2>
<p>Ketamine therapy is a clinically supervised treatment that uses ketamine, a medicine with a long medical history, to help selected patients whose conditions have not responded well to conventional care. At therapeutic doses under medical supervision, it works differently from standard antidepressants and pain medications, which is part of why doctors consider it when other approaches fall short.</p>
<p>At Brockwell Healthcare, we offer ketamine treatment in Dubai for carefully selected patients with treatment-resistant depression, anxiety-related distress, PTSD, trauma symptoms and certain chronic pain conditions. Brockwell treats it strictly as a supervised medical treatment. Every patient goes through a thorough clinical and psychiatric assessment first, and your doctor confirms safety, suitability and realistic expectations before anything begins.</p>

<h2>How Does Ketamine Therapy Work?</h2>
<p>Conventional antidepressants mainly work on serotonin pathways. Ketamine works differently: it acts on the glutamate system, and specifically on the NMDA receptors in the brain. Glutamate is the brain's main excitatory neurotransmitter, and it plays a central role in how neural connections form, adapt and repair.</p>
<p>At therapeutic doses under medical supervision, ketamine may drive a rapid rise in synaptic connections, a process called synaptogenesis, in brain areas tied to mood, emotional processing and pain perception. That may explain why some patients notice quicker changes in mood, thinking and pain than they would with conventional antidepressants, which often take weeks to build effect.</p>
<p>The experience during a session depends on the dose and delivery method, and most patients describe a dissociative state of varying intensity. The clinical team stays with you throughout to monitor safety and comfort. Results are never guaranteed, and individual responses vary widely.</p>

<img src="/static/img/services/ketamine-therapy-content.webp" alt="Doctor supervising a patient during ketamine therapy at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>Types of Ketamine Therapy</h2>
<p>The right delivery method depends on your condition, your clinical assessment and what your doctor judges is safest and most effective for your case.</p>
<h3>IV Ketamine Therapy</h3>
<p>Intravenous ketamine delivers the medicine into the bloodstream through a controlled infusion, which allows precise dosing and real-time adjustment during the session. It is one of the most established routes for ketamine therapy for depression and chronic pain, and sessions usually run from 40 minutes to several hours, depending on the protocol.</p>
<h3>Intramuscular Ketamine</h3>
<p>Here, a doctor delivers ketamine by injection into a muscle rather than into a vein. Its onset is a little slower than IV, though it still reaches therapeutic levels effectively, and it may suit selected cases where IV access is not preferred.</p>
<h3>Oral and Sublingual Ketamine</h3>
<p>These routes have lower bioavailability than IV and appear mainly in selected maintenance or follow-up plans after an initial IV course. They belong only in specific clinical situations, always within a supervised medical plan and never self-administered.</p>

<h2>Benefits of Ketamine Therapy</h2>
<p>For carefully selected patients under proper clinical supervision, ketamine therapy may offer several benefits. Responses vary widely with the condition, the patient's history, the number of sessions and individual biology.</p>
<p>Potential benefits include:</p>
<ul>
<li>Better mood regulation for some patients with treatment-resistant depression</li>
<li>Relatively rapid symptom relief in some cases, where conventional antidepressants have been slow</li>
<li>Eased trauma-related distress and steadier emotional regulation for selected PTSD patients</li>
<li>Help with certain chronic pain where the nervous system keeps generating pain signals</li>
<li>A different brain mechanism to standard antidepressants, which matters when those have not worked</li>
<li>Support for anxiety-related symptoms within a structured medical plan</li>
<li>Continuous monitoring under direct medical supervision throughout each session</li>
<li>A plan built around your specific condition, history and goals</li>
</ul>
<p>Results are never guaranteed. A thorough clinical and psychiatric assessment at Brockwell decides whether ketamine treatment in Dubai is right for you.</p>

<h2>The Ketamine Therapy Process at Brockwell Healthcare</h2>
<p>Every plan follows a structured clinical process, and nothing begins until your doctor has a full picture of your mental health history, physical health, medications and suitability.</p>
<h3>Step 1: Booking</h3>
<p>Contact Brockwell Healthcare to arrange your consultation. The team helps you choose the right appointment and tells you what to bring, including any psychiatric history, past treatment records and current medication lists.</p>
<h3>Step 2: Clinical and Psychiatric Assessment</h3>
<p>Your doctor reviews your full mental health history, physical health, past treatments, current medications, substance history, blood pressure, risk factors and goals. This is a thorough, in-depth assessment that decides whether ketamine treatment in Dubai is appropriate, which delivery method suits you and what the plan looks like. Your doctor screens for contraindications such as psychosis, cardiovascular conditions, substance history and pregnancy, and some patients may need a psychiatric review, medication adjustment or further investigation first.</p>
<h3>Step 3: Treatment Planning</h3>
<p>Your doctor walks you through the delivery method, session length, what the experience typically involves, the safety protocols, monitoring, follow-up schedule and recovery guidance. The full cost is confirmed before anything begins, and you get a clear, honest picture of what the treatment can and cannot do for your situation.</p>
<h3>Step 4: Supervised Treatment Session</h3>
<p>A doctor administers ketamine in a controlled clinical setting under direct supervision. For IV ketamine therapy, the doctor places a small cannula in your arm and runs the infusion at a carefully controlled rate, while the team monitors your blood pressure, heart rate and oxygen continuously. Most patients experience a dissociative state of varying intensity, and the environment stays calm, comfortable and closely supervised throughout.</p>
<h3>Step 5: Recovery and Follow-Up</h3>
<p>After the session, you stay in the clinic until the team confirms you are ready to leave, and you should not drive afterwards. You receive clear written aftercare guidance, and follow-up visits review your mood, pain or function and adjust the plan around your response. Your doctor confirms the number of sessions and the spacing between them based on how you are doing.</p>

<h2>Why Patients Choose Brockwell Healthcare for Ketamine Therapy</h2>
<ul>
<li>Every plan is built on a thorough clinical and psychiatric assessment.</li>
<li>A DHA-certified doctor supervises every session, with continuous vital-sign monitoring.</li>
<li>Your delivery method, dose and session plan are matched to your condition and history.</li>
<li>A full contraindication screen covers cardiovascular health, psychiatric history, medications and substance use before any treatment.</li>
<li>Realistic outcomes are discussed honestly before any ketamine treatment in Dubai begins.</li>
<li>Follow-up reviews track your response and adjust the plan as you go.</li>
<li>Upfront pricing is confirmed before your first session, with no surprises.</li>
</ul>
"""

FAQS = [
    ("Is ketamine therapy legal in Dubai?",
     "Ketamine is a controlled substance that may be used legally in approved medical settings, when a DHA-licensed professional prescribes and administers it. Using it outside a regulated clinical environment is not permitted, so always confirm your doctor's credentials and regulatory standing first."),
    ("What conditions can ketamine treatment support?",
     "Ketamine treatment in Dubai may be considered for treatment-resistant depression, anxiety-related distress, PTSD, trauma symptoms and certain chronic pain conditions, including nerve-related pain and pain that lingers after injury or surgery. Suitability comes down to your diagnosis, history and assessment."),
    ("Is IV ketamine therapy safe?",
     "IV ketamine therapy is considered safe when qualified doctors deliver it with proper screening and continuous vital-sign monitoring. It does not suit every patient, so a full screen covers cardiovascular conditions, psychosis, certain medications and substance history before any treatment."),
    ("Is ketamine therapy painful?",
     "No, the session itself is not painful. With IV delivery, you may feel mild discomfort where the cannula goes in. During the session, most patients experience a dissociative state of varying intensity, with the clinical team present throughout."),
    ("How long does one session take?",
     "IV ketamine therapy sessions usually last from 40 minutes to several hours, depending on the protocol, the condition and the dose. Your doctor confirms the expected duration at your consultation."),
    ("Is there downtime after treatment?",
     "Yes. You should not drive after a session, and most patients need a few hours of rest before returning to normal activity. You stay monitored in the clinic until the team clears you to leave, and a support person to accompany you home is recommended."),
    ("How many sessions will I need?",
     "It depends on the condition, your response and your goals. Some patients complete a short initial course, while others benefit from maintenance sessions over time. Your doctor confirms the plan after assessment and adjusts it around your response."),
    ("When will I notice results?",
     "Some patients notice changes in mood, pain or thinking within hours to days of the first session, while others improve gradually over a course. Responses vary widely, and results are never guaranteed."),
    ("Are the results permanent?",
     "For most patients, no. Ketamine therapy may open a window of meaningful improvement, during which work like psychotherapy or lifestyle change can take better hold. Maintenance sessions may help, depending on your response and goals."),
    ("What should I do before a session?",
     "Follow your clinic's preparation guidance. This usually means fasting for a set period, avoiding alcohol for at least 24 hours, arranging a support person to take you home, and telling your doctor about any changes in your medications or health."),
    ("What should I do afterwards?",
     "Rest, do not drive, avoid alcohol and follow the written aftercare guidance. Attend your follow-ups, and contact Brockwell if you notice anything unexpected in the hours or days after treatment."),
    ("Who should avoid ketamine therapy?",
     "Ketamine therapy does not suit patients with active psychosis, schizophrenia, uncontrolled cardiovascular conditions, a history of ketamine or dissociative misuse, pregnancy, certain thyroid conditions, or medications that interact with ketamine without specialist review. The clinical and psychiatric assessment screens for all of this first."),
    ("Can ketamine therapy be combined with psychotherapy?",
     "Yes. For some patients, research suggests that pairing ketamine treatment with psychotherapy may lead to better, longer-lasting outcomes than ketamine alone. Your doctor may recommend this based on your diagnosis and goals."),
    ("What does ketamine therapy cost in Dubai?",
     "Cost depends on the delivery method, the number of sessions and the clinical protocol. You receive clear pricing and a full estimate before any treatment begins."),
    ("Do I need a consultation first?",
     "Yes. A full clinical and psychiatric assessment comes before any ketamine therapy at Brockwell. It confirms suitability, screens for contraindications, reviews your history and lets your doctor build a safe, personalised plan, so nothing begins without it."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    svc = Service.objects.filter(region="uae", slug="ketamine-therapy").first()
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
        ("services", "0022_longevity_healthspan_content"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
