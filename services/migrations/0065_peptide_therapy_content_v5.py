"""Replace the Peptide Therapy service content with the user's restructured,
narrative, prescription-and-sourcing-focused copy. This version is prose-led with
no card grid, timeline or lists, a reworked section set and a shorter (6-item) FAQ.
New meta title. Keeps the hero and inline content images. Supersedes 0057.
Hero: static/img/services/peptide-therapy-hero.webp;
inline: static/img/services/peptide-therapy-content.webp."""

from django.db import migrations

SLUG = "peptide-therapy"

SEO_TITLE = "Peptide Therapy in Dubai | Doctor-Led & Prescription-Only | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led, prescription-only peptide therapy in Dubai at Brockwell Healthcare for "
    "recovery, hormonal, metabolic and skin goals, matched to you through a proper "
    "assessment."
)
HERO_HEADING = "Peptide therapy in Dubai"
SUMMARY = (
    "A prescription-only, doctor-led peptide service for recovery, hormonal, metabolic and "
    "skin goals, matched to you through a proper assessment and prescription-grade sourcing."
)

DESCRIPTION = """
<p>A peptide is a short chain of amino acids, usually forty or fewer, and your body makes thousands of them to carry messages from one place to another. Some tell the pituitary to release growth hormone. Some signal for repair. Others help manage appetite and blood sugar. Peptide therapy borrows that natural messaging by using specific, chosen peptides for a defined goal, and at Brockwell Healthcare it is a prescription-only, doctor-led service. The important thing to understand from the outset is that peptides are not one thing. A few are fully approved medicines. Many are not, and that distinction shapes everything about how we use them.</p>

<h2>What is peptide therapy, and why the approved-versus-unapproved line matters</h2>
<p>Peptide therapy is the medical use of specific peptides to influence a particular process, whether that is tissue repair, growth-hormone release, metabolism, immunity or skin. Each peptide is matched to a receptor and a purpose, which is what makes it precise when it is done properly.</p>
<p>That precision is only half the story though, and the other half is regulatory. Some peptide medicines are fully approved and widely prescribed, and the GLP-1 drugs for diabetes and weight, semaglutide and tirzepatide, are the clearest examples, along with tesamorelin. Many others talked about in recovery and performance circles, including BPC-157 and TB-500, are not approved as standard medicines, their status is unsettled, and several sit on anti-doping prohibited lists. Knowing which group a peptide belongs to is not a detail. It changes whether it can be prescribed at all, how it must be sourced, and what it means for anyone who competes under drug testing.</p>

<h2>How peptides actually work</h2>
<p>Peptides work by fitting a specific receptor, a bit like a key cut for one lock, and that specificity is the whole point. A growth-hormone-releasing peptide prompts your own pituitary to release growth hormone in its natural, pulsing rhythm, which is a gentler idea than injecting the hormone itself. A repair peptide acts on the pathways involved in healing and inflammation. A metabolic peptide such as semaglutide works on the GLP-1 system that governs appetite and blood sugar. Because each one speaks to a particular system, a plan can be aimed narrowly at a single goal, and a doctor can sometimes combine two where the goal calls for it.</p>

<img src="/static/img/services/peptide-therapy-content.webp" alt="Doctor discussing a prescription-grade peptide therapy protocol at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>The peptides we work with</h2>
<p>Peptides are grouped by the job they are studied for. For recovery and tissue repair, the two discussed most are BPC-157, a fifteen-amino-acid compound first isolated from gastric juice and studied for tendon, gut and soft-tissue healing, and TB-500, a fragment related to thymosin beta-4 that has a hand in cell repair. The growth-hormone family prompts your own pituitary and includes CJC-1295, which mimics the natural releasing hormone, and Ipamorelin, a selective one that lifts growth hormone with little effect on stress hormones, alongside Sermorelin, Tesamorelin and the oral compound MK-677. For metabolic and weight goals the approved GLP-1 medicines semaglutide and tirzepatide lead. Beyond these, the copper peptide GHK-Cu is studied for skin and collagen, PT-141 for sexual health, and Thymosin Alpha-1 for immune support. Matching the right one to your goal is the core of the work.</p>

<h2>What peptides are studied for</h2>
<p>Because a single peptide can be pointed at a single system, what the treatment is explored for follows directly from which peptide is used. Repair peptides are researched for healing in tendon, gut and soft tissue. The growth-hormone family is studied for supporting your own pulsing release of growth hormone, which people pursue for recovery, body composition and sleep. The approved GLP-1 medicines are prescribed for appetite and blood-sugar goals. Copper peptides are studied for skin quality and collagen, and others for immune and sexual-health goals.</p>
<p>None of that is a promise. Responses differ from one person to the next, several of these compounds are not approved as standard medicines, and for a number of them the strongest evidence still comes from laboratory and animal work and not large human trials. Our doctors would sooner tell you that plainly than sell you a result the science has not earned.</p>

<h2>Who it suits, and who it does not</h2>
<p>Peptide therapy tends to suit people chasing a specific, well-defined goal, a stubborn injury that will not settle, hormonal health shifting with age, a metabolic target, or skin, immune and sleep concerns. Because each peptide is matched to one purpose, it appeals to people who want something precise for a clearly defined problem.</p>
<p>There are firm lines too. Peptide therapy is set aside in active or past cancer without oncology clearance, in hormone-sensitive conditions, and during pregnancy or breastfeeding, and it is never used in minors. For anyone who competes in tested sport, the assessment also flags any anti-doping implications, because a peptide that is perfectly reasonable for a general patient can be banned in competition.</p>

<h2>Sourcing is where the real risk lives</h2>
<p>With most treatments the main safety questions are about the procedure. With peptides, the biggest single risk is where the material comes from. Peptides bought from unregulated online sellers, often labelled as research chemicals, carry genuine dangers of contamination, wrong dosing and mislabelling, and no clinical care around them makes that safe. This is the reason we prescribe only prescription-grade peptides through a regulated pharmacy, and it is the part of peptide therapy we are least willing to compromise on. It is also why a genuine consultation, and not an online order, sits at the front of everything we do.</p>

<h2>What a peptide course involves</h2>
<p>Treatment opens with a conversation about your symptoms, history and goals, and any baseline blood work worth doing, followed by an honest view of what a given peptide can and cannot do for you. If a peptide is prescribed, it is dispensed as a prescription-grade preparation and usually given by a small subcutaneous injection, with some taken by oral, nasal or topical routes instead. From there, the work is in the monitoring. Different peptides act over very different timescales, so a repair peptide might be judged over a few weeks, a growth-hormone protocol over three to six months, and a GLP-1 medicine titrated slowly to manage appetite and side effects. Your response is checked as the protocol runs and the plan is adjusted to match it, because these compounds act on real physiological systems and deserve that attention.</p>
"""

