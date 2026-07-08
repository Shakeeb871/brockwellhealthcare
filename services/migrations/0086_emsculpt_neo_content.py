"""Load the full Emsculpt NEO service content (under Anti-Aging Aesthetics), replacing
the placeholder. Narrative copy covering muscle strengthening, body contouring and the
functional core / back-pain angle, with a 5-item FAQ. Prose-led, no card grid, timeline
or lists. Images added later."""

from django.db import migrations

SLUG = "emsculpt-neo"

SEO_TITLE = "Emsculpt in Dubai | Muscle & Core Strengthening | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Emsculpt in Dubai at Brockwell Healthcare for non-invasive muscle strengthening and "
    "core stability, including support for back pain, using focused electromagnetic muscle "
    "training."
)
HERO_HEADING = "Emsculpt in Dubai"
SUMMARY = (
    "Non-invasive focused electromagnetic muscle training for muscle strengthening, "
    "definition and core stability, including support for back-pain management."
)

DESCRIPTION = """
<p>Emsculpt trains muscle in a way you cannot train it yourself, by forcing far more powerful contractions than your own nervous system will allow. Most people meet it as a body-contouring treatment, and it is one, but the more interesting use for us is the muscle strengthening and core stability that sits underneath. At Brockwell Healthcare we offer Emsculpt in Dubai with that functional angle in mind, since a stronger, better-activated core is more than an aesthetic goal, and a genuine part of managing certain kinds of pain.</p>

<h2>What is Emsculpt?</h2>
<p>Emsculpt is a non-invasive treatment that uses focused electromagnetic energy to make a muscle contract intensely, without any effort from you. You lie down while an applicator is strapped over the target area, usually the abdomen or buttocks, and the muscle underneath does the work. Nothing enters the body, there are no needles, and you stay clothed and still throughout.</p>

<h2>How the contractions work</h2>
<p>The mechanism has a proper name, HIFEM, meaning high-intensity focused electromagnetic energy, and the key idea is the supramaximal contraction. Normally your brain will only recruit a fraction of a muscle at once, holding some back as a safety margin. HIFEM bypasses that limit and contracts the muscle far more completely and far more often than voluntary effort can. A single thirty-minute session drives roughly twenty thousand of these powerful contractions, a volume no workout could match, and the muscle responds to that unusual demand by adapting and strengthening, much as it would to very heavy training.</p>

<h2>What it does to muscle and fat</h2>
<p>The best-known effect is on the body. By repeatedly driving muscle to that extreme, Emsculpt is studied for building muscle definition in the treated area, and some versions also reduce fat over the muscle at the same time, which is why it is popular for the abdomen and buttocks. It is worth being clear that this is muscle work, so it defines and strengthens what is there, and it is not a weight-loss treatment or a substitute for general fitness. Results build over a course and vary with the person and their starting point.</p>

<h2>The part that matters most to us: core and pain</h2>
<p>Away from aesthetics, the same technology has a functional use that interests our doctors more. A weak or poorly activated core is a common thread in persistent lower back pain, and rebuilding the deep abdominal muscles is a well-established part of managing it. Emsculpt can support that work by strengthening and, in effect, re-teaching those muscles to fire, which can complement a proper rehabilitation programme. It is not a cure for back pain and it does not replace physiotherapy, but as one tool inside a wider plan aimed at core stability, it has a genuine place.</p>

<h2>What a session is like</h2>
<p>A session is undemanding, which is the appeal. You lie down for around thirty minutes while the applicator delivers the contractions, and the sensation is a strong, rhythmic pulling and tensing of the muscle that builds through the session and feels distinctly odd the first time. It is not painful, there is no downtime, and afterwards the treated muscle can feel as though it has had a hard workout, sometimes with mild soreness the next day, which is exactly what you would expect.</p>

<h2>Who it suits</h2>
<p>Emsculpt suits people who want to strengthen and define a specific muscle group, and those working on core stability as part of managing back pain alongside proper rehabilitation. It works best as a course and alongside exercise, never a replacement for it. It is set aside over metal implants in the treated area, in pregnancy, and near certain electronic implants, and a brief assessment confirms it is suitable and sets the right expectation before you start.</p>
"""

FAQS = [
    ("What is Emsculpt?",
     "Emsculpt is a non-invasive treatment that uses focused electromagnetic energy to make a muscle contract far more intensely than voluntary effort allows, strengthening and defining it. It is used for body contouring and, functionally, for core strengthening."),
    ("Is Emsculpt a weight-loss treatment?",
     "No. It works on muscle, strengthening and defining the treated area, and while some versions also reduce overlying fat, it is not a weight-loss treatment or a substitute for general fitness and a healthy diet."),
    ("Can Emsculpt help with back pain?",
     "It can support the core-strengthening side of back-pain management, because a stronger, better-activated deep abdominal wall helps stabilise the spine. It is not a cure and does not replace physiotherapy, but it can complement a proper rehabilitation plan."),
    ("Is Emsculpt painful?",
     "No. You feel strong, rhythmic muscle contractions that feel unusual at first but not painful, and afterwards the muscle may feel worked, sometimes with mild soreness the next day."),
    ("How many sessions will I need?",
     "It is delivered as a course, not a single session, usually several over a couple of weeks, with maintenance after. Your clinician sets the plan around your goal and starting point."),
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
        ("services", "0085_emsella_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
