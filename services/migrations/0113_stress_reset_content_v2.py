"""Refresh the Stress Reset service with the user's doctor-led, measure-then-repair copy:
reworked section set (What is / How the assessment works / What we address [card grid] /
Treatments within the programme / What to expect / The programme process / Why patients
choose) and a 10-item FAQ. Prose-led.

No inline content image is embedded here yet: the ``stress 1/2`` images had not arrived
when this ran. The hero (``stress-reset-hero.webp``) resolves automatically once supplied,
and the inline content image is added in a follow-up migration when its file is in place."""

from django.db import migrations

SLUG = "stress-reset"

SEO_TITLE = "Stress Reset in Dubai | Doctor-Led Burnout Recovery | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "The doctor-led Stress Reset programme in Dubai at Brockwell Healthcare measures what "
    "chronic stress has done to your body, then repairs it, from cortisol rhythm to sleep "
    "and deficiencies."
)
HERO_HEADING = "Stress Reset in Dubai"
SUMMARY = (
    "A doctor-led programme that measures what chronic stress has done to your body, then "
    "repairs it, from cortisol rhythm to sleep and deficiencies."
)

DESCRIPTION = """
<p>The Stress Reset programme at Brockwell Healthcare is led by a qualified doctor and built for people who have been under sustained pressure for too long. Before any plan is written, you have a consultation and testing, because long-term stress changes measurable things in the body, and the plan depends on which of them it has changed in yours.</p>

<h2>What is the Stress Reset programme at Brockwell Healthcare?</h2>
<p>Most patients who come to us for this are still functioning. They are holding down demanding jobs and managing families, often while replying to work messages at midnight. What brings them in is how it has started to feel. Sleep no longer refreshes them, energy collapses in the afternoon, and their patience has become shorter than it used to be, alongside an odd sense of being tired and overstimulated at the same time.</p>
<p>Stress at this level is a physical state, and it can be measured. Cortisol should be high in the morning and low at night, and after months of pressure that rhythm flattens or inverts. Blood sugar control worsens, which drives the afternoon crashes and the cravings. Sleep becomes lighter, so recovery falls behind, and each day starts with some of the previous day's fatigue still carried over. Deficiencies such as low magnesium and vitamin D are common in this group and make everything harder.</p>
<p>The programme tests these things, then repairs them in order. Therapy or a proper holiday can sit alongside it, but the programme itself is medical work, aimed at restoring the physiology that chronic stress has worn down.</p>

<h2>How the assessment works</h2>
<p>The first appointment goes through your load and your symptoms in detail, covering your work pattern and hours, sleep quality and timing, energy through the day, caffeine and alcohol use, exercise, appetite, mood, and how long things have been this way. We also ask what has changed recently, because a stress problem that started with a specific event is handled differently from one that has been building for five years.</p>
<p>Testing typically covers cortisol rhythm, thyroid function, insulin and glucose markers, inflammatory markers, and nutrient levels including magnesium, vitamin D and B12. Hormone panels are added where the history points to them, since long-term stress suppresses sex hormones in both men and women. When the results are back, your doctor connects them to how you have been feeling. A flattened cortisol curve alongside borderline thyroid results and low magnesium explains a great deal, and it gives the plan a clear starting point.</p>

<h2>What we address</h2>
<h3>Burnout and exhaustion</h3>
<p>Exhaustion that a holiday no longer fixes is the most common presentation. Patients describe coming back from two weeks away and feeling tired again within days. Testing usually finds a physiological reason the rest is not landing, most often a disrupted cortisol rhythm, poor sleep quality, a deficiency or some combination. The plan treats what testing found, and recovery is tracked with repeat testing.</p>
<h3>Sleep that does not restore</h3>
<p>Many stressed patients technically sleep seven hours and still wake up tired. Cortisol that stays elevated at night keeps sleep shallow, and alcohol used to wind down makes the second half of the night worse. We look at the hormonal and metabolic side of sleep alongside the practical side, and where the picture suggests a primary sleep disorder such as sleep apnoea, we refer for a sleep study.</p>
<h3>The physical symptoms of stress</h3>
<p>Tension headaches, jaw clenching, gut symptoms, palpitations, recurring minor illnesses and skin flare-ups are all common in long-term stress, and patients are often relieved to hear these have a shared explanation. The assessment separates what stress is driving from what needs its own investigation, because some symptoms need a proper work-up regardless of how stressed you are.</p>
<h3>Mood, irritability and mental fog</h3>
<p>Long-term stress affects concentration, patience and mood, partly through the hormonal changes above and partly through the sleep debt, and these usually improve as the physiology recovers. Where the picture points to depression, an anxiety disorder or another condition that needs psychiatric or psychological care, your doctor says so directly and arranges the referral, and the physiological work continues alongside that care.</p>
<h3>Stress eating and weight change</h3>
<p>High cortisol drives appetite, particularly for sugar and refined carbohydrates, and it favours fat storage around the middle. Patients often gain weight during their most stressful years and blame themselves for it. Where weight is part of the picture, this programme connects into our nutrition and weight loss work, so both problems are treated with the same set of results.</p>

<h2>Treatments within the programme</h2>
<p>The plan is built from your results, and it usually combines several things. Deficiencies found in testing are corrected, with retesting to confirm the levels have recovered. Sleep is treated as a priority, with specific changes based on what your history and results show. And where hormonal suppression has occurred, your doctor discusses whether support is appropriate and what the options involve.</p>
<p>Some of the clinic's other services have a place here when the assessment supports them. IV nutrient therapy can speed the correction of confirmed deficiencies. Exomind, our TMS-based brain stimulation treatment, is an option for patients whose main complaint is mood and mental flatness, with the honest caveat that the evidence for TMS in general stress and wellbeing is younger than its evidence in depression. Patients who want a structured longer-term plan often continue into the longevity programme once the reset phase is done.</p>

<h2>What to expect</h2>
<p>The early weeks are usually about sleep and energy. Most patients notice their sleep deepening and the afternoon crashes easing before anything else changes, and mood and patience tend to follow. Recovery from a long period of chronic stress takes weeks to months, and your doctor gives you a realistic timeline at the results appointment, based on what the testing found and how long you have been under load.</p>
<p>The programme cannot remove the stress itself. If the job and the schedule stay exactly as they are, the physiology will come under the same pressure again. Your doctor is straightforward about this, and part of the follow-up conversation is what needs to change around you for the recovery to hold.</p>

<h2>The programme process</h2>
<p>It starts with booking, where you contact Brockwell Healthcare to arrange your consultation and the team books you with the doctor first. At the assessment, your doctor takes a detailed history covering your load, sleep, symptoms and timeline, followed by testing selected for your situation. At the results and plan appointment, your doctor goes through every finding with you and builds the plan from the results, covering deficiency correction, sleep, hormonal support where relevant and any supporting treatments, with costs confirmed before anything starts. Then comes the reset phase, the core weeks of the programme with the plan in action and support available when something is not working. Throughout, your progress is reviewed against how you feel and against repeat testing where needed, and the plan is adjusted as your results change.</p>

<h2>Why patients choose Brockwell Healthcare</h2>
<p>Stress programmes in Dubai range from meditation apps to retreat packages, and very few of them measure anything before they start. At Brockwell Healthcare the testing comes first, so the plan is aimed at what has actually happened in your body. A qualified doctor leads the programme, patients who need psychiatric or psychological care are referred on honestly, and supporting treatments are offered only where your results justify them. Full pricing is confirmed before your first session.</p>

<h2>Book a Stress Reset consultation in Dubai</h2>
<p>Book a Stress Reset consultation in Dubai at Brockwell Healthcare. Your doctor will measure what the stress has done, build the recovery plan from your results, and confirm the cost before anything begins.</p>
"""

