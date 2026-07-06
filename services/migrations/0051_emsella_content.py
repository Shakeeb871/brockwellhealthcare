"""Update the existing Emsella service (under Anti-Aging Aesthetics) with the full
refined content: SEO meta, keyword-rich H1 (full, with tagline), styled
rich-text sections (the 'May Support' section becomes a card grid and the
process becomes a numbered timeline), an inline content image, and the FAQ set.
Hero image: static/img/services/emsella-hero.webp; inline content image:
static/img/services/emsella-content.webp."""

from django.db import migrations

SLUG = "emsella"

SEO_TITLE = "Emsella in Dubai | Pelvic Floor & Incontinence | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Book Emsella in Dubai at Brockwell Healthcare for urinary incontinence, pelvic floor "
    "weakness, pelvic instability and sexual health support. Doctor-led pelvic floor "
    "treatment with personalised clinical plans."
)
HERO_HEADING = "Emsella in Dubai | Pelvic Floor Treatment & Incontinence Support"
SUMMARY = (
    "Doctor-led Emsella in Dubai: HIFEM pelvic floor therapy for urinary incontinence, "
    "pelvic floor weakness, pelvic instability and pelvic health in men and women."
)

DESCRIPTION = """
<p>Emsella at Brockwell Healthcare uses High-Intensity Focused Electromagnetic technology to stimulate deep pelvic floor muscle contractions beyond what voluntary exercise can achieve. In a clinical context, it supports pelvic floor rehabilitation, urinary incontinence treatment and pelvic health in both men and women.</p>

<h2>What Is Emsella?</h2>
<p>Emsella is a non-invasive medical device that uses HIFEM technology to deliver focused electromagnetic energy to the pelvic floor muscles. You sit fully clothed on the Emsella chair during the session while the device induces thousands of supramaximal pelvic floor contractions, contractions far stronger than the muscle can produce voluntarily, within a single treatment period.</p>
<p>At Brockwell Healthcare, Emsella treatment in Dubai is a clinical pelvic floor rehabilitation tool. Your doctor considers it for patients dealing with urinary incontinence, pelvic floor weakness, pelvic instability and selected pelvic health concerns, where strengthening the pelvic floor musculature is a clinically relevant goal. Every plan begins with a proper clinical assessment to confirm whether Emsella is appropriate and relevant to your specific presentation.</p>

<h2>How Does Emsella Work?</h2>
<p>The pelvic floor is a group of muscles and connective-tissue structures, known collectively as the levator ani, that support the bladder, bowel and uterus in women, and the bladder and bowel in men. When these muscles weaken through childbirth, ageing, hormonal change, surgery or sustained physical loading, the result can include urinary leakage, urgency, pelvic instability and reduced sexual function.</p>
<p>HIFEM pelvic floor therapy works by delivering focused electromagnetic energy through the chair into the pelvic floor musculature, inducing supramaximal contractions at an intensity the muscles cannot generate voluntarily. Over a course of sessions, these contractions may stimulate muscle fibre development, improve motor unit recruitment and restore the functional strength and endurance of the pelvic floor, so it can better perform its structural and sphincteric functions.</p>
<p>The session involves sitting fully clothed on the Emsella chair for the treatment duration. Most patients feel a strong muscle-contraction sensation throughout, and there are no needles, no incisions and no recovery period required.</p>

<img src="/static/img/services/emsella-content.webp" alt="Patient seated on the Emsella pelvic floor chair at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>What Emsella May Support</h2>
<p>Where Emsella fits depends on the specific pelvic floor concern and what your clinical assessment shows. It is not appropriate for every pelvic condition, and your doctor confirms suitability before recommending any session.</p>
<h3>Stress Urinary Incontinence</h3>
<p>Stress incontinence involves leakage triggered by physical activity, including coughing, sneezing, laughing or exercise, and reflects insufficient pelvic floor support of the bladder neck under load. Emsella for stress incontinence may help by strengthening the pelvic floor to better support the bladder neck during physical demands.</p>
<h3>Urge Urinary Incontinence</h3>
<p>Urge incontinence involves a sudden, strong need to urinate that is difficult to defer, and may reflect overactive bladder activity alongside pelvic floor dysfunction. Emsella may support pelvic floor function within a wider management plan for urge incontinence, though additional bladder-management strategies are often needed alongside pelvic floor strengthening.</p>
<h3>Mixed Urinary Incontinence</h3>
<p>Where both stress and urge components are present, pelvic floor strengthening through Emsella may contribute to the management plan alongside other approaches addressing the bladder component.</p>
<h3>Post-Natal Pelvic Floor Rehabilitation</h3>
<p>After childbirth, pelvic floor muscles are commonly weakened and may not recover fully through voluntary pelvic floor exercises alone. Emsella for post-natal recovery may support more effective rehabilitation during the recovery period, once appropriate clinical clearance is confirmed.</p>
<h3>Pelvic Floor Weakness in Men</h3>
<p>Male pelvic floor treatment with Emsella may be considered for urinary leakage following prostate surgery, pelvic instability or other pelvic floor concerns. Assessment confirms whether pelvic floor strengthening is relevant to the specific presentation.</p>
<h3>Pelvic Health and Sexual Function Support</h3>
<p>Pelvic floor function is linked to sexual health in both men and women. Improved pelvic floor strength and neuromuscular control may contribute to sexual function and satisfaction in selected patients where pelvic floor weakness is a contributing factor. Your doctor discusses this during the clinical assessment.</p>

<h2>Benefits of Doctor-Led Emsella</h2>
<p>Emsella may offer several potential benefits for selected patients when the right protocol is matched to the right clinical presentation through proper assessment. Results depend on the type and severity of the pelvic floor concern, the number of sessions and individual response.</p>
<p>Possible benefits include:</p>
<ul>
<li>Fewer urinary leakage episodes as pelvic floor strength and support improve over a course of sessions</li>
<li>Less urgency and frequency in selected patients where pelvic floor function is a contributing factor</li>
<li>Better pelvic floor endurance and control, supporting daily activities and exercise without leakage</li>
<li>Post-natal pelvic floor recovery supported more effectively than voluntary exercises alone in selected cases</li>
<li>Better pelvic stability where pelvic floor weakness is a contributing structural factor</li>
<li>A non-invasive incontinence treatment option, with no needles, incisions or recovery period</li>
<li>Integration within a wider pelvic health, physiotherapy or rehabilitation plan at Brockwell Healthcare</li>
</ul>
<p>Results are not guaranteed and vary with the type and severity of the pelvic floor concern, previous treatment history and individual response. A clinical assessment at Brockwell Healthcare decides whether Emsella treatment in Dubai is appropriate for your specific situation.</p>

<h2>The Emsella Process at Brockwell Healthcare</h2>
<p>Every Emsella plan at Brockwell Healthcare follows a clear clinical process, and nothing begins until your doctor confirms that HIFEM pelvic floor therapy is appropriate for your specific presentation.</p>
<h3>Step 1: Booking</h3>
<p>Get in touch with Brockwell Healthcare to arrange your Emsella Dubai consultation. The team helps you choose the right appointment for your main concern, whether that is stress incontinence, urge incontinence, post-natal pelvic floor recovery, male pelvic health or general pelvic floor strengthening.</p>
<h3>Step 2: Clinical Assessment</h3>
<p>Your doctor reviews your pelvic floor history, incontinence symptoms, obstetric history where relevant, previous treatments, relevant medications and goals, identifies the type of incontinence or pelvic floor concern, and confirms whether Emsella is likely to be of clinical value. Your doctor checks contraindications including implanted devices, metal implants, pregnancy, active infection and recent pelvic surgery before recommending any session.</p>
<h3>Step 3: Preparation</h3>
<p>You sit fully clothed on the Emsella chair, with no undressing, gel or preparation required. You confirm whether any implanted devices or metal implants are present in the body before the session begins, and your clinician confirms the device settings based on your assessment and comfort level.</p>
<h3>Step 4: Treatment</h3>
<p>The device delivers focused electromagnetic pulses to the pelvic floor through the chair, and you feel strong pelvic floor contractions throughout the session. Your clinician can adjust the intensity to your comfort and tolerance. Sessions typically take around 28 to 30 minutes, and most patients find the sensation manageable once the initial intensity is set appropriately.</p>
<h3>Step 5: Aftercare and Follow-Up</h3>
<p>After the session, most patients return to normal activity immediately. Some mild pelvic floor soreness may occur, similar to the feeling after intensive exercise, and usually settles within one to two days. Your doctor advises on how the sessions fit within your wider pelvic health or physiotherapy plan. Most Emsella protocols run as a course of sessions, typically six over three weeks, though this may vary with your assessment, and your doctor reviews progress at follow-up and adjusts the plan around your response.</p>

<h2>Why Choose Brockwell Healthcare for Emsella</h2>
<ul>
<li>A DHA-licensed doctor assesses and supervises every doctor-led Emsella plan for its clinical pelvic floor application.</li>
<li>The type and severity of your pelvic floor concern is properly identified through clinical assessment before any session.</li>
<li>A contraindication screen covering implanted devices, metal implants, pregnancy, pelvic infection and recent surgery comes before every session.</li>
<li>Treatment intensity is adjusted to your comfort and clinical response.</li>
<li>Sessions are integrated within a wider pelvic health, physiotherapy or rehabilitation plan where appropriate.</li>
<li>Realistic outcomes are discussed honestly before any HIFEM pelvic floor therapy begins.</li>
<li>Upfront pricing is confirmed before your first session, with no surprises.</li>
</ul>
"""

