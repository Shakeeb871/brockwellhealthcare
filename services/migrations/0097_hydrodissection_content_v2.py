"""Refresh the Hydrodissection & Injections service with the user's condensed, narrative
copy: reworked section set (What is / How it works / What it treats / What to expect /
Who it suits / Why ultrasound guidance) and a 6-item FAQ. Prose-led, no card grid,
timeline or lists. Keeps the hero and inline content images. Supersedes 0020.
Hero: static/img/services/hydrodissection-injections-hero.webp;
inline: static/img/services/hydrodissection-injections-content.webp."""

from django.db import migrations

SLUG = "hydrodissection-injections"

SEO_TITLE = "Hydrodissection & Guided Injections in Dubai | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Ultrasound-guided hydrodissection and injections in Dubai at Brockwell Healthcare for "
    "trapped nerves, joint and soft-tissue pain, placed with millimetre precision after a "
    "proper assessment."
)
HERO_HEADING = "Hydrodissection and injections in Dubai"
SUMMARY = (
    "Ultrasound-guided hydrodissection and injections for trapped nerves, joint and "
    "soft-tissue pain, placed with millimetre precision after a proper assessment."
)

DESCRIPTION = """
<p>A trapped nerve usually hurts for a reason that surprises people, since the nerve itself is often fine and something nearby is simply pressing on it. Hydrodissection is built around that one fact, using a small amount of fluid, placed with ultrasound precision, to ease a nerve free of whatever is crowding it. Our doctors at Brockwell Healthcare offer it, along with a range of guided injections in Dubai, for nerve, joint and soft-tissue pain that has not settled with rest, medication or physiotherapy, and every procedure starts with a proper look at what is actually causing the trouble.</p>

<h2>What is hydrodissection?</h2>
<p>Hydrodissection injects a small volume of fluid right alongside a compressed or trapped nerve. The fluid opens up a plane between the nerve and the tissue pressing on it, and with that bit of space the nerve can move freely again, which often eases the pain and lets it work as it should. It rarely travels alone, since our injection therapy also covers anti-inflammatory injections, regenerative solutions and guided joint injections, so one clinic can match the right tool to the right problem. The part that sets the work apart is that we never do it blind, because ultrasound guides every needle from start to finish.</p>

<h2>How it works</h2>
<p>The procedure delivers a small volume of fluid, usually saline, a little local anaesthetic or a regenerative solution, through a fine needle placed beside the affected nerve. As the fluid spreads, it lifts the nerve away from the adhesions, scar tissue or structures that were squeezing it, so it can glide through the surrounding tissue again the way it is meant to, without catching or pinching every time you move. Ultrasound is what turns a delicate procedure into a controlled one, letting our doctor watch the needle and the spreading fluid on screen in real time and lay it exactly where it belongs. That accuracy matters here more than almost anywhere, because these nerves often run within a hair of blood vessels and tendons that have to be left well alone.</p>

<img src="/static/img/services/hydrodissection-injections-content.webp" alt="Doctor performing an ultrasound-guided hydrodissection at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>What it treats</h2>
<p>Hydrodissection tends to be the option people reach for once a trapped nerve or an irritated joint has stopped answering to rest, tablets or physiotherapy. In practice that usually means carpal tunnel syndrome, cubital tunnel syndrome, a peripheral nerve caught in scar tissue, or scar-related nerve restrictions, while the related injections handle inflamed joints and tendons. In every case, suitability is confirmed by a proper assessment first.</p>

<h2>What to expect</h2>
<p>Your first step is a consultation, where our doctor examines the area, looks over any imaging or nerve studies, and confirms whether hydrodissection or a targeted injection genuinely fits your problem. On the day, you lie comfortably while the doctor uses ultrasound to steer a fine needle to the exact spot, usually after a little local anaesthetic. You might feel a brief press as the fluid spreads, and that is about it. The procedure takes only a short while, most people head home the same day, and any tenderness at the site tends to fade within a day or two.</p>

<h2>Who it suits, and its honest limits</h2>
<p>Hydrodissection suits people with a trapped or irritated nerve, or a stubborn joint or tendon, who would rather explore a precise, minimally invasive option before surgery. It is not a cure-all, and it would be wrong to pretend otherwise. Some nerves respond beautifully and others barely at all, a stubborn case may need repeating, and the relief holds best when rehabilitation carries it forward. Screening also sets it aside where there is active infection at the site, a bleeding disorder or blood-thinning medication that has not been reviewed, or a known allergy to the fluid, all checked before anything goes ahead.</p>

<h2>Why ultrasound guidance changes the result</h2>
<p>It is worth dwelling on the guidance, because it is the whole difference. Placing fluid to free a nerve is a millimetre task, and the nerves involved sit close to arteries and tendons that must not be touched. Watching the needle and the fluid live on screen lets our doctor reach the precise plane beside the nerve and confirm the fluid is spreading where it should, which protects your safety and gives the procedure its best chance of working. The same guidance runs through our joint and soft-tissue injections, so medication reaches the exact structure that needs it instead of the rough vicinity.</p>
"""

FAQS = [
    ("What is hydrodissection?",
     "Hydrodissection uses a small volume of fluid, placed beside a compressed nerve under ultrasound guidance, to separate the nerve from the tissue squeezing it. Freeing the nerve so it can move normally again often eases the pain, and it is used most for trapped-nerve conditions."),
    ("How is it different from a steroid injection?",
     "They do different jobs. A steroid injection mainly calms inflammation, while hydrodissection physically separates a nerve from the tissue compressing it, which is a mechanical release. Depending on the diagnosis, our doctor may suggest one, the other, or a combination."),
    ("What conditions is it used for?",
     "Most often carpal tunnel syndrome, cubital tunnel syndrome, peripheral nerve entrapment and scar-related nerve restrictions, while the related injections handle irritated joints and tendons, with suitability confirmed at assessment."),
    ("Why does ultrasound guidance matter?",
     "Because these nerves run close to blood vessels and tendons, watching the needle and fluid in real time lets our doctor place them exactly where intended, which protects your safety and improves the result."),
    ("Does it hurt?",
     "Most people feel only a brief press as the fluid spreads, usually after a little local anaesthetic, and any soreness at the site tends to settle within a day or two."),
    ("Is it a permanent fix?",
     "Responses vary. Some people gain lasting relief, others need more than one procedure or do better when it is combined with rehabilitation, and our doctor is honest about what is realistic for your case."),
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
        ("services", "0096_shock_wave_therapy_content_v3"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
