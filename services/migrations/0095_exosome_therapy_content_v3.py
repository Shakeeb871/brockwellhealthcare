"""Refresh the Exosome Therapy service with the user's condensed, education-first
narrative copy: reworked section set (What is / How it works / What it is explored for /
Who it suits) and a 6-item FAQ. Prose-led, no card grid, timeline or lists. New meta
title. Keeps the hero and inline content images. Supersedes 0064.
Hero: static/img/services/exosome-therapy-hero.webp;
inline: static/img/services/exosome-therapy-content.webp."""

from django.db import migrations

SLUG = "exosome-therapy"

SEO_TITLE = "Exosome Therapy in Dubai | Emerging Regenerative Science | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Exosome therapy in Dubai at Brockwell Healthcare, an advanced, emerging area of "
    "regenerative medicine. An honest, education-first look at the science and our "
    "assessment approach."
)
HERO_HEADING = "Exosome therapy in Dubai"
SUMMARY = (
    "An honest, education-first look at exosome therapy, one of the newest, cell-free "
    "areas of regenerative medicine, with suitability confirmed through proper assessment."
)

DESCRIPTION = """
<p>Exosomes are among the smallest messengers the body makes, tiny bubbles of membrane between thirty and a hundred and fifty nanometres across, far smaller than the cells that release them. Cells use them to send instructions to one another, and exosome therapy is built on that idea of cellular post. It sits among the newest and least settled corners of regenerative medicine, and our doctors at Brockwell Healthcare treat it exactly that way, explaining the biology, being honest about how early the evidence still is, and helping you understand where it might fit before anything is decided.</p>

<h2>What is exosome therapy?</h2>
<p>An exosome is a type of extracellular vesicle, a small package a cell releases into its surroundings. What sets exosomes apart is where they are made. They begin inside the cell, when part of an endosome buds inward to form a structure called a multivesicular body, which then travels to the cell surface and releases its vesicles outward. That endosomal origin distinguishes true exosomes from microvesicles, which bud straight off the outer membrane. Inside each one is a cargo of proteins, lipids, messenger RNA and short strands called microRNA, and on the outside they carry recognisable markers, in particular the tetraspanins CD9, CD63 and CD81. Because all that signalling material arrives without a whole cell attached, the approach is described as cell-free.</p>

<h2>How it works</h2>
<p>The whole idea rests on cell communication, a process known as paracrine signalling. When a cell releases exosomes, nearby cells can take them up and read their cargo, and that cargo can nudge how those cells behave. The microRNA is a particularly interesting part, because a single short strand can quietly turn the volume up or down on how a cell reads its own genes. The exosomes studied in regenerative medicine are usually derived from mesenchymal stem cells, and they draw interest partly because they carry a similar message to the cells themselves while being far simpler to handle. That is a reasonable scientific rationale, and it is still a long way from proof.</p>

<img src="/static/img/services/exosome-therapy-content.webp" alt="Doctor explaining the emerging science of exosome therapy at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>What it is explored for, honestly</h2>
<p>The areas discussed most in connection with exosomes are skin quality and rejuvenation, hair and scalp concerns, and joint or soft-tissue applications. These are best understood as directions of research, not settled or proven uses, and our team is upfront about that difference. Much of the promising work so far has been in the laboratory or in animals, and none of these is an established outcome. We separate what is genuinely supported from what is still speculative, and a good deal here sits firmly in the second group. Any preparation used in a clinic is handled under sterile conditions by trained professionals, and that standard never bends.</p>

<h2>Who it suits, and what to expect</h2>
<p>People who ask us about exosome therapy tend to be curious about advanced regenerative options and want to understand the science and its limits before committing. It suits those who value a careful, informed decision over a quick answer. Your starting point is a conversation, not a procedure, where our doctor reviews your history and goals, explains the current state of the science in plain terms, and is transparent about sourcing and the emerging nature of the field. Careful assessment sets exosome therapy aside where there is active cancer, an active infection or pregnancy, among other situations, and the caution around cancer in particular is deliberate, since exosomes carry signalling that can influence how cells behave.</p>
"""

FAQS = [
    ("What is the difference between exosome therapy and stem cell therapy?",
     "The difference is what gets delivered. Stem cell therapy works with whole cells, while exosome therapy uses only the tiny signalling packets that cells release, which is why it is called cell-free. The exosomes studied in this field are often derived from stem cells, so the two are closely related."),
    ("How big are exosomes?",
     "Very small, between about thirty and a hundred and fifty nanometres across, which makes them far smaller than a red blood cell. Their size and their endosomal origin are part of what defines them and separates them from other particles a cell releases."),
    ("Is exosome therapy proven?",
     "It is an emerging area, so it is best described as promising in research and not established in practice. Much of the work so far has been in the laboratory or in animals, and our doctors are honest about what the current science does and does not show."),
    ("What areas are exosomes studied for?",
     "The areas discussed most are skin quality and rejuvenation, hair and scalp concerns, and joint or soft-tissue applications, all understood as areas of active research and not proven uses."),
    ("Is exosome therapy safe?",
     "Any preparation we discuss is handled under sterile conditions by trained professionals, and suitability is confirmed at assessment first. It is not appropriate for everyone, and screening for situations such as active cancer, infection or pregnancy is part of that."),
    ("Where do the exosomes come from?",
     "In regenerative research they are usually derived from mesenchymal stem cells. Our doctors are transparent about sourcing and about the emerging nature of the field, and explain the current position openly during your consultation."),
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
        ("services", "0094_stem_cells_content_v4"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
