"""Replace the Regenerative Wellness category content with the user's whole-person,
philosophy-led copy, rendered through the professional category (homepage-style) layout
as alternating text + image sections. Hero, lead (intro) and the first two section images
are supplied under static/img/services/categories/regenerative-wellness/ (the two section
images were remapped to the new section slugs). Plus a 6-item FAQ. Supersedes the
previous category content."""

from django.db import migrations

SEO_TITLE = "Regenerative Wellness in Dubai | Whole-Person Care | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Regenerative wellness in Dubai at Brockwell Healthcare, a whole-person approach that "
    "helps the body repair, from joints and cells to skin and resilience, grounded in "
    "honest medicine."
)
HERO_HEADING = "Regenerative wellness in Dubai"
SUMMARY = (
    "A whole-person approach that helps the body repair, from joints and cells to skin and "
    "resilience, grounded in honest medicine."
)

DESCRIPTION = """
<p>Most of medicine is built to suppress a problem, to quiet a symptom or manage a disease once it has arrived. Regenerative wellness starts from a different question, which is how to help the body repair and function better in the first place. It is less a single treatment than a philosophy that runs across our clinic, joining the physical, the cellular and the preventive into one approach. At Brockwell Healthcare our regenerative wellness in Dubai brings those threads together, and holds all of them to the same honest standard about what the science does and does not yet show.</p>

<h2>What regenerative wellness means</h2>
<p>Regenerative wellness is an approach that aims to restore and support the body's own capacity to repair, and does more than mask symptoms. In practice that means using treatments and habits that work with your biology, from the growth factors that heal a tendon to the daily choices that protect your cells, and organising them around your goals. It is whole-person by nature, because the body does not separate its joints from its metabolism from its stress, and neither should good care.</p>

<h2>Helping the body repair itself</h2>
<p>The most established side of regenerative medicine is musculoskeletal, where the goal is to heal worn or injured tissue instead of only managing the pain. This is the home of our regenerative orthopaedics work, and of the specific treatments underneath it, including stem cell therapy, shockwave therapy and hydrodissection, supported by sports medicine and physiotherapy. These are the treatments with the firmest ground under them, and they aim to get a joint or tendon working again instead of simply quietening it.</p>

<h2>Regeneration at the cellular level</h2>
<p>Below the level of joints and muscles sits the cellular side, which shades into longevity medicine. Here the focus is the machinery of energy, repair and ageing, addressed through our longevity programme and through supportive treatments such as regenerative IV therapy, NAD+ infusions, peptide therapy and, at the more investigational end, exosome and therapeutic plasma exchange. The evidence across these varies a great deal, from well-supported to genuinely experimental, and we are careful to say which is which for each one.</p>

<h2>Regeneration you can see, and resilience you can feel</h2>
<p>Two more threads complete the picture. On the surface, aesthetic regeneration works with the skin's own repair, through collagen-stimulating and anti-ageing treatments that aim to look natural. Underneath behaviour, resilience matters just as much, which is why stress management sits within this philosophy too, since a nervous system stuck in overdrive undermines repair everywhere else. Regeneration is as much about how the whole system recovers as about any single treatment.</p>

<h2>How it fits together</h2>
<p>The thread that ties all of this is a plan built around you, and never a menu sold to you. It begins with a proper assessment, often supported by detailed diagnostics, so that effort goes where it will actually help. From there the pieces are chosen and sequenced with honesty about the evidence behind each, and always on top of the foundations that do the heavy lifting, meaning movement, sleep, nutrition and managed stress. No single treatment here is magic, and the value is in combining the right ones well.</p>
"""

FAQS = [
    ("What is regenerative medicine?",
     "Regenerative medicine is an approach that aims to restore the body's own ability to repair damaged tissue and function, and does more than suppress symptoms. It spans musculoskeletal treatments like PRP and stem cells, cellular and longevity approaches, and aesthetic and preventive care."),
    ("What treatments count as regenerative?",
     "A broad range, from orthopaedic treatments such as stem cell therapy, shockwave and hydrodissection, to cellular and longevity approaches like NAD+ and regenerative IV therapy, peptides, exosomes and plasma exchange, through to collagen-based aesthetic treatments. They vary widely in how well proven they are."),
    ("Is regenerative medicine proven?",
     "It depends entirely on the treatment. Some, like physiotherapy-supported orthopaedic care, are well established, while others, particularly at the cellular and longevity end, are still emerging or experimental. We are clear about where each one sits."),
    ("Is this just wellness marketing?",
     "Not the way we practise it. Credible regenerative wellness is built on assessment, honest evidence and the proven foundations of health, with each treatment judged on its merits. A clinic that promises miracles from every therapy is selling something else."),
    ("Where should I start?",
     "With an assessment, so the plan fits your goals and your health, not a fixed package. That conversation points you to the specific treatments worth exploring and, just as importantly, the ones that are not worth your time."),
]


def load_content(apps, schema_editor):
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    cat = ServiceCategory.objects.filter(region="uae", slug="regenerative-wellness").first()
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
        ("services", "0092_healthspan_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
