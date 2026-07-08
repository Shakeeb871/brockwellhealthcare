"""Update the existing Stress Management service with the user's restructured, narrative,
evidence-based copy. Prose-led with no card grid, timeline or lists, a reworked section
set and a 7-item FAQ. Keeps the hero and inline content images. Supersedes the previous
content. Hero: static/img/services/stress-management-hero.webp;
inline: static/img/services/stress-management-content.webp."""

from django.db import migrations

SLUG = "stress-management"

SEO_TITLE = "Stress Management in Dubai | Evidence-Based Support | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Stress management in Dubai at Brockwell Healthcare, a medical, evidence-based approach "
    "to chronic stress and burnout that addresses the biology as well as the habits behind "
    "it."
)
HERO_HEADING = "Stress management in Dubai"
SUMMARY = (
    "A medical, evidence-based approach to chronic stress and burnout that addresses the "
    "biology as well as the habits behind it."
)

DESCRIPTION = """
<p>Stress is a feeling, it is a measurable physical state, and left running for long enough it quietly wears the body down. Managing it well is one of the highest-value things anyone can do for their long-term health, which is why we treat it as medicine and not as an afterthought. At Brockwell Healthcare our approach to stress management in Dubai deals with the biology of stress as much as the habits around it, because lasting change usually needs both.</p>

<h2>What stress management actually means</h2>
<p>Stress management is the set of skills and changes that keep the body's stress response from staying switched on all the time. It is worth being clear that stress itself is not the enemy. A sharp, short burst of it is useful and even healthy, sharpening focus when you need it. The problem is chronic stress, the low, constant hum that never fully switches off, and managing it is about restoring the off switch, not removing stress entirely.</p>

<h2>The biology underneath</h2>
<p>There is real machinery behind the feeling, and knowing it helps. When you perceive a threat, a system called the HPA axis, running from the brain to the adrenal glands, releases cortisol, the main stress hormone, while the sympathetic nervous system triggers the familiar fight-or-flight surge. That response is designed to fire briefly and then switch off through the parasympathetic system, the body's rest-and-recover mode. Under chronic stress, cortisol stays elevated and the system never properly stands down. One useful window on all of this is heart rate variability, the subtle variation in time between heartbeats, which tends to be higher when you are recovered and balanced and lower when you are stuck in a stressed state.</p>

<img src="/static/img/services/stress-management-content.webp" alt="Doctor discussing an evidence-based stress management plan at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>Why chronic stress harms your health</h2>
<p>This is the part that turns stress from a mood into a medical issue. When the stress response never switches off, the constant cortisol and nervous-system activation drive low-grade inflammation, disturb sleep, push up blood pressure, unsettle blood sugar and appetite, and wear on mood and concentration. Over years, that background load is linked with cardiovascular, metabolic and mental health problems, which is why chronic stress is taken seriously in preventive medicine. It is not that stress causes one specific disease, but that it quietly raises the odds across many, which is reason enough to manage it deliberately.</p>

<h2>What genuinely works</h2>
<p>The evidence here is clearer than the wellness industry suggests, and it points to unglamorous things done consistently. The foundations are the ones with the strongest support, meaning regular physical activity, protected sleep, and structured relaxation practices such as mindfulness and slow breathing, which directly engage the parasympathetic recovery system. Cognitive behavioural approaches help by changing the thinking patterns that keep the stress response primed. Where stress has tipped into a clinical problem such as an anxiety disorder, depression or burnout, that deserves proper medical and psychological care, and not lifestyle advice alone, and part of a good assessment is recognising when that line has been crossed. Our role is to build a realistic, personal plan and, where useful, to measure the biology so progress is visible.</p>

<h2>How we approach it, and who it suits</h2>
<p>Stress management suits anyone carrying a sustained load they can feel affecting their sleep, mood, focus or health, and those building a preventive plan for the long term. We start by understanding your specific pressures and, where appropriate, looking at markers that reflect stress and recovery, then build a plan around the foundations that actually move the needle. The aim is not a calmer week but a more resilient nervous system, and that is built gradually, not bought.</p>
"""

FAQS = [
    ("What does chronic stress do to the body?",
     "Chronic stress keeps cortisol and the fight-or-flight system switched on, which drives low-grade inflammation, disturbs sleep, raises blood pressure and unsettles blood sugar and mood. Over time this background load is linked with cardiovascular, metabolic and mental health problems."),
    ("What is cortisol?",
     "Cortisol is the body's main stress hormone, released by the adrenal glands as part of the HPA axis when you face a demand. It is helpful in short bursts, but staying elevated under chronic stress is where the harm comes from."),
    ("How do you manage stress effectively?",
     "Through the foundations with the strongest evidence, namely regular exercise, protected sleep and relaxation practices like mindfulness and slow breathing, supported where needed by cognitive behavioural approaches. Consistency matters more than any single technique."),
    ("What is heart rate variability?",
     "Heart rate variability is the small variation in time between heartbeats. It tends to be higher when you are recovered and balanced and lower under sustained stress, which makes it a useful window on how your nervous system is coping."),
    ("Can stress actually make you ill?",
     "It does not cause one specific disease, but sustained stress raises the risk across cardiovascular, metabolic and mental health conditions by keeping the body in a state it was only meant to enter briefly. That is why managing it is genuine preventive medicine."),
    ("When is stress a medical problem?",
     "When it tips into a clinical condition such as an anxiety disorder, depression or burnout, or when it is seriously affecting your daily life, sleep or health. At that point it deserves proper medical and psychological care, and recognising that line is part of a good assessment."),
    ("Do I need to change everything at once?",
     "No. Lasting change comes from a few realistic, consistent habits built gradually, not a dramatic overhaul. A workable plan around your specific pressures beats an ideal one you cannot keep."),
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
        ("services", "0088_anti_aging_aesthetics_content_v3"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
