"""Refresh the Functional Medicine service with the user's doctor-led, root-cause copy:
reworked section set (What is / How the assessment works / Conditions we assess and treat
[card grid] / Regenerative approaches / What proper assessment changes / The consultation
process / Why patients choose) and a 9-item FAQ. Prose-led. Keeps the hero and a single
inline content image.
Hero: static/img/services/functional-medicine-hero.webp;
inline: static/img/services/functional-medicine-content.webp."""

from django.db import migrations

SLUG = "functional-medicine"

SEO_TITLE = "Functional Medicine in Dubai | Root-Cause Doctor-Led Care | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led functional medicine in Dubai at Brockwell Healthcare for chronic fatigue, "
    "gut, thyroid, hormonal and metabolic problems. Longer consultations, proper testing, "
    "honest plans."
)
HERO_HEADING = "Functional medicine in Dubai"
SUMMARY = (
    "Doctor-led, root-cause care for chronic fatigue, gut, thyroid, hormonal and metabolic "
    "problems, with longer consultations, proper testing and honest plans."
)

DESCRIPTION = """
<p>Functional medicine at Brockwell Healthcare is for people whose health problems have gone on too long without a proper answer. Consultations are led by a qualified doctor and run longer than a standard appointment, because these cases need the extra time.</p>

<h2>What is functional medicine at Brockwell Healthcare?</h2>
<p>Most people who book a functional medicine consultation in Dubai with us arrive with a similar history. The symptoms have been there for months, sometimes years. They have already seen two or three doctors. The blood tests came back normal, and at some point someone suggested it might be stress.</p>
<p>Feeling unwell with normal test results does not mean nothing is wrong. It usually means the standard panel did not measure the right things. Standard tests screen for disease, and there is nothing in a basic panel that explains long-term fatigue, brain fog or bloating, which is most of what ends up in our clinic. So we look at the systems underneath the symptoms, meaning digestion, hormones, thyroid function, blood sugar control, inflammation and nutrient status. A problem in one of them rarely stays contained there, which is why a single underlying issue can show up as several symptoms that look unrelated.</p>

<h2>How the assessment works</h2>
<p>The first appointment is built around your history. We go through the timeline of your symptoms in detail, because the timeline often holds the answer. A problem that began after a stomach infection points in a different direction than one that began during a brutal year at work. We also cover diet, sleep, digestion, medications, supplements, family history and everything you have already tried.</p>
<p>Testing comes second. Depending on what the history shows, we may run full thyroid function with antibodies, hormone panels, markers for insulin resistance and inflammation, and nutrient levels such as vitamin D, B12, iron and magnesium. Gut testing and autoimmune screening are added when there is a reason for them. We do not run every test on every patient, and we explain why each test is being ordered before you pay for it. When the results come back, we read them against your symptoms. A vitamin D level of 22 ng/mL counts as acceptable on many lab reports, but in someone with fatigue, low mood and an infection every other month, it is a finding worth treating.</p>

<img src="/static/img/services/functional-medicine-content.webp" alt="Extended, doctor-led functional medicine consultation and testing at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>Conditions we assess and treat</h2>
<h3>Chronic fatigue and low energy</h3>
<p>Take a typical case. Tired for two years, sleeping eight hours, blood tests "fine", coffee intake climbing. When we test properly, we usually find something. Thyroid dysfunction, low iron or vitamin D, unstable blood sugar, a disrupted cortisol rhythm and low-grade inflammation are the common culprits, and often two or three are present together.</p>
<h3>Gut and digestive health</h3>
<p>Bloating, irregular bowels, reflux and food reactions that have never had a clear diagnosis. Gut problems also cause trouble far from the gut, in skin, mood, energy and immunity. We look at digestion itself and at what has been disturbing it, including old courses of antibiotics, diet, stress and possible bacterial overgrowth.</p>
<h3>Hormonal imbalance</h3>
<p>Weight change, mood swings, poor sleep and low libido can all have a hormonal basis, along with irregular cycles in women and falling drive in men. Hormonal symptoms build slowly, which is why they get blamed on age or lifestyle for years before anyone tests properly. We run the panels relevant to your situation and read them against your symptoms.</p>
<h3>Thyroid disorders</h3>
<p>A large share of our thyroid patients arrive having been told their thyroid is fine, on the basis of a single TSH test. TSH alone misses early autoimmune thyroid disease, sometimes for years. We test free T4, free T3 and thyroid antibodies together, which gives a very different picture.</p>
<h3>Metabolic health and insulin resistance</h3>
<p>Insulin resistance develops quietly for a decade or more before it becomes diabetes. Weight collecting around the middle, energy crashes after meals and constant sugar cravings are the early signs. Caught at this stage, it responds well to a structured plan built on diet, training and targeted treatment where needed.</p>
<h3>Autoimmune and inflammatory conditions</h3>
<p>If you already have an autoimmune diagnosis, we work alongside your specialist on the factors that influence how often you flare, such as gut health, vitamin D, sleep and stress. If you have inflammatory symptoms and no diagnosis yet, the assessment helps establish what is driving the inflammation, and we refer on whenever specialist input is needed.</p>
<h3>Stress, sleep and burnout</h3>
<p>Long-term stress does measurable damage. The cortisol rhythm flattens out and blood sugar control slips. Sleep gets lighter, and people start catching every bug going around the office. Patients usually describe it as being wired and tired at the same time. We measure what the stress load has actually done, then work on repairing it.</p>
<h3>Skin, hair and unexplained symptoms</h3>
<p>Persistent skin problems, thinning hair, joint aches and recurring infections sometimes have internal drivers. When the creams and the external treatments have not worked, we check what is happening underneath.</p>

<h2>Regenerative approaches in functional medicine</h2>
<p>Brockwell Healthcare works extensively in regenerative medicine, and some of those treatments fit naturally into functional medicine plans. Peptide therapy can support hormonal signalling, sleep quality and recovery, and we only consider it after a full work-up. IV nutrient therapy is used where testing has confirmed a deficiency or where gut absorption is compromised, and we only recommend it when the blood work shows a reason for it. Patients thinking longer term can extend their plan into our structured longevity medicine programme, which manages hormonal, metabolic and regenerative support together over time.</p>

<h2>What proper assessment changes</h2>
<p>The main difference is in what gets found. A thyroid problem invisible on TSH shows up on a full panel. A patient treated for two years for low mood turns out to have iron deficiency and a flattened cortisol curve. Insulin resistance is caught while diet and training can still turn it around. Symptoms that were being managed separately by different doctors turn out to have the same cause.</p>
<p>Results depend on the condition, how long it has been there and how you respond. We tell you before treatment starts what a realistic outcome looks like, and we are upfront that this kind of work takes time.</p>

<h2>The consultation process</h2>
<p>It starts with booking, where the team points you to the right appointment for your concern. The first consultation is an extended one, covering your symptoms, their timeline and the systems likely involved, and it helps to bring old test results if you have them, since they are genuinely useful. Testing comes next, selected for your case and explained before it is ordered. At the results appointment we go through every finding with you and build the plan from the results, usually combining treatment with specific changes to diet, sleep or stress load, with costs confirmed before anything starts. Then, because chronic problems improve in stages, follow-up reviews your progress, repeats tests where needed and adjusts as you go.</p>

<h2>Why patients choose Brockwell Healthcare</h2>
<p>Functional medicine has a mixed reputation, and some of it is earned. Our answer to that is to keep the practice clinical. Consultations are with a qualified doctor. Testing uses recognised laboratory markers, and each test has to be justified by your history before we order it. If the evidence for something is thin, we say so, and we refer to a specialist whenever a case needs one. Regenerative treatments such as peptide therapy and IV nutrient support are available in-house when your results support them, and full pricing is confirmed before your first session.</p>

<h2>Book a functional medicine consultation in Dubai</h2>
<p>Book a functional medicine consultation in Dubai at Brockwell Healthcare. We will take your history properly and only test what needs testing, and the cost is confirmed before anything begins.</p>
"""

