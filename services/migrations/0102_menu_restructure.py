"""Restructure the services menu to match the agreed navigation.

* Recover the old 'Emsculpt for Pain' page as a *sub-service* of Chronic Pain
  (content and images recovered from the retired category), with its FAQ.
* Move Hydrodissection & Injections from Regenerative Wellness to Chronic Pain.
* Move NAD+ IV Therapy out from under Longevity IVs and into Regenerative
  Wellness as a top-level service.
* Move Peptide Therapy from Longevity | Healthspan to Regenerative Wellness.
* Re-order the categories and the services within each category to the agreed
  menu order. Services not named in the new menu (Ozone Therapy, IV Drips,
  Therapeutic Plasma Exchange, Biological Integrative Medicine) are kept in
  their current categories and simply appended after the named ones.
"""

from django.db import migrations

EMS_SLUG = "emsculpt-for-pain"
EMS_NAME = "Emsculpt for Pain"
EMS_HERO = "Emsculpt for Pain in Dubai"
EMS_SEO_TITLE = (
    "Emsculpt for Pain in Dubai | Neuromuscular Stimulation | Brockwell Healthcare"
)
EMS_SEO_DESCRIPTION = (
    "Book Emsculpt for pain in Dubai at Brockwell Healthcare for chronic pain, muscle "
    "weakness, core instability, back pain and rehabilitation support. Doctor-led "
    "neuromuscular stimulation with personalised treatment plans."
)
EMS_SUMMARY = (
    "Doctor-led HIFEM neuromuscular stimulation for chronic pain, muscle weakness, core "
    "instability and rehabilitation support."
)

