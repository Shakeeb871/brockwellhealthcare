"""Replace the IV Laser Therapy service content with the user's restructured, narrative,
honest-about-the-evidence copy. Prose-led with no card grid, timeline or lists, a
reworked section set and a 6-item FAQ. Keeps the hero and inline content images.
Supersedes 0061. Hero: static/img/services/iv-laser-therapy-hero.webp;
inline: static/img/services/iv-laser-therapy-content.webp."""

from django.db import migrations

SLUG = "iv-laser-therapy"

SEO_TITLE = "IV Laser Therapy in Dubai | ILIB | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led IV laser (ILIB) therapy in Dubai for fatigue, inflammation and circulation "
    "support. An honest, assessment-first look at a developing wellness therapy."
)
HERO_HEADING = "IV laser therapy in Dubai"
SUMMARY = (
    "A supervised, exploratory IV laser (ILIB) option for fatigue, inflammation and "
    "recovery, delivered honestly as a developing therapy within a wider plan."
)

DESCRIPTION = """
<p>Most light therapy stops at the skin. IV laser therapy is the unusual one that goes further, sending low-level laser light directly into the bloodstream through a fine fibre-optic probe. It is also known as ILIB, short for intravenous laser blood irradiation, and the idea is that light delivered to circulating blood can act throughout the body instead of on one patch of skin. Our doctors at Brockwell Healthcare offer it in Dubai as a supervised option for fatigue, inflammation and recovery, and they are candid from the start that it is a developing therapy, which shapes how we talk about it.</p>

<h2>What is IV laser therapy?</h2>
<p>IV laser therapy passes low-level laser light through a thin fibre-optic probe placed into a vein, usually through a standard cannula. Once the probe is in, the light meets the blood as it flows past, so the whole circulation is exposed and not a single area. The lasers used are low level, which means they work by a gentle photochemical effect on cells and not by heat, the same broad principle behind red light therapy on the skin, only delivered from the inside.</p>

<h2>How light inside the blood is thought to work</h2>
<p>The proposed mechanism sits at the level of the cell. Low-level light in particular wavelengths is absorbed by components of blood and by parts of the cell involved in energy production, and this is thought to nudge how efficiently cells make energy and how they handle inflammation and oxygen. Because the light reaches blood travelling everywhere, any effect would be systemic. That is the theory, and it is a reasonable one, but the honest position is that the human evidence is still limited and uneven, which our doctors say plainly.</p>

<img src="/static/img/services/iv-laser-therapy-content.webp" alt="Clinician delivering IV laser (ILIB) therapy through an intravenous probe at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>The wavelengths, and what each is studied for</h2>
<p>Different colours of laser interact with the blood differently, so the wavelength is chosen around the goal. Red light, at roughly 630 to 650 nanometres, is the most widely used and is studied for energy, oxygen delivery and general support, which is why it features in most fatigue and recovery protocols. Green light, near 520 to 532 nanometres, interacts with haemoglobin in its own way and is looked at for circulation. Blue light, around 405 nanometres, has antimicrobial properties in laboratory work and appears in selected immune-focused protocols. Yellow light, near 589 nanometres, is sometimes added within combined-wavelength sessions and studied for mood and nervous-system support. A doctor selects one, or a combination, from your clinical picture.</p>

<h2>An honest word about the evidence</h2>
<p>It would be easy to oversell this, so we would rather not. IV laser therapy has a plausible mechanism and a following, but the quality of human trials behind it is modest, and results vary a great deal between individuals. We offer it as a supportive, exploratory option within a wider plan, never as a treatment for a specific disease, and we think anyone considering it deserves that context before a first session and not after.</p>

<h2>Who explores it, and the screening that comes first</h2>
<p>The people who look into IV laser therapy are often dealing with persistent fatigue, low-grade inflammation or slow recovery that has not shifted with the usual measures, and who want a systemic, supervised option. Because fatigue has many causes, a proper assessment looks for anything treatable first. IV laser is set aside for people with photosensitivity or porphyria, for anyone taking medication that makes the skin light-sensitive, and during pregnancy without clearance, all of which are checked beforehand.</p>
"""

FAQS = [
    ("Is IV laser the same as red light therapy on the skin?",
     "No, and the difference is delivery. Topical red light only reaches the skin's surface, while IV laser sends light directly into the bloodstream through a probe, so it can act throughout the body. The underlying idea of low-level light affecting cells is shared."),
    ("What does ILIB stand for?",
     "Intravenous laser blood irradiation, which is simply another name for IV laser therapy, describing light delivered into circulating blood through a fibre-optic probe."),
    ("What does a session feel like?",
     "Beyond the small needle when the probe is placed, most people feel very little and just rest, and a session commonly lasts around thirty to sixty minutes."),
    ("Which wavelength would I have?",
     "It depends on the goal. Red is the most common for energy and recovery, while green, blue and yellow are used in selected protocols, and your doctor confirms the choice."),
    ("Is it proven?",
     "It has a plausible mechanism but limited human evidence, so we treat it as exploratory and supportive, not established, and we are open about that."),
    ("Is an assessment needed before starting?",
     "It is. A first appointment looks for treatable causes behind your symptoms and screens for the light-sensitivity conditions that would rule the treatment out."),
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
        ("services", "0070_nad_iv_therapy_inline_image"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