FAQS = [
    ("How is this different from a normal doctor's appointment?",
     "Mainly time and depth. The first consultation is much longer, the history goes further back, and testing looks at how your body's systems are functioning instead of only screening for disease."),
    ("Is functional medicine evidence-based?",
     "Yes, the way we practise it. We stick to recognised lab markers and established treatments, and we are honest about where the evidence is strong and where it is thin. Some clinics in this field over-promise, and when a case needs a specialist we refer it on instead of holding onto it."),
    ("My blood tests were normal. Is there any point testing again?",
     "Usually, yes. Standard panels screen for disease, and a result can sit inside the reference range while still being far from right for you. A fuller panel read against your symptoms often explains what the basic screen missed."),
    ("What conditions do you see most?",
     "Chronic fatigue, gut problems, hormonal imbalance, thyroid disorders, insulin resistance, inflammatory symptoms and burnout. If you are not sure your situation fits, ask the team before booking."),
    ("How long until I feel better?",
     "It depends what we find. Correcting a deficiency can change how you feel within weeks. A problem that took five years to build usually takes months to unwind. You get a realistic timeline at the results appointment."),
    ("Will I end up on a shelf full of supplements?",
     "No. Anything we recommend has to be justified by your results, and we review it at follow-up, so you are not left on things indefinitely."),
    ("Can this work alongside my existing specialist or medications?",
     "Yes. We coordinate with your existing care and never stop or change a medication without proper clinical review."),
    ("What does it cost?",
     "It depends on the testing and treatment involved. You get a clear estimate before anything begins, and nothing is added without your agreement."),
    ("Do I need a referral?",
     "No. Contact the clinic directly and the team will book you in and tell you what to bring."),
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
        ("services", "0106_mens_sexual_health_content"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