EMS_DESCRIPTION = """
<p>Emsculpt for pain at Brockwell Healthcare uses high-intensity focused electromagnetic technology to stimulate deep muscle contractions beyond what voluntary exercise can achieve. In a clinical pain-management context, it supports muscle rehabilitation, strengthens weakened supporting muscles and addresses the muscular contributors to chronic pain and functional instability.</p>

<h2>What Is Emsculpt for Pain?</h2>
<p>Emsculpt is a non-invasive device that uses High-Intensity Focused Electromagnetic therapy (HIFEM) to induce powerful contractions in targeted muscle groups. In a conventional aesthetic context, it is used for body contouring. At Brockwell Healthcare, Emsculpt for pain is considered specifically for its clinical role in neuromuscular rehabilitation, where the goal is to restore muscle function, strength and stability in areas contributing to chronic pain.</p>
<p>The clinical rationale is straightforward. Many chronic pain conditions, particularly those affecting the lower back, pelvis, hips and core, involve muscle weakness, inhibition or atrophy that standard pain management and passive physiotherapy alone may not fully address. Strengthening these muscles through high-intensity neuromuscular stimulation may reduce the mechanical load on painful structures and support a more stable movement pattern over time.</p>
<p>At Brockwell Healthcare, HIFEM therapy in Dubai is recommended only after a proper clinical assessment confirms it is appropriate and relevant to your specific pain presentation.</p>

<img src="/static/img/services/emsculpt-for-pain-content.webp" alt="Emsculpt HIFEM applicator positioned for neuromuscular pain treatment at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>How Does Emsculpt for Pain Work?</h2>
<p>HIFEM technology delivers focused electromagnetic energy through a paddle-shaped applicator placed against the skin over the target muscle group. The electromagnetic field induces supramaximal contractions, contractions of a greater intensity than the muscle can produce voluntarily, and a single session typically induces thousands of them within the treatment period.</p>
<p>In a clinical pain context, the aim of these contractions is not muscle size or appearance. It is neuromuscular re-education and functional strengthening. When a muscle becomes inhibited, weak or atrophied through pain, disuse or injury, voluntary exercise is often not enough to fully recruit and strengthen it, particularly in the early stages of rehabilitation. Emsculpt neuromuscular stimulation works around this limitation by directly inducing high-intensity contractions, independent of voluntary motor recruitment.</p>
<p>Over a course of sessions, these contractions may stimulate muscle fibre growth, improve motor unit recruitment, restore functional strength and reduce the area's mechanical vulnerability to pain and re-injury. The sessions complement physiotherapy, manual therapy and other clinical approaches within a wider pain-management plan.</p>

<img src="/static/img/services/emsculpt-for-pain-content-2.webp" alt="Deep supramaximal muscle contraction during an Emsculpt for pain session at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>What Emsculpt for Pain May Support</h2>
<p>Where Emsculpt for pain fits depends on the specific pain presentation and what the clinical assessment shows. It is not appropriate for every pain condition, and your doctor considers it only within a structured clinical plan. In general, Emsculpt for muscle weakness may be considered when reduced muscle activation or atrophy has become a significant contributor to pain or reduced function.</p>
<h3>Lower Back Pain and Core Weakness</h3>
<p>Emsculpt for back pain may be considered when weakness in the deep core muscles, including the multifidus, transverse abdominis and pelvic floor, contributes to chronic lower back pain. Core strengthening for back pain is an important part of rehabilitation when weakness in the deep stabilising muscles feeds ongoing symptoms.</p>
<h3>Hip and Pelvic Instability</h3>
<p>Weakness in the gluteal and hip-stabiliser muscles can drive pain in the hips, lower back and knees through altered load distribution. Targeted HIFEM therapy to the gluteal and hip musculature may support functional stability and ease pain in the surrounding structures. Emsculpt for hip pain may be considered when weakness of the gluteal and hip-stabilising muscles contributes to symptoms.</p>
<h3>Post-Surgical Muscle Rehabilitation</h3>
<p>After orthopaedic surgery, muscle inhibition and atrophy are common even when patients are otherwise recovering well. Emsculpt rehabilitation may help restore muscle activation and strength in the affected area more efficiently than voluntary exercise alone during early recovery, subject to surgical clearance and timing.</p>
<h3>Knee Pain from Quadriceps Weakness</h3>
<p>Emsculpt for knee pain may be considered when quadriceps weakness contributes to knee pain and instability. Strengthening the quadriceps through neuromuscular stimulation may reduce load on the knee joint and support better movement mechanics where this is a contributing factor.</p>
<h3>Shoulder Instability and Rotator Cuff Weakness</h3>
<p>Selected shoulder pain presentations involving weakness in the rotator cuff or surrounding stabiliser muscles may benefit from targeted Emsculpt sessions within a wider shoulder rehabilitation plan.</p>

<h2>Benefits of Doctor-Led Emsculpt for Pain</h2>
<p>Emsculpt for pain may offer several potential benefits for selected patients when the right protocol is matched to the right clinical presentation through proper assessment. Results depend on the pain condition, the specific muscles targeted, the number of sessions and individual response.</p>
<p>Possible benefits include:</p>
<ul>
<li>Neuromuscular stimulation for pain may help restore muscle activation and functional stability in selected patients</li>
<li>Better functional strength in the muscles contributing to pain, over a course of sessions</li>
<li>Less mechanical load on painful joints and structures as supporting muscle function improves</li>
<li>Muscle inhibition after injury or surgery addressed more efficiently than voluntary exercise alone</li>
<li>Non-invasive sessions with no needles, injections or downtime</li>
<li>A suitable option for non-invasive muscle rehabilitation in appropriately selected patients</li>
<li>Integration within a wider physiotherapy, rehabilitation or pain-management plan at Brockwell Healthcare</li>
</ul>
<p>Results are not guaranteed and vary with the underlying pain condition, the degree of muscle weakness and individual response. A clinical assessment at Brockwell Healthcare decides whether Emsculpt for pain in Dubai is appropriate for your specific situation.</p>

<h2>The Emsculpt for Pain Process at Brockwell Healthcare</h2>
<p>Every Emsculpt for pain plan at Brockwell Healthcare follows a clear clinical process, and nothing begins until your doctor confirms that HIFEM therapy is appropriate and relevant to your specific pain presentation.</p>
<h3>Step 1: Booking</h3>
<p>Get in touch with Brockwell Healthcare to arrange your Emsculpt pain treatment Dubai consultation. The team helps you choose the right appointment for your main concern, whether that is lower back pain, hip instability, post-surgical rehabilitation, knee pain or another musculoskeletal concern with a muscle-weakness component.</p>
<h3>Step 2: Clinical Assessment</h3>
<p>Your doctor reviews your pain history, previous treatments, relevant imaging, current medications and treatment goals, identifies the specific muscles contributing to your pain, and confirms whether HIFEM neuromuscular stimulation is likely to be of clinical value. Your doctor checks contraindications including implanted devices, metal implants, pregnancy and active cancer before recommending any session.</p>
<h3>Step 3: Preparation</h3>
<p>Your clinician exposes the treatment area and positions the applicator against the skin over the target muscle group. No gel is required, and your clinician holds the applicator in place during the session. You confirm whether any metal implants or devices are present in the body before the session begins.</p>
<h3>Step 4: Treatment</h3>
<p>The device delivers high-intensity focused electromagnetic pulses through the applicator to the target muscle group. Most patients feel a strong muscle-contraction sensation, from mildly to moderately intense depending on the intensity settings and individual tolerance, and your clinician adjusts the intensity to your comfort and response during the session. Sessions typically take 20 to 30 minutes per treatment area.</p>
<h3>Step 5: Aftercare and Follow-Up</h3>
<p>After the session, you may feel muscle soreness similar to intense exercise, which usually settles within one to two days. Your doctor advises on activity recommendations and how the sessions fit within your wider physiotherapy or rehabilitation plan. Most Emsculpt for pain protocols run as a course of sessions, typically several, and your doctor reviews progress at follow-up appointments and adjusts the plan around your response.</p>

<h2>Why Choose Brockwell Healthcare for Emsculpt for Pain</h2>
<ul>
<li>A DHA-licensed doctor assesses and supervises every Emsculpt for pain plan for its clinical pain application.</li>
<li>Emsculpt is used specifically for its clinical pain-management and rehabilitation applications at Brockwell Healthcare.</li>
<li>A contraindication screen covering implanted devices, metal implants, pregnancy and active cancer comes before every session.</li>
<li>Treatment intensity is adjusted to your comfort and clinical response.</li>
<li>Sessions are integrated within a wider physiotherapy, rehabilitation or pain-management plan.</li>
<li>Realistic outcomes are discussed honestly before any HIFEM therapy begins.</li>
<li>Upfront pricing is confirmed before your first session, with no surprises.</li>
</ul>
"""

