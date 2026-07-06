"""Create the Peptide Therapy sub-service (under Longevity | Healthspan) and load
its full content: keyword-rich H1 (full, with tagline), SEO meta, styled
rich-text sections ('Can Support' → card grid, process → numbered timeline via
the enhance pipeline), two clinical photos and the FAQ set."""

from django.db import migrations

SEO_TITLE = "Peptide Therapy in Dubai | Doctor-Prescribed | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-prescribed peptide therapy in Dubai for recovery, hormonal balance, metabolic "
    "and skin health. Prescription-only, medically supervised, assessment-first care."
)
HERO_HEADING = "Peptide Therapy in Dubai | Doctor-Prescribed & Medically Supervised"
NAME = "Peptide Therapy"
SLUG = "peptide-therapy"
CATEGORY_SLUG = "longevity-healthspan"
ICON = "🧬"
SUMMARY = (
    "Doctor-prescribed peptide therapy in Dubai for recovery, hormonal balance, metabolic "
    "and skin health."
)

DESCRIPTION = """
<p>Peptide therapy uses short chains of amino acids to support specific processes in the body, from tissue repair and hormonal balance to metabolism, recovery and skin health. At Brockwell Healthcare, it is a prescription-only, doctor-led treatment, tailored to each patient after a proper clinical assessment.</p>

<h2>What Is Peptide Therapy?</h2>
<p>Peptides are short chains of amino acids that act as signalling molecules, carrying instructions between cells. Your body makes many of them naturally to regulate healing, hormones, metabolism, immune function and more. Peptide therapy uses specific, targeted peptides to support these processes where they have slowed, shifted or become less efficient.</p>
<p>At Brockwell Healthcare, peptide therapy in Dubai is indication-based, meaning your doctor prescribes it for a defined clinical reason, not as a general supplement. Every plan begins with a clinical assessment and, where relevant, baseline lab work. A consultation does not automatically lead to a prescription: your doctor recommends peptide therapy only when it is clinically appropriate and safe for you.</p>

<h2>How Does Peptide Therapy Work?</h2>
<p>Peptides work by binding to specific receptors on or inside cells, which triggers a targeted biological response. Because each peptide is designed for a particular receptor and function, the effect is comparatively focused: one may signal for tissue repair, another may support the body's own growth-hormone release, and another may influence appetite or metabolic pathways.</p>
<p>That specificity is the point. Rather than acting broadly across the body, a well-chosen peptide is matched to the exact process your assessment identifies as needing support, delivered usually by subcutaneous injection within a supervised protocol. Because peptides can influence powerful systems such as hormones and cell growth, medical supervision and correct sourcing matter as much as the peptide itself.</p>

<img src="/static/img/services/peptide-therapy-content.webp" alt="Doctor administering peptide therapy at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>What Peptide Therapy Can Support</h2>
<p>Peptides fall into several therapeutic categories. Your doctor selects the right category and specific peptide around your clinical need, and only well-characterised, prescription-grade peptides are used.</p>
<h3>Recovery and Tissue Repair</h3>
<p>Repair-focused peptides, such as BPC-157, may support the healing of tendons, muscles and soft tissue and help manage inflammation, which is why they draw interest for recovery after injury or surgery.</p>
<h3>Growth Hormone Support</h3>
<p>Growth-hormone secretagogues, a group that includes GHRH analogues, may support the body's own growth-hormone release, with potential effects on body composition, recovery and sleep. These influence a powerful hormonal system and need careful supervision.</p>
<h3>Metabolic and Weight Support</h3>
<p>Certain peptides may support appetite regulation, metabolism and fat utilisation as part of a wider, medically supervised weight-management plan, alongside nutrition and lifestyle care.</p>
<h3>Skin and Hair Support</h3>
<p>Peptides such as copper peptides (GHK-Cu) may support collagen production, skin quality and scalp health within a wider aesthetic or regenerative plan.</p>
<h3>Immune and Cellular Support</h3>
<p>Some peptides may support immune modulation and cellular repair, considered within a broader wellness plan where relevant.</p>
<h3>Sleep, Recovery and Cognitive Support</h3>
<p>Selected peptides may support sleep quality, recovery and cognitive clarity, and your doctor considers them only where the assessment points to a genuine need.</p>

<h2>Benefits of Doctor-Led Peptide Therapy</h2>
<p>For suitable patients, prescribed and monitored properly, peptide therapy may offer several benefits. Responses vary widely with the peptide, the individual and the underlying goal, and many peptides act gradually over months rather than days.</p>
<p>Potential benefits include:</p>
<ul>
<li>Support for tissue repair and recovery after injury, surgery or physical strain</li>
<li>Support for the body's own hormonal signalling, including growth-hormone pathways</li>
<li>Help with appetite regulation and metabolism within a supervised weight plan</li>
<li>Support for skin quality, collagen and scalp health in aesthetic protocols</li>
<li>Support for sleep, recovery and cognitive clarity where relevant</li>
<li>A targeted, receptor-specific approach matched to a defined clinical need</li>
</ul>
<p>Results are never guaranteed, and several peptides are not yet approved as standard medicines for these uses. A clinical assessment at Brockwell decides whether peptide therapy in Dubai is appropriate for you.</p>

<h2>The Peptide Therapy Process at Brockwell Healthcare</h2>
<p>Every plan follows a structured clinical process, and your doctor prescribes nothing until a proper assessment confirms peptide therapy is appropriate.</p>
<h3>Step 1: Booking</h3>
<p>Contact Brockwell Healthcare to arrange your consultation. The team matches you to the right appointment for your main concern, whether that is recovery, hormonal balance, metabolic health, skin or general wellness.</p>
<h3>Step 2: Consultation and Assessment</h3>
<p>Your doctor reviews your symptoms, medical history, current medications, goals and, where relevant, baseline lab work. This step confirms whether peptide therapy suits you, which peptide category fits and what the protocol should look like, and your doctor screens for contraindications such as active cancer, pregnancy and hormone-sensitive conditions.</p>
<h3>Step 3: Prescription and Protocol</h3>
<p>If peptide therapy is appropriate, your doctor prescribes a specific, prescription-grade peptide sourced through a regulated pharmacy, and sets out the protocol, expected timeline, monitoring plan and realistic outcomes. You hear clearly what the treatment can and cannot do for your situation.</p>
<h3>Step 4: Administration and Monitoring</h3>
<p>Your protocol is delivered under medical guidance, usually by subcutaneous injection, with instructions provided by the clinical team. Your doctor monitors your response and adjusts, pauses or stops the protocol as needed.</p>
<h3>Step 5: Review and Follow-Up</h3>
<p>Follow-up visits review your progress, repeat relevant labs where useful and refine the plan around how you respond. Because many peptides act gradually, your doctor reviews outcomes over the course of the protocol rather than after a single dose.</p>

<h2>Is Peptide Therapy Legal in the UAE?</h2>
<p>Peptide therapy is legal in the UAE when a licensed doctor prescribes it and administers or supervises it within a regulated clinical setting. Many peptides are classified as prescription-only, and importing them without the proper approvals is not permitted.</p>
<p>This is why sourcing matters. Peptides bought from online vendors are often mislabelled, under-dosed or contaminated, with no quality assurance. At Brockwell, every peptide is prescription-grade and sourced through a regulated pharmacy, prescribed and monitored by a DHA-licensed doctor. Competitive athletes should also note that many peptides are prohibited in sport under anti-doping rules, so anyone subject to testing should confirm the status of any peptide with their doctor first.</p>
"""

