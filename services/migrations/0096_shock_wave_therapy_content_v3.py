"""Refresh the Shock Wave Therapy service with the user's condensed, narrative copy:
reworked section set (What is / Radial and focused / What it treats / What to expect /
Who it suits) and a 9-item FAQ. Prose-led, no card grid, timeline or lists. Keeps the
hero and inline content images. Supersedes 0062.
Hero: static/img/services/shock-wave-therapy-hero.webp;
inline: static/img/services/shock-wave-therapy-content.webp."""

from django.db import migrations

SLUG = "shock-wave-therapy"

SEO_TITLE = "Shockwave Therapy in Dubai | ESWT | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led shockwave therapy (ESWT) in Dubai for plantar fasciitis, calcific shoulder, "
    "tendon pain and stubborn soft-tissue injuries, built around a proper assessment."
)
HERO_HEADING = "Shockwave therapy in Dubai"
SUMMARY = (
    "Doctor-led shockwave therapy (ESWT) for plantar fasciitis, calcific shoulder, tendon "
    "pain and stubborn soft-tissue injuries, built around a proper assessment."
)

DESCRIPTION = """
<p>Some tendon pain fades with rest, and some of it just moves in and stays. Shockwave therapy is built for the second, stubborn kind, the pain that has stopped answering to everything sensible you have tried. It uses focused acoustic pressure waves to nudge stalled tissue back into repair, and our doctors at Brockwell Healthcare reach for it only once a proper assessment says it genuinely fits your case. It is one of the better-evidenced options for chronic tendon problems, which is worth knowing before you resign yourself to living with one.</p>

<h2>What is shockwave therapy, and how it works</h2>
<p>Shockwave therapy, or ESWT to give it its clinical name, sends pulses of acoustic energy through the skin into the tissue beneath. These are not electric shocks despite the name, but tuned mechanical pressure waves aimed at the spot where the trouble sits. Once the waves land, several things start moving at once. They help break down the calcium that hardens inside a stubborn tendon, they draw new blood vessels into poorly supplied areas through a process called neovascularisation, which matters because tendons are notoriously starved of blood, they switch the collagen-building cells back on, and they settle the local nerve fibres that have been firing pain on a loop. What shockwave really does is add just enough controlled stress to restart a repair job the body had quietly given up on.</p>

<img src="/static/img/services/shock-wave-therapy-content.webp" alt="Clinician delivering shockwave therapy (ESWT) to a tendon at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>Radial and focused waves</h2>
<p>The right kind of wave depends on the tissue, so your doctor settles the approach after examining you. Radial shockwave therapy, or RSWT, sends its pressure waves spreading outward from the point of contact, which covers a broader, shallower area and makes it the everyday choice for surface-level tendon and muscle-insertion pain. Focused shockwave therapy, or FSWT, drives its energy to one precise depth, so a specific target like a calcific deposit or a single degenerated patch of tendon can be reached accurately, which suits deeper problems. Where a case needs reach and precision together, the two are sometimes combined in a single session.</p>

<h2>What it treats</h2>
<p>Most people find their way to shockwave the same way, after months of a nagging tendon, plenty of rest and a course of physiotherapy, with the pain still lingering. The usual candidates are plantar fasciitis, Achilles and patellar tendinopathy, tennis and golfer's elbow, calcific shoulder tendinitis, hip and gluteal tendon pain, and the ache where a muscle anchors to bone. It is most useful precisely when a problem has turned chronic and conservative care has run out of road, which is the point at which many people assume nothing else will help.</p>

<h2>What to expect, and the course</h2>
<p>Your first visit is a conversation, not a treatment, where our doctor examines the area, looks over any scans, and works out whether ESWT suits your problem and which form it calls for. The session itself is quick. A clinician runs the handpiece over the area with a little gel, and it taps out the pulses as it goes, which can sting for a moment over a tender spot, so the intensity is dialled to what you can handle. A few minutes per area, no anaesthetic, and most people walk straight back into their day. Because shockwave leans on your own repair, results arrive over weeks, and treatment usually runs as a short series of weekly sessions, with improvement often continuing for weeks after the course ends, especially when good rehabilitation carries it forward.</p>

<h2>Who it suits, and who it does not</h2>
<p>Shockwave suits people with a chronic tendon or soft-tissue problem that has not settled with rest and physiotherapy, and who are willing to give repair the weeks it needs. It asks for patience, and it would be dishonest not to say so, because one session rarely settles a chronic tendon and progress differs from person to person. Screening also comes first for good reason. Our doctor sets shockwave aside during pregnancy, over an area affected by a bleeding disorder or blood thinners, near an active infection or a tumour, and over a child's growth plates, and any pacemaker or implant is reviewed on its own merits.</p>
"""

FAQS = [
    ("What is shockwave therapy?",
     "Shockwave therapy, or ESWT, uses focused acoustic pressure waves delivered through the skin to stimulate repair in chronic tendon and soft-tissue problems. It works by breaking down calcific deposits, drawing in new blood vessels and restarting stalled collagen repair, and it is usually used once conservative care has not done enough."),
    ("Does shockwave therapy actually work?",
     "For the chronic tendon problems it is aimed at, it is one of the better-evidenced non-surgical options, though results build gradually and vary between people. Our doctor is honest about how likely it is to help your particular condition."),
    ("Is it the same as the treatment for kidney stones?",
     "They come from the same family but do different jobs. The lithotripsy used to shatter kidney stones runs at far higher energy, while musculoskeletal ESWT uses gentler waves tuned to prompt repair in tendons and soft tissue."),
    ("Does shockwave therapy hurt?",
     "Over a tender area you feel a firm tapping that can sting for a moment, though the intensity is adjusted to what you can take. No anaesthetic is needed, and any soreness afterwards is usually mild and gone within a day or two."),
    ("How many sessions will I need?",
     "Most people have a short course of weekly sessions, though the number depends on the condition and how it responds. Our doctor sets a plan after the assessment and revisits it as you go."),
    ("When might I notice a difference?",
     "Because it works with your own repair, improvement tends to build over the weeks during and after the course, which is why our doctor keeps expectations grounded from the start."),
    ("What is the difference between radial and focused shockwave?",
     "Radial waves spread across a broader, shallower area, while focused waves drive energy to one precise depth for a specific structure, and our doctor picks, or combines, them based on what is being treated."),
    ("Is there any downtime?",
     "Most people return to normal activity straight away, sometimes a little sore for a day or two, and our doctor flags any activity to ease off on for your condition."),
    ("How much does shockwave therapy cost in Dubai?",
     "It depends on the area treated, the type of delivery and the number of sessions, and we go through the pricing in full up front."),
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
        ("services", "0095_exosome_therapy_content_v3"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
