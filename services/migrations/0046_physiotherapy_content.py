"""Load the full Physiotherapy content into the existing sub-service: keyword-rich
H1 (full, with tagline), SEO meta, styled rich-text sections (conditions and
techniques → card grids, process → numbered timeline via the enhance pipeline)
and the FAQ set. Photos are added later."""

from django.db import migrations

SEO_TITLE = "Physiotherapy in Dubai | Doctor-Led Rehabilitation | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Book physiotherapy in Dubai at Brockwell Healthcare for pain, injury recovery, "
    "mobility, sports rehabilitation and post-surgical care. Doctor-led physiotherapy with "
    "personalised treatment plans."
)
HERO_HEADING = "Physiotherapy in Dubai | Doctor-Led Rehabilitation & Recovery"
SLUG = "physiotherapy"
SUMMARY = (
    "Doctor-led physiotherapy in Dubai for pain, injury recovery, mobility, sports "
    "rehabilitation and post-surgical care."
)

DESCRIPTION = """
<p>Physiotherapy at Brockwell Healthcare is a doctor-led clinical service focused on restoring movement, reducing pain and rebuilding physical function through structured, evidence-based rehabilitation. It suits anyone whose movement, strength or recovery has been affected by injury, surgery, pain or a musculoskeletal condition, and who wants a proper, personalised clinical plan.</p>

<h2>What Is Physiotherapy?</h2>
<p>Physiotherapy is a clinical discipline focused on assessing, diagnosing and treating conditions that affect how the body moves and functions. It uses targeted exercise, manual therapy, movement correction and rehabilitation planning to restore strength, mobility and physical capacity after injury, surgery or the gradual effects of a musculoskeletal condition.</p>
<p>At Brockwell Healthcare, physiotherapy in Dubai sits alongside and complements the clinic's regenerative, sports medicine and orthopedic services. That means your physiotherapy plan can be coordinated with injection therapy, shockwave therapy, post-procedure recovery or a wider rehabilitation programme as a single, joined-up clinical plan, with your physiotherapist and the medical team working together.</p>

<h2>How Does Physiotherapy Work?</h2>
<p>Physiotherapy works by identifying the specific movement deficits, strength gaps, tissue restrictions or biomechanical patterns contributing to a patient's pain, limited function or slow recovery, then addressing them in a structured, progressive way.</p>
<p>Assessment always comes before exercise. Every physiotherapy rehabilitation plan at Brockwell Healthcare begins with a thorough assessment of the affected area and the factors contributing to the problem, including movement quality, strength testing, joint mobility, neural tension and how the whole kinetic chain is functioning, not only the symptomatic site.</p>
<p>Treatment is then built around what the assessment actually shows. This might involve hands-on manual therapy to release tissue restrictions, targeted exercise to rebuild strength and control, movement retraining to correct patterns that load the wrong structures, graded exposure to build tolerance in previously painful movements, and structured progression that advances at the right pace for each individual.</p>

<h2>Conditions We Treat With Physiotherapy</h2>
<p>Physiotherapy at Brockwell Healthcare addresses a wide range of musculoskeletal, sports-related and post-surgical conditions. The conditions below are the most frequent presentations, and the approach extends to any concern where movement, pain or physical function has been affected.</p>
<h3>Musculoskeletal Physiotherapy</h3>
<p>Musculoskeletal physiotherapy addresses neck pain, lower back pain, shoulder pain, hip pain, knee pain and other joint and soft-tissue concerns that have lasted weeks, months or longer. Assessment identifies the specific structures involved and the contributing factors before any treatment.</p>
<h3>Sports Injury Rehabilitation</h3>
<p>Ligament sprains, muscle strains, tendon conditions and joint injuries from sport or physical activity. Sports physiotherapy in Dubai at Brockwell Healthcare addresses both the injured tissue and the movement patterns, strength deficits and load-management issues that contributed to the injury.</p>
<h3>Post-Surgical Rehabilitation</h3>
<p>Recovery from orthopaedic surgery, including joint replacements, ligament reconstruction, rotator cuff repair and other procedures. A structured post-surgical physiotherapy plan lowers re-injury risk, supports tissue healing and restores strength and movement more reliably than unguided rest.</p>
<h3>Chronic Pain Conditions</h3>
<p>Long-term pain conditions, including fibromyalgia, chronic back pain and persistent joint pain that have not responded to standard approaches. Physiotherapy for chronic pain works by addressing movement avoidance, deconditioning, central sensitisation and the lifestyle factors behind ongoing symptoms, looking beyond the painful site.</p>
<h3>Neurological Rehabilitation</h3>
<p>Physiotherapy following stroke, neurological conditions or nerve injuries affecting movement and coordination. Plans focus on restoring as much function as possible through progressive, goal-directed rehabilitation.</p>
<h3>Post-Procedure Recovery</h3>
<p>After regenerative treatments including PRP therapy, stem cell therapy, shockwave therapy or hydrodissection, structured physiotherapy supports the tissue-repair process with appropriate loading and movement progression, so the area is neither overloaded too soon nor left under-used.</p>
<h3>Balance, Coordination and Falls Prevention</h3>
<p>For older adults or patients recovering from injury, improving balance and proprioception lowers the risk of future falls and supports confident, safe movement in daily life.</p>
<h3>Workplace and Postural Assessment</h3>
<p>Neck pain, shoulder tension, lower-back stiffness and headaches linked to desk-based or repetitive work are common presentations. Physiotherapy addresses both the symptoms and the postural and ergonomic factors driving them.</p>

<h2>Physiotherapy Treatments &amp; Techniques</h2>
<p>The specific techniques used in a session depend on the condition, the stage of recovery and what the assessment shows. Brockwell Healthcare draws on a range of established clinical approaches within each plan.</p>
<h3>Manual Therapy</h3>
<p>Hands-on treatment, including joint mobilisation, soft-tissue techniques and neural mobilisation, to address tissue restrictions, joint stiffness and movement limitations contributing to pain or reduced function.</p>
<h3>Targeted Exercise Rehabilitation</h3>
<p>Structured exercise programmes designed for your condition and stage of recovery, progressed systematically in step with how you respond.</p>
<h3>Movement Retraining and Biomechanical Correction</h3>
<p>Assessment and correction of movement patterns that load the wrong structures or contribute to recurrence. This matters particularly in sports injury rehabilitation and chronic pain management.</p>
<h3>Dry Needling</h3>
<p>A technique using fine needles to address myofascial trigger points contributing to pain and restricted movement, used selectively where clinically appropriate within a wider physiotherapy plan.</p>
<h3>Taping and Bracing</h3>
<p>Therapeutic taping and supportive bracing may offload structures, support movement patterns and aid rehabilitation in certain conditions.</p>
<h3>Electrotherapy</h3>
<p>Selected electrotherapy modalities, including TENS and ultrasound therapy, may support pain relief and tissue healing where clinically indicated.</p>
<h3>Education and Self-Management</h3>
<p>Understanding your condition, your pain behaviour and the role of movement in recovery is a critical part of effective physiotherapy. Your physiotherapist teaches you self-management strategies, so you can support your own recovery between sessions and hold your progress over the long term.</p>

<h2>Benefits of Doctor-Led Physiotherapy</h2>
<p>Physiotherapy may offer several potential benefits when assessment and treatment are properly structured around your specific condition and goals. Results depend on the condition, its severity and duration, your engagement with the rehabilitation process and individual response.</p>
<p>Possible benefits include:</p>
<ul>
<li>Less pain as the contributing structural and movement factors are found and addressed</li>
<li>Better strength, coordination and movement quality through progressive, targeted movement rehabilitation</li>
<li>A safer return to daily activity, work or sport, guided by a structured injury rehabilitation programme</li>
<li>Lower re-injury risk once movement patterns, strength deficits and load are corrected alongside the tissue</li>
<li>Physical performance restored to previous levels, or improved, when rehabilitation is thorough and well progressed</li>
<li>Progress on chronic pain and long-term limitations, where care looks beyond the symptomatic site</li>
<li>Self-management strategies that keep benefiting you well beyond the course of treatment</li>
</ul>
<p>Results are not guaranteed and vary with the condition, its duration and your engagement with the rehabilitation process. A clinical assessment at Brockwell Healthcare decides what is realistic before any plan begins.</p>

<h2>The Physiotherapy Process at Brockwell Healthcare</h2>
<p>Every physiotherapy rehabilitation plan at Brockwell Healthcare starts with a proper clinical assessment, and your physiotherapist prescribes nothing until they understand what is actually driving your symptoms.</p>
<h3>Step 1: Booking</h3>
<p>Get in touch with Brockwell Healthcare to arrange your physiotherapy Dubai consultation. The team helps you choose the right appointment for your main concern, whether that is a specific injury, chronic pain, post-surgical recovery or general movement and rehabilitation support.</p>
<h3>Step 2: Assessment</h3>
<p>Your physiotherapist takes a full clinical history covering your symptoms, how they started, what makes them better or worse, your activity level and what you want to get back to. They then assess your movement quality, strength, joint range and functional capacity, and review relevant imaging where available.</p>
<h3>Step 3: Personalised Rehabilitation Plan</h3>
<p>From the assessment, your physiotherapist creates a specific rehabilitation plan around your condition and goals. This covers the techniques to be used, the frequency and duration of sessions, your home exercise programme and the criteria for progressing through the plan.</p>
<h3>Step 4: Treatment Sessions</h3>
<p>A qualified physiotherapist delivers each session using the techniques confirmed in your plan. Your physiotherapist assesses progress at each session and adjusts the plan around your response.</p>
<h3>Step 5: Discharge and Self-Management</h3>
<p>Once your goals are met and you have the tools to maintain and continue your progress independently, your physiotherapist provides a discharge plan. This includes a home programme, activity guidance and clear advice on when to return if symptoms recur.</p>

<h2>Why Choose Brockwell Healthcare for Physiotherapy</h2>
<ul>
<li>A qualified physiotherapist builds every plan from a proper assessment, within a DHA-licensed clinic.</li>
<li>Physiotherapy is integrated with the clinic's regenerative, sports medicine and orthopedic services, so your rehabilitation is coordinated with other treatments as one plan.</li>
<li>Each plan is personalised to your specific condition, movement findings and goals.</li>
<li>Progression follows your clinical response, not a fixed calendar.</li>
<li>Realistic outcomes are discussed honestly before any rehabilitation plan begins.</li>
<li>Upfront pricing is confirmed before your first session, with no surprises.</li>
</ul>
"""

