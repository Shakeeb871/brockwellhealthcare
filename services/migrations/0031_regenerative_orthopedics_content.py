"""Load the full Regenerative Orthopedics content: keyword-rich H1, SEO meta,
styled rich-text sections (conditions and treatments → card grids, process →
numbered timeline via the enhance pipeline), two clinical photos and the FAQ
set."""

from django.db import migrations

SEO_TITLE = "Regenerative Orthopedic Treatment in Dubai | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led non-surgical regenerative orthopedic treatment in Dubai for joint pain, "
    "cartilage wear, tendon and sports injuries. PRP, stem cell and ultrasound-guided care."
)
HERO_HEADING = "Regenerative Orthopedic Treatment in Dubai"
SUMMARY = (
    "Doctor-led non-surgical regenerative orthopedic treatment for joint pain, cartilage "
    "wear, tendon and sports injuries."
)

DESCRIPTION = """
<p>Regenerative orthopedic treatment is a doctor-led approach to joint and tissue repair that uses biologic therapies to address the underlying cause of pain, stiffness and reduced mobility. Patients often choose it when they want a structured, non-surgical alternative to surgery or long-term pain medication.</p>

<h2>What Is Regenerative Orthopedic Treatment?</h2>
<p>Regenerative orthopedic treatment uses biologic therapies, including PRP therapy, stem cell treatment, hyaluronic acid injections, prolotherapy and shockwave therapy, to support tissue repair, ease inflammation and improve joint function at the structural level. The goal is to address what is actually happening inside the joint or soft tissue and create the conditions for meaningful, lasting recovery.</p>
<p>At Brockwell Healthcare, we use regenerative orthopedic care in Dubai mainly for joint pain, cartilage wear, tendon and ligament injuries, sports injuries, and conditions where conventional treatment has not brought enough lasting improvement. Every plan begins with a thorough clinical and imaging assessment, and DHA-licensed physicians carry out treatment within the UAE's regulatory frameworks. When a joint is too far gone for biologics to help, we say so plainly and guide you toward the right surgical care.</p>

<h2>How Does Regenerative Orthopedic Treatment Work?</h2>
<p>Most joint and soft-tissue problems share a pattern. Cartilage wears down. Tendons degenerate from overuse. Ligaments stretch or tear. Joints lose lubrication. Inflammation turns chronic instead of settling. The body's repair capacity in these structures is limited, partly because cartilage and tendons have a poor blood supply, so the healing signals that work elsewhere in the body struggle to reach them.</p>
<p>Regenerative orthopedic therapy delivers biologic agents straight to the affected structure under ultrasound guidance. PRP delivers concentrated growth factors from your own blood to stimulate repair and calm inflammation. Stem cell treatment introduces cells that may support tissue repair, considered for selected patients after a full discussion of suitability and realistic expectations. Hyaluronic acid restores joint lubrication. Prolotherapy triggers the body's own repair response in ligaments and tendons. Shockwave therapy delivers acoustic energy to degenerated tissue to reset the repair process. Each therapy targets a different part of the structural problem, based on what your assessment shows.</p>

<img src="/static/img/services/regenerative-orthopedics-content.webp" alt="Ultrasound-guided regenerative knee injection at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>Joint &amp; Tissue Conditions We Treat</h2>
<p>Each condition below needs individual clinical assessment before any treatment. Suitability depends on the diagnosis, severity, duration and previous treatment history.</p>
<h3>Knee Pain and Osteoarthritis</h3>
<p>Knee pain from cartilage wear, early osteoarthritis, meniscal degeneration or inflammatory joint disease is one of the most common concerns we see. Regenerative knee treatment may involve PRP, hyaluronic acid, stem cell therapy or a combination, depending on the degree of joint involvement confirmed on assessment and imaging.</p>
<h3>Shoulder Pain and Rotator Cuff Injuries</h3>
<p>Rotator cuff tears, impingement, tendinopathy and chronic shoulder pain affect movement, sleep and daily function. Regenerative shoulder treatment targets the specific structure involved, whether tendon, bursa or joint, through ultrasound-guided biologic delivery.</p>
<h3>Hip Pain</h3>
<p>Hip pain from cartilage wear, labral irritation or surrounding soft-tissue inflammation can restrict walking, sitting and movement. Ultrasound-guided injection therapy and regenerative approaches may support joint health and ease pain in selected patients, depending on the structural involvement.</p>
<h3>Ankle and Foot Conditions</h3>
<p>Ligament injuries, tendon degeneration and joint pain in the ankle and foot affect balance, walking and performance. Regenerative ankle treatment and shockwave therapy for plantar fasciitis may shorten recovery and support longer-term joint stability in selected patients.</p>
<h3>Tennis Elbow and Golfer's Elbow</h3>
<p>Tendon degeneration at the elbow from repetitive strain causes pain that reaches into daily tasks and sport. PRP injection therapy and shockwave therapy are among the most common regenerative approaches here, once rest and physiotherapy have not brought lasting relief.</p>
<h3>Achilles Tendinopathy</h3>
<p>Achilles tendon pain from overuse or degeneration can turn chronic without proper management. Regenerative Achilles treatment using PRP, prolotherapy or shockwave therapy may support tendon repair and ease pain in patients who have not responded to conservative care.</p>
<h3>Lower Back Pain</h3>
<p>Disc-related discomfort, facet-joint irritation and soft-tissue pain in the lower back affect posture, movement and daily function. A regenerative assessment identifies the specific structure involved before any treatment.</p>
<h3>Sports Injuries</h3>
<p>Ligament sprains, muscle tears, tendon injuries and joint stress from sport may benefit from regenerative support when standard recovery has stalled. Regenerative sports-injury treatment may shorten recovery and support a fuller return to activity.</p>
<h3>Cartilage Damage</h3>
<p>Cartilage regeneration therapy using stem cell treatment or PRP may be considered when imaging confirms cartilage thinning or damage driving joint pain and stiffness. The degree of involvement guides which approach fits best.</p>

<h2>Our Regenerative Orthopedic Treatments</h2>
<p>The treatment depends on your condition, the structure involved, the degree of damage and your clinical assessment. Brockwell selects the right option, or combination, after reviewing your case in full.</p>
<h3>Platelet-Rich Plasma (PRP) Therapy</h3>
<p>PRP injection therapy concentrates growth factors from your own blood and delivers them precisely to the affected joint or tissue under ultrasound guidance. It may support tendon repair, ease inflammation and improve joint health over time, and it is one of the most widely used and studied regenerative orthopedic treatments.</p>
<h3>Stem Cell Therapy</h3>
<p>Your doctor may consider stem cell therapy when joint or tissue damage is more advanced, or when other approaches have not helped enough. It uses cells from your own bone marrow, as a bone marrow aspirate concentrate (BMAC), or from adipose tissue, as a stromal vascular fraction. Your doctor assesses suitability individually and discusses it in detail, including the current evidence, at your consultation.</p>
<h3>Hyaluronic Acid Injection</h3>
<p>Restores lubrication inside a joint where thinning cartilage has cut its natural cushioning. It may improve joint comfort and movement mechanics, and while it is most common in the knee, it suits other joints too, depending on the assessment.</p>
<h3>Prolotherapy</h3>
<p>A solution injected into damaged ligaments or tendons to stimulate the body's own repair and strengthening response. It suits chronic ligament laxity, tendon degeneration and joint instability where connective tissue has not recovered through rest or physiotherapy.</p>
<h3>Shockwave Therapy (ESWT)</h3>
<p>Extracorporeal shockwave therapy delivers focused acoustic energy to degenerated tendon or soft tissue to reset the repair process. It suits chronic tendinopathies, including Achilles, patellar, rotator cuff and tennis elbow, when conservative treatment has not been enough.</p>
<h3>Ultrasound-Guided Injection Therapy</h3>
<p>Your doctor uses real-time ultrasound to guide every injection to the exact location of the affected structure, whether PRP, hyaluronic acid, prolotherapy or an anti-inflammatory injection. Placement accuracy directly affects how well the treatment works.</p>
<h3>Ozone Therapy for Joints</h3>
<p>Medical ozone delivered into or around a joint may support anti-inflammatory processes and tissue oxygenation in selected patients, sometimes alongside PRP or hyaluronic acid within a combined regenerative plan.</p>

<h2>Benefits of Doctor-Led Regenerative Orthopedic Care</h2>
<p>For selected patients, when the right treatment is matched to the right condition through proper assessment, regenerative orthopedic care may offer several benefits.</p>
<p>Potential benefits include:</p>
<ul>
<li>Less joint pain and stiffness as inflammation eases and tissue repair gains support</li>
<li>Better mobility and range of movement over a course of treatment</li>
<li>Stronger tendon and ligament recovery, beyond what rest alone tends to achieve</li>
<li>Better-preserved cartilage health when treatment starts before severe structural loss</li>
<li>A non-surgical pathway for patients who want to delay or avoid surgery</li>
<li>Lower rejection risk, since autologous protocols use your own cells</li>
<li>A minimally invasive route with limited downtime next to surgery</li>
<li>Care that combines with physiotherapy, shockwave and other regenerative approaches in one plan</li>
<li>Sharper accuracy at every injection through ultrasound guidance</li>
</ul>
<p>Results are never guaranteed. A clinical assessment at Brockwell decides whether regenerative orthopedic care in Dubai suits your condition.</p>

<h2>The Regenerative Orthopedic Treatment Process at Brockwell Healthcare</h2>
<p>Every plan follows a clear clinical process, and your doctor confirms the treatment type, delivery method and session plan before anything begins.</p>
<h3>Step 1: Booking</h3>
<p>Contact Brockwell Healthcare to arrange your consultation. The team matches you to the right appointment for your main concern, whether that is knee pain, a shoulder injury, tendon degeneration, sports recovery or general joint health.</p>
<h3>Step 2: Clinical Assessment and Imaging Review</h3>
<p>Your doctor reviews your symptoms, medical history, how long the condition has lasted, past treatments, imaging and goals, then assesses the joint, tendon or tissue clinically. Ultrasound may help visualise the affected structure in real time before any plan is set, and your doctor screens for contraindications such as infection, clotting disorders, recent corticosteroid injections, active cancer and systemic disease.</p>
<h3>Step 3: Personalised Treatment Plan</h3>
<p>From the assessment and imaging, your doctor builds a plan around your diagnosis and needs, whether that means one therapy or a combination. You hear what each treatment does, why it was chosen, what the procedure involves, how many sessions you are likely to need and what realistic outcomes look like. The cost is confirmed before anything begins.</p>
<h3>Step 4: Treatment Procedure</h3>
<p>Your clinician delivers each treatment in a sterile clinical setting, under ultrasound guidance for injection-based therapy. For PRP, the team takes a small blood sample, processes it and delivers it to the target. For stem cell treatment, harvesting, processing and injection happen in a structured sequence on the same day. For shockwave therapy, your clinician applies the device over the site using the confirmed protocol. For hyaluronic acid or prolotherapy, the solution goes precisely to the intended structure under real-time imaging. The clinical team monitors every procedure throughout.</p>
<h3>Step 5: Aftercare and Follow-Up</h3>
<p>Afterwards, you receive clear aftercare instructions for the treatment delivered, usually covering rest, activity limits, physiotherapy timing and warning signs to watch. Follow-up visits review your pain, mobility and function, and your doctor adjusts the plan around your response and discusses further sessions where clinically appropriate.</p>

<h2>Why Choose Brockwell Healthcare for Regenerative Orthopedics</h2>
<ul>
<li>A DHA-certified doctor with specialist training in biologic orthopedic therapies builds every plan.</li>
<li>Ultrasound guidance directs every injection-based procedure for precise, accurate delivery.</li>
<li>Multiple biologic options sit under one clinical framework, so the right approach fits each condition.</li>
<li>A full contraindication screen comes before any regenerative orthopedic therapy begins.</li>
<li>Realistic outcomes are discussed honestly, including the limits of biologics for advanced joint disease.</li>
<li>Follow-up reviews track your response and adjust the plan over time.</li>
<li>Upfront pricing is confirmed before your first session, with no surprises.</li>
</ul>
"""

