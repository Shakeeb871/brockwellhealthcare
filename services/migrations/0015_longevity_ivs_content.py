"""Load the full Longevity IVs content: styled rich-text sections, SEO meta and
FAQs. Rendered through the site's `.prose` styles + the `enhance` filter, so the
"Types" section becomes a card grid, the process a numbered timeline and bullet
lists become icon lists. (Images will be added later; the hero falls back to the
default until one is uploaded.)"""

from django.db import migrations

SEO_TITLE = "Longevity IVs in Dubai | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led longevity IVs in Dubai for energy, cellular health, recovery, brain fog and healthy "
    "ageing. Personalised IV drip therapy with realistic guidance."
)
SUMMARY = (
    "Doctor-led longevity IV drips — NAD+, glutathione, Vitamin C and more — for energy, recovery "
    "and healthy ageing."
)

DESCRIPTION = """
<p>Longevity IVs in Dubai are doctor-led IV drip therapies that support cellular energy, hydration, recovery, mental clarity and healthy ageing. Depending on your symptoms, health history and goals, your Brockwell doctor may recommend NAD+ IV therapy, glutathione IV therapy, Vitamin C IV therapy or another wellness IV infusion.</p>

<h2>What Are Longevity IVs?</h2>
<p>Longevity IVs are a form of anti-ageing IV therapy that delivers a targeted mix of vitamins, minerals, antioxidants and coenzymes straight into your bloodstream through an intravenous line. Because the nutrients skip the digestive system, they reach your cells faster and at higher concentrations than oral supplements can manage.</p>
<p>At Brockwell Healthcare, longevity IV drip therapy supports patients living with persistent low energy, slow recovery, brain fog, oxidative stress and broader wellness concerns. It does not replace medical treatment. Instead, a doctor may recommend it within a wider wellness and healthy ageing plan once an assessment confirms it fits.</p>

<h2>How Do Longevity IVs Work?</h2>
<p>Delivered straight into a vein, the nutrients reach your cells almost at once, at a bioavailability oral supplements rarely match. NAD+, for instance, supports mitochondrial function and cellular energy production, while glutathione, a powerful antioxidant, helps counter the oxidative stress that builds up with age, stress and poor recovery. Other ingredients support immune balance, tissue repair and hydration at a cellular level.</p>
<p>Across a course of sessions, this targeted delivery may help restore what daily life and ageing slowly wear down.</p>

<h2>Types of Longevity IVs</h2>
<p>Each formulation depends on your health goals, symptoms and clinical assessment. Brockwell chooses the right drip after reviewing your case.</p>
<h3>NAD+ IV Drip</h3>
<p>NAD+ infusion therapy delivers nicotinamide adenine dinucleotide into the bloodstream to support cellular energy, DNA repair and cognitive function. Patients dealing with fatigue, low stamina, poor recovery or brain fog often choose it.</p>
<h3>Glutathione IV Drip</h3>
<p>Glutathione IV therapy delivers one of the body's main antioxidants directly to your cells. It may support oxidative stress management, cellular protection and clearer skin from within.</p>
<h3>Myers Cocktail IV Drip</h3>
<p>A well-established wellness IV infusion of magnesium, B vitamins, Vitamin C and calcium. Patients turn to it for general energy, hydration and recovery after stress, illness or travel.</p>
<h3>Vitamin C IV Drip</h3>
<p>High-dose Vitamin C IV therapy supports immune function, collagen production and antioxidant activity at levels oral intake cannot reliably reach. It features often in immune, recovery and skin-health protocols.</p>
<h3>Alpha-Lipoic Acid (ALA) IV Drip</h3>
<p>ALA IV therapy uses alpha-lipoic acid, an antioxidant, within some cellular health IV therapy plans. It may support oxidative stress management, inflammation balance and metabolic wellness.</p>
<h3>Hydration IV Drip</h3>
<p>A saline and electrolyte infusion for fast rehydration after travel, illness or exertion, and one of the simplest cellular health IV therapy options.</p>
<h3>B Vitamin IV Drip</h3>
<p>B12, B6 and B-complex delivered intravenously to support energy metabolism, nerve function and recovery from fatigue or poor concentration.</p>

<h2>Benefits of Longevity IVs</h2>
<p>Used consistently within a clinical plan, longevity IV drip therapy can offer several benefits. How much you notice depends on the concern, the formulation, the number of sessions and how your body responds.</p>
<p>Reported benefits include:</p>
<ul>
<li>Steadier energy as cellular production gets better support</li>
<li>Clearer thinking, as hydration, B vitamins and antioxidants ease brain fog</li>
<li>Faster recovery after illness, travel or hard physical effort</li>
<li>Better oxidative stress management through glutathione and antioxidant protocols</li>
<li>Stronger immune resilience from targeted nutrient delivery</li>
<li>Clearer skin from within, as part of an anti-ageing IV drip plan</li>
<li>Cellular hydration that drinking water alone often misses</li>
<li>Full nutrient delivery that skips digestive absorption limits</li>
<li>A plan personalised to your specific concern and goals</li>
</ul>
<p>Results are never guaranteed. A clinical assessment at Brockwell decides whether healthy ageing IV therapy suits your situation.</p>

<h2>The Longevity IVs Process at Brockwell Healthcare</h2>
<p>Every session follows a structured clinical process, and your doctor confirms the right formulation, dose and plan before anything goes into the line.</p>
<h3>Step 1: Booking</h3>
<p>Contact Brockwell Healthcare to schedule your consultation. The team matches you to the right appointment for your main concern, whether that is fatigue, brain fog, recovery, oxidative stress or general wellness.</p>
<h3>Step 2: Consultation and Assessment</h3>
<p>Your doctor reviews your symptoms, health history, current medications, lifestyle and goals, then selects the formulation that fits your case. Before anything is prepared, your doctor checks kidney function, cardiovascular health, allergies and possible medication interactions, so the drip genuinely matches your concern.</p>
<h3>Step 3: Preparation</h3>
<p>A clinician prepares your formulation in a sterile clinical environment, then confirms the exact ingredients, concentrations and delivery rate before you begin. On arrival, the team checks your blood pressure and hydration to make sure you are ready.</p>
<h3>Step 4: Treatment</h3>
<p>A trained medical professional places a small IV cannula into a vein, usually in your arm or hand, connects the drip and starts the infusion at a controlled rate. You sit or recline comfortably throughout, and most patients feel nothing more than a mild coolness along the vein. Sessions usually run 30 to 90 minutes, depending on the formulation and plan, while the clinical team monitors your comfort and response.</p>
<h3>Step 5: Aftercare and Follow-Up</h3>
<p>Afterwards, the nurse removes the IV line and runs a quick check. Your doctor explains what to expect over the next few hours, how often to schedule sessions and what comes next. If you have a course planned, you leave with the next appointment booked.</p>

<h2>Why Patients Choose Brockwell Healthcare for Longevity IVs</h2>
<p>At Brockwell Healthcare we offer:</p>
<ul>
<li>A DHA-certified doctor plans and supervises every longevity IV session personally</li>
<li>Each formulation is built around your symptoms and health goals, start to finish</li>
<li>A full contraindication screen covers kidney function, cardiovascular health and medication interactions before each session</li>
<li>Medical-grade ingredients go into every anti-ageing IV therapy and NAD+ infusion</li>
<li>Clear, realistic expectations come first, before any longevity infusion therapy begins</li>
<li>Follow-up reviews track your response and fine-tune the formulation over time</li>
<li>Upfront pricing is confirmed before your first session, with no hidden costs</li>
</ul>

<h2>Book Longevity IVs in Dubai</h2>
<p>Book a doctor-led longevity IV consultation at Brockwell Healthcare in Dubai. Your doctor reviews your health goals, explains the recommended formulation, sets out the results and limits you can expect, and confirms the cost before your first session. Every IV drip plan is personalised around your symptoms, medical history and wellness goals.</p>
"""