FAQS = [
    ("Do I need a referral before physiotherapy?",
     "No formal referral is required. You can contact Brockwell Healthcare directly to book a physiotherapy consultation Dubai, and the team helps you choose the right appointment for your concern and advises on what to bring."),
    ("When should I see a physiotherapist for ongoing pain?",
     "If pain or a movement problem has lasted more than one to two weeks despite rest, keeps coming back, limits your normal activity or is not improving as you would expect, a physiotherapy assessment is the right next step."),
    ("Is doctor-led physiotherapy painful?",
     "Some techniques, including manual therapy or dry needling, may cause temporary discomfort during the session, which usually settles quickly. Exercise-based rehabilitation may involve mild muscle soreness as strength and movement capacity are progressively challenged. Your physiotherapist explains what to expect before using any technique."),
    ("How long does one physiotherapy session take?",
     "Sessions typically take 45 to 60 minutes, depending on the condition, the stage of recovery and the techniques used. Your physiotherapist confirms the expected duration at your initial consultation."),
    ("How many physiotherapy sessions are usually needed?",
     "It varies considerably with the condition, its duration and severity, and how consistently you follow the programme. Acute injuries may resolve in a small number of sessions, while chronic conditions or post-surgical rehabilitation usually need a longer structured programme. Your physiotherapist gives an honest estimate after the initial assessment."),
    ("Can physiotherapy help with chronic pain?",
     "Physiotherapy for chronic pain may help by addressing movement avoidance, deconditioning, lifestyle factors and the biomechanical contributors to ongoing symptoms, looking beyond the painful site. Results vary with the nature and duration of the pain and your engagement with the rehabilitation process."),
    ("Can physiotherapy be combined with other treatments at Brockwell Healthcare?",
     "Yes. Physiotherapy at Brockwell Healthcare is designed to work alongside regenerative treatments, injection therapy, shockwave therapy and other services within one coordinated clinical plan. Your physiotherapist works with the broader clinical team so rehabilitation complements the other treatments you are receiving."),
    ("What should I wear to a physiotherapy session?",
     "Wear comfortable clothing that lets your physiotherapist assess and treat the affected area easily. For lower-limb conditions, shorts help. For upper-limb or shoulder conditions, a vest or loose top works well."),
    ("What is the cost of physiotherapy in Dubai?",
     "The cost depends on the session type, duration and the number of sessions in your rehabilitation plan. Brockwell Healthcare provides clear pricing and a full cost estimate before your first session begins."),
    ("Is physiotherapy at Brockwell Healthcare DHA-regulated?",
     "Yes. All clinical services at Brockwell Healthcare operate within a DHA-licensed facility and follow the regulatory standards required for medical practice in Dubai."),
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
        ("services", "0045_genomics_medicine_content"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
