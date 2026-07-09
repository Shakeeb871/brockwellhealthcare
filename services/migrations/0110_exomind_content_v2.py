"""Refresh the Exomind TMS Wellness service with the user's doctor-led, honest-evidence
copy: reworked section set (What is / How Exomind works / What we use Exomind for
[card grid] / How it fits with our other services / What to expect / The treatment
process / Why patients choose) and a 10-item FAQ. Prose-led. The nav name is left
unchanged. Keeps a single inline content image; the hero uses the shared default until
a hero file is supplied.
inline: static/img/services/exomind-tms-wellness-content.webp."""

from django.db import migrations

SLUG = "exomind-tms-wellness"

SEO_TITLE = "Exomind TMS in Dubai | Doctor-Led Brain Stimulation | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led Exomind TMS in Dubai at Brockwell Healthcare, a non-invasive brain "
    "stimulation treatment with its strongest evidence in low mood and depression. Honest, "
    "screened, no downtime."
)
HERO_HEADING = "Exomind TMS in Dubai"
SUMMARY = (
    "A doctor-led, non-invasive brain stimulation treatment (TMS) with its strongest "
    "evidence in low mood and depression. Honest, screened, no downtime."
)

DESCRIPTION = """
<p>Exomind at Brockwell Healthcare is a doctor-led brain stimulation treatment built on transcranial magnetic stimulation, or TMS. Every course starts with a consultation with a qualified doctor, and treatment only goes ahead if the assessment shows you are a suitable candidate.</p>

<h2>What is Exomind at Brockwell Healthcare?</h2>
<p>Exomind is a TMS device made by BTL. It uses focused magnetic pulses to stimulate the dorsolateral prefrontal cortex, the part of the brain involved in mood regulation, decision-making and self-control. TMS itself is not new. It has been used in psychiatry for well over a decade, with its strongest evidence in depression, particularly in patients who did not get enough relief from medication.</p>
<p>What Exomind changes is the experience of getting TMS. A core course runs around six sessions instead of the thirty to forty that older TMS systems needed, each session takes about thirty minutes, and the pulse is designed to feel gentler on the scalp. There are no needles, no anaesthesia and no downtime, and most patients drive themselves home and get on with their day.</p>
<p>We want to be straightforward about one thing. Exomind is marketed around the world for a long list of wellness benefits, from focus to cravings, and the honest position is that the strong clinical evidence sits with depression and low mood. For other uses the evidence is still developing. When you come in, your doctor tells you plainly which category your goal falls into, and what improvement is realistic to expect.</p>

<h2>How Exomind works</h2>
<p>TMS delivers repeated magnetic pulses through a coil resting against your head. The pulses pass painlessly through the skull and stimulate activity in the targeted brain region. In depression, that region is typically underactive, and repeated stimulation over a course of sessions helps restore more normal activity and connectivity. The effect builds across the course instead of arriving in a single session.</p>
<p>During a session you sit in a chair, awake, while the device runs. Most people describe a tapping sensation on the scalp. Some notice mild scalp tenderness or a short-lived headache after the first couple of sessions, and this usually settles as the course continues. You can talk, listen to music or simply rest while it runs.</p>
<p>Not everyone is a candidate. Metal implants in or near the head, cochlear implants, certain cardiac devices and a history of seizures all need careful review, and for some patients TMS is ruled out entirely. This is one of the reasons the doctor's assessment comes before anything else.</p>

<img src="/static/img/services/exomind-tms-wellness-content.webp" alt="Doctor-led Exomind TMS brain stimulation session at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>What we use Exomind for</h2>
<h3>Low mood and depression</h3>
<p>This is where TMS has its strongest track record, especially for people whose symptoms have not responded well to medication, or who do not want to take medication at all. Your doctor assesses the severity and history of your symptoms first. Where the picture points to a condition that needs psychiatric care, we say so and arrange the referral, and Exomind can then run alongside that care, not in place of it.</p>
<h3>Mental wellbeing and stress load</h3>
<p>Some patients come in without a diagnosis. They feel flat, mentally drained or stuck after a long stretch of pressure, and they want a drug-free option to help reset. Exomind can be part of that plan. We are careful with expectations here, because the research on TMS for general wellbeing is younger than the research on depression, and your doctor walks you through what the evidence does and does not show before you commit to a course.</p>
<h3>Focus and mental clarity</h3>
<p>The prefrontal cortex is central to concentration and executive function, and stimulating it is the basis for Exomind's use in this area. As with wellbeing, the evidence is early. If sharper focus is your main goal, the consultation also looks at sleep, stress, hormones and nutrition, because in our experience these are often the bigger levers, and a brain stimulation course cannot compensate for six hours of broken sleep.</p>
<h3>Appetite and cravings</h3>
<p>Self-control circuits sit in the same region Exomind targets, and the device has regulatory approval for binge eating support in some markets outside the US. If cravings or eating patterns are the concern, your doctor assesses the full picture first, including the hormonal and metabolic factors covered in our functional medicine work, and positions Exomind honestly within that plan.</p>

<h2>How Exomind fits with our other services</h2>
<p>Mood, energy and focus problems often have contributors that no brain stimulation device can fix. Low vitamin D, thyroid dysfunction, a disrupted cortisol rhythm and poor sleep all produce symptoms that look like the ones Exomind is marketed for. Because Brockwell Healthcare runs functional medicine and male wellness services under the same roof, your doctor can test for these contributors as part of the same assessment. Some patients end up doing an Exomind course. Others end up correcting a deficiency instead, at a fraction of the cost. The assessment is what decides which one you are.</p>

<h2>What to expect from a course</h2>
<p>Improvement with TMS builds gradually across the course instead of appearing after one session. Many patients start noticing a shift in mood or mental energy partway through, and the effect continues to consolidate after the final session. Some patients benefit from occasional maintenance sessions afterwards, which your doctor plans based on how you responded.</p>
<p>Results vary from person to person, and your doctor tells you before you start what a realistic outcome looks like for your situation. If we do not think Exomind is likely to help you, we will tell you that too.</p>

<h2>The treatment process</h2>
<p>It starts with booking, where you contact Brockwell Healthcare to arrange your Exomind consultation, and the team books you with the doctor first, not straight onto the machine. At the assessment, your doctor reviews your symptoms, goals, medical history and any contraindications, and where blood work would explain part of the picture, it is offered at this stage. If Exomind is suitable, your doctor builds the treatment plan, setting the number of sessions, usually around six for a core course, and confirming the full cost before you start. The sessions themselves take about thirty minutes each, during which you sit comfortably, the coil is positioned and the device runs, and you can return to work straight afterwards. Finally, your response is reviewed during and after the course, with maintenance sessions planned only if they are needed.</p>

<h2>Why patients choose Brockwell Healthcare for Exomind</h2>
<p>TMS in a wellness setting is only as good as the clinical judgement behind it. At Brockwell Healthcare, Exomind sits inside a proper medical practice. A qualified doctor screens every patient, contraindications are taken seriously, and patients whose symptoms need psychiatric care are referred on instead of sold a package. We are honest about where the evidence for Exomind is strong and where it is still emerging, blood work is available when the symptoms suggest another cause, and full pricing is confirmed before your first session.</p>

<h2>Book an Exomind consultation in Dubai</h2>
<p>Book an Exomind consultation in Dubai at Brockwell Healthcare. Your doctor will assess whether you are a suitable candidate, explain honestly what to expect, and confirm the cost before anything begins.</p>
"""

