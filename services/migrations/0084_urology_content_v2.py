"""Update the existing Urology Services service with the user's restructured, narrative
copy. Prose-led with no card grid, timeline or lists, a reworked section set and a
6-item FAQ. Keeps the hero and inline content images. Supersedes the previous content.
Hero: static/img/services/urology-services-hero.webp;
inline: static/img/services/urology-services-content.webp."""

from django.db import migrations

SLUG = "urology-services"

SEO_TITLE = "Urology in Dubai | Urologist & Men's Health | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Urology in Dubai at Brockwell Healthcare for prostate, bladder, kidney-stone, urinary "
    "and men's health concerns, with discreet assessment and clear, evidence-based "
    "treatment."
)
HERO_HEADING = "Urology in Dubai"
SUMMARY = (
    "Discreet, evidence-based urology for prostate, bladder, kidney-stone, urinary and "
    "men's health concerns, with clear assessment and mostly non-surgical treatment."
)

DESCRIPTION = """
<p>Urology deals with a part of the body most people would rather not discuss, which is exactly why good, discreet urological care matters. It covers the urinary system in everyone and the reproductive system in men, from a nagging bladder to a kidney stone to prostate health. At Brockwell Healthcare our urology service in Dubai is built to make these conversations straightforward, because the symptoms that send people to a urologist are common, treatable, and far easier to deal with when they are not left to worsen in silence.</p>

<h2>What a urologist treats</h2>
<p>A urologist diagnoses and treats conditions of the urinary tract, the kidneys, bladder, ureters and urethra, and of the male reproductive system. The workload spans a wide range, and most of it is common. It includes urinary infections, kidney and bladder stones, an overactive or leaking bladder, prostate problems, blood in the urine, and men's health concerns such as erectile dysfunction and fertility. Some of these are minor irritations and some are early signs of something that needs attention, and telling them apart is the point of a proper assessment.</p>

<h2>The conditions we see most</h2>
<p>A handful of problems make up much of urology, so they are worth naming plainly. Benign prostatic hyperplasia, or BPH, is the non-cancerous enlargement of the prostate that troubles many men as they age, causing a weak stream, urgency and night-time trips to the bathroom. Kidney stones cause some of the sharpest pain in medicine and often need specific treatment. Urinary tract infections are common and usually straightforward but occasionally signal something more. Overactive bladder and urinary incontinence affect quality of life more than people admit and respond well to treatment. And prostate health, including sensible use of the PSA blood test, matters for men from midlife onwards.</p>

<img src="/static/img/services/urology-services-content.webp" alt="Doctor discussing urology and men's health assessment discreetly at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>How urological problems are worked up</h2>
<p>Getting to the right diagnosis is usually quick and undramatic. It starts with a frank history and examination, supported by simple tests such as a urine sample and blood tests, including PSA where prostate assessment is relevant. Imaging often completes the picture, and ultrasound is a workhorse here because it shows the kidneys, bladder and prostate without any radiation. The aim is a clear answer with the least invasive testing that will give it, so treatment can start with confidence.</p>

<h2>How these conditions are treated</h2>
<p>Most urological problems are managed without surgery, which surprises people who arrive braced for the worst. Bladder symptoms and BPH often respond to lifestyle changes, pelvic floor work or medication, and for pelvic floor weakness and certain kinds of incontinence, non-invasive options such as electromagnetic pelvic floor treatment can help before anything more is considered. Stones, infections and prostate concerns each have their own established pathways. Where a procedure is genuinely needed, it is explained clearly, but the starting point is almost always the simplest effective step.</p>

<h2>When to see a urologist</h2>
<p>People too often wait, so this is worth being direct about. It is worth booking an appointment for a persistent change in how you pass urine, for getting up repeatedly at night, for any blood in the urine, for recurring infections, for stone pain, or for men's health concerns such as erectile difficulties or prostate questions from midlife on. Blood in the urine in particular should never be ignored, even once, even if it settles. Most of what a urologist sees turns out to be treatable, and seeing someone early usually makes it more so.</p>
"""

FAQS = [
    ("What does a urologist treat?",
     "A urologist treats conditions of the urinary tract, the kidneys, bladder and urethra, and the male reproductive system. That includes urinary infections, kidney stones, prostate problems, an overactive or leaking bladder, blood in the urine, and men's health issues such as erectile dysfunction."),
    ("When should I see a urologist?",
     "Book an appointment for a lasting change in urination, frequent night-time trips, any blood in the urine, recurring infections, stone pain, or prostate and erectile concerns. Blood in the urine should always be checked, even if it happens only once."),
    ("What is BPH?",
     "Benign prostatic hyperplasia is a non-cancerous enlargement of the prostate that is common with age. It can cause a weak urinary stream, urgency and waking at night to pass urine, and it usually responds well to lifestyle measures or medication."),
    ("Is blood in the urine serious?",
     "It always deserves assessment. It often has a harmless cause, but because it can occasionally be an early sign of something important, it should never be ignored, even if it appears once and then stops."),
    ("What is a PSA test?",
     "PSA is a blood test that measures a protein made by the prostate, used as part of assessing prostate health in men. It is one piece of the picture, interpreted alongside your history and examination, not a standalone answer."),
    ("Are urology problems usually treated with surgery?",
     "No. Most are managed with lifestyle changes, pelvic floor work or medication, and surgery is reserved for the specific cases that need it. The usual starting point is the simplest effective treatment."),
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
        ("services", "0083_ultrasound_diagnostics_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
