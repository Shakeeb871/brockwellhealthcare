"""Update the existing Pure Plasma service (under Anti-Aging Aesthetics) with the
full refined content: SEO meta, keyword-rich H1 (full, with tagline), styled
rich-text sections (the 'May Support' section becomes a card grid and the
process becomes a numbered timeline), an inline content image, and the FAQ set.
Hero image: static/img/services/pure-plasma-hero.webp; inline content image:
static/img/services/pure-plasma-content.webp."""

from django.db import migrations

SLUG = "pure-plasma"

SEO_TITLE = "Pure Plasma Therapy in Dubai | Doctor-Led PRP | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Book Pure Plasma therapy in Dubai at Brockwell Healthcare for skin rejuvenation, "
    "hair restoration, joint health, tissue repair and cellular regeneration. Doctor-led "
    "plasma treatment with personalised clinical plans."
)
HERO_HEADING = "Pure Plasma Therapy in Dubai | Doctor-Led PRP & Plasma Treatment"
SUMMARY = (
    "Doctor-led Pure Plasma therapy in Dubai: a highly concentrated, purified plasma "
    "preparation for skin rejuvenation, hair restoration, joint health and tissue repair."
)

DESCRIPTION = """
<p>Pure Plasma therapy at Brockwell Healthcare is an advanced form of platelet-rich plasma treatment that uses a highly concentrated, purified plasma preparation to support tissue repair, skin rejuvenation, hair restoration and joint health. Patients often consider it when they want a more refined regenerative approach than standard PRP, using the body's own biological components in a more precisely concentrated form.</p>

<h2>What Is Pure Plasma Therapy?</h2>
<p>Pure Plasma is a highly purified, concentrated plasma preparation derived from your own blood. Like advanced PRP therapy, it uses your own biological material, which keeps immune-rejection considerations to a minimum. The difference lies in the concentration and purification process, which aims to produce a preparation with a higher concentration of the relevant growth factors and fewer components that may not contribute to the regenerative goal. In short, this concentrated plasma therapy aims to deliver a more refined regenerative preparation than conventional PRP.</p>
<p>At Brockwell Healthcare, we offer Pure Plasma treatment in Dubai within a wider regenerative medicine framework. Your doctor may consider it for skin rejuvenation, hair restoration, joint and soft-tissue repair, and cellular health. Every plan begins with a proper clinical assessment that confirms whether Pure Plasma therapy is appropriate and realistic for your specific concern.</p>

<h2>How Does Pure Plasma Therapy Work?</h2>
<p>Blood contains several components, including red blood cells, white blood cells, platelets and plasma. Platelets are of particular interest in regenerative medicine because they carry growth factors, signalling proteins and other bioactive molecules involved in the body's natural healing and repair. In effect, this plasma growth factor therapy aims to support those repair processes through concentrated biological signalling.</p>
<p>When your blood is processed through centrifugation, the platelet-rich fraction separates from the rest. Pure Plasma therapy takes this a step further, using a more refined processing approach to produce an autologous preparation with a higher platelet and growth-factor concentration and reduced, leukocyte-lowered red and white blood cell content compared with standard PRP. Your clinician then delivers the preparation to the target area, where the concentrated growth factors may communicate with surrounding cells to support repair, calm inflammation and encourage tissue renewal.</p>
<p>The clinical effect depends on the concentration achieved, the delivery method, the target tissue and individual biological response. Results are not guaranteed, and individual response varies.</p>

<img src="/static/img/services/pure-plasma-content.webp" alt="Doctor preparing a Pure Plasma preparation at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>What Pure Plasma Therapy May Support</h2>
<p>Where Pure Plasma therapy fits depends on the concern and what your clinical assessment shows. It is not appropriate for every condition, and your doctor confirms suitability before recommending any session.</p>
<h3>Skin Rejuvenation</h3>
<p>Pure Plasma for skin may support collagen production, skin texture, tone and cellular renewal. Your doctor may consider it for skin-ageing concerns including dullness, fine lines, uneven texture and loss of firmness, where a regenerative approach is clinically appropriate.</p>
<h3>Hair Restoration</h3>
<p>Pure Plasma for hair loss is a form of hair restoration plasma therapy that delivers concentrated growth factors to the scalp to support follicle activity, calm follicle inflammation and encourage healthier growth. Your doctor may consider it for androgenetic alopecia and hair thinning within a wider hair restoration plan.</p>
<h3>Joint and Soft Tissue Repair</h3>
<p>Pure Plasma for joints may support tissue repair and ease inflammation in joints affected by cartilage wear, tendon degeneration or sports-related damage. Your doctor may consider it alongside or as an alternative to standard PRP, depending on the degree of involvement and the assessment.</p>
<h3>Wound Healing and Tissue Recovery</h3>
<p>Where tissue healing has been slow after injury or a procedure, concentrated plasma growth factors may support the repair environment. Your clinician confirms timing and suitability based on the healing stage and your specific situation.</p>

<h2>Benefits of Doctor-Led Pure Plasma Therapy</h2>
<p>Pure Plasma therapy may offer several potential benefits for selected patients when the right protocol is matched to the right concern through proper clinical assessment. Results depend on the concentration achieved, the application method, the target tissue and individual response.</p>
<p>Possible benefits include:</p>
<ul>
<li>A higher growth-factor concentration than standard PRP, which may produce a stronger regenerative signal at the treatment site</li>
<li>Better skin texture, tone and firmness as collagen production and cellular renewal are supported</li>
<li>Better-supported hair-follicle activity where concentrated growth factors reach the scalp</li>
<li>Support for joint and soft-tissue repair through targeted, ultrasound-guided growth-factor delivery</li>
<li>An autologous preparation, made from your own blood, which minimises immune considerations</li>
<li>Minimally invasive sessions with limited downtime</li>
<li>The option to combine this regenerative plasma treatment with other therapies in a personalised plan</li>
</ul>
<p>Results are not guaranteed. The evidence base for concentrated plasma preparations compared with standard PRP is still developing, and a clinical assessment at Brockwell Healthcare decides whether Pure Plasma treatment is appropriate for your specific situation.</p>

<h2>The Pure Plasma Therapy Process at Brockwell Healthcare</h2>
<p>Every Pure Plasma therapy session at Brockwell Healthcare follows a clear clinical process, and nothing begins until your doctor confirms the treatment is appropriate and the preparation suits your specific concern.</p>
<h3>Step 1: Booking</h3>
<p>Get in touch with Brockwell Healthcare to arrange your Pure Plasma therapy Dubai consultation. The team helps you choose the right appointment for your main concern, whether that is skin rejuvenation, hair restoration, joint health or tissue repair.</p>
<h3>Step 2: Consultation and Assessment</h3>
<p>Your doctor reviews your symptoms, medical history, previous treatments, current medications and goals, then assesses the concern and target area clinically. Your doctor checks contraindications including active infection, active cancer, clotting disorders and pregnancy, and discusses whether Pure Plasma or standard PRP suits your clinical picture.</p>
<h3>Step 3: Blood Collection</h3>
<p>Your clinician draws a small volume of blood using a standard blood-draw procedure under sterile conditions. The volume depends on the treatment area and the amount of preparation required.</p>
<h3>Step 4: Processing</h3>
<p>The team processes the blood using a refined centrifugation protocol designed to produce a highly concentrated, purified plasma preparation. Processing usually takes 15 to 30 minutes, and the team checks the preparation for quality before delivery.</p>
<h3>Step 5: Delivery</h3>
<p>Your clinician delivers the Pure Plasma preparation using the method suited to the application. For joint and soft-tissue applications, delivery is under ultrasound guidance for precise placement. For the scalp, microinjections spread the preparation across the treatment area. For skin, your clinician introduces it through targeted injections or microneedling, depending on the confirmed protocol, and may use local anaesthetic depending on the area and your sensitivity.</p>
<h3>Step 6: Aftercare and Follow-Up</h3>
<p>After the session, you receive clear aftercare instructions for the treatment area and delivery method, usually covering activity, skincare or scalp care, and what to watch for in the days after. Follow-up appointments review your response and whether further sessions are appropriate.</p>

<h2>Why Choose Brockwell Healthcare for Pure Plasma Therapy</h2>
<ul>
<li>Every doctor-led plasma therapy session is planned and supervised by a DHA-licensed doctor with regenerative medicine expertise.</li>
<li>Your doctor assesses individually whether Pure Plasma or standard PRP fits your case.</li>
<li>The team performs blood collection, processing and delivery in a sterile clinical setting, following established protocols.</li>
<li>Ultrasound guidance directs joint and soft-tissue applications for precise placement.</li>
<li>A contraindication screen comes before any session is recommended.</li>
<li>Realistic outcomes are discussed honestly, including where the evidence currently stands.</li>
<li>Upfront pricing is confirmed before your first session, with no surprises.</li>
</ul>
"""

