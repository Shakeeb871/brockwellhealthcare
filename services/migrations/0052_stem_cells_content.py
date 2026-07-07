"""Update the existing Stem Cells service with the full refined content: SEO
meta, H1, and styled rich-text sections. The 'Types' and 'Client Expectations &
Timeline' sections become card grids, the 'Your Patient Journey' steps become a
numbered timeline, and the benefit / why-choose lists become icon lists. Plus
the FAQ set. Supersedes the previous stem cell content."""

from django.db import migrations

SLUG = "stem-cells"

SEO_TITLE = "Stem Cell Therapy in Dubai | Regenerative Medicine | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Discover stem cell therapy in Dubai at Brockwell Healthcare, a refined regenerative "
    "medicine service for joint, tendon and soft-tissue concerns, built around your "
    "individual assessment."
)
HERO_HEADING = "Stem Cell Therapy in Dubai"
SUMMARY = (
    "A refined regenerative medicine service working with the body's own cells for joint, "
    "tendon and soft-tissue concerns, built around your individual assessment."
)

DESCRIPTION = """
<p>Welcome to Brockwell Healthcare, where advanced regenerative medicine meets a considered, deeply personal standard of care. Our stem cell therapy in Dubai works with the body's own cells as part of an approach centred on natural repair, crafted for discerning individuals who want to understand every non-surgical option for joint, tendon and soft-tissue concerns. Every programme begins not with a procedure, but with an in-depth clinical conversation, because meaningful regenerative care is always built around the individual.</p>

<h2>What Is Stem Cell Therapy?</h2>
<p>Stem cell therapy is a sophisticated field of regenerative medicine that works with cells which have not yet settled into a single fixed role in the body. The cells most often used are mesenchymal stem cells (MSCs), drawn from a person's own bone marrow or adipose (fat) tissue and prepared with precision in a controlled clinical setting.</p>
<p>At Brockwell Healthcare, our stem cell treatment in Dubai sits within a comprehensive regenerative medicine framework and is most often explored for musculoskeletal concerns. Our medical team delivers it as part of a considered, individually tailored plan. We take the time to explain exactly what the approach involves, and what it is designed to support, before anything is decided.</p>

<h2>How Does Stem Cell Therapy Work?</h2>
<p>Stem cell therapy is centred on the elegant language of cell signalling. Mesenchymal stem cells are valued for their paracrine activity, meaning the growth factors and signalling molecules they release, and these signals form the foundation of how the approach is intended to interact with the surrounding tissue and the local repair environment.</p>
<p>Once a cell source is prepared, our clinician places the preparation into the target area. For joints and soft tissue, we carry this out under real-time ultrasound guidance for meticulous, accurate positioning. Regeneration is, by its nature, a gradual process, so this approach is designed to support the body gradually over time, never as an overnight change.</p>

<h2>Types of Stem Cell Therapy</h2>
<p>The most suitable approach depends on your condition, the area involved and what your clinical assessment reveals. Our doctors consider each case individually before selecting a cell source.</p>
<h3>Autologous Stem Cell Therapy</h3>
<p>The cells come from your own body, most often bone marrow or fat. Because the material is your own, the likelihood of rejection remains very low, which is why this route is so common in orthopaedic regenerative care.</p>
<h3>Mesenchymal Stem Cell Therapy (MSC)</h3>
<p>Mesenchymal stem cells are among the most studied cell types in regenerative medicine. Found in bone marrow, fat and other tissues, they are frequently considered for joint, tendon, cartilage and soft-tissue concerns.</p>
<h3>Bone Marrow Concentrate (BMC)</h3>
<p>Here, a clinician draws bone marrow and concentrates it before delivering it to the treatment area. The concentrate carries stem cells, growth factors and other components studied for their role in tissue support.</p>
<h3>Adipose-Derived Preparations</h3>
<p>This method draws cells from your own fat tissue, usually the abdomen. It is a straightforward harvest that yields a healthy number of cells with minimal disruption.</p>

<h2>Benefits of Stem Cell Therapy</h2>
<p>As part of a properly assessed clinical plan, stem cell therapy is explored for a number of potential benefits. Responses differ from one individual to another, depending on the condition, its severity, the number of sessions and how the body responds.</p>
<p>Potential benefits this approach is designed to support include:</p>
<ul>
<li>A non-surgical option for suitable candidates with joint or soft-tissue concerns</li>
<li>Support for the local repair environment through concentrated cell signalling</li>
<li>A minimally invasive procedure with limited downtime</li>
<li>Use of your own cells in autologous protocols, keeping rejection risk low</li>
<li>Coordination alongside PRP, physiotherapy and other regenerative approaches within one plan</li>
</ul>
<p>Outcomes are never guaranteed, and our assessment establishes what is realistic for your situation before any plan begins.</p>

<h2>Who Is Stem Cell Therapy For?</h2>
<p>Stem cell therapy is most often explored by individuals living with musculoskeletal concerns. In practice, the areas it is most commonly considered for include knee osteoarthritis, meniscal and ligament injuries, hip and shoulder conditions such as rotator cuff concerns, ankle and elbow complaints, tendon conditions such as tendinopathy, and sacroiliac (SI) joint pain. Many of the people who come to us have already navigated conservative measures, such as rest, physiotherapy, medication or standard injections, and wish to understand their non-surgical options fully before considering surgery.</p>
<p>Suitability is never assumed from symptoms alone. Our doctors review your history, examination and imaging with care. Certain situations, including active cancer, active infection or some blood disorders, mean the approach is not appropriate, which is precisely why a thorough, unhurried assessment always comes first.</p>

<h2>What to Expect from Stem Cell Therapy in Dubai</h2>
<p>Your journey with us begins with a consultation, not a procedure. Our doctor reviews your history, current health and any relevant imaging, explains what the approach involves for your particular situation, and answers your questions in full, so your decision is an informed and confident one.</p>
<p>Where treatment proceeds, cell collection, preparation and delivery all take place within a sterile, discreet clinical environment, and ultrasound guides any injection into a joint or soft tissue. For most, the experience involves a collection step, a preparation period on the same day, and a refined delivery step, followed by clear aftercare guidance. Because autologous protocols use your own cells, any effects tend to be minor and temporary, such as mild swelling, bruising or soreness at the harvest or injection site, and our clinician explains what is normal beforehand. Our clinical team talks you through each stage and remains attentively by your side throughout.</p>

<h2>Stem Cell Therapy: Client Expectations &amp; Timeline</h2>
<p>We believe honest, realistic expectations are the mark of genuine care. Regeneration is gradual, so any change that is noticed tends to unfold gradually, over weeks to months, and every individual responds differently.</p>
<h3>The Consultation</h3>
<p>Your first appointment is dedicated to understanding your situation, explaining what the approach is designed to support, and being equally clear about its limitations.</p>
<h3>The Following Weeks</h3>
<p>During the period after any procedure, tailored aftercare and activity advice support your body through its natural repair processes.</p>
<h3>Ongoing Review</h3>
<p>Follow-up appointments allow us to track your progress attentively over time and keep expectations grounded in your own experience.</p>

<h2>Tailored Stem Cell Therapy Programs for Your Lifestyle</h2>
<p>Regenerative care is most effective when it is woven seamlessly into your life, and we shape every plan accordingly. For active adults and those in sport, we coordinate stem cell therapy with rehabilitation, load management and a graded return to the activities you love.</p>
<p>For discerning individuals focused on long-term joint and mobility health, we plan it alongside movement, physiotherapy and overall wellbeing, with total clinical discretion. Whatever your world looks like, our team explains how the approach fits your routine and how it complements the other elements of your care, so your programme feels effortless and sustainable.</p>

<h2>Why Consider Stem Cell Therapy?</h2>
<p>Discerning patients consider stem cell therapy for a range of thoughtful reasons, and we believe in weighing each one openly. Common motivations include a preference for autologous approaches that use one's own cells, an interest in minimally invasive options alongside or instead of surgery, and a desire to understand precisely where regenerative medicine sits within a broader plan.</p>
<p>We are equally candid about the other side of the picture. Responses vary, the approach suits some situations and not others, and a doctor should confirm whether it is right for you first. This balanced, transparent conversation is one we always welcome, because a truly informed choice is a more confident one.</p>

<h2>Your Patient Journey</h2>
<h3>Step 1: Consultation &amp; Assessment</h3>
<p>Our doctor reviews your history, symptoms, medications, imaging and goals, explains what the approach involves for your situation, and screens carefully for anything that would make it unsuitable.</p>
<h3>Step 2: Your Personalised Plan</h3>
<p>We craft a plan around your assessment, explaining the cell source, the process, the realistic expectations and the limitations, so your decision is fully informed.</p>
<h3>Step 3: The Procedure</h3>
<p>Where the approach is appropriate, cell collection, preparation and image-guided delivery take place within a sterile, discreet clinical setting, with your comfort attended to throughout.</p>
<h3>Step 4: Aftercare &amp; Review</h3>
<p>You receive considered aftercare guidance, and follow-up appointments track your progress over time and refine the wider plan as needed.</p>

<h2>Why Choose Brockwell Healthcare for Stem Cell Therapy</h2>
<ul>
<li><strong>Physician-Led Expertise.</strong> Experienced doctors lead every programme, and each case begins with a thorough, individual clinical assessment.</li>
<li><strong>A Considered, Honest Approach.</strong> We set realistic expectations, discuss the limitations openly, and make informed consent a natural part of how we work.</li>
<li><strong>Precision &amp; Discretion.</strong> For any joint or soft-tissue procedure, we use ultrasound guidance for accurate placement, within a private, refined clinical environment.</li>
<li><strong>Continuity of Care.</strong> Follow-up reviews keep your plan on track over time, as part of one coordinated regenerative framework.</li>
<li><strong>Complete Transparency.</strong> We explain your pricing and plan clearly before anything begins, with no surprises.</li>
</ul>
"""