FAQS = [
    ("What can peptide therapy help with?",
     "Peptide therapy in Dubai may support tissue repair and recovery, hormonal balance, metabolic and weight goals, skin and hair health, immune function and sleep, depending on the peptide and your assessment. It is prescribed for a specific clinical reason, not as a general supplement."),
    ("Is peptide therapy legal and safe in the UAE?",
     "Yes, when a licensed doctor prescribes and supervises it with prescription-grade peptides sourced through a regulated pharmacy. It does not suit patients with active cancer, hormone-sensitive conditions or pregnancy, so a thorough assessment confirms suitability first, and several peptides are not approved as standard medicines for these uses."),
    ("Do I need a prescription for peptide therapy?",
     "Yes. Peptide therapy at Brockwell is prescription-only. A consultation does not automatically lead to a prescription; your doctor recommends it only when a proper assessment confirms it is appropriate and safe for you."),
    ("Are peptides bought online safe?",
     "No. Peptides from unregulated online vendors are frequently mislabelled, under-dosed or contaminated, with no quality assurance, and importing prescription peptides without approval is not permitted in the UAE. Prescription-grade, pharmacy-sourced peptides under medical supervision are the safe route."),
    ("Can athletes use peptide therapy?",
     "Many peptides are prohibited in competitive sport under anti-doping rules. Any athlete subject to testing should confirm the status of a specific peptide with their doctor before starting, since a prohibited substance can affect eligibility."),
    ("How is peptide therapy given?",
     "Most peptides are given by small subcutaneous injection within a supervised protocol. Your doctor and clinical team explain the method, schedule and monitoring at the start of treatment."),
    ("Is it painful?",
     "Subcutaneous injections use a very fine needle and cause only mild discomfort for most patients. Any site sensitivity is usually minor and short-lived."),
    ("How long until I notice results?",
     "It varies by peptide. Repair-focused peptides may show effects on inflammation within weeks, while growth-hormone-related protocols often take three to six months for meaningful body-composition change. Your doctor sets realistic timelines at consultation and reviews them at each follow-up."),
    ("How long does treatment last?",
     "Peptide protocols are usually time-limited and reviewed regularly. Some run for a defined course, others continue with monitoring, depending on the goal and your response. Your doctor confirms the plan and reviews it at follow-up."),
    ("Can peptide therapy be combined with other treatments?",
     "Yes. Peptide therapy may sit alongside other regenerative and wellness treatments at Brockwell, including IV therapy, PRP and lifestyle support, where clinically appropriate. Your doctor advises on the right combination."),
    ("What does peptide therapy cost in Dubai?",
     "Cost depends on the peptide, the protocol and the monitoring involved. You receive clear pricing before anything is prescribed, and no protocol starts without a full discussion of cost."),
    ("Who should avoid peptide therapy?",
     "Peptide therapy does not suit patients with active or past cancer without oncology clearance, hormone-sensitive conditions, pregnancy or breastfeeding, or serious uncontrolled illness. Minors should not use it. The consultation reviews all of this first."),
    ("Do I need a consultation before peptide therapy in Dubai?",
     "Yes. A clinical assessment, and often baseline labs, come before any peptide therapy at Brockwell. It confirms suitability, screens for contraindications and lets your doctor build a safe, prescription-based plan, so nothing begins without it."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    cat = ServiceCategory.objects.filter(region="uae", slug=CATEGORY_SLUG).first()
    if not cat:
        return

    last = cat.services.filter(parent__isnull=True).order_by("-order").first()
    next_order = (last.order + 1) if last else 0

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
        ("services", "0043_advanced_diagnostics_content"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, remove_content)]
