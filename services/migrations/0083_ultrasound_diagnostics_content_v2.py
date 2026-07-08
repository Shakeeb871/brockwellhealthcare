"""Update the existing Ultrasound Diagnostics service with the user's restructured,
narrative copy. Prose-led with no card grid, timeline or lists, a reworked section set
and a 5-item FAQ. Keeps the hero and inline content images. Supersedes the previous
content. Hero: static/img/services/ultrasound-diagnostics-hero.webp;
inline: static/img/services/ultrasound-diagnostics-content.webp."""

from django.db import migrations

SLUG = "ultrasound-diagnostics"

SEO_TITLE = "Ultrasound Diagnostics in Dubai | Real-Time Imaging | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Diagnostic ultrasound in Dubai at Brockwell Healthcare for tendons, muscles, joints "
    "and soft tissue. Safe, radiation-free, real-time imaging that shows the body actually "
    "moving."
)
HERO_HEADING = "Ultrasound diagnostics in Dubai"
SUMMARY = (
    "Safe, radiation-free, real-time diagnostic ultrasound for tendons, muscles, joints "
    "and soft tissue, and for guiding treatment precisely."
)

DESCRIPTION = """
<p>Ultrasound is the quiet workhorse of medical imaging, and for soft tissue it often beats the more expensive machines. It builds a live picture of the inside of the body using nothing but sound, with no radiation and no discomfort. At Brockwell Healthcare our doctors use diagnostic ultrasound in Dubai to examine tendons, muscles, joints and blood vessels, and to guide treatments precisely, and one of its quiet advantages is that it lets us watch tissue while it moves, which a still image can never do.</p>

<h2>What is diagnostic ultrasound?</h2>
<p>Diagnostic ultrasound is an imaging method that uses high-frequency sound waves to create real-time pictures of structures inside the body. A small handheld probe, called a transducer, is placed on the skin with a little gel, and the image appears immediately on a screen. It is painless, it involves nothing entering the body, and a scan can be done and interpreted in the same visit.</p>

<h2>How it works</h2>
<p>The physics is refreshingly simple. The transducer sends pulses of sound into the body, far too high-pitched to hear, and then listens for the echoes that bounce back off different tissues. Dense structures and fluid reflect sound differently, so the machine turns the returning echoes into a detailed grey-scale picture, rebuilt many times a second to produce live motion. A mode called Doppler goes a step further and measures movement, which lets it show blood flowing through a vessel and reveal a blockage or a leak. Sound in, echoes out, a moving picture built from the difference.</p>

<img src="/static/img/services/ultrasound-diagnostics-content.webp" alt="Doctor performing a real-time diagnostic ultrasound scan at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>Two things that make ultrasound special</h2>
<p>Most of its value comes down to two qualities the other scanners lack. The first is that it works in real time, so instead of a frozen snapshot the doctor sees the tissue actually working, watching a tendon glide as you bend a finger or a muscle contract as you tense. That dynamic view often reveals a problem that a static image would miss entirely. The second is that it uses no ionising radiation at all, unlike X-rays and CT scans, which makes it safe to repeat as often as needed and safe in situations where radiation is a concern. Live movement and complete safety, together, are why it is so useful for soft tissue.</p>

<h2>What it is used for</h2>
<p>Ultrasound is versatile, and its strengths sit in a few areas. In musculoskeletal work it is excellent for tendons, muscles, ligaments and joints, which is why it is central to sports injury assessment and to guiding injections exactly where they need to go. It examines abdominal organs such as the liver, gallbladder and kidneys. With Doppler it assesses blood vessels and circulation. And because it is portable and immediate, it can be used at the point of care to answer a question on the spot instead of sending you away for a scan another day.</p>

<h2>Guiding treatment in real time</h2>
<p>One use deserves its own mention, because it changes outcomes. Ultrasound does more than find problems, because it also guides the needle when a problem is treated. When our doctors place an injection into a joint, free a trapped nerve during hydrodissection, or target a specific point in a tendon, ultrasound shows the needle and the target together on screen throughout. That live guidance is the difference between reaching the exact structure and working blind, which is why it runs through so much of our regenerative and sports work.</p>

<h2>What to expect during a scan</h2>
<p>A scan is straightforward and comfortable. You rest while the doctor applies a water-based gel to the area, which helps the sound travel, and moves the probe over the skin, sometimes asking you to move the part being examined so the tissue can be seen in action. It takes a matter of minutes for most areas, there is no preparation for many scans, and because the doctor is watching live, you often get an answer there and then, not after waiting for a report.</p>
"""

FAQS = [
    ("What is diagnostic ultrasound?",
     "Diagnostic ultrasound uses high-frequency sound waves to create live, moving images of structures inside the body, such as tendons, muscles, joints, organs and blood vessels. A probe on the skin sends sound in and builds a picture from the echoes, with no radiation and no discomfort."),
    ("Does ultrasound use radiation?",
     "No. Ultrasound uses sound waves, not ionising radiation, which is why it is considered very safe and can be repeated as often as needed, unlike X-rays or CT scans which do carry radiation."),
    ("When is ultrasound better than an MRI?",
     "Ultrasound is excellent for soft tissue near the surface and has the advantage of showing tissue moving in real time, which suits tendon and muscle problems and guiding injections. An MRI is better for deeper structures and complex joint interiors, so the two are complementary."),
    ("Is ultrasound safe?",
     "Yes. Because it uses sound and no radiation, and nothing enters the body, diagnostic ultrasound has an excellent safety record and is used widely, including in situations where radiation must be avoided."),
    ("Does it hurt?",
     "No. You feel the cool gel and the light pressure of the probe on your skin, and nothing more. It is one of the most comfortable imaging tests there is."),
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
        ("services", "0082_advanced_diagnostics_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