FAQS = [
    ("Does Exomind hurt?",
     "No. You feel a tapping sensation on the scalp while the device runs. Some people get mild scalp tenderness or a brief headache after the first sessions, and this usually fades as the course goes on."),
    ("How many sessions will I need?",
     "A core course is usually around six sessions. Your doctor confirms the number at your assessment and reviews it based on how you respond, and some patients add occasional maintenance sessions later."),
    ("How long does each session take?",
     "About thirty minutes. There is no downtime, so you can go straight back to work or drive home afterwards."),
    ("Is Exomind safe?",
     "TMS has a long safety record when patients are properly screened. That screening matters, which is why every course here starts with a doctor's assessment. Metal implants in or near the head, certain medical devices and a history of seizures can rule the treatment out."),
    ("Is Exomind a replacement for antidepressants or therapy?",
     "Not automatically, and no one here will frame it that way. For some patients it works alongside existing treatment, and for others it is an option when medication has not helped enough. Your doctor reviews your situation and coordinates with your existing care, and nothing you are already taking is stopped without proper clinical review."),
    ("Can Exomind help with focus or productivity?",
     "It targets the brain region involved in concentration and executive function, but the research on TMS for focus in healthy people is still early, and we tell you that upfront. The consultation also checks sleep, stress and relevant blood markers, because those frequently turn out to be the real problem."),
    ("Who should not have Exomind?",
     "People with metal implants in or near the head, cochlear implants, certain pacemakers or other implanted devices, and people with a history of epilepsy or seizures. Your doctor goes through the full screening list at your assessment."),
    ("When will I notice a difference?",
     "Usually partway through the course, not after the first session. The effect builds with repeated sessions and continues to settle in after the course ends."),
    ("What does Exomind cost in Dubai?",
     "It depends on the number of sessions in your plan. You get the full cost at your assessment, before any session is booked, and nothing is added without your agreement."),
    ("Do I need a referral?",
     "No. Contact the clinic directly and the team will book your assessment and tell you what to bring."),
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
        ("services", "0109_emsculpt_neo_inline_image"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
