"""Refresh the Biological Integrative Medicine service with the user's doctor-led,
conventional-care-at-the-centre copy: reworked section set (What is / How the assessment
works / What we address [card grid] / Treatments within the programme / What to expect /
The programme process / Why patients choose) and a 10-item FAQ. Prose-led. Keeps the hero
and a single inline content image.
Hero: static/img/services/biological-integrative-medicine-hero.webp;
inline: static/img/services/biological-integrative-medicine-content.webp."""

from django.db import migrations

SLUG = "biological-integrative-medicine"

SEO_TITLE = "Biological Integrative Medicine in Dubai | Doctor-Led | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led biological integrative medicine in Dubai at Brockwell Healthcare, combining "
    "conventional care with evidence-led regenerative and supportive treatments in one "
    "coordinated plan."
)
HERO_HEADING = "Biological integrative medicine in Dubai"
SUMMARY = (
    "Doctor-led care that combines conventional medicine with evidence-led regenerative and "
    "supportive treatments in one coordinated plan."
)

DESCRIPTION = """
<p>Biological integrative medicine at Brockwell Healthcare is led by a qualified doctor and brings conventional medicine together with the clinic's regenerative and supportive treatments in one coordinated plan. Every plan begins with a consultation and proper diagnostics, and conventional medical care stays at the centre of everything we do.</p>

<h2>What is biological integrative medicine at Brockwell Healthcare?</h2>
<p>The idea behind this approach is that the body works as one connected system. Digestion affects immunity, chronic inflammation feeds into hormones, mood and recovery, and the state of your cells' energy production shapes how every organ performs. Conventional medicine is very good at diagnosing and treating specific diseases, and integrative medicine adds a second layer around it, supporting the wider system so the body heals better, tolerates treatment better and stays well for longer.</p>
<p>One thing needs saying clearly at the start. Integrative medicine here does not replace conventional diagnosis or treatment. Patients with a diagnosed condition keep their specialist, keep their medication unless a doctor properly reviews it, and get our full support in coordinating both sides. Every treatment in the integrative layer has to be justified by evidence and by your test results, and where the evidence for a particular therapy is limited, your doctor tells you that before you spend money on it.</p>
<p>Patients come to this service from a few directions. Some have a chronic condition and want their overall health supported alongside their specialist care, while others arrive after our functional medicine assessment wanting a broader treatment plan built on those findings. A third group is essentially well and wants a structured, medically supervised way to look after inflammation, gut health and cellular health as they age.</p>

<h2>How the assessment works</h2>
<p>The first appointment covers your medical history, current diagnoses and medications, digestion, sleep, energy, diet, stress load, and the exposures that come with modern city life, from processed food to disrupted sleep and low daily movement. If you are under the care of other doctors, we ask you to bring their reports, because the integrative plan has to fit around your existing treatment.</p>
<p>Testing depends on your situation. It can include inflammatory markers, gut and microbiome assessment, nutrient status, hormone panels, markers of blood sugar regulation, and organ function tests such as liver and kidney panels. Where your specialist has already run recent blood work, we use it and add only what is missing. Your doctor then reviews everything together and explains what the results mean for your plan, since the findings decide the treatment and each part of the plan is tied to something the assessment actually found.</p>

<img src="/static/img/services/biological-integrative-medicine-content.webp" alt="Doctor-led biological integrative medicine consultation and coordinated planning at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>What we address</h2>
<h3>Chronic low-grade inflammation</h3>
<p>Persistent inflammation sits underneath a wide range of modern health problems, from joint pain and skin conditions to fatigue and slow recovery. Blood markers pick it up, and the plan then works on its sources, which commonly include gut problems, visceral fat, poor sleep and untreated infections. Progress is confirmed by retesting the same markers.</p>
<h3>Gut health and the microbiome</h3>
<p>The gut affects far more than digestion. It houses a large share of the immune system, influences inflammation throughout the body, and has a documented relationship with mood and energy. We assess digestion, diet, past antibiotic use and, where indicated, the microbiome itself, and rebuild from there with dietary work and targeted treatment.</p>
<h3>Cellular energy and mitochondrial support</h3>
<p>Mitochondria produce the energy every organ runs on, and their function declines with age, poor metabolic health and chronic inflammation. The practical result is fatigue, slow recovery and reduced physical capacity. Support here starts with correcting what damages mitochondria, particularly blood sugar problems, deficiencies and sleep debt, before any supplement or therapy is added on top.</p>
<h3>Immune support</h3>
<p>Patients who catch every infection going around, or who take weeks to shake off a simple cold, often have identifiable reasons for it. Low vitamin D is the most common finding, alongside poor sleep, high stress load and gut problems. The plan corrects what testing finds, and where the pattern of infections suggests something that needs specialist immunology input, we refer.</p>
<h3>Supporting patients with chronic conditions</h3>
<p>Patients managing long-term conditions such as autoimmune disease, diabetes or cardiovascular disease can carry a heavy overall load, and their general health often gets less attention than the condition itself. Your specialist continues to lead the treatment of the condition, and we work alongside them on the parts of your health that make living with it easier, meaning nutrition, deficiencies, sleep, inflammation and physical capacity. Nothing in your existing treatment is changed without proper clinical review and coordination with your treating doctor.</p>
<h3>Healthy ageing</h3>
<p>For patients without a diagnosis who want to stay that way, this service overlaps with our longevity medicine programme. The integrative layer contributes the gut, inflammation and cellular health work, and the longevity programme adds the structured long-term tracking.</p>

<h2>Treatments within the programme</h2>
<p>The plan is built from your results, and the treatments are drawn from across the clinic. Nutritional correction and dietary work form the base of most plans. IV nutrient therapy is used where deficiencies are confirmed or absorption is poor. Peptide therapy is considered where hormonal signalling, recovery or metabolic regulation need support, always after a full work-up. Hyperbaric oxygen therapy has a role in recovery and tissue health for selected patients, and our regenerative treatments such as PRP are available where a specific application fits your situation.</p>
<p>Each of these has its own evidence base, and they are not all equal. Your doctor is open with you about which parts of your plan rest on strong evidence and which are reasonable options with evidence still developing, so you can decide with accurate information.</p>

<h2>What to expect</h2>
<p>Integrative plans work on the timescale of the systems they treat. Deficiency corrections show up in blood work and energy within weeks. Gut and inflammation work usually takes a few months to show its full effect, and the improvements tend to arrive as better energy, better sleep, easier digestion and fewer sick days before they show up as anything dramatic.</p>
<p>Your doctor sets expectations honestly at the results appointment. Plans are reviewed and adjusted as your retesting comes back, and treatments that are not producing results get removed from the plan.</p>

<h2>The programme process</h2>
<p>It starts with booking, where you contact Brockwell Healthcare to arrange your consultation and the team books you with the doctor first. At the assessment, your doctor takes a detailed history, reviews your existing diagnoses, medications and specialist reports, and selects testing for your situation. At the results and plan appointment, your doctor goes through the findings with you and builds a coordinated plan, with each treatment tied to a result and the evidence behind it explained, and costs confirmed before anything starts. During the treatment phase the plan runs, with the clinic coordinating any communication needed with your other doctors. Throughout, your progress is reviewed against how you feel and against repeat testing, and the plan is adjusted as results change.</p>

<h2>Why patients choose Brockwell Healthcare</h2>
<p>This service is run as a medical practice. A qualified doctor leads every plan, treatments have to be justified by your results, and the evidence behind each one is discussed with you honestly. We coordinate openly with your specialists, we refer when a problem is outside our scope, and full pricing is confirmed before your first session.</p>

<h2>Book an integrative medicine consultation in Dubai</h2>
<p>Book a biological integrative medicine consultation in Dubai at Brockwell Healthcare. Your doctor will review your history and results, build a plan that works alongside your existing care, and confirm the cost before anything begins.</p>
"""

