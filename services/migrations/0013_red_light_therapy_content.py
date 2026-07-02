"""Load the full Red Light Therapy content: styled rich-text sections, SEO meta
and FAQs. Rendered through the site's `.prose` styles + the `enhance` filter so
the process becomes a timeline and bullet lists become icon lists — matching the
other service pages. The hero image is auto-detected from
static/img/services/red-light-therapy-hero.webp by the view."""

from django.db import migrations

SEO_TITLE = "Red Light Therapy in Dubai | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Medical-grade red light therapy in Dubai for skin, muscle recovery and wellness. "
    "DHA-certified, non-invasive and personalised. Book your consultation today."
)
SUMMARY = (
    "Non-invasive red and near-infrared light therapy for skin health, muscle recovery and wellness."
)

DESCRIPTION = """
<p>Red light therapy is a non-invasive, light-based treatment that uses red and near-infrared wavelengths to support skin health, muscle recovery and everyday wellness. It is a gentle, needle-free option with little to no downtime, which is why so many patients add it to their care.</p>

<img src="/static/img/services/red-light-therapy-content.webp" alt="Red light therapy in Dubai at Brockwell Healthcare" loading="lazy" decoding="async">

<h2>What Is Red Light Therapy?</h2>
<p>Red light therapy uses focused wavelengths of red and near-infrared light to support the skin and the tissue beneath it. Your cells absorb this light and put it to work, driving the body's own repair and recovery. There is no UV, no tanning and no heat that could harm tissue. It is a calm, non-thermal treatment. At Brockwell Healthcare, every session runs on medical-grade equipment and begins only after a proper clinical assessment.</p>

<h2>How Does Red Light Therapy Work?</h2>
<p>Red and near-infrared light work through photobiomodulation, a mechanism also known as low-level laser therapy. When the light reaches your cells, the mitochondria, the tiny engines that power each cell, absorb it and produce more ATP, the body's cellular fuel. With more energy on hand, cells repair, regenerate and settle inflammation far more efficiently.</p>
<p>Depth is what sets the two wavelengths apart. Visible red light works mainly at the surface, where it stimulates fibroblasts, the cells that build collagen and elastin. Near-infrared light travels deeper, reaching muscle, joint and connective tissue. Over a course of sessions, this gentle, non-thermal stimulation adds up, and the benefits build for skin, recovery and comfort alike.</p>

<h2>Types of Red Light Therapy</h2>
<p>The right wavelength depends on your goal. Your Brockwell clinician chooses it after reviewing your concern, the treatment area and your health profile.</p>
<h3>Red Light (630 to 700 nm)</h3>
<p>This range targets surface-level skin concerns such as texture, tone and firmness. It suits facial skin health and general rejuvenation.</p>
<h3>Near-Infrared Light (700 to 850 nm)</h3>
<p>This range reaches deeper than visible light and works well for muscle recovery, joint comfort and soft-tissue inflammation. Clinicians often combine it with red wavelengths in one session for broader benefit.</p>

<h2>Benefits of Red Light Therapy</h2>
<p>Used consistently within a clinical plan, red light therapy can offer several benefits. How much you notice depends on the concern, the number of sessions and how your body responds.</p>
<p>Reported benefits include:</p>
<ul>
<li>Smoother skin texture, tone and firmness</li>
<li>Stronger collagen and elastin production</li>
<li>A softer appearance of fine lines</li>
<li>Faster muscle recovery after exercise or physical strain</li>
<li>Calmer soft-tissue inflammation</li>
<li>Better joint comfort</li>
<li>A non-invasive option with little to no downtime</li>
<li>A treatment that fits neatly into a wider wellness or regenerative plan</li>
</ul>

<h2>The Red Light Therapy Process at Brockwell Healthcare</h2>
<p>Care follows a clear, five-step clinical path. Before the light ever goes on, your clinician confirms the right wavelength, device settings and protocol for your concern.</p>
<h3>Step 1: Booking</h3>
<p>Contact Brockwell Healthcare to schedule your session. The team matches you to the right appointment and explains any preparation you need beforehand.</p>
<h3>Step 2: Consultation and Assessment</h3>
<p>First, your clinician reviews your goal, health history, medications and any skin or tissue concerns. Light sensitivity, photosensitising medications and other contraindications are all checked here, and the correct wavelength, device and session length are set before anything starts.</p>
<h3>Step 3: Preparation</h3>
<p>Next comes the treatment area. For facial sessions, you remove makeup, heavy creams, serums and oils so the light can penetrate cleanly. For body or recovery sessions, the clinician positions the area and hands you protective eyewear, standard for every visit.</p>
<h3>Step 4: Treatment</h3>
<p>You sit or lie comfortably while the clinician positions the medical-grade device at the correct distance. The session is painless, and most patients feel nothing more than a gentle warmth. No needles, no UV, no burning. Most sessions run 10 to 20 minutes, depending on the protocol and the area treated.</p>
<h3>Step 5: Aftercare and Follow-Up</h3>
<p>Afterwards, your clinician talks you through post-session care, how often to return and what to expect as the plan progresses. You leave with your next appointment already booked.</p>

<h2>Why Patients Choose Brockwell Healthcare for Red Light Therapy</h2>
<p>At Brockwell Healthcare we offer:</p>
<ul>
<li>A DHA-certified doctor plans and oversees every session personally</li>
<li>Medical-grade devices deliver precise, calibrated red and near-infrared wavelengths</li>
<li>Each protocol is matched to your concern, from wavelength and distance to session length</li>
<li>A full contraindication screen protects your safety before every session</li>
<li>Clear, realistic expectations come first, so you always know what the therapy can and cannot do</li>
<li>Regular follow-ups track your progress and shape the next stage of your plan</li>
<li>Upfront, transparent pricing means no hidden costs and no surprises</li>
</ul>

<h2>Book Red Light Therapy in Dubai</h2>
<p>Book a red light therapy consultation in Dubai at Brockwell Healthcare to find out whether the treatment fits your skin, recovery or wellness goals. Your clinician reviews your health profile, walks you through the session plan, sets out the results you can realistically expect, and confirms the cost before treatment begins.</p>
"""

