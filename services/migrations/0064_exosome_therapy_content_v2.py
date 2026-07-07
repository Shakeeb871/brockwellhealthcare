"""Update the existing Exosome Therapy service with the user's revised, education-first
narrative copy. This version is prose-led: only the 'What exosome therapy is explored
for' section carries a list; the remaining sections (including 'Your patient journey'
and 'Why choose') are single paragraphs, with no card grid or timeline. Keeps the hero
and inline content images. Supersedes the previous exosome content.
Hero: static/img/services/exosome-therapy-hero.webp;
inline: static/img/services/exosome-therapy-content.webp."""

from django.db import migrations

SLUG = "exosome-therapy"

SEO_TITLE = "Exosome Therapy in Dubai | Regenerative Medicine | Brockwell Healthcare"
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
<p>Exosomes are among the smallest messengers the body makes. Each one is a tiny bubble of membrane, somewhere between thirty and a hundred and fifty nanometres across, which is far smaller than the cells that release them. Cells use these bubbles to send instructions to one another, and exosome therapy is built on that idea of cellular post. It is one of the newest and least settled corners of regenerative medicine, and our doctors at Brockwell Healthcare treat it exactly that way. We explain the biology, we are honest about how early the evidence still is, and we help you understand where it might fit before anything is decided.</p>

<h2>What is exosome therapy?</h2>
<p>An exosome is a type of extracellular vesicle, which simply means a small package that a cell releases into its surroundings. What sets exosomes apart is where they are made. They begin inside the cell, when part of an endosome buds inward to form a structure called a multivesicular body, which then travels to the cell surface and releases its little vesicles outward. That endosomal origin is what distinguishes true exosomes from microvesicles, which bud straight off the outer membrane, and from the debris shed by dying cells.</p>
<p>Inside each exosome is a cargo of proteins, lipids, messenger RNA and short strands called microRNA, and sometimes fragments of DNA. On the outside they carry recognisable markers, in particular the tetraspanin proteins CD9, CD63 and CD81, along with others such as Alix and TSG101. Because all of that signalling material arrives without a whole cell attached, the approach is described as cell-free, and that single feature is a large part of why it interests researchers.</p>

<h2>How does exosome therapy work?</h2>
<p>The whole idea rests on cell communication, a process known as paracrine signalling. When a cell releases exosomes, nearby cells can take them up and read their cargo, and that cargo can nudge how those cells behave. The microRNA is a particularly interesting part, because a single short strand can quietly turn the volume up or down on how a cell reads its own genes. This is the messaging that exosome therapy hopes to borrow.</p>
<p>There is an honest point to make here, and we make it early. This is an area of active research, not settled medicine, and much of the promising work so far has been in the laboratory or in animals. The exosomes studied in regenerative medicine are usually derived from mesenchymal stem cells, and they are of interest partly because they carry a similar signalling message to the cells themselves while being far simpler to handle. That is a reasonable scientific rationale, and it is still a long way from proof. Any preparation used in a clinic is handled under sterile conditions by trained professionals, and that standard never bends.</p>

<img src="/static/img/services/exosome-therapy-content.webp" alt="Doctor explaining the emerging science of exosome therapy at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>What Exosome Therapy Is Explored For</h2>
<p>The areas discussed most often in connection with exosomes are skin quality and rejuvenation, hair and scalp concerns, and joint or soft-tissue applications. These are best understood as directions of research and areas of interest, not settled or proven uses, and our team is upfront about that difference.</p>
<p>Read as questions the science is still working on, these are the areas under study:</p>
<ul>
<li>skin quality, tone and the visible signs of ageing</li>
<li>hair and scalp concerns</li>
<li>joint and soft-tissue support within wider regenerative research</li>
<li>a cell-free option studied alongside cell-based methods, since it avoids handling whole cells</li>
</ul>
<p>None of these is an established outcome. Our doctors will always separate what is genuinely supported from what is still speculative, and there is a good deal that sits firmly in the second group.</p>

<h2>Who is exosome therapy for?</h2>
<p>The people who ask us about exosome therapy tend to be curious about advanced regenerative options and want to understand the science and its limits before committing to anything. It suits those who value a careful, informed decision over a quick answer, and who are comfortable with a field that is genuinely still taking shape.</p>
<p>Careful assessment always comes first. Our doctor reviews your history and goals and sets exosome therapy aside where there is active cancer, an active infection or pregnancy, among other situations that make it unsuitable. The caution around cancer in particular is deliberate, because exosomes are known to carry signalling that can influence cell behaviour, and that is not something to introduce lightly into the wrong setting.</p>

<h2>What to expect from exosome therapy in Dubai</h2>
<p>Your starting point with us is a conversation, not a procedure. Our doctor reviews your history and goals, explains the current state of the science in plain terms, and is transparent about where the preparations come from and how early the field still is.</p>
<p>The aim of that first meeting is genuinely to inform. You leave with a clear picture of what is known, what is still uncertain, and whether looking into the option any further makes sense for you. There is no pressure to proceed, and honestly, for many people the responsible conclusion is to wait and watch the evidence develop, which is a perfectly good outcome from an honest consultation.</p>

