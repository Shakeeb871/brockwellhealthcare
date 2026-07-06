"""Load the full Healthspan content: keyword-rich H1 (full, with tagline), SEO
meta, styled rich-text sections (assessment 'Covers' → card grid, process →
numbered timeline via the enhance pipeline), two clinical photos and the FAQ
set."""

from django.db import migrations

SEO_TITLE = "Healthspan in Dubai | Doctor-Led Healthy Ageing | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led healthspan medicine in Dubai for biological age assessment, energy, "
    "recovery and healthy ageing. Evidence-guided, biology-first personalised plans."
)
HERO_HEADING = "Healthspan in Dubai | Doctor-Led Healthy Ageing Medicine"
SUMMARY = (
    "Doctor-led healthspan medicine in Dubai for biological age assessment, energy, "
    "recovery and healthy ageing."
)

DESCRIPTION = """
<p>Healthspan medicine at Brockwell Healthcare is a doctor-led approach focused on the number of years you live in good health, not just the number of years you live. It suits patients who want to get ahead of how they age, before function starts to decline.</p>

<h2>What Is Healthspan?</h2>
<p>Healthspan is the share of your life spent in good physical and mental health, free from significant disease or functional decline. It differs from lifespan, which only measures how long you live. Two people can reach the same age with very different healthspans: one keeps strength, clarity and independence well into later life, the other spends years managing chronic conditions.</p>
<p>At Brockwell Healthcare, we build healthspan medicine in Dubai around understanding where your body stands biologically and addressing the specific factors ageing it faster than they need to. Every plan starts with a proper assessment, and your doctor recommends nothing without first understanding your individual biology. This is evidence-guided support for healthy ageing, not a promise to stop the clock.</p>

<h2>How Does Healthspan Medicine Work?</h2>
<p>Ageing is not one process. It is driven by several biological factors, often called the hallmarks of ageing, including declining cellular energy, accumulated oxidative stress, chronic low-grade inflammation (sometimes called inflammaging), hormonal changes and a reduced capacity for tissue repair. These do not progress at the same rate in everyone, which is why two people of the same age can feel and function very differently.</p>
<p>Healthspan medicine identifies which of these factors are most active in your case, through proper assessment, then addresses them with targeted clinical support. That might mean supporting cellular energy with NAD+ therapy, easing oxidative load with antioxidant IV protocols, supporting tissue repair with regenerative approaches, or addressing hormonal and metabolic changes with peptide therapy. The combination depends entirely on what your assessment shows.</p>

<img src="/static/img/services/healthspan-content.webp" alt="An active couple maintaining their healthspan through healthy ageing at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>What a Healthspan Assessment Covers</h2>
<p>A healthspan assessment is not one test. It is a clinical review built from several parts, depending on what your symptoms and goals point to.</p>
<h3>Biological Age and Functional Review</h3>
<p>Your doctor reviews relevant blood markers, inflammatory indicators, hormonal status and functional health to build a picture of where your body stands biologically against your chronological age.</p>
<h3>Cellular Energy Support</h3>
<p>Mitochondrial decline is one of the most consistent drivers of age-related fatigue. Targeted nutrient support, including NAD+ IV therapy, may help support cellular energy production where the assessment points to it.</p>
<h3>Hormonal and Metabolic Review</h3>
<p>Hormonal shifts affect energy, body composition, sleep and mood as we age. Peptide therapy and other targeted approaches may support hormonal balance where your assessment indicates it is relevant.</p>
<h3>Inflammation and Recovery Support</h3>
<p>Chronic low-grade inflammation speeds up ageing across the body. Antioxidant support and recovery-focused therapies may help manage it where appropriate.</p>
<h3>Tissue and Joint Health</h3>
<p>The body's repair capacity fades with age. Regenerative approaches may be considered within a wider healthspan plan for patients with joint or soft-tissue concerns.</p>
<h3>Lifestyle Review</h3>
<p>Sleep, nutrition, movement and stress all shape how you age. Your doctor reviews these alongside any clinical treatment, so the plan addresses daily habits as well as biology.</p>

<h2>Benefits of Doctor-Led Healthspan Medicine</h2>
<p>Delivered within a properly structured, individualised plan, healthspan medicine may offer several benefits. Outcomes depend on your starting biology, the treatments involved and how consistently you follow the plan.</p>
<p>Potential benefits include:</p>
<ul>
<li>Better energy and stamina as cellular function gains support</li>
<li>More consistent physical recovery after exercise or exertion</li>
<li>Sharper cognitive clarity as inflammation and oxidative stress are addressed</li>
<li>Better sleep once hormonal and recovery factors are managed</li>
<li>Better-maintained joint and tissue health when support starts before significant decline</li>
<li>A clear picture of your biological age, giving you and your doctor a measurable baseline</li>
<li>A plan shaped around your individual biology</li>
</ul>
<p>Results are never guaranteed and vary widely between individuals. A proper clinical assessment at Brockwell decides which parts of healthspan medicine in Dubai suit your situation.</p>

<h2>The Healthspan Assessment Process at Brockwell Healthcare</h2>
<p>Every plan starts with a proper clinical review, and your doctor recommends nothing until they have a clear picture of your biology, history and goals.</p>
<h3>Step 1: Booking</h3>
<p>Contact Brockwell Healthcare to arrange your consultation. The team matches you to the right appointment for your main concern, whether that is energy, recovery, physical performance or general proactive health planning.</p>
<h3>Step 2: Assessment</h3>
<p>Your doctor reviews your medical history, current medications, lifestyle and goals, alongside relevant blood work and functional health markers. This is the step that makes the plan precise and meaningful, identifying which biological systems most need support in your case.</p>
<h3>Step 3: Personalised Plan</h3>
<p>From the assessment, your doctor builds a plan around what your biology actually shows, whether that means one therapy or a small combination. You hear what each option involves, how many sessions you are likely to need and what a realistic outcome looks like. The cost is confirmed before anything begins.</p>
<h3>Step 4: Treatment</h3>
<p>A DHA-licensed doctor or supervised clinical team delivers each session with medical-grade equipment and sterile protocols. Whatever your plan involves, every session follows the protocol set during your assessment.</p>
<h3>Step 5: Ongoing Review</h3>
<p>Healthspan medicine works best as an ongoing relationship, not a single course. Follow-up visits review your progress, repeat relevant assessments where useful and adjust the plan as your biology and goals evolve.</p>

<h2>Why Choose Brockwell Healthcare for Healthspan Medicine</h2>
<ul>
<li>A DHA-licensed doctor builds every plan around a proper biological assessment.</li>
<li>Treatment is chosen around what your specific biology shows.</li>
<li>A contraindication screen comes before any treatment session.</li>
<li>Realistic outcomes are discussed honestly, including the limits of what any single treatment can achieve.</li>
<li>Follow-up reviews track your progress and adjust the plan over time.</li>
<li>The focus stays on evidence-guided healthy ageing, not hype.</li>
<li>Upfront pricing is confirmed before your first session, with no surprises.</li>
</ul>
"""

