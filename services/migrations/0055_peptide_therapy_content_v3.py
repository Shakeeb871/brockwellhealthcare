"""Refresh the Peptide Therapy service description with the user's revised copy:
a new lead intro, a reworded second paragraph in 'Tailored ... Programs', and a
rewritten 'Why Consider Peptide Therapy?' section. Structure, sections, inline
image and FAQs are otherwise unchanged from 0054. Only the description is
re-saved here."""

from django.db import migrations

SLUG = "peptide-therapy"

DESCRIPTION = """
<p>Peptides are the body's own messengers, short chains of amino acids that tell cells precisely what to do, and peptide therapy puts that signalling to work for a specific, defined purpose. At Brockwell Healthcare, it is a prescription-only, doctor-led service in Dubai, spanning goals as varied as recovery, hormonal balance, metabolism, skin and cognition. Because a peptide can influence powerful systems such as hormones and cellular repair, our doctors treat every plan as a genuinely medical decision, beginning with a full assessment and a clear clinical reason for anything prescribed.</p>

<h2>What Is Peptide Therapy?</h2>
<p>Peptides are short chains of amino acids that act as signalling molecules, carrying precise instructions between cells. The body produces many of them naturally, drawing on them to help regulate everything from healing and growth-hormone release to metabolism and immune function. Peptide therapy works with specific, targeted peptides intended to support these processes where they have slowed or become less efficient.</p>
<p>At Brockwell Healthcare, our peptide therapy in Dubai is indication-based, which means our doctor prescribes it for a defined clinical reason, never as a general supplement. Each plan begins with a clinical assessment and, where relevant, baseline lab work. A consultation does not automatically lead to a prescription; our doctor recommends peptide therapy only where it is clinically appropriate and safe for you.</p>

<h2>How Does Peptide Therapy Work?</h2>
<p>Peptide therapy is built on precision. Each peptide binds to a particular receptor on or inside a cell, prompting a focused biological response. Growth-hormone peptides, for instance, signal the pituitary gland to release the body's own growth hormone in a natural, pulsatile rhythm, which in turn influences the growth-hormone and IGF-1 pathways, while repair peptides act on tissue-healing and inflammatory pathways.</p>
<p>That specificity is the essence of the approach. Our doctor then matches a well-chosen peptide to the exact process your assessment identifies, and it is usually delivered by a small subcutaneous injection, with some peptides given instead by oral, nasal or topical routes, always within a supervised protocol. Because peptides can influence powerful systems such as hormones and cellular activity, medical supervision and correct, prescription-grade sourcing matter as much as the peptide itself.</p>

<img src="/static/img/services/peptide-therapy-content.webp" alt="Doctor discussing a prescription-grade peptide therapy protocol at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>Types of Peptides Used in Peptide Therapy</h2>
<p>Peptides are grouped by the goal they are studied for. Our doctor selects the right category, and the specific peptide, around your clinical need, and only well-characterised, prescription-grade peptides are used. Several of the peptides below are not approved as standard medicines, and our doctor explains the current status of any peptide before it is considered.</p>
<h3>Recovery and Tissue-Repair Peptides</h3>
<p>BPC-157 (Body Protection Compound) and TB-500, a fragment related to thymosin beta-4, are often discussed together and studied for their role in tendon, muscle, ligament and gut-tissue repair, angiogenesis and inflammation. They draw particular interest for recovery after injury, surgery or physical strain.</p>
<h3>Growth-Hormone Peptides (Secretagogues)</h3>
<p>CJC-1295, Ipamorelin, Sermorelin and Tesamorelin are designed to support the body's own growth-hormone release, with possible influence on body composition, recovery and sleep. Ipamorelin is valued for a selective, clean pulse of growth hormone, while Tesamorelin is studied specifically for visceral fat. MK-677 works as an oral secretagogue in the same family.</p>
<h3>Metabolic and Weight-Support Peptides</h3>
<p>AOD-9604 and MOTS-c are studied for fat metabolism, and GLP-1 receptor agonists, such as semaglutide and tirzepatide, are studied for appetite regulation and weight, always within a wider, medically supervised weight-management plan alongside nutrition and lifestyle care.</p>
<h3>Immune-Support Peptides</h3>
<p>Thymosin Alpha-1 and KPV are studied for immune modulation, considered within a broader wellbeing plan for those carrying a chronic immune burden.</p>
<h3>Skin and Anti-Ageing Peptides</h3>
<p>Copper peptides, such as GHK-Cu, are studied for their role in collagen production, skin quality and scalp health, and feature within aesthetic and regenerative protocols.</p>
<h3>Sexual-Health Peptides</h3>
<p>PT-141 (bremelanotide) is studied for libido and sexual function, considered where clinically appropriate.</p>
<h3>Sleep, Longevity and Cognitive Peptides</h3>
<p>Epitalon and DSIP are explored for sleep quality and longevity pathways, while Semax and Selank are studied for focus, mood and cognitive clarity. Our doctor considers these only where the assessment points to a genuine need.</p>

<h2>Benefits of Peptide Therapy</h2>
<p>For suitable patients, prescribed and monitored properly, peptide therapy is explored for a number of potential benefits. Responses vary widely with the peptide, the individual and the underlying goal, and many peptides act gradually over months.</p>
<p>Potential benefits this approach is designed to support include:</p>
<ul>
<li>A targeted, receptor-specific approach matched to a clearly defined clinical need</li>
<li>Tissue repair and recovery support after injury, surgery or physical strain</li>
<li>A role in the body's own growth-hormone signalling, body composition and recovery</li>
<li>Metabolic and weight support within a wider, medically supervised plan</li>
<li>Skin quality, collagen and scalp support within aesthetic protocols</li>
<li>Immune, sleep, sexual-health and cognitive support where clinically relevant</li>
</ul>
<p>Outcomes are never guaranteed, and several peptides are not approved as standard medicines for these uses. Our assessment establishes whether peptide therapy in Dubai is appropriate for you before anything is prescribed.</p>

<h2>Who Is Peptide Therapy For?</h2>
<p>Peptide therapy is explored by individuals seeking targeted support, whether that means recovering from injury or physical strain, navigating age-related hormonal change, working towards metabolic and weight goals, or caring for skin, hair, immune wellbeing, sexual health and sleep. Because each peptide is matched to a particular purpose, the approach tends to appeal to people who want something precise for a clearly defined goal. It suits both men and women; women, for example, often explore GHK-Cu for skin, BPC-157 for recovery and growth-hormone peptides for hormonal and metabolic balance.</p>
<p>Suitability is confirmed through clinical assessment, never assumed. Our doctor reviews your history, medications, goals and, where relevant, baseline labs. Certain situations, such as active or past cancer without oncology clearance, hormone-sensitive conditions, and pregnancy or breastfeeding, mean peptide therapy is not appropriate, and it is not suitable for minors. This is why a full assessment always comes first.</p>

<h2>What to Expect from Peptide Therapy in Dubai</h2>
<p>Your journey with us begins with a consultation, not a prescription. Our doctor reviews your symptoms, history, medications and goals, arranges baseline lab work where relevant, and explains honestly what a given peptide is and is not designed to do for your situation.</p>
<p>Where peptide therapy is appropriate, our doctor prescribes a specific, prescription-grade peptide sourced through a regulated compounding pharmacy, and sets out the protocol, the expected timeline and the monitoring plan. Most protocols involve a small subcutaneous injection you can learn to self-administer, with clear guidance from our clinical team, though some peptides are given orally, nasally or topically. Your response is monitored and adjusted throughout, and we are transparent at every step, so you always understand what you are taking and why.</p>

<h2>Peptide Therapy: Client Expectations &amp; Timeline</h2>
<p>We place real value on honest, realistic expectations. Peptides tend to act gradually, so any effect usually develops over weeks to months, and responses differ considerably from one person to another.</p>
<h3>The Consultation</h3>
<p>Your first appointment is dedicated to assessment, baseline testing where relevant, and an honest explanation of what is appropriate and what is not.</p>
<h3>The Protocol</h3>
<p>Once prescribed, your protocol is time-limited and monitored, with your response reviewed, never assumed. Repair peptides may show effects within a few weeks, while growth-hormone protocols often take three to six months.</p>
<h3>Ongoing Review</h3>
<p>Follow-up appointments track how you are responding, repeat relevant labs where useful, and refine or conclude the protocol accordingly.</p>

<h2>Tailored Peptide Therapy Programs for Your Lifestyle</h2>
<p>Peptide therapy is most effective when it is shaped around your life and your goals, and we plan it with that in mind. For active adults and athletes focused on recovery, it is coordinated with training, rest and rehabilitation, and any athlete subject to testing is advised on prohibited-substance rules first. For those focused on hormonal wellbeing, metabolic goals or healthy ageing, it is planned as one considered element within a wider, medically supervised programme.</p>
<p>Throughout, our doctor keeps the protocol practical: how it fits your week, how it is monitored, and how it works with the rest of your care, so the plan stays realistic to live with and never a burden to keep up.</p>

<h2>Why Consider Peptide Therapy?</h2>
<p>What draws people to peptide therapy is usually its precision. A single, well-chosen peptide can be aimed at a single goal, whether that is quicker recovery, steadier sleep or hormonal support, and for many people that focused quality is the whole appeal, especially alongside a broader wellbeing plan.</p>
<p>It is worth seeing the full picture just as clearly. Responses differ from person to person, several peptides are not approved as standard medicines, the regulatory landscape is still settling, and safe, prescription-grade sourcing with proper monitoring is not optional. Our doctors would far rather have that honest conversation upfront than promise more than the science supports.</p>

<h2>Your Patient Journey</h2>
<h3>Step 1: Consultation &amp; Assessment</h3>
<p>Our doctor reviews your history, medications, goals and, where relevant, baseline labs, and confirms whether peptide therapy is appropriate and safe for you.</p>
<h3>Step 2: Prescription &amp; Protocol</h3>
<p>Where suitable, our doctor prescribes a specific, prescription-grade peptide sourced through a regulated compounding pharmacy and sets out the protocol, timeline and monitoring plan.</p>
<h3>Step 3: Administration &amp; Monitoring</h3>
<p>Your protocol is delivered under medical guidance, usually by subcutaneous injection, with your response monitored and adjusted throughout.</p>
<h3>Step 4: Review &amp; Refinement</h3>
<p>Follow-up appointments track your progress, repeat relevant labs where useful, and refine or conclude the protocol accordingly.</p>

<h2>Why Choose Brockwell Healthcare for Peptide Therapy</h2>
<ul>
<li><strong>Prescription-Only, Physician-Led.</strong> Every peptide is prescribed and supervised by an experienced doctor, never offered as an off-the-shelf product.</li>
<li><strong>Prescription-Grade Sourcing.</strong> We prescribe only well-characterised peptides through a regulated compounding pharmacy, with full transparency about what you are taking.</li>
<li><strong>Assessment First.</strong> A consultation, and where relevant baseline labs, come before any prescription, and a consultation never automatically leads to one.</li>
<li><strong>Honest, Ongoing Care.</strong> We set realistic expectations, are open about limitations and regulatory status, and monitor your response through structured follow-up.</li>
<li><strong>Complete Transparency.</strong> We explain your protocol, monitoring and pricing clearly before anything begins.</li>
</ul>
"""


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc:
        return
    svc.description = DESCRIPTION.strip()
    svc.save(update_fields=["description"])


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0054_peptide_therapy_content_v2"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