FAQS = [
    ("What is the difference between this and functional medicine?",
     "They overlap, and many patients use both. Functional medicine is mainly the diagnostic side, finding the root cause of chronic or unexplained symptoms through detailed testing. Biological integrative medicine is broader on the treatment side, combining conventional care with the clinic's supportive and regenerative treatments in one plan. If you are unsure which fits your situation, the team can advise before you book."),
    ("Will I have to stop my current medication or leave my specialist?",
     "No, and we would advise against both. Your specialist and your existing treatment stay in place. Our work runs alongside them, we coordinate with your treating doctors, and no medication is ever changed without proper clinical review."),
    ("Is this alternative medicine?",
     "No. Conventional diagnosis and treatment remain the foundation. What we add are supportive treatments chosen from your test results, and your doctor is open about the strength of the evidence behind each one. Anything without a reasonable evidence base does not go in your plan."),
    ("What conditions can this help with?",
     "Common reasons patients come to us include chronic inflammation, gut problems, frequent infections, persistent fatigue, and wanting structured support for general health while managing a long-term condition. If your situation is different, ask the team whether the service fits before booking."),
    ("Can you support me during treatment for a serious illness?",
     "In coordination with your treating specialist, yes, for things such as nutrition, deficiencies and general strength. Your specialist leads your treatment, and we do not offer or suggest alternatives to it. We would also encourage caution about any clinic that does."),
    ("What does the testing involve?",
     "It depends on your situation, and recent results from your other doctors are used so you do not repeat tests unnecessarily. Typical additions include inflammatory markers, nutrient levels, gut assessment and hormone panels where your history points to them."),
    ("How long does a programme take?",
     "Most patients work with us over several months, since gut and inflammation work needs that long to show its full effect. Deficiency corrections and energy improvements usually come earlier."),
    ("Do treatments like IV therapy and peptides really work?",
     "It depends on the treatment and the situation, and we give you a straight answer for each one in your plan. IV therapy for a confirmed deficiency has a clear rationale, while some other applications have evidence that is still developing, and your doctor tells you which category each recommendation falls into."),
    ("What does the programme cost?",
     "It depends on the testing and the treatments in your plan. You get a clear cost estimate at your assessment, before anything is booked, and nothing is added without your agreement."),
    ("Do I need a referral?",
     "No. Contact the clinic directly and the team will book your assessment. Bring your specialist reports and any recent blood results, because the plan is built around them."),
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
        ("services", "0114_stress_reset_inline_image"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
