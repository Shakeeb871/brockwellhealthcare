from django.db import migrations
from django.utils import timezone
from datetime import timedelta


CATEGORIES = [
    ("Regenerative Medicine", "regenerative-medicine", "The science and practice of helping the body heal itself.", 1),
    ("Stem Cell Therapy", "stem-cell-therapy", "Advances and answers on cellular therapies.", 2),
    ("Longevity & Wellness", "longevity-wellness", "Living healthier for longer, backed by evidence.", 3),
    ("Patient Care & Recovery", "patient-care-recovery", "Guidance for your treatment and recovery journey.", 4),
    ("Research & Innovation", "research-innovation", "The latest clinical research shaping modern care.", 5),
]

POSTS = [
    {
        "cat": "regenerative-medicine",
        "title": "Understanding Regenerative Medicine: How Your Body Heals Itself",
        "slug": "understanding-regenerative-medicine",
        "excerpt": "Regenerative medicine works with your body’s own repair systems. Here’s what it is, how it works, and who it can help.",
        "featured": True,
        "body": (
            "Regenerative medicine is one of the most exciting fields in modern healthcare. Rather than "
            "simply managing symptoms, it aims to restore the structure and function of damaged tissue by "
            "supporting the body’s own ability to heal.\n\n"
            "## What is regenerative medicine?\n\n"
            "At its core, regenerative medicine uses biological tools — cells, growth factors and "
            "signalling molecules — to encourage repair. Instead of masking a problem, the goal is to "
            "address its underlying cause and help tissue recover.\n\n"
            "## Common applications\n\n"
            "Regenerative approaches are increasingly used across a range of conditions, including:\n\n"
            "- Joint and soft-tissue injuries\n"
            "- Chronic pain and degenerative conditions\n"
            "- Post-surgical and sports recovery\n"
            "- Skin and aesthetic rejuvenation\n\n"
            "## Is it right for you?\n\n"
            "Every patient is different. A thorough consultation and diagnostic assessment are essential "
            "to determine whether a regenerative approach is appropriate — and to build a plan tailored to "
            "your goals. Speak to a specialist to understand your options."
        ),
    },
    {
        "cat": "stem-cell-therapy",
        "title": "Stem Cell Therapy Explained: Myths, Facts and What to Expect",
        "slug": "stem-cell-therapy-explained",
        "excerpt": "There’s a lot of noise around stem cell therapy. We separate evidence-based facts from common myths.",
        "featured": True,
        "body": (
            "Stem cell therapy has attracted enormous attention — and, unfortunately, a fair amount of "
            "misinformation. Understanding the facts helps you make informed, confident decisions about "
            "your care.\n\n"
            "## What stem cells actually do\n\n"
            "Stem cells are the body’s raw materials, capable of developing into specialised cells and "
            "supporting repair. In a clinical setting, evidence-based protocols use them to encourage "
            "healing in targeted areas.\n\n"
            "## Common myths\n\n"
            "- Myth: stem cell therapy is a cure-all. Fact: outcomes depend on the condition, the patient "
            "and the protocol used.\n"
            "- Myth: results are instant. Fact: regeneration is a gradual, biological process.\n"
            "- Myth: all clinics are the same. Fact: safety, sourcing and clinical standards vary widely.\n\n"
            "## What to expect\n\n"
            "A responsible clinic will always begin with assessment, explain realistic outcomes, and "
            "monitor your recovery. Transparency and evidence should guide every step."
        ),
    },
    {
        "cat": "longevity-wellness",
        "title": "The Science of Longevity: Small Habits, Long-Term Impact",
        "slug": "science-of-longevity",
        "excerpt": "Longevity isn’t about living longer alone — it’s about staying healthy and active for more of your life.",
        "featured": False,
        "body": (
            "Longevity medicine focuses on healthspan — the number of years you live in good health — not "
            "just lifespan. The encouraging news is that small, consistent habits have a powerful "
            "cumulative effect.\n\n"
            "## Foundations that matter most\n\n"
            "- Restorative sleep and stress management\n"
            "- Balanced nutrition and regular movement\n"
            "- Preventive screening and early intervention\n"
            "- Meaningful social connection\n\n"
            "## Where medicine helps\n\n"
            "Advanced diagnostics can reveal your biological age and highlight risks before they become "
            "problems. Paired with a personalised plan, this turns prevention into a precise, measurable "
            "strategy rather than guesswork."
        ),
    },
    {
        "cat": "patient-care-recovery",
        "title": "Preparing for Treatment: A Simple Guide for Patients",
        "slug": "preparing-for-treatment",
        "excerpt": "A little preparation makes your treatment smoother and your recovery stronger. Here’s how.",
        "featured": False,
        "body": (
            "Feeling prepared before any treatment reduces anxiety and supports better outcomes. Here are "
            "practical steps to help you feel confident and ready.\n\n"
            "## Before your appointment\n\n"
            "- Note your symptoms, questions and goals\n"
            "- Bring relevant medical history and medications\n"
            "- Arrange support for travel and rest if needed\n\n"
            "## During recovery\n\n"
            "Follow your care team’s guidance closely, stay hydrated and rested, and attend follow-up "
            "reviews. Recovery is a partnership — reach out whenever you have a concern."
        ),
    },
    {
        "cat": "research-innovation",
        "title": "How Advanced Diagnostics Are Transforming Patient Care",
        "slug": "advanced-diagnostics-transforming-care",
        "excerpt": "Precise data leads to precise care. Modern diagnostics let clinicians personalise treatment like never before.",
        "featured": False,
        "body": (
            "The quality of any treatment plan depends on the quality of the information behind it. Modern "
            "diagnostics give clinicians a detailed, data-rich picture of each patient’s health.\n\n"
            "## From guesswork to precision\n\n"
            "Advanced imaging, biomarker panels and genetic profiling reveal what’s really happening in "
            "the body. This clarity means treatment can be targeted, monitored and adjusted with "
            "confidence.\n\n"
            "## The patient benefit\n\n"
            "- Earlier detection of risks\n"
            "- Truly personalised treatment plans\n"
            "- Measurable progress you can see\n\n"
            "As technology advances, this precision will only deepen — making care safer, smarter and more "
            "effective for everyone."
        ),
    },
    {
        "cat": "regenerative-medicine",
        "title": "Recovery After Regenerative Treatment: What Really Helps",
        "slug": "recovery-after-regenerative-treatment",
        "excerpt": "Regeneration continues long after your appointment. These habits give your body the best chance to heal.",
        "featured": False,
        "body": (
            "Regenerative treatment sets healing in motion, but what you do afterwards matters just as "
            "much. Supporting your body during recovery helps you get the most from your treatment.\n\n"
            "## Give healing time\n\n"
            "Biological repair is gradual. Rest, patience and consistency are your allies — results build "
            "steadily over weeks, not hours.\n\n"
            "## Support your recovery\n\n"
            "- Prioritise sleep and gentle movement\n"
            "- Eat nutrient-dense, anti-inflammatory foods\n"
            "- Stay hydrated and avoid overexertion\n"
            "- Keep every follow-up appointment\n\n"
            "Your care team is there to guide each stage. Together, small, steady steps lead to lasting "
            "results."
        ),
    },
]


