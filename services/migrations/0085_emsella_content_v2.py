"""Update the Emsella service (under Anti-Aging Aesthetics) with the user's restructured,
narrative copy. Prose-led with no card grid, timeline or lists, a reworked section set and
a 7-item FAQ. Keeps the hero and inline content images. Supersedes 0051.
Hero: static/img/services/emsella-hero.webp;
inline: static/img/services/emsella-content.webp."""

from django.db import migrations

SLUG = "emsella"

SEO_TITLE = "Emsella in Dubai | Non-Surgical Pelvic Floor Treatment | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Emsella in Dubai at Brockwell Healthcare, a non-invasive treatment for urinary "
    "incontinence and pelvic floor weakness. You stay fully clothed and seated, with no "
    "downtime."
)
HERO_HEADING = "Emsella in Dubai"
SUMMARY = (
    "A non-invasive, fully-clothed, seated treatment for urinary incontinence and pelvic "
    "floor weakness, with no needles and no downtime."
)

DESCRIPTION = """
<p>Bladder leaks are far more common than anyone lets on, and most people quietly put up with them for years. Emsella is a non-invasive treatment aimed squarely at the muscle weakness behind many of those leaks, and it does its work while you sit, fully clothed, on a chair. At Brockwell Healthcare we offer Emsella in Dubai for pelvic floor weakness and urinary incontinence, and its appeal is simple, since it strengthens muscles that are genuinely hard to train on your own, without surgery and without downtime.</p>

<h2>What is Emsella, and how it works</h2>
<p>Emsella is a chair-shaped device that uses HIFEM technology, which stands for high-intensity focused electromagnetic energy, to make the pelvic floor muscles contract. When you sit on it, the field passes into the pelvic floor and triggers deep, powerful contractions that you could not produce voluntarily. A single twenty-eight minute session induces the equivalent of around eleven thousand pelvic floor contractions, far more than anyone could manage doing Kegel exercises at home. The point is to retrain and strengthen the sling of muscle that supports the bladder, which is exactly the muscle that weakens with age, childbirth and time. Because it is the sheer volume of strong contractions that drives the effect, the machine achieves in half an hour what would take an enormous amount of unaided effort.</p>

<img src="/static/img/services/emsella-content.webp" alt="Patient seated fully clothed on the Emsella pelvic floor chair at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>What it treats</h2>
<p>Emsella is used for urinary incontinence and the pelvic floor weakness underneath it. That includes stress incontinence, the leaks that come with a cough, sneeze, laugh or jump, urge incontinence, the sudden desperate need to go, and the mixed picture that combines both. It is relevant to women after childbirth or around menopause and to men, including after prostate treatment, since a weak pelvic floor is far from only a female problem. Results build over a course and vary between people, and our team is clear about what is realistic for your situation.</p>

<h2>What a session is actually like</h2>
<p>This is the part that puts people at ease. You stay fully clothed and simply sit on the Emsella chair for about twenty-eight minutes, during which you feel a tingling and the odd sensation of your pelvic floor muscles contracting on their own, which is a little strange at first and not painful. There are no needles, no gel, no undressing and no recovery time. Most people read or scroll through their phone during the session and walk straight back into their day afterwards, which is a large part of why it suits busy lives.</p>

<h2>Who it suits, and an honest note</h2>
<p>Emsella suits people bothered by bladder leaks or pelvic floor weakness who would like to avoid surgery and struggle to do effective pelvic floor exercises on their own. It works best as a course, not a single session, and it pairs well with proper pelvic floor physiotherapy. There are honest limits. It is not used during pregnancy or over metal implants in the area, severe cases may need more than Emsella can offer, and a proper assessment comes first to check the cause of the leaks and confirm it is a sensible fit. Our team prefers to set the right expectation instead of overselling a chair.</p>
"""

FAQS = [
    ("What is Emsella?",
     "Emsella is a non-invasive treatment for urinary incontinence and pelvic floor weakness. You sit fully clothed on a chair that uses focused electromagnetic energy to make the pelvic floor muscles contract deeply, strengthening them over a course of sessions."),
    ("How does Emsella work?",
     "It uses HIFEM electromagnetic energy to trigger thousands of strong pelvic floor contractions you could not achieve voluntarily, around eleven thousand in a single twenty-eight minute session, which retrains and strengthens the muscles that support the bladder."),
    ("Does Emsella actually work?",
     "Many people report fewer leaks and better bladder control over a course, and it is genuinely useful for the muscle weakness behind stress and urge incontinence. Results build over sessions and vary, and it works best alongside pelvic floor physiotherapy."),
    ("Is Emsella painful?",
     "No. You feel tingling and the odd sensation of your pelvic floor contracting on its own, which is unusual at first but not painful, and you stay fully clothed and seated throughout."),
    ("How many sessions will I need?",
     "It is delivered as a course, not a one-off, typically several sessions over a few weeks, with the exact number set around your response. Your clinician plans it after the assessment."),
    ("Is there any downtime?",
     "None. You walk straight back into your day, which is one of the main reasons people choose it."),
    ("Can men have Emsella?",
     "Yes. A weak pelvic floor affects men too, including after prostate treatment, and Emsella is used for male urinary incontinence as well as female."),
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
        ("services", "0084_urology_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