FAQS = [
    ("What conditions can regenerative orthopedic treatment help with?",
     "Regenerative orthopedic care in Dubai may help with knee pain and osteoarthritis, rotator cuff injuries, hip pain, ankle and foot conditions, tennis elbow, Achilles tendinopathy, lower back pain, sports injuries and cartilage damage. Suitability depends on the diagnosis, severity and treatment history."),
    ("Are regenerative orthopedic treatments regulated in the UAE?",
     "Yes. DHA-licensed physicians deliver them within the Dubai Health Authority and UAE Ministry of Health frameworks, and your suitability is confirmed by clinical assessment first."),
    ("Can regenerative orthopedic treatment replace surgery?",
     "For selected patients, non-surgical regenerative approaches may delay or avoid surgery, especially when the condition is caught before significant structural damage. It is not a guaranteed alternative, though, and suitability depends on the diagnosis and the degree of joint involvement on imaging."),
    ("Which regenerative treatment is best for knee pain?",
     "It depends on the cause and severity on assessment and imaging. Early cartilage changes may respond to PRP injection therapy or hyaluronic acid, while more advanced involvement may benefit from stem cell treatment. Your doctor selects the right option after reviewing your specific picture."),
    ("Is PRP therapy effective for tendon injuries?",
     "PRP injection therapy is one of the most studied regenerative approaches for tendon conditions, including rotator cuff, Achilles, tennis elbow and patellar tendinopathy. It may support repair and reduce chronic inflammation in selected patients, though results vary with the tendon, the degree of degeneration and individual response."),
    ("Is regenerative orthopedic treatment painful?",
     "Most procedures bring mild discomfort at the injection site, which local anaesthetic keeps low. Shockwave therapy can feel moderately uncomfortable depending on the energy level and the area's sensitivity. Most patients tolerate treatment well and return to light activity within a few days."),
    ("How long does one session take?",
     "It depends on the treatment. PRP usually takes 45 to 90 minutes including blood processing; stem cell treatment two to three hours including harvesting and processing; shockwave 15 to 30 minutes; and hyaluronic acid or prolotherapy 20 to 40 minutes. Your doctor confirms the time at your consultation."),
    ("Is there downtime after treatment?",
     "It varies by treatment. Most injection procedures call for 24 to 48 hours of relative rest, then a graded return to activity over one to two weeks. Shockwave needs 24 to 48 hours of reduced loading. Your clinician gives specific aftercare each session."),
    ("How many sessions will I need?",
     "It depends on the treatment, the condition and your response. Some patients benefit from a single PRP or stem cell session, shockwave usually runs three to six sessions, and hyaluronic acid may be given as a course. Your doctor confirms the plan after assessment."),
    ("When will I notice results?",
     "Early gains in pain or mobility may show within four to six weeks. Fuller results usually build over three to six months as tissue repair progresses, and shockwave results tend to develop over four to eight weeks after the course. The timeline depends on the condition, severity and your response."),
    ("Can regenerative orthopedic treatments be combined?",
     "Yes. Regenerative orthopedic care in Dubai at Brockwell can combine PRP, stem cell treatment, hyaluronic acid, prolotherapy, shockwave therapy and physiotherapy in one plan. Your doctor advises on the right combination for your diagnosis and goals."),
    ("What should I do before a session?",
     "Follow your clinic's guidance for your treatment type. In general, bring recent imaging, tell your doctor about any medication changes, avoid anti-inflammatory medication in the days before injection-based treatments, and arrange transport home after stem cell procedures."),
    ("What should I do afterwards?",
     "Follow your clinician's aftercare, which usually covers rest, activity limits, physiotherapy timing and avoiding anti-inflammatory medication for a set period after injection-based treatments. Attend your follow-ups, and contact Brockwell if anything feels unexpected."),
    ("Who should avoid regenerative orthopedic treatment?",
     "It does not suit patients with an active infection near the treatment area, clotting disorders, active cancer without specialist clearance, pregnancy without clearance, severe joint destruction that needs surgery, or (for shockwave) a corticosteroid injection at the same site within the past six weeks. The consultation reviews all contraindications first."),
    ("What does regenerative orthopedic treatment cost in Dubai?",
     "Cost depends on the treatment type, the joint or tissue area, the number of sessions and the protocol. You receive clear pricing and a full estimate before any treatment begins."),
    ("Do I need a consultation first?",
     "Yes. A clinical assessment and imaging review come before any regenerative orthopedic treatment in Dubai. It confirms the diagnosis, checks contraindications and lets your doctor build the right plan, so nothing begins without it."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    svc = Service.objects.filter(region="uae", slug="regenerative-orthopedics").first()
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
        ("services", "0030_urology_content"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
