"""Replace the Anti-Aging Aesthetics category content with the user's injectables- and
rejuvenation-focused copy (British 'anti-ageing' spelling in the visible text), rendered
through the professional category (homepage-style) layout as alternating text + image
sections. Hero, lead (intro) and the first two section images are supplied under
static/img/services/categories/anti-aging-aesthetics/ (the two section images were
remapped to the new section slugs). Plus a 6-item FAQ. Supersedes 0048 / 0049."""

from django.db import migrations

SEO_TITLE = "Anti-Ageing Aesthetics in Dubai | Natural Results | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Anti-ageing aesthetics in Dubai at Brockwell Healthcare, using anti-wrinkle "
    "injections, dermal fillers and collagen-boosting treatments for natural, doctor-led "
    "facial rejuvenation."
)
HERO_HEADING = "Anti-ageing aesthetics in Dubai"
SUMMARY = (
    "Natural, doctor-led facial rejuvenation using anti-wrinkle injections, dermal fillers "
    "and collagen-boosting treatments, chosen with restraint."
)

DESCRIPTION = """
<p>Good aesthetic work is the kind nobody notices, because it leaves you looking like a rested version of yourself. Anti-ageing aesthetics covers the treatments that soften the visible signs of ageing in the skin and face, and the skill lies as much in restraint as in technique. At Brockwell Healthcare our doctors approach anti-ageing aesthetics in Dubai with that principle first, since the aim is to look refreshed and natural, and never to look done.</p>

<h2>Why skin ages in the first place</h2>
<p>Understanding the causes explains why the treatments are what they are. Skin ages from the inside and the outside at once. On the inside, the body gradually makes less collagen and elastin, the two proteins that keep skin firm and springy, so it thins and begins to sag and line. On the outside, sunlight does most of the damage, since ultraviolet light breaks down collagen and drives the majority of visible ageing, which is why sun-exposed skin looks older than skin that has been covered. Movement plays a part too, as years of the same expressions etch lines where the muscles fold the skin. Each of those causes has a treatment aimed at it.</p>

<h2>The main treatments, and what each is for</h2>
<p>The core of aesthetic medicine is a small number of well-understood tools used judiciously. Anti-wrinkle injections use a purified botulinum toxin to relax specific muscles, which softens the dynamic lines that come from movement, such as frown lines and crow's feet. Dermal fillers, usually made from hyaluronic acid, a substance your skin already contains, restore lost volume and support structure where the face has hollowed. A separate group of treatments works by prompting your own skin to rebuild, with collagen-stimulating biostimulators and microneedling encouraging fresh collagen over time, and skin boosters improving hydration and quality. The art is choosing the right tool for the right cause instead of reaching for the same one every time.</p>

<h2>A word on looking natural, not frozen</h2>
<p>This is where philosophy matters more than product. The frozen, overfilled look that gives aesthetics a bad name comes from doing too much, not from the treatments themselves, which are subtle in careful hands. Our doctors work conservatively, treating the specific cause of a concern and stopping there, because the face is a whole and small, considered changes read as freshness while heavy ones read as work. It is always easier to add a little more later than to undo too much, so we start gently and build only if needed.</p>

<h2>Who it suits, and honest expectations</h2>
<p>Anti-ageing aesthetics suits people who want to soften specific signs of ageing while still looking like themselves, and who value a medical, measured approach over a menu of packages. Results are not permanent, since anti-wrinkle injections last a few months and most fillers a year or so, and treatments are best seen as maintenance, not a one-time fix. Everything begins with an honest conversation about what will genuinely help and what will not, because part of good aesthetic medicine is talking people out of things they do not need.</p>
"""

FAQS = [
    ("What is the difference between anti-wrinkle injections and fillers?",
     "They do different jobs. Anti-wrinkle injections relax specific muscles to soften lines caused by movement, such as frown lines, while dermal fillers restore lost volume and structure where the face has hollowed. Many treatment plans use a little of both for different areas."),
    ("Why does skin age?",
     "Skin ages because the body makes less collagen and elastin over time, so it thins and sags, and because ultraviolet light breaks down collagen and drives most visible ageing. Repeated facial expressions also etch lines where the skin folds."),
    ("Do anti-ageing treatments actually work?",
     "The core treatments have well-understood effects, softening movement lines, restoring volume and stimulating collagen. Results vary with the person and the treatment, they are not permanent, and they work best as considered maintenance, not a single fix."),
    ("Are these treatments safe?",
     "In trained medical hands they have well-established safety profiles, and most side effects are minor and temporary, such as bruising. A proper assessment and conservative technique are what keep them safe, which is why they belong with a doctor."),
    ("Will I look frozen or overdone?",
     "Not if the work is done conservatively. The overdone look comes from too much treatment, not from the treatments themselves, so we work gently, treat the specific concern and build only if needed."),
    ("How long do results last?",
     "It depends on the treatment. Anti-wrinkle injections typically last a few months and most dermal fillers around a year, after which they are topped up, which is why aesthetics is usually ongoing maintenance."),
]


def load_content(apps, schema_editor):
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    cat = ServiceCategory.objects.filter(region="uae", slug="anti-aging-aesthetics").first()
    if not cat:
        return

    cat.hero_heading = HERO_HEADING
    cat.summary = SUMMARY
    cat.description = DESCRIPTION.strip()
    cat.seo_title = SEO_TITLE
    cat.seo_description = SEO_DESCRIPTION
    cat.is_published = True
    cat.save()

    ct, _ = ContentType.objects.get_or_create(
        app_label="services", model="servicecategory"
    )
    FAQItem.objects.filter(content_type=ct, object_id=cat.id).delete()
    for i, (question, answer) in enumerate(FAQS):
        FAQItem.objects.create(
            content_type=ct, object_id=cat.id,
            question=question, answer=answer, order=i, is_published=True,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0087_clear_emoji_icons"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
