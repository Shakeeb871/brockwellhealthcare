"""Create a new IV Drips service under the Regenerative Wellness category (level-2,
so it appears in that category's nav dropdown). Doctor-led, honest, narrative copy
covering hydration, vitamins and recovery, with a 7-item FAQ. Images added later."""

from django.db import migrations
from django.utils.text import slugify

SLUG = "iv-drips"
NAME = "IV Drips"
ICON = "💧"

SEO_TITLE = "IV Drips in Dubai | Doctor-Led IV Therapy | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led IV drips in Dubai at Brockwell Healthcare for hydration, vitamins and "
    "recovery support. An honest look at what IV therapy can do, and what it cannot."
)
HERO_HEADING = "IV drips in Dubai"
SUMMARY = (
    "Doctor-led IV drips for hydration, nutrient support and recovery, with an honest view "
    "of which drips genuinely help and which do not."
)

DESCRIPTION = """
<p>An IV drip delivers fluids, vitamins or minerals straight into a vein, so they reach the bloodstream directly without passing through the gut. That single fact, direct delivery, is the whole appeal and also the source of most of the exaggerated claims around it. At Brockwell Healthcare our doctors offer IV drips in Dubai for hydration, nutrient support and recovery, and a large part of the service is being honest about which drips genuinely help and which are mostly expensive water.</p>

<h2>What is an IV drip?</h2>
<p>An IV drip, also called intravenous therapy, is a controlled infusion of a fluid, usually sterile saline, often mixed with specific vitamins, minerals or antioxidants, given through a small cannula in the arm. A session typically takes somewhere between thirty and sixty minutes while the fluid runs in slowly. It is a medical procedure, so it is set up and supervised by trained clinicians, and it should not be treated casually.</p>

<h2>Why give nutrients by vein at all</h2>
<p>The argument for IV over a tablet comes down to bioavailability, which is how much of something actually reaches your bloodstream. When you swallow a vitamin, your gut absorbs only a fraction of it, and the amount varies from person to person and nutrient to nutrient. An infusion skips that step and delivers close to the full dose directly, which can matter when someone is genuinely depleted, dehydrated, or has a gut that absorbs poorly. That is the honest, real basis for IV therapy, and it is a narrower basis than the marketing suggests.</p>

<h2>What is usually in a drip</h2>
<p>The contents are chosen around the goal, and a few combinations come up again and again. The best known is the Myers' cocktail, a blend developed decades ago that combines magnesium, calcium, several B vitamins and vitamin C, used for general support and recovery. Glutathione, a naturally occurring antioxidant, is a common addition, often requested for skin and wellness. Plain saline is a simple, effective rehydration drip in its own right. Higher-dose vitamin C and specific mineral mixes are used in other blends. Our doctor confirms a combination that makes sense for you instead of selling a fixed menu.</p>

<h2>An honest word about what drips can and cannot do</h2>
<p>This is where we differ from a lot of drip lounges. The genuine benefits of IV therapy are real but specific. It rehydrates quickly, it corrects a true vitamin or mineral shortfall efficiently, and it can help someone recover from a bout of illness or heavy dehydration. What it does not do is detoxify a healthy body, cure disease, or deliver lasting energy to someone who is simply tired for ordinary reasons, since a well-nourished body clears the excess of most water-soluble vitamins and passes it out. If your levels are normal, topping them up intravenously mostly produces expensive urine, and we would rather tell you that than take the booking.</p>

<h2>Who it suits, and the safety side</h2>
<p>IV drips suit people who are dehydrated, recovering from illness, genuinely low in a nutrient, or who absorb poorly through the gut, and they can be a sensible support around a demanding period. They are generally well tolerated, though they are not for everyone. People with certain heart or kidney conditions have to be careful with the fluid and mineral load, some nutrients interact with medications, and anyone with those concerns is screened first. A brief assessment, and sometimes a blood test, is what makes the drip appropriate, not arbitrary.</p>
"""

FAQS = [
    ("Do IV vitamin drips actually work?",
     "For specific purposes, yes. They rehydrate quickly and correct genuine vitamin or mineral deficiencies efficiently, because they bypass the gut. For a healthy, well-nourished person, though, the benefits are limited, since the body simply clears the excess of most water-soluble vitamins."),
    ("What is in a Myers' cocktail?",
     "A Myers' cocktail is a long-standing blend of magnesium, calcium, several B vitamins and vitamin C, given by infusion and used for general support and recovery. The exact mix can be adjusted to the person."),
    ("Are IV drips safe?",
     "Given by trained clinicians they are generally safe and well tolerated. The main cautions involve the fluid and mineral load for people with certain heart or kidney conditions, and possible interactions with medication, which is why a quick assessment comes first."),
    ("How long does a drip take?",
     "Most sessions run between thirty and sixty minutes while the fluid infuses slowly, and you can sit and rest throughout."),
    ("Will a drip give me more energy?",
     "If low energy is down to dehydration or a real deficiency, correcting it can help. If you are simply tired for everyday reasons, a drip is unlikely to do much beyond the short term, and we will say so honestly."),
    ("Can a drip detox my body?",
     "No. A healthy liver and kidneys already handle that continuously, and no infusion improves on them. We do not make detox claims for IV therapy."),
    ("Do I need a blood test first?",
     "Sometimes. For a simple hydration drip it may not be needed, but where the aim is to correct a deficiency, a blood test makes the treatment targeted, not guesswork."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    cat = ServiceCategory.objects.filter(region="uae", slug="regenerative-wellness").first()
    if not cat:
        return

    # Place after the current last service in this category.
    last = (
        Service.objects.filter(region="uae", category=cat, parent__isnull=True)
        .order_by("-order")
        .first()
    )
    next_order = (last.order + 1) if last else 1

    svc, _ = Service.objects.update_or_create(
        region="uae", slug=SLUG,
        defaults=dict(
            category=cat,
            parent=None,
            name=NAME,
            hero_heading=HERO_HEADING,
            icon=ICON,
            summary=SUMMARY,
            description=DESCRIPTION.strip(),
            benefits="",
            seo_title=SEO_TITLE,
            seo_description=SEO_DESCRIPTION,
            order=next_order,
            is_published=True,
        ),
    )

    ct, _ = ContentType.objects.get_or_create(app_label="services", model="service")
    FAQItem.objects.filter(content_type=ct, object_id=svc.id).delete()
    for i, (question, answer) in enumerate(FAQS):
        FAQItem.objects.create(
            content_type=ct, object_id=svc.id,
            question=question, answer=answer, order=i, is_published=True,
        )


def remove_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if svc:
        ct, _ = ContentType.objects.get_or_create(app_label="services", model="service")
        FAQItem.objects.filter(content_type=ct, object_id=svc.id).delete()
        svc.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0076_physiotherapy_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, remove_content)]