FAQS = [
    ("What cells are used in stem cell therapy?",
     "The cells most often used are mesenchymal stem cells, drawn from a person's own bone marrow or adipose (fat) tissue, along with related preparations such as bone marrow concentrate. Our doctor confirms the most suitable approach for you during your assessment."),
    ("Is stem cell therapy a cure?",
     "No. Stem cell therapy is an area of regenerative medicine centred on supporting the body's own processes, and responses vary from person to person. We never present it as a guaranteed cure, and our doctor explains clearly what it is designed to support for your particular situation."),
    ("Who is not suitable for stem cell therapy?",
     "Our doctor determines suitability after assessment. Situations such as active cancer, active infection or certain blood disorders may mean it is not appropriate, which is why careful screening always comes first."),
    ("How long does it take to notice a difference?",
     "Regeneration is gradual. Where any change is noticed, it typically develops gradually, over weeks to months, and individual responses differ. Follow-up reviews help us track your progress realistically."),
    ("Does stem cell therapy involve surgery?",
     "The delivery step is minimally invasive and, for joints and soft tissue, guided by ultrasound. Our doctor explains the full process and everything it involves before any decision is made."),
    ("Can it be combined with other treatments?",
     "Yes. We often coordinate stem cell therapy elegantly with physiotherapy, PRP and other regenerative approaches as part of one plan. Our team advises on the right combination for your situation."),
    ("Is stem cell therapy painful?",
     "Most people find it well tolerated. The collection and delivery steps may involve brief discomfort, and our clinician uses local anaesthetic where appropriate. Any soreness at the site is usually mild and short-lived."),
    ("How long does the procedure take?",
     "On a treatment day, collection, same-day preparation and delivery typically take a few hours in total, though this varies with the approach and area involved. Our doctor confirms the expected timing during your assessment."),
    ("What is the recovery time?",
     "The delivery step is minimally invasive, and most people return to light activity within a day or two, following tailored aftercare. Because regeneration is gradual, your doctor will guide activity and any physiotherapy over the weeks that follow."),
    ("Is stem cell therapy safe?",
     "Autologous approaches use your own cells, which keeps rejection risk low, and most effects are minor and temporary. Careful screening at assessment, and situations such as active cancer or active infection, are reviewed before anything proceeds, which is central to how we work."),
    ("How is stem cell therapy different from PRP?",
     "PRP uses concentrated platelets and growth factors from your own blood, while stem cell approaches work with cells from bone marrow or fat. Both are regenerative and sometimes used together, and our doctor explains which is more appropriate for your situation."),
    ("Am I a good candidate for stem cell therapy?",
     "Candidacy is confirmed through assessment. It is generally explored by people with earlier-stage joint or soft-tissue concerns who have not found lasting relief from conservative care and wish to understand their non-surgical options. Our doctor reviews your history and imaging to advise honestly."),
    ("How much does stem cell therapy cost in Dubai?",
     "The cost depends on the cell source, the area treated, the number of sessions and the wider plan. We explain your pricing clearly and in full before anything begins, with no surprises."),
    ("Do I need a consultation first?",
     "Yes. A thorough clinical assessment comes before any regenerative treatment, both to confirm suitability and to craft a plan that genuinely fits your life."),
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
        ("services", "0051_emsella_content"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
