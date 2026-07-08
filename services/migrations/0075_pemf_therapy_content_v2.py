"""Update the existing PEMF Therapy service with the user's restructured, narrative,
evidence-honest copy. Prose-led with no card grid, timeline or lists, a reworked section
set and a 7-item FAQ. Keeps the hero and inline content images. Supersedes the previous
content. Hero: static/img/services/pemf-therapy-hero.webp;
inline: static/img/services/pemf-therapy-content.webp."""

from django.db import migrations

SLUG = "pemf-therapy"

SEO_TITLE = "PEMF Therapy in Dubai | Pulsed Electromagnetic Field | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "PEMF therapy in Dubai at Brockwell Healthcare for bone healing, pain and recovery "
    "support. An honest look at how pulsed electromagnetic fields work and where the "
    "evidence is strongest."
)
HERO_HEADING = "PEMF therapy in Dubai"
SUMMARY = (
    "Non-invasive pulsed electromagnetic field therapy for bone healing, pain and recovery "
    "support, delivered honestly around where the evidence is strongest."
)

DESCRIPTION = """
<p>PEMF therapy uses pulsed electromagnetic fields to influence the body at the level of the cell, without needles, drugs or heat. It stands for pulsed electromagnetic field therapy, and unlike many wellness treatments it has a genuine, decades-old medical use behind part of its story. At Brockwell Healthcare our doctors offer PEMF therapy in Dubai for recovery, pain and bone healing support, and they are clear about which of its many claims the evidence actually stands behind.</p>

<h2>What is PEMF therapy?</h2>
<p>PEMF therapy delivers brief, pulsing magnetic fields to the body through a mat, a coil or a targeted applicator. The fields are low in strength, measured in units called Gauss, and pulsed at particular frequencies measured in Hertz. Nothing touches or enters the body beyond the field itself, so a session is entirely non-invasive, and the treated area feels little or nothing during it.</p>

<h2>How PEMF works</h2>
<p>The mechanism is electrical, which surprises people. A changing magnetic field induces a tiny electrical current in the tissue it passes through, and cells are quietly electrical things, holding a voltage across their membranes and moving charged ions in and out through channels. PEMF is thought to influence this membrane activity gently, which in turn affects processes like inflammation, circulation and the signalling that drives repair. In bone specifically, these induced currents appear to encourage the cells that build new bone, which is the mechanism behind its most established use.</p>

<img src="/static/img/services/pemf-therapy-content.webp" alt="Patient receiving non-invasive PEMF (pulsed electromagnetic field) therapy at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>Where the evidence is strongest, and where it thins out</h2>
<p>This is the honest heart of the page, because PEMF is marketed for almost everything. Its strongest, oldest evidence is in bone healing, where pulsed electromagnetic field devices have a recognised medical use as bone growth stimulators for fractures that are slow to knit, going back decades. There is reasonable evidence for help with certain kinds of pain and post-injury recovery, which is why it appears alongside rehabilitation. Beyond that, the sweeping wellness claims, from detox to curing unrelated diseases, run well ahead of what the science shows. Our doctors will tell you plainly which category your goal sits in before you commit to a course.</p>

<h2>What to expect, and who it suits</h2>
<p>A PEMF session is simple and comfortable. You sit or lie with the mat or applicator over the treated area for a set time, usually somewhere between ten and thirty minutes, feeling little more than nothing at all. It suits people looking to support bone healing, recovery or certain persistent pain, and it works best as one part of a plan that includes proper rehabilitation. It is well tolerated by most, though it is not used over an active implanted electronic device such as a pacemaker, or during pregnancy without clearance, and anyone with such a device is screened first.</p>
"""

FAQS = [
    ("What is PEMF therapy?",
     "PEMF, or pulsed electromagnetic field therapy, uses brief pulses of a low-strength magnetic field to induce tiny electrical currents in tissue, which are thought to support processes like bone healing, inflammation and recovery. It is non-invasive, with nothing entering the body beyond the field."),
    ("How does PEMF actually work?",
     "A pulsing magnetic field induces a small electrical current in the tissue, and because cells hold a voltage across their membranes and move charged ions, this gently influences their activity, affecting inflammation, circulation and repair signalling, and in bone the cells that build new bone."),
    ("Does PEMF really work?",
     "It depends on the goal. It has strong, long-standing evidence for helping slow-healing bone fractures, reasonable evidence for some pain and recovery, and little support for the broader wellness claims. We are upfront about which applies to you."),
    ("Is it an approved medical treatment?",
     "For bone healing, pulsed electromagnetic field devices have a recognised medical use as bone growth stimulators going back decades. Other uses are more exploratory, and we describe them that way."),
    ("What does a session feel like?",
     "Usually like nothing much. You rest with the applicator over the area for ten to thirty minutes, and most people feel no sensation at all, which is normal."),
    ("Is PEMF safe?",
     "For most people it is very well tolerated and non-invasive. It is not used over pacemakers or other active implanted electronics, or in pregnancy without clearance, and anyone with an implanted device is screened beforehand."),
    ("How many sessions are needed?",
     "Effects build over a course and not a single visit, so a series is usual, with the number and timing set around your goal and reviewed as you go."),
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
        ("services", "0074_sports_medicine_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
