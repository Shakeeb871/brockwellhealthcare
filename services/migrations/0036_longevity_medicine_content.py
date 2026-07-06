"""Load the full Longevity Medicine content: keyword-rich H1 (full, with
tagline), SEO meta, styled rich-text sections (plan 'Covers' → card grid,
process → numbered timeline via the enhance pipeline), two clinical photos and
the FAQ set."""

from django.db import migrations

SEO_TITLE = "Longevity Medicine in Dubai | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led longevity medicine in Dubai for biological age assessment, cellular "
    "health, energy and healthy ageing. Evidence-guided, biology-first personalised plans."
)
HERO_HEADING = "Longevity Medicine in Dubai | Doctor-Led Healthy Ageing"
SUMMARY = (
    "Doctor-led longevity medicine in Dubai for biological age assessment, cellular "
    "health, energy and healthy ageing."
)

DESCRIPTION = """
<p>Longevity medicine at Brockwell Healthcare is a doctor-led clinical approach to how your body ages, built around a proper understanding of your biology. It suits patients who want to stay physically and mentally capable for longer, and who are ready to start that work before problems become harder to manage.</p>

<h2>What Is Longevity Medicine?</h2>
<p>Longevity medicine is the clinical field focused on extending the years you live in good health and function, not simply the years you live overall. It studies the biological processes that drive ageing, often called the hallmarks of ageing, including cellular energy decline, inflammation, oxidative stress, hormonal change and reduced tissue-repair capacity, and addresses them directly through assessment and targeted treatment.</p>
<p>At Brockwell Healthcare, longevity medicine in Dubai starts with understanding where your body currently stands biologically. From there, your doctor decides what is genuinely relevant to your case. This is evidence-guided support for healthy ageing, not a promise to stop the clock.</p>

<h2>How Does Longevity Medicine Work?</h2>
<p>Ageing happens at different rates in different people, and even within one person, some systems age faster than others. One person might have strong cardiovascular health but declining cellular energy. Another might have good energy but significant joint and tissue wear. Longevity medicine begins by identifying which of these processes are most active in your specific case.</p>
<p>Once that picture is clear, treatment is matched to it. That might mean supporting cellular energy where mitochondrial decline drives fatigue, easing chronic inflammation where it fuels tissue or cognitive symptoms, supporting hormonal balance where that has shifted, or supporting tissue-repair capacity in joints and soft tissue. The combination depends entirely on your assessment. The goal is honest and clear: keep your body's systems working as well as possible for as long as possible.</p>

<img src="/static/img/services/longevity-medicine-content.webp" alt="Doctor-led longevity medicine consultation at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>What a Longevity Medicine Plan Covers</h2>
<p>A longevity plan is built from several possible components, depending on what your assessment shows. Not every patient needs every element.</p>
<h3>Biological Assessment</h3>
<p>A proper clinical review of relevant blood markers, inflammatory indicators, hormonal status and functional health, giving your doctor a clear starting point before anything is recommended.</p>
<h3>Cellular Energy Support</h3>
<p>Where mitochondrial decline is contributing to fatigue or reduced stamina, targeted nutrient support, including NAD+ IV therapy, may be considered.</p>
<h3>Hormonal and Metabolic Support</h3>
<p>Hormonal shifts affect energy, body composition, sleep and mood with age. Peptide therapy and other targeted approaches may support hormonal balance where your assessment points to it.</p>
<h3>Inflammation and Recovery Support</h3>
<p>Chronic low-grade inflammation, sometimes called inflammaging, is linked to accelerated ageing across many systems. Antioxidant-focused support may help manage it where it shows up as a factor.</p>
<h3>Tissue and Joint Support</h3>
<p>The body's natural repair capacity declines with age. Regenerative approaches may be considered within a longevity plan for patients with relevant joint or soft-tissue concerns.</p>
<h3>Lifestyle Review</h3>
<p>Sleep, nutrition, movement and stress all shape the pace of ageing. Your doctor reviews these alongside any clinical treatment, so daily habits support the plan rather than work against it.</p>

<h2>Benefits of Doctor-Led Longevity Medicine</h2>
<p>Delivered within a properly individualised plan, longevity medicine may offer several benefits. Outcomes depend heavily on your starting biology, the treatments involved and how consistently you follow the plan.</p>
<p>Potential benefits include:</p>
<ul>
<li>Better energy and physical performance as cellular function gains support</li>
<li>More consistent recovery after exercise or physical demands</li>
<li>Sharper cognitive clarity as inflammation and oxidative stress are addressed</li>
<li>Improvement in hormonal symptoms, from mood and sleep to body composition, where hormonal support is relevant</li>
<li>Better-maintained joint and tissue health when support begins before significant decline</li>
<li>A clear biological baseline you and your doctor can track over time</li>
<li>A plan shaped around your individual biology</li>
</ul>
<p>Results are never guaranteed and vary widely between individuals. A clinical assessment at Brockwell decides which parts of longevity medicine in Dubai suit your situation.</p>

<h2>The Longevity Medicine Process at Brockwell Healthcare</h2>
<p>Every plan starts with a proper assessment, and your doctor recommends nothing until they have a clear picture of your biology, history and goals.</p>
<h3>Step 1: Booking</h3>
<p>Contact Brockwell Healthcare to arrange your consultation. The team matches you to the right appointment for your main concern, whether that is energy, recovery, cognitive performance or general proactive health planning.</p>
<h3>Step 2: Biological Assessment</h3>
<p>Your doctor reviews your medical history, current medications, lifestyle and goals, alongside relevant blood work and functional health markers. This step identifies which biological systems most need attention in your specific case.</p>
<h3>Step 3: Personalised Plan</h3>
<p>From the assessment, your doctor builds a plan around what your biology actually shows, whether that means one therapy or a small combination. You hear what each option involves, how many sessions you are likely to need and what a realistic outcome looks like. The cost is confirmed before anything begins.</p>
<h3>Step 4: Treatment</h3>
<p>A DHA-licensed doctor or supervised clinical team delivers each session with medical-grade equipment and sterile protocols. Whatever your plan involves, every session follows the protocol set during your assessment.</p>
<h3>Step 5: Ongoing Review</h3>
<p>Longevity medicine works best as an ongoing relationship, not a single course. Follow-up visits review your progress, repeat relevant assessments where useful and adjust the plan as your biology and goals change over time.</p>

<h2>Why Choose Brockwell Healthcare for Longevity Medicine</h2>
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
    ("How is longevity medicine different from general wellness?",
     "Longevity medicine in Dubai starts with a proper biological assessment, then matches treatment to what your specific biology shows. That means the plan looks different for every patient, depending on which systems need the most support."),
    ("What does a longevity biological assessment involve?",
     "A biological assessment may include relevant blood markers, inflammatory indicators, hormonal status and functional health screening. Together, they show your doctor where your body stands and which areas need the most attention."),
    ("Can longevity medicine help with low energy?",
     "It may support patients with age-related fatigue through treatments that target cellular energy and hormonal balance, depending on what the assessment finds. Fatigue has several possible causes, so your doctor identifies the underlying driver properly first."),
    ("Can longevity medicine support joint and tissue health?",
     "Regenerative approaches may be considered within a longevity plan where joint or soft-tissue decline shows up. Suitability depends on the specific condition and is confirmed through assessment."),
    ("What therapies might a longevity plan include?",
     "A longevity plan is built from whatever your biological assessment points to. That might mean targeted IV support for cellular energy, peptide therapy for hormonal balance, or regenerative approaches for tissue health, depending on which systems need the most support."),
    ("Is longevity medicine safe?",
     "Yes, when DHA-licensed doctors deliver it with proper screening and clinical protocols. Not every therapy suits every patient, so a thorough assessment confirms what is suitable for your health profile first."),
    ("How many sessions will I need?",
     "It depends on the therapies involved and how your body responds. Some patients notice meaningful change after a short initial course, while others benefit from an ongoing programme with regular reviews. Your doctor confirms the approach after the biological assessment."),
    ("When will I notice results?",
     "Some changes, such as energy or sleep, may show within the first few sessions. Others, such as inflammatory markers or hormonal balance, develop more gradually over weeks to months. The timeline varies considerably between individuals."),
    ("What does a longevity medicine consultation cost in Dubai?",
     "Cost depends on the assessment needed and the therapies selected. You receive clear pricing and a full estimate before any treatment begins."),
    ("Who should consider longevity medicine?",
     "It may suit anyone who wants a clearer picture of how their body is ageing, notices early signs of decline, or wants to get ahead of long-term health before problems become harder to manage."),
    ("Who should speak to a doctor before starting longevity treatments?",
     "Patients with active cancer, serious uncontrolled conditions, pregnancy without clearance, implanted electronic devices or medications that interact with specific therapies should discuss it with a doctor first. The consultation reviews all of this before anything is recommended."),
    ("Do I need a consultation before starting a longevity plan in Dubai?",
     "Yes. A proper biological assessment comes before any longevity therapy at Brockwell. It is what makes the plan clinically meaningful, so nothing begins without it."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    svc = Service.objects.filter(region="uae", slug="longevity-medicine").first()
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
        ("services", "0035_healthspan_content"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
