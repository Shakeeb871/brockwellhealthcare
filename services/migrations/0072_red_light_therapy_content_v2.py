"""Update the existing Red Light Therapy service with the user's restructured, narrative,
evidence-honest copy. Prose-led with no card grid, timeline or lists, a reworked section
set and a 7-item FAQ. Keeps the hero and inline content images. Supersedes the previous
red light content. Hero: static/img/services/red-light-therapy-hero.webp;
inline: static/img/services/red-light-therapy-content.webp."""

from django.db import migrations

SLUG = "red-light-therapy"

SEO_TITLE = "Red Light Therapy in Dubai | Photobiomodulation | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led red light therapy in Dubai for skin, recovery and hair support. An honest "
    "look at what photobiomodulation does, where the evidence is real, and where it is not."
)
HERO_HEADING = "Red light therapy in Dubai"
SUMMARY = (
    "Doctor-led red and near-infrared light therapy (photobiomodulation) for skin, recovery "
    "and hair, delivered honestly around where the evidence is real."
)

DESCRIPTION = """
<p>Red light therapy is one of the few wellness treatments with a genuine, well-described mechanism behind it, which is refreshing. It uses specific wavelengths of red and near-infrared light to reach into cells and give their energy machinery a gentle push. The proper name is photobiomodulation, and it has real evidence in some areas and a lot of overblown marketing in others. Our doctors at Brockwell Healthcare offer it in Dubai for skin, recovery and hair, and part of the job is being clear about which of those claims the science actually supports.</p>

<h2>What is red light therapy?</h2>
<p>Red light therapy delivers light at particular wavelengths onto the skin, without heat and without ultraviolet, so there is no burning and no tanning involved. Two bands do the work. Visible red light, roughly 630 to 660 nanometres, is absorbed at the surface and in the skin itself, while near-infrared light, around 810 to 850 nanometres, travels deeper into tissue. The device might be a panel, a handheld unit or a mask, but the active ingredient is always the wavelength and the dose, not the gadget.</p>

<h2>How it actually works</h2>
<p>The mechanism is genuinely neat, and worth understanding. Inside your cells, the mitochondria carry an enzyme called cytochrome c oxidase, the fourth complex in the chain that produces energy. This enzyme happens to absorb red and near-infrared light very well, and when it does, two useful things follow. It nudges the mitochondria to produce a little more ATP, the cell's energy currency, and it prompts the release of nitric oxide, which relaxes small blood vessels and improves local blood flow. More available energy and better circulation in the treated tissue is the simple version of what red light does, and it is why the effects show up in skin and healing.</p>

<img src="/static/img/services/red-light-therapy-content.webp" alt="Patient receiving red and near-infrared light therapy (photobiomodulation) at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>Where the evidence is real, and where it is not</h2>
<p>This is the part that matters most, because red light is sold for almost everything. The reasonable evidence sits in a few areas. It is genuinely studied for skin quality, where it is linked with collagen production and a softening of fine lines, for wound and tissue healing, for certain kinds of hair loss, and for easing muscle soreness and some joint and tendon pain. Those uses have a real mechanism and a reasonable body of work behind them. The claims to treat with more caution are the sweeping ones, the promises of fat loss, detoxification or a cure for unrelated conditions, which run well ahead of the evidence. Our doctors will happily tell you which bucket your goal falls into before you spend a session on it.</p>

<h2>What to expect, and who it suits</h2>
<p>A session is straightforward and comfortable. You sit or lie near the device for the treated area for a set time, usually a matter of minutes, feeling a mild warmth at most, with eye protection where it is needed. Red light suits people looking to support skin quality, recovery or hair, and it pairs well with other skin and wellness care. It is well tolerated by most, though anyone taking medication that increases light sensitivity, or with a condition that flares with light, is reviewed first, and the dose and wavelength are matched to the goal.</p>
"""

FAQS = [
    ("Is red light therapy the same as a sunbed?",
     "Not at all. Sunbeds use ultraviolet light, which damages skin and drives tanning and ageing. Red light therapy uses red and near-infrared wavelengths with no ultraviolet, so it does not tan or burn the skin."),
    ("What is the difference between red and near-infrared light?",
     "Red light, around 630 to 660 nanometres, works at the skin's surface and is favoured for skin concerns, while near-infrared, around 810 to 850 nanometres, penetrates deeper and is used for muscle, joint and tissue recovery. Many devices combine the two."),
    ("What does it actually do inside the cell?",
     "The light is absorbed by cytochrome c oxidase in the mitochondria, which nudges up ATP energy production and releases nitric oxide to improve local blood flow. That combination is what supports skin and healing."),
    ("Does it help with wrinkles and skin?",
     "Skin is one of its better-supported uses, where it is linked with collagen production and softer fine lines over a course of sessions, though results build gradually and vary between people."),
    ("Can it regrow hair?",
     "There is reasonable evidence for certain types of hair loss, and it is used for that, but it works best as part of a wider plan and does not suit every kind of hair loss. A proper assessment sorts out which."),
    ("Is it safe?",
     "For most people it is very well tolerated, since there is no ultraviolet and no significant heat. Anyone on light-sensitising medication or with a light-triggered condition is checked beforehand."),
    ("How many sessions are needed?",
     "Effects build over a course and not a single visit, so a series is usual, and your doctor sets the number and spacing around your goal."),
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
        ("services", "0071_iv_laser_therapy_content_v3"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