FAQS = [
    ("Are peptides the same as steroids or SARMs?",
     "No. Anabolic steroids are synthetic hormones and SARMs act directly on hormone receptors to force a response, whereas therapeutic peptides are signalling molecules that work with the body's own pathways, for instance prompting the pituitary to release its own growth hormone. That difference in mechanism is why they are used so differently."),
    ("Which peptides are actually approved?",
     "Semaglutide, tirzepatide and tesamorelin are approved prescription medicines. Many others, including BPC-157, TB-500 and CJC-1295, are not approved as standard medicines and their regulatory status is unsettled, with several on anti-doping lists. Your doctor tells you exactly where any given peptide stands."),
    ("Do peptides affect drug testing in sport?",
     "They can, and it matters. Several peptides appear on anti-doping prohibited lists, so a compound that is fine for a general patient may be banned in tested competition. We make this explicit for any athlete before anything is prescribed."),
    ("Why is sourcing such a big deal?",
     "Because peptides from unregulated sellers risk contamination, wrong dosing and mislabelling, and that risk cannot be managed after the fact. Prescription-grade preparations from a regulated pharmacy are the single most important safety step in this treatment."),
    ("How are peptides taken?",
     "Most are given by a small subcutaneous injection, though some are oral, nasal or topical depending on the peptide. Your doctor explains the route that suits your protocol."),
    ("Is a consultation required before treatment?",
     "It is, without exception, because peptide therapy is prescription-only. The assessment confirms suitability, screens for the situations that rule it out, and builds a monitored plan around your goal."),
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
        ("services", "0064_exosome_therapy_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
