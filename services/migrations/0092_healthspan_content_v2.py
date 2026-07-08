"""Update the existing Healthspan service with the user's restructured, narrative,
explainer-style copy. Prose-led with no card grid, timeline or lists, a reworked section
set and a 5-item FAQ. Keeps the hero and inline content images. Supersedes the previous
content. Hero: static/img/services/healthspan-hero.webp;
inline: static/img/services/healthspan-content.webp."""

from django.db import migrations

SLUG = "healthspan"

SEO_TITLE = "Healthspan vs Lifespan | What the Difference Means | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Healthspan versus lifespan explained: what each term means, why the gap between them "
    "matters more than living longer, and how the healthy years can be extended."
)
HERO_HEADING = "Healthspan and lifespan, and why the difference matters"
SUMMARY = (
    "What healthspan and lifespan each mean, why the gap between them matters more than "
    "living longer, and how the healthy years can be extended."
)

DESCRIPTION = """
<p>Most people, asked what they want, will say a long life. Ask a little more carefully and what they really mean is a long healthy life, and those are not the same thing. The gap between how long you live and how long you stay well is one of the most useful ideas in modern medicine, and it quietly reshapes what good health advice looks like. This is a plain explanation of healthspan and lifespan, the difference between them, and why the second number is the one worth chasing.</p>

<h2>What lifespan means</h2>
<p>Lifespan is the simple one. It is how long you live, the total number of years from birth to death. Medicine spent much of the last century extending it with extraordinary success, through sanitation, vaccines, antibiotics and the treatment of acute disease, and average lifespans across the world rose dramatically as a result. The trouble is that living longer turned out to be only half the goal, because those extra years are not automatically good ones.</p>

<h2>What healthspan means</h2>
<p>Healthspan is the years you spend in good health, active, independent and free of serious chronic disease. It ends not when you die but when illness begins to limit your life in a lasting way. Someone might have a long lifespan and a short healthspan, living into their late eighties but spending their final fifteen years managing several chronic conditions. Someone else might match that lifespan while staying active and well almost to the end. Same number of years lived, very different lives, and the difference is entirely healthspan.</p>

<img src="/static/img/services/healthspan-content.webp" alt="Active, healthy ageing supported by a healthspan-focused plan at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>The gap, and compression of morbidity</h2>
<p>The space between healthspan and lifespan is really a period of decline, the years lived with illness and limitation at the end. Researchers describe the goal of narrowing it as compression of morbidity, which is a clinical way of saying keep people well for as long as possible and compress the period of sickness into as short a window as possible near the very end. A long life with a short, late decline is the target. A long life with a long, slow decline is what modern medicine accidentally became good at producing, and correcting that is much of what preventive and longevity medicine is now trying to do.</p>

<h2>How healthspan is actually extended</h2>
<p>The honest answer is unglamorous, which is why it is worth stating clearly. Healthspan is extended mostly through the fundamentals done consistently and early, regular physical activity that preserves muscle and heart health, good nutrition, protected sleep, managed stress, and the early control of blood pressure, blood sugar and other risks before they become disease. Measuring where you stand, sometimes including an estimate of biological age, how old your body behaves compared with your years, helps make that personal and trackable. There is no shortcut and no single treatment that does it, which is precisely why the everyday choices carry so much weight.</p>
"""

FAQS = [
    ("What is the difference between healthspan and lifespan?",
     "Lifespan is how long you live, while healthspan is how long you stay healthy, active and free of serious chronic disease. The two often differ, since many people spend their final years living with illness, so a long lifespan does not guarantee a long healthspan."),
    ("Why does healthspan matter more than lifespan?",
     "Because the quality of your years matters as much as the quantity. Extending healthspan means more of your life is spent well and independent, which is what most people actually want when they say they hope to live a long time."),
    ("What is compression of morbidity?",
     "It is the goal of keeping people healthy for as long as possible and compressing the period of illness and decline into as short a window as possible near the end of life, so a long life is not paid for with a long, slow decline."),
    ("What is biological age?",
     "Biological age is an estimate of how old your body behaves, based on biomarkers, as opposed to your chronological age in years. It is used as a way to gauge whether your habits and health are ageing you faster or slower than the calendar."),
    ("Can healthspan actually be extended?",
     "Yes, mostly through the fundamentals done consistently, exercise, nutrition, sleep, stress management and early risk control. No single treatment does it, which is why the everyday choices, started early, matter so much."),
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
        ("services", "0091_regenerative_iv_therapy_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
