"""Load the full Ultrasound Diagnostics content: keyword-rich H1, SEO meta,
styled rich-text sections (scan types → card grid, process → numbered timeline
via the enhance pipeline), two clinical photos and the FAQ set."""

from django.db import migrations

SEO_TITLE = "Ultrasound Diagnostics in Dubai | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led ultrasound diagnostics in Dubai for abdominal, pelvic, musculoskeletal, "
    "vascular, soft-tissue and pregnancy imaging, with clear same-visit results."
)
HERO_HEADING = "Ultrasound Diagnostics in Dubai"
SUMMARY = (
    "Doctor-led ultrasound diagnostics in Dubai for abdominal, pelvic, musculoskeletal, "
    "vascular, soft-tissue and pregnancy imaging, with clear same-visit results."
)

DESCRIPTION = """
<p>Ultrasound diagnostics is a non-invasive imaging service that uses sound waves to create real-time images of organs, soft tissue, blood vessels and musculoskeletal structures. It gives your doctor a clear view of what is happening inside the body, without radiation, surgery or long waits.</p>

<h2>What Are Ultrasound Diagnostics?</h2>
<p>Ultrasound diagnostics uses high-frequency sound waves, sent into the body by a small handheld device called a transducer. The waves bounce back from internal structures, and the system turns those echoes into live images on a screen. From there, the doctor assesses organs, tissue, fluid, blood flow and structural changes in real time, as the scan happens.</p>
<p>At Brockwell Healthcare, our medical imaging in Dubai covers a full range of scans, from abdominal, pelvic and musculoskeletal to vascular, soft-tissue and pregnancy imaging. It also guides clinical procedures such as injections and hydrodissection, where precise needle placement matters. A DHA-certified doctor reviews every scan and explains the findings clearly, so you know what was found and what comes next.</p>

<h2>How Do Ultrasound Diagnostics Work?</h2>
<p>Your clinician applies a small amount of gel to the skin over the area being scanned, then places the transducer against it and moves it slowly across the surface. The transducer sends sound waves into the body and picks up the echoes that return from different structures, and the system processes those echoes into images on the monitor in real time.</p>
<p>Different structures reflect sound differently. Fluid-filled areas, such as cysts or the bladder, show up dark, while solid structures like organs and tissue appear in shades of grey. For blood flow, Doppler ultrasound adds colour and speed to the picture. Because it all happens live, the doctor can watch movement, check blood flow and judge structural changes as they occur, rather than from a single frozen image.</p>
<p>Most external scans feel comfortable. A few specialised scans, such as certain pelvic or prostate assessments, use a small internal probe for a closer view, and your clinician explains exactly what the scan involves before it begins.</p>

<img src="/static/img/services/ultrasound-diagnostics-content.webp" alt="Patient undergoing an ultrasound scan at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>Types of Ultrasound Scans at Brockwell Healthcare</h2>
<p>The right scan depends on your symptom, the body area and the clinical reason for imaging. Brockwell chooses it after reviewing your concern and referral details.</p>
<h3>Abdominal Ultrasound</h3>
<p>Assesses the liver, gallbladder, pancreas, spleen, kidneys and abdominal blood vessels. Useful for upper abdominal pain, bloating, abnormal blood tests, suspected gallstones and kidney concerns.</p>
<h3>Pelvic Ultrasound</h3>
<p>Assesses the uterus, ovaries and surrounding structures in women, and the bladder, prostate and nearby structures in men. Useful for pelvic pain, abnormal bleeding, urinary symptoms, ovarian cysts and fibroids.</p>
<h3>Kidney and Bladder Ultrasound</h3>
<p>Checks kidney size, swelling, stones and cysts, along with how well the bladder empties. Useful for urinary pain, blood in the urine, recurrent infections and incomplete emptying.</p>
<h3>Musculoskeletal Ultrasound</h3>
<p>Assesses muscles, tendons, ligaments, joints and surrounding soft tissue. Useful for tendon pain, ligament strain, muscle injury, bursitis and joint swelling.</p>
<h3>Soft Tissue and Lump Assessment</h3>
<p>Evaluates lumps, bumps and swelling under the skin to tell whether they are fluid-filled, solid or attached to surrounding tissue, before any clinical decision is made.</p>
<h3>Doppler Ultrasound</h3>
<p>Assesses blood flow direction and speed through selected vessels, including the head, neck, abdominal aorta and legs. Useful for circulation concerns, limb swelling and follow-up after vascular procedures. A full vascular Doppler assessment of the head, neck, abdominal aorta and legs usually takes around 90 minutes.</p>
<h3>Pregnancy Ultrasound</h3>
<p>Monitors foetal development, confirms gestational age, assesses the placenta and checks amniotic fluid. It also covers early-pregnancy concerns, including ectopic-pregnancy assessment and evaluation of early bleeding.</p>
<h3>Breast Ultrasound</h3>
<p>Assesses lumps, pain, skin changes or findings from an examination or mammogram, and helps tell whether a breast lump looks solid or fluid-filled. It often works alongside mammography, especially with denser breast tissue.</p>
<h3>Thyroid Ultrasound</h3>
<p>Assesses the size, structure and appearance of the thyroid gland and nearby lymph nodes. Useful for neck lumps, abnormal thyroid results, swallowing difficulty and known thyroid conditions.</p>
<h3>Ultrasound-Guided Procedures</h3>
<p>Uses real-time imaging to guide needle placement during injections, hydrodissection and aspiration, so the doctor confirms exact positioning before delivering any solution or withdrawing fluid.</p>

<h2>Benefits of Ultrasound Diagnostics</h2>
<p>Ultrasound is one of the most widely used imaging tools in medicine, for good reason. What each scan reveals depends on the type, the area and the concern being investigated.</p>
<p>Key benefits include:</p>
<ul>
<li>No radiation, which makes it safe for repeat scans and for most patients, including during pregnancy</li>
<li>Real-time imaging, so the doctor sees movement, blood flow and structural change as it happens</li>
<li>Non-invasive, with no needles, incisions or anaesthesia for most scans</li>
<li>A single session that can cover several structures, from organs to vessels to soft tissue</li>
<li>Precise guidance for procedures such as injections and hydrodissection</li>
<li>Findings reviewed and explained during or soon after the scan</li>
<li>Broad use across many concerns and body systems</li>
<li>Comfortable for most patients, with little or no preparation for many scans</li>
</ul>

<h2>The Ultrasound Diagnostics Process at Brockwell Healthcare</h2>
<p>Every scan follows a clear clinical process, and we confirm your scan type and any preparation before your appointment, so you arrive ready.</p>
<h3>Step 1: Booking</h3>
<p>Contact Brockwell Healthcare and share your symptoms, referral reason or the area you need imaged. The team confirms the right scan and explains any preparation, such as fasting or a full bladder, depending on the scan.</p>
<h3>Step 2: Preparation and Arrival</h3>
<p>Arrive having followed any instructions given. Some abdominal scans need a few hours of fasting; some pelvic and bladder scans need a full bladder; many scans need nothing at all. The team tells you what applies when you book.</p>
<h3>Step 3: The Scan</h3>
<p>You sit or lie down, depending on the area. Your clinician applies gel to help the transducer make good contact, then moves it slowly over the area while watching the live images. Most scans feel like light pressure; a tender or swollen area may feel slightly uncomfortable, though the scan itself is not painful. For certain pelvic or prostate assessments, your clinician may use a small internal probe with your consent. Most scans take 15 to 45 minutes, depending on the area and detail needed.</p>
<h3>Step 4: Results and Next Steps</h3>
<p>The appropriate clinician reviews your findings during and after the session, and you leave with clear guidance on what the scan showed and what comes next. That might mean monitoring, further testing, treatment, a guided procedure or a specialist referral.</p>

<h2>Why Patients Choose Brockwell Healthcare for Ultrasound Diagnostics</h2>
<ul>
<li>A DHA-certified doctor with imaging expertise performs and reviews every scan.</li>
<li>A full range of medical imaging sits under one roof, from abdominal and pelvic to musculoskeletal, vascular, soft-tissue and guided-procedure scans.</li>
<li>Real-time findings are explained clearly, so you understand what was found and what comes next.</li>
<li>Ultrasound guidance is on hand for injections, hydrodissection and aspiration that need precise placement.</li>
<li>Your preparation is confirmed before the appointment, so you arrive ready.</li>
<li>Results are reviewed promptly and the next steps spelled out plainly.</li>
<li>Upfront pricing is confirmed before your scan, with no surprises.</li>
</ul>
"""

