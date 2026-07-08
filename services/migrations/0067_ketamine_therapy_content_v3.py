"""Replace the Ketamine Therapy service content with the user's restructured, narrative,
mechanism-and-honesty-focused copy. Prose-led with no card grid, timeline or lists, a
reworked section set and an 8-item FAQ. Keeps the hero and inline content images.
Supersedes 0059. Hero: static/img/services/ketamine-therapy-hero.webp;
inline: static/img/services/ketamine-therapy-content.webp."""

from django.db import migrations

SLUG = "ketamine-therapy"

SEO_TITLE = "Ketamine Therapy in Dubai | Doctor-Supervised | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Ketamine therapy in Dubai at Brockwell Healthcare, a doctor-supervised option for "
    "treatment-resistant depression, anxiety, PTSD and chronic pain, delivered under close "
    "psychiatric care."
)
HERO_HEADING = "Ketamine therapy in Dubai"
SUMMARY = (
    "A doctor-supervised option for treatment-resistant depression, anxiety, PTSD and "
    "chronic pain, delivered under close psychiatric care."
)

DESCRIPTION = """
<p>Ketamine has been used safely in operating theatres for decades as an anaesthetic. What changed more recently is the finding that much smaller doses can help in mental health, particularly where the usual treatments have not worked. It is a controlled medication, so at Brockwell Healthcare it is given only under close medical and psychiatric supervision, as a considered option for people whose depression, anxiety or chronic pain has held on despite standard care. Because it is controlled and acts powerfully on the brain, every step is handled with real clinical rigour.</p>

<h2>What is ketamine therapy?</h2>
<p>Ketamine therapy is the supervised use of low, carefully measured doses of ketamine in psychiatry and pain medicine. The doses are a fraction of those used for surgical anaesthesia, and they are given in a monitored setting, most often for treatment-resistant depression and related conditions that have not responded to standard treatment. There is no take-home version and no casual use. It is provided only after a thorough psychiatric assessment, as one part of a wider mental-health or pain-management plan.</p>

<h2>Why ketamine works differently</h2>
<p>This is the part that makes ketamine genuinely interesting. Most antidepressants work slowly on serotonin over weeks. Ketamine takes a different path entirely. It blocks a receptor in the brain called the NMDA receptor, and that block sets off a surge in glutamate, one of the brain's main signalling chemicals. The glutamate surge activates another receptor, the AMPA receptor, and this is thought to raise a protein called brain-derived neurotrophic factor, or BDNF, and to switch on the mTOR pathway. Between them, these encourage new connections to form between brain cells, a process called synaptogenesis.</p>
<p>Researchers believe this is why some people notice a shift in mood within hours to days, far quicker than a standard antidepressant. It is a genuinely different mechanism, and it is exactly why the treatment belongs in expert hands, because the same properties that make it useful demand careful dosing and close monitoring.</p>

<img src="/static/img/services/ketamine-therapy-content.webp" alt="Clinician monitoring a patient during a supervised ketamine therapy session at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>The forms it takes</h2>
<p>The right form depends on your history, your diagnosis and a specialist assessment. An intravenous infusion is the most established route, with a precisely measured dose given slowly over roughly forty to sixty minutes in a calm, monitored room, and because it can be slowed or paused at any moment it offers fine control. Esketamine, a refined form made from one half of the ketamine molecule and delivered as a nasal spray, is used within specialist protocols for treatment-resistant depression and followed by a period of observation. In selected cases a measured dose is given by intramuscular injection under the same supervision. A specialist always makes the choice and matches it to your situation.</p>

<h2>Who it is considered for, and the strict lines around it</h2>
<p>Ketamine therapy is generally considered for adults with treatment-resistant depression, and it is also explored in anxiety disorders, PTSD, obsessive-compulsive disorder and certain chronic or neuropathic pain. Most people who reach this point have already tried adequate courses of standard treatment without enough relief.</p>
<p>The lines around it are firm, because it does not suit everyone. Our specialists set it aside for people with active psychosis, uncontrolled high blood pressure, certain heart or vascular conditions, a history of substance misuse unless it is being managed, and during pregnancy or breastfeeding. A full psychiatric and medical assessment, sometimes with an ECG and blood work, is what confirms whether it is appropriate and safe.</p>

<h2>What a session actually feels like</h2>
<p>On a treatment day you rest in a calm, low-stimulus room while a clinician gives the measured dose and watches you closely, checking blood pressure, heart rate and comfort throughout. A short period of dissociation, a dream-like sense of detachment, can happen during the session, and it usually settles soon after the dose ends. You then stay for a recovery period of around two hours. Because your judgement and coordination can be affected for the rest of the day, you arrange not to drive and to have someone take you home.</p>

<h2>The honest part: what it can and cannot do</h2>
<p>Ketamine can be real for some people and, at the same time, disappointing for others, and an honest account has to hold both. Within specialist care it is researched for a comparatively rapid effect on treatment-resistant depression, and it is explored in anxiety, PTSD, obsessive-compulsive disorder and stubborn neuropathic pain, usually alongside psychotherapy. But the effect can fade, which is why an initial course and planned, spaced maintenance often matter, and it is never a first-line treatment or a cure. Side effects are possible, and it works best as one element of a broader plan. Our specialists say all of this before anything begins, because a decision this significant should be made with clear eyes.</p>
"""

FAQS = [
    ("Is medical ketamine the same as the recreational drug?",
     "The molecule is the same, but the context could not be more different. Medical ketamine is a precisely measured, low dose given under continuous supervision as part of an assessed plan, whereas recreational use involves uncontrolled doses without oversight and real risk. It is provided here only within strict clinical limits."),
    ("How does it differ from ordinary antidepressants?",
     "Standard antidepressants act slowly on serotonin over weeks, while ketamine blocks the NMDA receptor and triggers a glutamate surge thought to encourage new brain-cell connections through BDNF and the mTOR pathway. That is why some people notice a change within hours to days."),
    ("How long does the benefit last?",
     "For some people it is comparatively brief, which is precisely why an initial course and planned maintenance, alongside wider care, tend to matter. Your specialist sets realistic expectations for your situation."),
    ("What conditions is it used for?",
     "Most often treatment-resistant depression, and also anxiety disorders, PTSD, obsessive-compulsive disorder and certain chronic or neuropathic pain, generally after standard treatments have not helped enough."),
    ("How is it given?",
     "As an intravenous infusion, an esketamine nasal spray, or an intramuscular injection, always under supervision, with the route chosen by a specialist."),
    ("What are the possible side effects?",
     "During a session some people experience dissociation, nausea, a temporary rise in blood pressure, dizziness or headache, which are monitored and usually settle soon afterwards."),
    ("Can it be combined with therapy?",
     "Yes, and it is often most useful that way, with the two coordinated so they support each other within your overall plan."),
    ("Who should not have it?",
     "It is set aside for people with active psychosis, uncontrolled high blood pressure, certain heart conditions, a history of substance misuse unless managed, and during pregnancy or breastfeeding, all of which a full assessment reviews first."),
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
        ("services", "0066_ozone_therapy_content_v4"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
