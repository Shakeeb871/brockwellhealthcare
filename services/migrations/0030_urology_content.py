"""Load the full Urology content: keyword-rich H1, SEO meta, styled rich-text
sections (conditions and regenerative approaches → card grids, process →
numbered timeline via the enhance pipeline), two clinical photos and the FAQ
set."""

from django.db import migrations

SEO_TITLE = "Urology in Dubai | Doctor-Led Urological Care | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led urology in Dubai for urinary symptoms, prostate health, kidney stones, "
    "sexual function and hormonal concerns. Private, root-cause assessment and care."
)
HERO_HEADING = "Urology Clinic in Dubai"
SUMMARY = (
    "Doctor-led urology in Dubai for urinary symptoms, prostate health, kidney stones, "
    "sexual function and hormonal concerns."
)

DESCRIPTION = """
<p>Urology at Brockwell Healthcare is a doctor-led clinical service for diagnosing and managing conditions of the urinary tract and the male reproductive system. Patients often choose it after putting off urinary symptoms, prostate concerns or sexual-health issues, when they want a private, thorough and clinically grounded assessment.</p>

<h2>What Is Urology?</h2>
<p>Urology is the medical field that covers the kidneys, bladder, ureters, urethra and the male reproductive organs, including the prostate, testes and penis. Urological conditions run from everyday concerns like urinary frequency and urgency to more complex issues such as prostate disease, kidney stones, sexual dysfunction and bladder conditions.</p>
<p>At Brockwell Healthcare, we approach urological assessment in Dubai with the same root-cause philosophy we apply across the clinic. Our doctors look at what is actually driving your concern, whether structural, hormonal, inflammatory or functional, and build a plan around that understanding. Every assessment starts with a thorough clinical review before any investigation or treatment.</p>

<h2>How Does a Urology Assessment Work?</h2>
<p>A urology consultation at Brockwell begins with a detailed clinical history: your symptoms, how long you have had them, how they affect daily life and any relevant medical background. Your doctor then carries out a focused examination and chooses investigations based on what the clinical picture suggests.</p>
<p>Those investigations may include ultrasound diagnostics for the kidneys, bladder and prostate, blood tests such as PSA for prostate assessment, urine analysis and uroflowmetry (flow studies) where relevant. Your doctor reads the findings alongside your symptoms and history, not in isolation, so the diagnosis reflects what is genuinely happening. Treatment comes up only once the cause is clear.</p>

<img src="/static/img/services/urology-services-content.webp" alt="Urologist explaining the urinary system to a patient at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>Urological Conditions We Assess and Treat</h2>
<p>The concerns below come up most often in urology consultations at Brockwell, and each needs individual clinical assessment before any treatment.</p>
<h3>Prostate Health</h3>
<p>Urinary symptoms such as frequency, urgency, weak flow, incomplete emptying and nocturia often trace back to the prostate. Prostate assessment in Dubai here covers benign prostatic hyperplasia (BPH), prostatitis and prostate-cancer risk evaluation, including PSA testing and ultrasound. Given the high rates of prostate disease in the region, men over 40 with any urinary symptoms should get assessed early.</p>
<h3>Urinary Tract Infections</h3>
<p>Recurrent UTIs, in men and women, can point to an underlying structural or functional issue rather than a one-off infection. A proper assessment works out whether anatomy, bladder function or other factors are driving the recurrence, so each episode is not simply treated in isolation.</p>
<h3>Kidney Stones</h3>
<p>Kidney stones cause some of the most severe acute pain a person can feel. Assessment covers stone size, location, composition risk factors and the right management, whether that is watchful waiting, medical management or referral for urological intervention.</p>
<h3>Bladder Conditions</h3>
<p>Overactive bladder, urinary urgency, stress incontinence and urge incontinence each have their own underlying mechanism, which shapes the best approach. Stress incontinence usually follows physical activity, while urge incontinence stems from an overactive bladder. A proper assessment pins down the type and cause before any treatment.</p>
<h3>Male Sexual Health and Erectile Dysfunction</h3>
<p>Erectile dysfunction is one of the most under-reported urological concerns, despite being very common. It may reflect vascular, hormonal, neurological or psychological factors that assessment can identify. Here, we handle male sexual-health assessment privately and without judgement, covering erectile function, libido, ejaculatory concerns and related hormones.</p>
<h3>Haematuria</h3>
<p>Blood in the urine, visible or found on testing, always warrants proper investigation. Causes range from benign to serious, so assessment includes urine analysis, imaging and, where needed, specialist referral to rule out significant pathology.</p>
<h3>Low Testosterone and Hormonal Concerns</h3>
<p>Low testosterone affects energy, libido, muscle mass, mood and overall wellbeing. A testosterone assessment covers your symptoms, blood levels, contributing factors and whether hormonal support fits as part of a wider men's-health plan.</p>
<h3>Scrotal and Testicular Concerns</h3>
<p>Pain, swelling or a palpable change in the scrotum or testes needs prompt assessment and imaging, to find the cause and rule out anything requiring urgent attention.</p>

<h2>Regenerative Urology Approaches</h2>
<p>At Brockwell, selected urological concerns may benefit from the clinic's wider regenerative medicine expertise, considered alongside conventional urological management where clinically appropriate.</p>
<h3>PRP Therapy for Male Sexual Health</h3>
<p>Platelet-rich plasma therapy may support erectile function and tissue health in selected patients. The evidence is still developing, so we consider it alongside conventional management, not as a standalone proven treatment.</p>
<h3>Peptide Therapy for Hormonal and Sexual Health</h3>
<p>Peptide therapy may support hormonal signalling, libido, energy and sexual function in men facing age-related hormonal decline, always alongside a full hormonal assessment.</p>
<h3>Shockwave Therapy for Erectile Dysfunction</h3>
<p>Low-intensity shockwave therapy may support vascular function in erectile tissue. We consider it for selected patients where a doctor identifies a vascular component to erectile dysfunction.</p>

<h2>Benefits of Doctor-Led Urological Care</h2>
<p>Doctor-led urology in Dubai at Brockwell may offer several benefits when assessment and treatment are structured around your clinical picture.</p>
<p>Potential benefits include:</p>
<ul>
<li>Urinary symptoms diagnosed and managed accurately, around the real cause</li>
<li>Prostate concerns caught early, when options are broader and outcomes tend to be better</li>
<li>Fewer recurrent UTIs once the underlying contributors are found and addressed</li>
<li>Improvement in erectile dysfunction and sexual-health concerns once the specific cause is treated</li>
<li>More effective kidney-stone management when stone type, size and risk factors are properly evaluated</li>
<li>Better response in bladder dysfunction when the exact type and mechanism are identified first</li>
<li>Hormonal concerns, including low testosterone, handled within a comprehensive men's-health plan</li>
<li>Regenerative options integrated where clinically appropriate for patients who prefer non-surgical routes</li>
</ul>
<p>Results depend on the condition, its severity and your health profile. A clinical assessment decides what is appropriate before any treatment begins.</p>

<h2>The Urology Consultation Process at Brockwell Healthcare</h2>
<p>Every consultation follows a clear clinical process, and your doctor takes time to understand your concern before any investigation or treatment.</p>
<h3>Step 1: Booking</h3>
<p>Contact Brockwell Healthcare to arrange your consultation. The team matches you to the right appointment for your main concern, whether that is urinary symptoms, prostate assessment, sexual health, kidney concerns or hormonal evaluation.</p>
<h3>Step 2: Clinical History and Assessment</h3>
<p>Your doctor takes a detailed history, covering your symptoms, their duration and severity, their impact on daily life, and relevant background such as past investigations, medications and family history. A focused examination follows where clinically appropriate.</p>
<h3>Step 3: Investigations</h3>
<p>Based on your history and examination, your doctor selects the right investigations, which may include ultrasound diagnostics for the kidneys, bladder and prostate, blood tests such as PSA and testosterone, urine analysis and flow studies. The choice is shaped around your specific clinical picture.</p>
<h3>Step 4: Diagnosis and Treatment Plan</h3>
<p>Once results are in, your doctor reviews them against your symptoms and history, then talks you through a clear diagnosis and plan. That may mean medical management, lifestyle guidance, regenerative approaches where appropriate, or referral for specialist urological intervention. Cost and next steps are confirmed before anything begins.</p>
<h3>Step 5: Follow-Up and Ongoing Management</h3>
<p>Follow-up visits review your response, repeat investigations where needed and adjust the plan around your progress. Conditions such as prostate disease, recurrent UTIs and hormonal concerns often do better with ongoing review than with a single consultation.</p>

<h2>Why Patients Choose Brockwell Healthcare for Urology</h2>
<ul>
<li>A DHA-licensed doctor with urological expertise carries out every consultation.</li>
<li>Investigations are chosen around your specific clinical picture.</li>
<li>Ultrasound diagnostics for the kidneys, bladder and prostate are available in-house.</li>
<li>Regenerative options such as PRP, peptide and shockwave therapy can be integrated where clinically appropriate.</li>
<li>Sensitive concerns, from sexual health to incontinence, are handled privately and without judgement.</li>
<li>Realistic outcomes are discussed clearly before any treatment begins.</li>
<li>Upfront pricing is confirmed before your first session, with no surprises.</li>
</ul>
"""