FAQS = [
    ("How is Pure Plasma different from standard PRP?",
     "Both Pure Plasma and standard PRP therapy use your own blood. The difference is in the processing method and the concentration achieved. Pure Plasma uses a more refined centrifugation protocol to produce a preparation with a higher platelet and growth-factor concentration and reduced red and white blood cell content. Whether that produces a meaningfully different clinical outcome depends on the indication and individual response."),
    ("What concerns can Pure Plasma therapy support?",
     "Pure Plasma treatment in Dubai may support skin rejuvenation, hair restoration, joint and soft-tissue repair and wound healing. Suitability depends on the specific concern and clinical assessment, and it is not appropriate for every condition."),
    ("Can Pure Plasma therapy improve skin quality?",
     "Pure Plasma for skin may support collagen production, skin texture, tone and cellular renewal. Results develop gradually over a course of sessions and vary between individuals, depending on skin type, age and biological response."),
    ("Can Pure Plasma therapy help with hair loss?",
     "Pure Plasma for hair loss delivers concentrated growth factors to the scalp to support follicle activity and calm follicle inflammation. Your doctor may consider it for androgenetic alopecia and hair thinning within a wider hair restoration plan. Results develop over several months, and individual response varies."),
    ("Can Pure Plasma therapy support joint health?",
     "Pure Plasma for joints may support tissue repair and ease inflammation in joints affected by cartilage wear or soft-tissue damage. Delivery is under ultrasound guidance for precise placement. Suitability depends on the specific joint condition and degree of involvement confirmed at assessment."),
    ("Is Pure Plasma therapy safe?",
     "Pure Plasma therapy is generally well tolerated when qualified doctors perform it with proper screening and sterile protocols. Because it uses your own blood, immune-rejection considerations are minimal. Your doctor reviews contraindications including active infection, cancer, clotting disorders and pregnancy before recommending any session."),
    ("Is Pure Plasma therapy painful?",
     "Blood collection involves the usual venepuncture discomfort. Delivery to the treatment area may cause mild discomfort depending on the site and method, and your clinician uses local anaesthetic where appropriate. Post-session soreness usually settles within a few days."),
    ("How long does one Pure Plasma therapy session take?",
     "A complete session, including blood collection, processing and delivery, usually takes 60 to 90 minutes, depending on the treatment area and the volume of preparation required. Your doctor confirms the expected duration at your consultation."),
    ("Is there downtime after Pure Plasma treatment?",
     "Downtime depends on the application. Most patients return to normal light activity within 24 to 48 hours. Your clinician provides specific activity restrictions and skincare or scalp care guidance after every session, based on the treatment area."),
    ("How many Pure Plasma therapy sessions are usually needed?",
     "It depends on the concern, the target area and individual response. Some conditions benefit from a single session tracked over several months, while others need a structured course. Your doctor confirms the recommended plan after the initial assessment."),
    ("When can results from Pure Plasma therapy be noticed?",
     "Results develop gradually over weeks to months. Skin and hair results typically become clearer over two to four months, while joint and tissue results may show within four to eight weeks. The timeline varies with the application and individual response."),
    ("Can Pure Plasma therapy be combined with other treatments?",
     "Yes. Pure Plasma therapy can complement red light therapy, shockwave therapy and other regenerative services at Brockwell Healthcare. Where patients ask about newer options such as exosome therapy, your doctor explains their current evidence and regulatory status. Your doctor advises on the most appropriate combination for your goals and assessment."),
    ("What is the cost of Pure Plasma therapy in Dubai?",
     "The cost depends on the treatment area, the preparation volume and the number of sessions. Brockwell Healthcare provides clear pricing and a full cost estimate before any session begins."),
    ("Who should avoid Pure Plasma therapy?",
     "Patients with active infection near the treatment area, active cancer without clearance, clotting disorders, anticoagulant medication, platelet dysfunction, pregnancy without clearance or serious uncontrolled systemic disease should not proceed with Pure Plasma treatment without speaking to a doctor first. All of this is reviewed during the consultation."),
    ("Do I need a consultation before Pure Plasma therapy in Dubai?",
     "Yes. A clinical assessment is required before any Pure Plasma therapy in Dubai begins. It confirms suitability, reviews the clinical rationale for Pure Plasma versus other options and lets your doctor build the right treatment plan, so nothing begins without it."),
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
        ("services", "0049_anti_aging_aesthetics_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