def seed(apps, schema_editor):
    BlogCategory = apps.get_model("blog", "BlogCategory")
    BlogPost = apps.get_model("blog", "BlogPost")
    now = timezone.now()

    cat_objs = {}
    for i, (name, slug, desc, order) in enumerate(CATEGORIES):
        obj, _ = BlogCategory.objects.get_or_create(
            region="uae", slug=slug,
            defaults={"name": name, "description": desc, "order": order, "is_published": True},
        )
        cat_objs[slug] = obj

    for i, p in enumerate(POSTS):
        if BlogPost.objects.filter(region="uae", slug=p["slug"]).exists():
            continue
        BlogPost.objects.create(
            region="uae",
            category=cat_objs.get(p["cat"]),
            title=p["title"],
            slug=p["slug"],
            excerpt=p["excerpt"],
            body=p["body"],
            author="Brockwell Healthcare",
            published_at=now - timedelta(days=i * 6),
            is_published=True,
            is_featured=p.get("featured", False),
        )


def unseed(apps, schema_editor):
    BlogPost = apps.get_model("blog", "BlogPost")
    BlogCategory = apps.get_model("blog", "BlogCategory")
    BlogPost.objects.filter(slug__in=[p["slug"] for p in POSTS]).delete()
    BlogCategory.objects.filter(slug__in=[c[1] for c in CATEGORIES]).delete()


class Migration(migrations.Migration):
    dependencies = [("blog", "0001_initial")]
    operations = [migrations.RunPython(seed, unseed)]