EMS_FAQS = [
    ("Is Emsculpt for pain the same as Emsculpt for body contouring?",
     "It uses the same device and technology, but the clinical goal is different. In a pain-management context at Brockwell Healthcare, Emsculpt is used to restore muscle function, strength and stability in areas contributing to pain, not for appearance-related goals."),
    ("What pain conditions might Emsculpt support?",
     "Emsculpt for pain in Dubai may be considered for chronic lower back pain with core weakness, hip and pelvic instability, post-surgical muscle rehabilitation, knee pain from quadriceps weakness and selected shoulder instability presentations. Suitability depends on the specific pain condition and is confirmed through clinical assessment."),
    ("Is Emsculpt for pain safe?",
     "Emsculpt is generally well tolerated when a trained clinical team uses appropriate settings after proper contraindication screening. It is not appropriate for patients with implanted electronic devices, metal implants in the treatment area, pregnancy, active cancer near the treatment site or epilepsy. Your doctor reviews all contraindications before recommending any session."),
    ("Is the treatment painful?",
     "Most patients feel a strong muscle-contraction sensation during the session, from mildly to moderately intense depending on the settings and individual tolerance. Your clinician adjusts the intensity to your comfort. Muscle soreness similar to post-exercise soreness may occur for one to two days afterwards."),
    ("How long does one Emsculpt session take?",
     "Sessions typically take 20 to 30 minutes per treatment area. Your doctor confirms the expected duration during your Emsculpt pain treatment Dubai consultation."),
    ("Is there downtime after Emsculpt for pain?",
     "There is no formal downtime. Most patients return to normal light activity after the session. Muscle soreness in the treated area may occur for one to two days, similar to the feeling after an intense workout. Your clinician advises on any activity changes relevant to your pain condition and rehabilitation plan."),
    ("How many Emsculpt sessions are usually needed?",
     "Most protocols run as a course of sessions, typically several. The number depends on the pain condition, the degree of muscle weakness and how your body responds. Your doctor confirms the recommended plan after the clinical assessment and reviews it as you progress."),
    ("When can results from Emsculpt for pain be noticed?",
     "Some patients notice improvements in muscle control and pain during and after the course of sessions. Results typically develop gradually as functional strength improves and the mechanical contributors to pain are addressed. The timeline varies with the condition and individual response."),
    ("Can Emsculpt for pain be combined with other treatments?",
     "Yes. HIFEM neuromuscular stimulation is designed to complement physiotherapy, manual therapy, injection therapy and other pain-management approaches at Brockwell Healthcare. Your doctor advises on how Emsculpt fits within your wider rehabilitation plan."),
    ("What is the cost of Emsculpt for pain in Dubai?",
     "The cost depends on the treatment area, the number of sessions and the clinical protocol. Brockwell Healthcare provides clear pricing and a full cost estimate before your first session begins."),
    ("Who should avoid Emsculpt for pain?",
     "Patients with implanted electronic devices such as pacemakers, metal implants in the treatment area, pregnancy, active cancer near the treatment site, epilepsy or serious uncontrolled medical conditions should not have Emsculpt without speaking to a doctor first. All contraindications are reviewed during the consultation before anything is recommended."),
    ("Do I need a consultation before Emsculpt for pain in Dubai?",
     "Yes. A clinical assessment is required before any Emsculpt for pain treatment at Brockwell Healthcare. It confirms that muscle weakness is contributing to your pain, checks contraindications and lets your doctor build the right protocol within your wider rehabilitation plan, so nothing begins without it."),
]