<h2>Exosome therapy recovery timeline and what to expect over time</h2>
<p>We put real weight on honest expectations here, precisely because this is such an early field. Responses differ from one person to the next, regenerative processes are slow by nature, and this is never presented as a quick fix.</p>
<p>Any conversation about timelines therefore begins with uncertainty, openly acknowledged. Where a plan involves other, better-established regenerative treatments alongside it, our doctor sets out what to expect from each of those, and keeps checking in as things go. The guiding principle stays the same throughout, which is that you always know where the settled science ends and the research begins.</p>

<h2>Tailored exosome therapy programmes for your lifestyle</h2>
<p>Regenerative approaches work best as one thread in a wider picture, so we shape any discussion around your goals and your daily life. For people focused on skin and appearance, exosomes are considered alongside overall skin health and a broader aesthetic plan, not treated as a shortcut.</p>
<p>For those thinking about joints, tissue or general wellbeing, the conversation sits alongside movement, recovery and the rest of your health. In every case, our team is clear about how an emerging option would fit with the more established parts of your care, so the whole plan stays grounded in what actually works.</p>

<h2>Why consider exosome therapy?</h2>
<p>People look into exosome therapy for understandable reasons, usually a genuine curiosity about newer, cell-free regenerative science and a wish to understand every advanced option before choosing a direction. For the right person, simply having that knowledge is worth the conversation.</p>
<p>The honest counterweight is important. This is an emerging area, the evidence is still forming, individual responses vary, and it should always sit within a wider, well-established plan. Our doctors talk all of this through openly, because with a field this new, a clear-eyed decision is the only responsible one.</p>

<h2>Your patient journey</h2>
<p>The path here is deliberately unhurried. It begins with a consultation, where our doctor reviews your history and goals and explains the current science in plain terms. From there we talk through the options honestly, separating what is genuinely supported from what is still under research, so your decision rests on a clear picture. If anything proceeds, any preparation is handled under sterile conditions by trained professionals. And throughout, we keep reviewing and stay transparent, so you always understand where the settled science ends.</p>

<h2>Why choose Brockwell Healthcare for exosome therapy</h2>
<p>A few principles shape how we approach this. Our doctors lead every conversation and put education first, because a field this new deserves honesty over enthusiasm. We are transparent about where preparations come from and about the emerging state of the science, and we never present research as if it were proof. We confirm suitability through a proper assessment first, including screening for the situations that rule it out. And we only ever discuss exosomes within a wider, well-established plan, with your questions answered plainly before anything is decided.</p>
"""

FAQS = [
    ("What is the difference between exosome therapy and stem cell therapy?",
     "The difference is what gets delivered. Stem cell therapy works with whole cells, while exosome therapy uses only the tiny signalling packets that cells release, which is why it is called cell-free. Interestingly, the exosomes studied in this field are often derived from stem cells, so the two are closely related, and our doctor explains how each is understood at present."),
    ("How big are exosomes?",
     "Very small, between about thirty and a hundred and fifty nanometres across, which makes them far smaller than a red blood cell. Their size and their endosomal origin are part of what defines them and separates them from other particles a cell releases."),
    ("Is exosome therapy proven?",
     "It is an emerging area, so it is best described as promising in research and not established in practice. Much of the work so far has been in the laboratory or in animals, and our doctors are honest about what the current science does and does not show."),
    ("What areas are exosomes studied for?",
     "The areas discussed most often are skin quality and rejuvenation, hair and scalp concerns, and joint or soft-tissue applications, all understood as areas of active research and not proven uses."),
    ("Why do you take an education-first approach?",
     "Because this is such a new field, an informed decision matters more than a fast one. We would rather you fully understood the science, the uncertainty and the limits before considering anything, and that is how every conversation runs."),
    ("Is exosome therapy safe?",
     "Any preparation we discuss is handled under sterile conditions by trained professionals, and suitability is confirmed at assessment first. It is not appropriate for everyone, and screening for situations such as active cancer, infection or pregnancy is part of that, partly because exosomes carry signalling that can influence how cells behave."),
    ("Where do the exosomes come from?",
     "In regenerative research they are usually derived from mesenchymal stem cells. Our doctors are transparent about sourcing and about the emerging nature of the field, and they explain the current position openly during your consultation."),
    ("When might I see results?",
     "Regenerative processes are gradual and responses vary widely, and because this is an early field, honest uncertainty is part of the conversation. Our doctor keeps expectations realistic instead of promising a timeline."),
    ("How much does exosome therapy cost in Dubai?",
     "The cost depends on the plan discussed and any established treatments considered alongside it, and we explain the details clearly before anything is decided."),
    ("Do I need a consultation first?",
     "You do. A proper assessment confirms suitability, screens for the situations that rule it out, and gives you an honest picture of the science, so it always comes first."),
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
    svc.benefits = ""  # benefits are a styled section inside the content above
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
        ("services", "0063_stem_cells_content_v3"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