FAQS = [
    ("Can longevity IVs help with energy and fatigue?",
     "Yes. Longevity IV drip therapy delivers nutrients that support mitochondrial function and cellular energy, which can help patients who feel constantly tired despite decent sleep and routine."),
    ("Can they support brain fog and mental clarity?",
     "Sometimes. Brain fog often links to poor hydration, low nutrient levels, stress or oxidative stress, so a wellness IV infusion may combine NAD+, B vitamins and antioxidants to support clearer thinking."),
    ("Does glutathione IV therapy help skin and wellness?",
     "Glutathione IV therapy sends the body's primary antioxidant straight to your cells, which may support skin clarity, cellular protection and oxidative stress management."),
    ("Is NAD+ infusion therapy safe?",
     "Yes, when qualified doctors administer it after proper screening. Some patients feel mild flushing, warmth or nausea during the infusion, and it usually passes quickly."),
    ("How are longevity IVs different from a regular IV drip?",
     "Longevity IVs are tailored to cellular health, oxidative stress, energy and recovery, whereas a regular IV drip usually focuses on hydration or basic wellness support."),
    ("How long does one session take?",
     "Most sessions run 30 to 90 minutes. The exact time depends on the drip, the ingredients and the plan your doctor recommends."),
    ("Is there any downtime?",
     "No. Most patients return to normal activity straight away. Some feel more energised soon after, while others notice a gradual lift over the following hours or days."),
    ("How many sessions will I need?",
     "It depends on your goals, symptoms and response. Some patients benefit from a short course, others from occasional maintenance, and your doctor guides you after the first consultation."),
    ("Are the results permanent?",
     "No. Longevity infusion therapy works best as an ongoing wellness plan rather than a one-off. Maintenance sessions often help sustain gains in energy, recovery and cellular health."),
    ("What should I do before a session?",
     "Arrive well hydrated, eat a light meal beforehand, and tell your doctor about any change in your health or medications since your last visit. Follow any specific instructions from the team."),
    ("What should I do afterwards?",
     "Keep hydrated and skip heavy exercise for a few hours. Most people carry on with their day as usual. Contact the clinic if anything feels unusual."),
    ("Who should avoid anti-ageing IV drip therapy?",
     "Patients with kidney disease, heart failure, fluid-management conditions, uncontrolled diabetes, known allergies to IV components, active infection or clotting disorders should avoid it without medical clearance. Pregnant patients need specific review, and the consultation screens for every contraindication."),
    ("Can it be combined with other treatments?",
     "Yes. It can pair with red light therapy, PRP, detox therapy or other regenerative wellness services, and your doctor advises what makes sense for your goals."),
    ("What do longevity IVs cost in Dubai?",
     "Cost depends on the formulation, session length and number of sessions. You receive transparent pricing and a full estimate before any session begins."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    svc = Service.objects.filter(region="uae", slug="longevity-ivs").first()
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
        ("services", "0014_stem_cells_content"),
        ("core", "0010_remove_oscar_tellez"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