FAQS = [
    ("What types of incontinence can Emsella support?",
     "Emsella for stress incontinence may help by strengthening pelvic floor support of the bladder neck under physical load. Emsella may also contribute to management plans for urge incontinence and mixed incontinence, where pelvic floor weakness is a confirmed contributing factor alongside other appropriate clinical approaches."),
    ("Is Emsella suitable for men?",
     "Yes. Emsella may be considered for men dealing with urinary leakage following prostate surgery, pelvic instability or other pelvic floor concerns, where strengthening the pelvic musculature is a clinically relevant goal. A proper assessment confirms whether it is appropriate for the specific presentation."),
    ("Do I need to undress for Emsella treatment?",
     "No. You sit fully clothed on the Emsella chair throughout the session. No undressing, gel or preparation is required, which makes it a straightforward and discreet treatment option."),
    ("Is Emsella painful?",
     "Most patients feel strong pelvic floor contractions during the session, from mildly to moderately intense depending on the settings and individual sensitivity. Your clinician adjusts the intensity to your comfort. Some mild pelvic floor soreness may occur for one to two days afterwards, similar to post-exercise soreness."),
    ("How long does one Emsella session take?",
     "Sessions typically take around 28 to 30 minutes. Your doctor confirms the expected duration during your Emsella Dubai consultation."),
    ("Is there downtime after Emsella treatment?",
     "There is no formal downtime. Most patients return to normal activity immediately after the session. Some mild pelvic floor soreness may occur for one to two days, which is normal and usually settles without intervention."),
    ("How many Emsella sessions are usually needed?",
     "Most protocols involve six sessions over about three weeks, though this may vary with your assessment and response. Your doctor confirms the recommended plan after the clinical assessment and reviews it at follow-up appointments as you progress."),
    ("When can results from Emsella be noticed?",
     "Some patients notice improvements in urinary control and pelvic floor function during the course of sessions, while others improve more gradually in the weeks after the course as muscle strength continues to develop. The timeline varies with the severity of the concern and individual response."),
    ("Can Emsella be combined with other treatments?",
     "Yes. HIFEM pelvic floor therapy is designed to complement physiotherapy, pelvic floor rehabilitation programmes, urological management and other clinical approaches at Brockwell Healthcare. Your doctor advises on how Emsella fits within your wider pelvic health plan."),
    ("Is Emsella safe?",
     "Emsella is generally well tolerated when a trained clinical team uses appropriate settings after proper contraindication screening. It is not appropriate for patients with implanted electronic devices, metal pelvic implants, pregnancy, active pelvic infection, certain IUDs, recent pelvic surgery without clearance or epilepsy. Your doctor reviews all contraindications before recommending any session."),
    ("What is the cost of Emsella in Dubai?",
     "The cost depends on the number of sessions in the protocol and the clinical plan. Brockwell Healthcare provides clear pricing and a full cost estimate before your first session begins."),
    ("Who should avoid Emsella?",
     "Patients with implanted electronic devices, metal implants in the pelvic region or lower spine, pregnancy, active cancer in the pelvic area without clearance, a copper IUD, active pelvic infection, recent pelvic surgery without clearance or epilepsy should not have Emsella without speaking to a doctor first. All contraindications are reviewed during the consultation before anything is recommended."),
    ("Do I need a consultation before Emsella in Dubai?",
     "Yes. A clinical assessment is required before any Emsella treatment in Dubai begins. It confirms the type and severity of your pelvic floor concern, checks all contraindications and lets your doctor confirm whether HIFEM pelvic floor therapy is appropriate and build the right protocol, so nothing begins without it."),
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
        ("services", "0050_pure_plasma_content"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