FAQS = [
    ("How do I know if I need this programme?",
     "The usual signs are waking up tired regardless of how long you slept, crashing in the afternoon, getting ill more often than you used to, and needing caffeine to get through a normal day. If several of those have been true for more than a couple of months, an assessment will tell you what is going on underneath them."),
    ("Is this a mental health treatment?",
     "No, and we are careful about the difference. This programme treats the physical effects of chronic stress, such as a disrupted cortisol rhythm, poor sleep and deficiencies. If your assessment suggests depression, an anxiety disorder or anything else that needs psychiatric or psychological care, your doctor will tell you plainly and arrange the referral, and the two can run together."),
    ("What does the testing involve?",
     "Blood work covering cortisol, thyroid function, blood sugar markers, inflammation and key nutrients, with hormone panels added where your history points to them. Everything is explained before it is ordered."),
    ("How long does the programme take?",
     "It depends on how long you have been under load and what the testing finds. Most patients work with us over a period of weeks to a few months, with the early improvements usually showing in sleep and energy first."),
    ("Can you fix my sleep?",
     "Often, once we know why it is broken. Elevated night-time cortisol, alcohol, blood sugar swings and untreated deficiencies all damage sleep quality in different ways, and the fix depends on which of them your results show. Where a primary sleep disorder is suspected, we refer for a sleep study."),
    ("Will I need medication?",
     "Not necessarily. Many plans are built on deficiency correction, sleep work and targeted lifestyle change. Where medication or hormonal support would help, your doctor explains the reasoning, the alternatives and the risks before anything is prescribed."),
    ("I do not have time for a long programme. Is there any point starting?",
     "Yes. The programme is built around working life in Dubai, appointments are kept efficient, and much of the plan runs inside your normal routine. The clinic visits themselves are a small part of it."),
    ("Can this be combined with therapy or counselling?",
     "Yes, and the combination often works well, since the physical and psychological sides of stress feed each other. We coordinate with your therapist where you have one."),
    ("What does the programme cost?",
     "It depends on the testing and the treatments in your plan. You get a clear cost estimate at your assessment, before anything is booked, and nothing is added without your agreement."),
    ("Do I need a referral?",
     "No. Contact the clinic directly and the team will book your assessment. Bring any recent blood results you have, so you are not paying to repeat tests that were already done."),
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
        ("services", "0112_nutrition_weight_loss_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