FAQS = [
    ("How is a healthspan assessment different from a general check-up?",
     "A healthspan assessment in Dubai looks specifically at the biological drivers of ageing, including cellular energy, inflammation, hormonal balance and tissue-repair capacity. The goal is to spot which systems are ageing faster than they should and address them directly."),
    ("What does a biological age review involve?",
     "A biological age review may include relevant blood markers, inflammatory indicators, hormonal status and functional health assessment. Together, they give your doctor a picture of where your body stands biologically against your chronological age."),
    ("Can healthspan medicine help with low energy?",
     "It may support patients with age-related fatigue through treatments that target cellular energy, hormonal balance and recovery. Your doctor assesses the cause of fatigue properly first, since it can stem from several different biological factors."),
    ("Can healthspan medicine support cognitive function?",
     "Cognitive clarity may improve when the contributors, such as inflammation, oxidative stress and poor sleep, are addressed within a structured healthspan plan. Results vary considerably with the individual and what is actually driving the symptoms."),
    ("What therapies might a healthspan plan include?",
     "A healthspan plan is built from whatever your biological assessment points to. That might mean targeted IV support for cellular energy, peptide therapy for hormonal balance, or regenerative approaches for joint and tissue health, depending on which systems need the most support."),
    ("Is doctor-led healthspan medicine safe?",
     "Yes, when DHA-licensed doctors deliver it with proper screening and clinical protocols. Not every therapy suits every patient, so a thorough assessment confirms what is suitable for your health profile first."),
    ("How many sessions will I need?",
     "It depends on the therapies involved and how your body responds. Some patients notice meaningful change after a short initial course, while others benefit from an ongoing programme with regular reviews. Your doctor confirms the approach after the biological assessment."),
    ("When will I notice results?",
     "Some changes, such as energy or sleep, may show within the first few sessions. Others, such as inflammatory markers or hormonal balance, develop more gradually over weeks to months. The timeline varies considerably between individuals."),
    ("What does a healthspan consultation cost in Dubai?",
     "Cost depends on the assessment needed and the therapies selected. You receive clear pricing and a full estimate before any treatment begins."),
    ("Who should consider a healthspan assessment?",
     "It may suit anyone who wants a clearer picture of how their body is functioning, notices early signs of decline, or wants to get ahead of long-term health before problems become harder to manage."),
    ("Who should speak to a doctor before starting healthspan treatments?",
     "Patients with active cancer, serious uncontrolled conditions, pregnancy without clearance, implanted electronic devices or medications that interact with specific therapies should discuss it with a doctor first. The consultation reviews all of this before anything is recommended."),
    ("Do I need a consultation before starting a healthspan plan in Dubai?",
     "Yes. A proper biological assessment comes before any healthspan therapy at Brockwell. It is what makes the plan clinically meaningful, so nothing begins without it."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    svc = Service.objects.filter(region="uae", slug="healthspan").first()
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
        ("services", "0034_exosome_therapy_content"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