FAQS = [
    ("What can ultrasound diagnostics detect?",
     "Ultrasound diagnostics in Dubai can detect gallstones, kidney stones, cysts, organ enlargement, tendon and ligament injuries, soft-tissue lumps, joint effusions, vascular abnormalities, ovarian cysts, fibroids and foetal development concerns, among other structural changes. Some conditions still need MRI or CT for a full picture."),
    ("Is ultrasound imaging safe?",
     "Yes. Ultrasound uses sound waves rather than ionising radiation, which makes it safe for repeat scans and for most patients. It is one of the most established imaging modalities in medicine."),
    ("Is an ultrasound scan painful?",
     "Most scans are not painful. You may feel light pressure from the transducer, especially over a tender or swollen area. Internal probes for certain pelvic or prostate assessments can bring brief discomfort, but most patients tolerate them well."),
    ("How long does a scan take?",
     "Most scans take 15 to 45 minutes, depending on the area, the type and the detail needed. A full vascular Doppler assessment of the head, neck, abdominal aorta and legs usually takes around 90 minutes. The team confirms the expected time when you book."),
    ("Do I need to prepare?",
     "It depends on the scan. Some abdominal scans need fasting; some pelvic and bladder scans need a full bladder; many need nothing at all. Brockwell gives you specific instructions before your appointment."),
    ("What is Doppler ultrasound used for?",
     "Doppler ultrasound assesses the direction and speed of blood flow through vessels. It helps with circulation concerns, limb swelling, arterial and venous disease and follow-up after vascular procedures, showing what standard imaging alone cannot."),
    ("Can ultrasound guide injections and procedures?",
     "Yes. Ultrasound-guided procedures use live imaging to confirm precise needle placement before an injection, hydrodissection or aspiration, which improves accuracy and lowers the risk of misplacement."),
    ("Can ultrasound detect cancer?",
     "Ultrasound can flag structural changes, lumps and abnormalities that need further investigation, but it cannot diagnose cancer on its own. If a finding raises concern, your doctor advises on the next step, which may include a biopsy, MRI or specialist referral."),
    ("What is the difference between ultrasound, MRI and CT?",
     "Ultrasound uses sound waves, gives real-time images and involves no radiation. CT uses X-rays for detailed cross-sectional images, useful for dense structures and trauma. MRI uses magnetic fields and suits detailed soft-tissue, neurological and joint assessment. Your doctor picks the right one for your symptoms."),
    ("Is ultrasound safe during pregnancy?",
     "Yes. Pregnancy ultrasound is considered safe throughout pregnancy for medical assessment. It is a cornerstone of antenatal care, used to monitor foetal development, confirm dates, assess the placenta and check on early-pregnancy concerns."),
    ("What does ultrasound diagnostics cost in Dubai?",
     "Cost depends on the scan type, the area assessed and whether it includes a guided procedure. You receive clear pricing and a full estimate before your appointment begins."),
    ("Do I need a referral?",
     "Not always. You can contact Brockwell directly to book a scan for symptoms you want investigated, and the team confirms the right scan type and any preparation before your appointment."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    svc = Service.objects.filter(region="uae", slug="ultrasound-diagnostics").first()
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
        ("services", "0023_ketamine_therapy_content"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