FAQS = [
    ("Can red light therapy help with skin quality?",
     "Yes. Over a course of sessions, it can support collagen production, refine texture and tone, and soften the look of fine lines."),
    ("Can red light therapy support muscle recovery?",
     "Yes. Near-infrared wavelengths may ease post-exercise soreness and support tissue repair, so many active patients use it within a wider recovery plan."),
    ("Does red light therapy support collagen?",
     "It stimulates the fibroblasts in your skin, and that activity can encourage collagen and elastin production over time. Results build gradually and differ from person to person."),
    ("Can it help manage inflammation?",
     "Near-infrared light may calm soft-tissue inflammation. It does not treat every inflammatory condition, so your clinician confirms suitability during the consultation."),
    ("Is non-invasive light therapy safe?",
     "Yes, when a clinician delivers it with medical-grade equipment after an assessment. It does not suit photosensitive conditions, some medications or active wounds, which is exactly what the pre-treatment screen checks for."),
    ("Is the treatment painful?",
     "No. Sessions are painless, and most patients feel only a mild warmth. There are no needles, no UV exposure and no downtime."),
    ("How many sessions will I need?",
     "Most patients need three to ten sessions, depending on the concern and goal. Your clinician builds the plan after the first assessment and fine-tunes it as you respond."),
    ("When will I notice results?",
     "Some patients see early changes within a few sessions. Most improvements develop gradually across a full course, and the timeline depends on your concern and health profile."),
    ("Are the results permanent?",
     "No. Maintenance sessions help hold your results, especially for skin and recovery goals, and your clinician advises on the right interval."),
    ("What side effects can occur?",
     "Side effects are uncommon with proper screening and protocols. You might notice mild, temporary redness or warmth. Serious effects are rare."),
    ("What should I do before a session?",
     "Clear the treatment area of makeup, heavy creams and oils, and tell your clinician about any new medications or skin treatments beforehand."),
    ("Can it be combined with PRP, IV therapy or other treatments?",
     "Yes. Light therapy pairs well with PRP, IV treatments, stem cell therapy and other regenerative services at Brockwell. Your clinician advises on the best combination for you."),
    ("What does red light therapy cost in Dubai?",
     "Cost depends on the area, protocol and number of sessions. You get transparent pricing and a clear estimate before treatment begins, and no session starts without a full cost discussion."),
    ("Is LED light therapy the same as red light therapy?",
     "LED light therapy is a broader term that covers red and near-infrared treatments. At Brockwell, a clinician delivers both under the same clinical framework and chooses the protocol around your goal."),
    ("Who should consider red light therapy?",
     "It may suit anyone wanting to support skin health, recover from muscle soreness, ease joint discomfort or add a non-invasive option to a wider wellness plan."),
    ("Who should avoid it?",
     "Avoid light therapy if you take photosensitising medications or have active skin irritation, open wounds, light-sensitive conditions, active cancer or a serious unmanaged condition. Pregnant or breastfeeding patients need medical clearance first."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    svc = Service.objects.filter(region="uae", slug="red-light-therapy").first()
    if not svc:
        return

    svc.description = DESCRIPTION.strip()
    svc.summary = SUMMARY
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
        ("services", "0012_detox_therapy_content"),
        ("core", "0010_remove_oscar_tellez"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
