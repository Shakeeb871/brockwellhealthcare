"""Replace the NAD+ IV Therapy service content with the user's restructured, narrative,
mechanism-and-honesty-focused copy. Prose-led with no card grid, timeline or lists, a
reworked section set and a 6-item FAQ. Supersedes 0060. Images added later."""

from django.db import migrations

SLUG = "nad-iv-therapy"

SEO_TITLE = "NAD+ IV Therapy in Dubai | Doctor-Led Infusion | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "NAD+ IV therapy in Dubai at Brockwell Healthcare for cellular energy, recovery and "
    "healthy-ageing support. Doctor-led, slow-drip infusions built around a proper "
    "assessment."
)
HERO_HEADING = "NAD+ IV therapy in Dubai"
SUMMARY = (
    "Doctor-led, slow-drip NAD+ infusions delivering the coenzyme directly into the "
    "bloodstream to support cellular energy, recovery and healthy ageing, built around a "
    "proper assessment."
)

DESCRIPTION = """
<p>NAD+ is one of the busiest molecules in your body, and there is a fair chance you have less of it than you used to. It stands for nicotinamide adenine dinucleotide, a coenzyme that sits at the centre of how cells turn food into energy and how they carry out repair. Levels fall as we age, and NAD+ IV therapy is one way people try to top them back up. Our doctors at Brockwell Healthcare offer it in Dubai as a slow, supervised infusion, and always after an assessment, because who it suits and how carefully it is run matter more than the drip itself.</p>

<h2>What NAD+ is, and why it runs down with age</h2>
<p>NAD+ is a coenzyme found in every cell, and it does two big jobs. It shuttles electrons through the reactions that produce ATP, the fuel cells run on, and it feeds a set of enzymes that keep cells in good order. Three enzyme families lean on it in particular. The sirtuins, a group of seven proteins often called longevity genes, need NAD+ to work. The PARP enzymes spend it repairing damaged DNA. And CD38, an enzyme tied to inflammation and immune function, consumes it as well.</p>
<p>Here is the problem the whole treatment is built around. NAD+ falls steadily with age, by something like half between your twenties and your forties or fifties, and the decline has three drivers working together. DNA damage keeps the PARP enzymes busy and burning through it, the machinery that makes fresh NAD+ slows down, and CD38 activity climbs, degrading it faster than cells can replace it. Less NAD+ means the sirtuins and PARPs end up competing for a shrinking pool, and cellular housekeeping starts to slip.</p>

<h2>Why deliver it through a drip</h2>
<p>Precursors like NMN and NR, taken as capsules, are the common way to raise NAD+, and they work through the body's own synthesis pathways. An intravenous infusion takes a more direct route, putting NAD+ straight into the bloodstream so it does not depend on gut absorption or conversion. That directness is the appeal. It is also worth saying plainly that the research on IV NAD+ specifically is thinner than the research on oral precursors, and our doctors treat it as a supportive option, not a proven one.</p>

<h2>Why the drip has to be slow</h2>
<p>This is the part most people are not told, and it shapes the whole experience. NAD+ cannot be rushed into a vein. Push it in too quickly and it commonly brings on nausea, flushing, a tight feeling in the chest and a general sense of unease, none of them dangerous but all of them unpleasant. The answer is simply to slow down, which is why a single session often runs anywhere from one to a few hours, with the rate eased up or down to keep you comfortable. A clinician stays with you and adjusts the drip to how you feel, so any of those sensations settle as the pace comes back. If a clinic offers you a quick NAD+ infusion, that is a reason to ask questions, not a convenience.</p>

<h2>What people use it for</h2>
<p>Most of the interest in NAD+ IV therapy is about energy, recovery and healthy ageing, and the honest picture is a mixed one. Because NAD+ underpins mitochondrial energy production, it is explored for persistent fatigue where cellular energy is a genuine factor, and for recovery after illness, heavy training or a long stretch of stress. Its links to sirtuins and DNA repair are why it appears in longevity and healthspan plans as levels decline. The realistic read is that any effect tends to be modest on its own and is reported most often when NAD+ is paired with the things that actually create metabolic demand, such as exercise, better sleep and sensible nutrition. It is a support within a wider plan, and our doctors are straight about that and not promising a transformation.</p>

<h2>Who it suits, and the checks first</h2>
<p>NAD+ IV therapy tends to appeal to people dealing with stubborn fatigue or slower recovery, and to those building a longevity plan as they get older. Since fatigue has many possible causes, a good assessment looks for the ones worth treating directly before reaching for an infusion. It is generally set aside during pregnancy and breastfeeding and where a specific condition makes it unsuitable, and anyone with liver or kidney concerns is reviewed carefully, since those organs handle NAD+ metabolism. The assessment is where all of that is worked through.</p>
"""

FAQS = [
    ("Is an IV drip better than NAD+ capsules?",
     "They are different approaches. Oral precursors like NMN and NR raise NAD+ through the body's own synthesis and have more research behind them, while an infusion delivers NAD+ directly but is less studied in that specific form. Your doctor talks through which makes sense for your goals."),
    ("Why does a NAD+ infusion take so long?",
     "Because giving it quickly tends to cause nausea, flushing and chest tightness. Slowing the drip prevents most of that, so a session commonly runs from one to a few hours with the rate adjusted to your comfort."),
    ("Will it make me feel more energetic straight away?",
     "Sometimes people notice a lift, but honestly the effect is usually modest on its own and clearer when NAD+ sits alongside exercise, good sleep and nutrition. We keep the expectations realistic."),
    ("Is it safe?",
     "Given slowly by trained clinicians, NAD+ infusions are generally well tolerated, with the main sensations tied to infusing too fast. It does not suit everyone, and the assessment screens for that."),
    ("How often would I have it?",
     "That depends on your goal and response. Many people start with a short series of infusions and then space them out, and your doctor sets a plan after the assessment."),
    ("Should I be checked over before an infusion?",
     "It is well worth it. Fatigue and low energy deserve a proper look for a treatable cause before any drip, and the same assessment confirms whether NAD+ therapy suits you."),
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
        ("services", "0068_ozone_therapy_inline_image"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