FAQS = [
    ("What does a urology consultation at Brockwell Healthcare involve?",
     "A urology consultation involves a detailed clinical history, a focused examination and selected investigations based on your symptoms. Your doctor reviews the findings in context before discussing a diagnosis and treatment plan."),
    ("When should a man get a prostate assessment?",
     "Men over 40 with any urinary symptoms, and men over 50 without symptoms, should discuss prostate assessment in Dubai with a doctor. Earlier assessment makes sense with a family history of prostate cancer."),
    ("Can urological conditions be treated without surgery?",
     "Many can. Benign prostatic hyperplasia, recurrent UTIs, overactive bladder, erectile dysfunction and early hormonal concerns are often managed through medical treatment, lifestyle guidance and, where appropriate, regenerative approaches."),
    ("Can shockwave therapy help erectile dysfunction?",
     "Only after assessment identifies a vascular cause. If reduced blood flow to the erectile tissue is a factor, your doctor may discuss low-intensity shockwave therapy as part of the wider plan."),
    ("Can PRP therapy help male sexual-health concerns?",
     "PRP therapy may be considered within a wider male sexual-health plan where your doctor confirms it is clinically appropriate for your specific findings."),
    ("What does a testosterone assessment involve?",
     "A testosterone assessment covers your symptoms, such as fatigue, low libido, mood changes and muscle loss, along with blood tests for total and free testosterone, LH, FSH and other relevant markers. Your doctor reads these against your symptoms and overall health before discussing any treatment."),
    ("Is blood in the urine always serious?",
     "Blood in the urine, visible or found on testing, always needs proper investigation. Many causes are benign, but some need urgent assessment to rule out serious pathology, so book a consultation promptly if you notice it."),
    ("Can recurrent UTIs be prevented?",
     "Prevention starts with finding why they keep returning. Beyond anatomy and bladder function, your doctor looks at hydration, voiding patterns, hormonal factors and hygiene. Addressing these directly tends to cut recurrence, often more than repeat antibiotic courses alone."),
    ("How is kidney-stone management approached?",
     "Once a stone is confirmed, the approach depends on whether it is likely to pass on its own. Smaller stones are often managed with hydration, pain control and monitoring, while larger or symptomatic ones go for urological intervention. Your doctor also reviews diet and risk factors to lower the chance of future stones."),
    ("Is a urology consultation confidential?",
     "Yes. Every urology consultation at Brockwell is private and confidential. Sensitive concerns, including sexual health, incontinence and prostate issues, are handled without judgement in a discreet clinical setting."),
    ("What does a urology consultation cost in Dubai?",
     "Cost depends on the assessment, the investigations and any treatment recommended. You receive clear pricing and a full estimate before any investigation or treatment begins."),
    ("Do I need a referral before a urology consultation?",
     "No formal referral is needed. You can contact Brockwell directly to book a urology consultation in Dubai, and the team helps you choose the right appointment and explains what to prepare."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    svc = Service.objects.filter(region="uae", slug="urology-services").first()
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
        ("services", "0029_stress_management_content"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
