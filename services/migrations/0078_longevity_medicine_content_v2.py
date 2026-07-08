"""Update the existing Longevity Medicine service with the user's restructured, narrative,
healthspan-and-honesty-focused copy. Prose-led with no card grid, timeline or lists, a
reworked section set and a 6-item FAQ. Keeps the hero and inline content images.
Supersedes the previous content. Hero: static/img/services/longevity-medicine-hero.webp;
inline: static/img/services/longevity-medicine-content.webp."""

from django.db import migrations

SLUG = "longevity-medicine"

SEO_TITLE = "Longevity Medicine in Dubai | Healthspan Focus | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Longevity medicine in Dubai at Brockwell Healthcare, a preventive, data-led approach "
    "focused on extending healthspan, the years you stay well, using biomarkers and a "
    "personalised plan."
)
HERO_HEADING = "Longevity medicine in Dubai"
SUMMARY = (
    "A preventive, data-led approach focused on extending healthspan, the years you stay "
    "well, using detailed biomarkers and a personalised plan."
)

DESCRIPTION = """
<p>Longevity medicine is preventive medicine with a sharper focus, aimed less at treating disease once it arrives and more at keeping you well for as long as possible. The goal is not simply a longer life but more good years inside it. At Brockwell Healthcare our longevity service in Dubai is built on measurement and honesty, because this is a young, fast-moving field with real science underneath it and a great deal of hype sitting on top, and telling the two apart is most of the value.</p>

<h2>What is longevity medicine?</h2>
<p>Longevity medicine is a preventive, data-led approach that uses detailed testing to understand how a person is ageing and then acts early to slow the problems before they become disease. It leans on the ordinary, well-proven foundations of health, sleep, nutrition, exercise and metabolic control, and adds careful measurement to make the plan personal. It is medicine aimed at the trajectory you are on, as much as the symptoms you have today.</p>

<h2>Healthspan and lifespan are not the same thing</h2>
<p>This distinction is the heart of the field, and it is worth being precise about. Lifespan is how long you live. Healthspan is how long you stay healthy, active and free of chronic disease, and the two can drift far apart. Many people spend their final decade or more managing illness, which is a long lifespan with a short healthspan. Longevity medicine is aimed squarely at closing that gap, at extending the healthy years instead of simply adding frail ones at the end. When we talk about success here, we mean healthspan.</p>

<h2>The science underneath: the hallmarks of ageing</h2>
<p>Ageing is not one process but many, and researchers have organised them into a set of recognised hallmarks of ageing, first described in a landmark paper and expanded since. They include genomic instability as DNA damage accumulates, the gradual shortening of telomeres that cap our chromosomes, epigenetic changes that alter how genes are read, declining mitochondrial function, the build-up of worn-out senescent cells that will not clear, and a slow rise in chronic, low-grade inflammation. These are the biological targets the field is genuinely interested in. It is honest to say that no treatment has been shown to reverse human ageing, but understanding these mechanisms is what turns longevity from a slogan into science.</p>

<img src="/static/img/services/longevity-medicine-content.webp" alt="Doctor reviewing detailed biomarker and biological-age data as part of a longevity medicine plan at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>How it works in practice</h2>
<p>In the clinic, the work starts with measurement, not a product. Detailed biomarkers, blood panels, metabolic markers and where appropriate measures of biological age, which use patterns such as DNA methylation to estimate how old your body behaves compared with your years, build a picture of where you actually stand. From there our doctor builds a personalised plan around the foundations that have the strongest evidence, refining nutrition, exercise, sleep, metabolic and cardiovascular health, and reviewing it against repeat testing over time. Any newer intervention is weighed on its evidence and framed as exploratory, never sold as a proven fountain of youth.</p>

<h2>Who it suits, and an honest boundary</h2>
<p>Longevity medicine suits people who want to invest in staying well ahead of time, who are comfortable with data, and who understand that the real gains come from doing the fundamentals exceptionally well, not from a miracle. It is not a way to escape ageing, and anyone promising that is not being straight with you. The honest promise is smaller and more valuable, which is a considered, measured effort to add healthy, capable years, grounded in what the evidence actually supports.</p>
"""

FAQS = [
    ("What is longevity medicine?",
     "Longevity medicine is a preventive, data-led approach focused on extending healthspan, the years you stay healthy, and not lifespan alone. It uses detailed testing to understand how you are ageing and acts early, mainly through evidence-based nutrition, exercise, sleep and metabolic health."),
    ("What is the difference between healthspan and lifespan?",
     "Lifespan is how long you live, while healthspan is how long you stay healthy and free of chronic disease. The two often differ, and longevity medicine aims to extend healthspan so more of your years are good ones."),
    ("Can ageing actually be slowed?",
     "The fundamentals, exercise, nutrition, sleep and metabolic control, genuinely influence how well and how long you stay healthy. No treatment has been shown to reverse human ageing, so we focus on what the evidence supports and are honest about what is still experimental."),
    ("What is biological age?",
     "Biological age is an estimate of how old your body behaves, based on biomarkers such as DNA methylation patterns, as opposed to your chronological age in years. It is a useful way to track whether a plan is helping, though the tests are still maturing."),
    ("Is longevity medicine just supplements?",
     "No. Credible longevity medicine is built on measurement and the proven foundations of health, with any supplement or newer intervention judged on its evidence. A clinic leading with a shelf of pills is selling something else."),
    ("How do I start?",
     "It begins with detailed assessment and testing to establish where you stand, followed by a personalised plan reviewed over time. That measurement is what makes the approach specific to you, not generic advice."),
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
        ("services", "0077_iv_drips_content"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