# Agreed category order (top-level menu).
CATEGORY_ORDER = [
    "chronic-pain",
    "advanced-diagnostics",
    "anti-aging-aesthetics",
    "longevity-healthspan",
    "regenerative-medicine",
    "regenerative-wellness",
]

# Agreed service order within each category. Services not named in the new menu
# are appended, in their existing relative order, after the named ones.
SERVICE_ORDER = {
    "chronic-pain": [
        "emsculpt-for-pain",
        "hydrodissection-injections",
    ],
    "advanced-diagnostics": [
        "ultrasound-diagnostics",
    ],
    "anti-aging-aesthetics": [
        "pure-plasma",
        "emsculpt-neo",
        "emsella",
    ],
    "longevity-healthspan": [
        "healthspan",
        "longevity-medicine",
        "stem-cells",
        "stress-reset",
        "ketamine-therapy",
        "longevity-ivs",
        # kept (not in the new menu list), appended:
        "therapeutic-plasma-exchange",
    ],
    "regenerative-medicine": [
        "regenerative-orthopedics",
        "sports-medicine",
        "exosome-therapy",
        "functional-medicine",
        "physiotherapy",
        "genomics-medicine",
        # kept, appended:
        "biological-integrative-medicine",
    ],
    "regenerative-wellness": [
        "detox-therapy",
        "exomind-tms-wellness",
        "hyperbaric-oxygen-therapy",
        "iv-laser-therapy",
        "male-wellness",
        "sexual-health",
        "nutrition-weight-loss",
        "pemf-therapy",
        "shock-wave-therapy",
        "stress-management",
        "urology-services",
        "regenerative-iv-therapy",
        "nad-iv-therapy",
        "peptide-therapy",
        # kept, appended:
        "ozone-therapy",
        "iv-drips",
    ],
}


def restructure(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    cats = {c.slug: c for c in ServiceCategory.objects.filter(region="uae")}

    chronic = cats.get("chronic-pain")
    wellness = cats.get("regenerative-wellness")
    if not chronic or not wellness:
        return

    # 1. Recover Emsculpt for Pain as a sub-service of Chronic Pain.
    svc, _ = Service.objects.update_or_create(
        region="uae", slug=EMS_SLUG,
        defaults=dict(
            category=chronic, parent=None, name=EMS_NAME, hero_heading=EMS_HERO,
            summary=EMS_SUMMARY, description=EMS_DESCRIPTION.strip(),
            benefits="", seo_title=EMS_SEO_TITLE, seo_description=EMS_SEO_DESCRIPTION,
            icon="", is_published=True,
        ),
    )
    ct_svc, _ = ContentType.objects.get_or_create(
        app_label="services", model="service"
    )
    FAQItem.objects.filter(content_type=ct_svc, object_id=svc.id).delete()
    for i, (q, a) in enumerate(EMS_FAQS):
        FAQItem.objects.create(
            content_type=ct_svc, object_id=svc.id,
            question=q, answer=a, order=i, is_published=True,
        )

    # 2. Move Hydrodissection to Chronic Pain.
    Service.objects.filter(region="uae", slug="hydrodissection-injections").update(
        category=chronic, parent=None
    )

    # 3. Move NAD+ IV Therapy to Regenerative Wellness, top-level.
    Service.objects.filter(region="uae", slug="nad-iv-therapy").update(
        category=wellness, parent=None
    )

    # 4. Move Peptide Therapy to Regenerative Wellness.
    Service.objects.filter(region="uae", slug="peptide-therapy").update(
        category=wellness, parent=None
    )

    # 5. Category order.
    for i, slug in enumerate(CATEGORY_ORDER):
        c = cats.get(slug)
        if c:
            c.order = i
            c.save(update_fields=["order"])

    # 6. Service order within each category. Named services get 0..n; any other
    #    published top-level services in that category are appended after.
    for cat_slug, ordered in SERVICE_ORDER.items():
        cat = cats.get(cat_slug)
        if not cat:
            continue
        index = {slug: i for i, slug in enumerate(ordered)}
        tail = len(ordered)
        svcs = Service.objects.filter(
            region="uae", category=cat, parent__isnull=True
        )
        for s in svcs:
            if s.slug in index:
                s.order = index[s.slug]
            else:
                s.order = tail
                tail += 1
            s.save(update_fields=["order"])


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0101_chronic_pain_category"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(restructure, migrations.RunPython.noop)]
