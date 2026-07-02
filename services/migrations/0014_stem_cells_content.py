"""Load the full Stem Cell Therapy content: styled rich-text sections, SEO meta
and FAQs. Rendered through the site's `.prose` styles + the `enhance` filter, so
the "Types" section becomes a card grid, the process a numbered timeline and
bullet lists become icon lists — matching the other service pages. (Images will
be added later; the hero falls back to the default until one is uploaded.)"""

from django.db import migrations

SEO_TITLE = "Stem Cell Therapy in Dubai | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led stem cell therapy in Dubai for joint pain, cartilage repair, sports injuries and "
    "tissue regeneration. Personalised, non-surgical regenerative care."
)
SUMMARY = (
    "Doctor-led stem cell therapy using your own cells to repair joints, cartilage and soft tissue."
)

DESCRIPTION = """
<p>Stem cell therapy is a regenerative treatment that uses your body's own cells to repair tissue, calm inflammation and support natural healing. For patients who want to avoid surgery, or who have not found lasting relief from earlier treatments, it often becomes the next step worth considering.</p>

<h2>What Is Stem Cell Therapy?</h2>
<p>Stem cell therapy is a form of regenerative cell treatment that places specialised cells into a damaged or inflamed area to help the body repair itself. These cells have not yet settled into a fixed role, so they respond to what the surrounding tissue needs and support recovery from within.</p>
<p>At Brockwell Healthcare, stem cell treatment in Dubai mainly targets joint pain, cartilage wear, tendon damage and sports injuries. Most patients reach it after rest, physiotherapy, medication or injections have stopped short of lasting results, and when they would rather not go straight to surgery.</p>

<h2>How Does Stem Cell Therapy Work?</h2>
<p>Regenerative stem cell therapy delivers active cells straight into the damaged area. Once in place, the cells release growth factors and chemical signals that communicate with the surrounding tissue. Those signals can calm inflammation, prompt the body to build new tissue and slow further damage.</p>
<p>None of this happens overnight. The therapy sets up better conditions for the body to heal on its own, and healing takes time. Most patients notice early changes within a few weeks, while fuller results tend to develop over three to six months.</p>

<h2>Types of Stem Cell Therapy</h2>
<p>The right approach depends on your condition, the area treated and what the clinical assessment reveals. Brockwell reviews every case individually before settling on a cell source.</p>
<h3>Autologous Stem Cell Therapy</h3>
<p>The cells come from your own body, usually bone marrow or fat. Because they are your own, the risk of rejection stays very low, which is why this is the most common route in orthopedic stem cell therapy.</p>
<h3>Mesenchymal Stem Cell Therapy (MSC)</h3>
<p>Mesenchymal stem cells rank among the most studied cell types in regenerative medicine. Found in bone marrow, fat and other tissues, MSC therapy is a frequent choice for joint, tendon, cartilage and soft-tissue concerns.</p>
<h3>Bone Marrow Concentrate (BMC)</h3>
<p>Here, a clinician draws bone marrow and concentrates it before injecting it into the treatment area. The concentrate carries stem cells, growth factors and other components that can support tissue recovery.</p>
<h3>Adipose-Derived Stem Cell Therapy</h3>
<p>This method takes stem cells from your fat tissue, usually the abdomen. Adipose-derived stem cell treatment is a straightforward harvest that yields a healthy number of cells with minimal disruption.</p>

<h2>Benefits of Stem Cell Therapy</h2>
<p>As part of a proper clinical plan, stem cell therapy can offer several benefits. How much you gain depends on the condition, its severity, the number of sessions and how your body responds.</p>
<p>Reported benefits include:</p>
<ul>
<li>Support for cartilage repair and healthier joints</li>
<li>Less long-term inflammation in joints and soft tissue</li>
<li>Better tendon and ligament recovery</li>
<li>Smoother, more comfortable joint movement over time</li>
<li>A non-surgical joint treatment option for suitable patients</li>
<li>Slower joint degeneration in some cases</li>
<li>A minimally invasive procedure with limited downtime</li>
<li>A treatment that works well alongside PRP, physiotherapy or other orthobiologic care</li>
<li>Lower rejection risk, since autologous protocols use your own cells</li>
</ul>
<p>Results are never guaranteed. A proper assessment decides whether regenerative medicine in Dubai fits your condition.</p>

<h2>The Stem Cell Therapy Process at Brockwell Healthcare</h2>
<p>Care runs through a clear, step-by-step process, and your doctor confirms the right approach before any of it starts.</p>
<h3>Step 1: Booking</h3>
<p>Get in touch with Brockwell Healthcare to arrange your consultation. The team helps you choose the right appointment and explains what to prepare, whether that means imaging, blood tests or fasting.</p>
<h3>Step 2: Consultation and Assessment</h3>
<p>Your doctor works through your medical history, past treatments, scans, medications and goals, then examines the affected joint or tissue in person. This stage settles whether regenerative stem cell therapy suits you, which cell source to use and how the plan should look. Any reason the treatment might not be safe is flagged here.</p>
<h3>Step 3: Harvesting</h3>
<p>For patients using their own cells, harvesting happens in a sterile clinical setting under local anaesthetic. For bone marrow stem cell therapy, the doctor draws a small amount of marrow from the back of the pelvis with a needle, which takes around 15 to 30 minutes. For adipose-derived stem cell treatment, a mini-liposuction technique removes a small amount of fat from the abdomen or sides. The site is cleaned and dressed straight after.</p>
<h3>Step 4: Processing</h3>
<p>The sample goes to a sterile lab at once. A centrifuge separates the useful cells and growth factors from the rest, creating bone marrow concentrate from marrow, or a cell-rich fraction from fat. Your doctor checks the stem cell concentrate before using it.</p>
<h3>Step 5: Administration</h3>
<p>Next, the doctor injects the concentrate into the treatment area under ultrasound guidance, watching the needle position in real time. That precision matters most in joints, tendons and deeper tissue. The injection itself takes only a few minutes, local anaesthetic keeps discomfort low, and the team monitors you throughout.</p>
<h3>Step 6: Aftercare and Follow-Up</h3>
<p>Afterwards, the doctor dresses the site and hands you clear aftercare instructions. These often include resting for 24 to 48 hours, easing off certain activities for a while, and guidance on when to start physiotherapy. Follow-up visits track your recovery, review your progress and decide whether any further treatment makes sense.</p>

<h2>Why Patients Choose Brockwell Healthcare for Stem Cell Therapy</h2>
<p>At Brockwell Healthcare we offer:</p>
<ul>
<li>A DHA-licensed doctor with regenerative medicine expertise plans and supervises every session</li>
<li>Harvesting, processing and administration all take place under sterile clinical conditions</li>
<li>Ultrasound guidance directs every injection for accurate, real-time placement</li>
<li>Each protocol, cell source and session plan is built around your specific condition</li>
<li>A full contraindication screen comes before any regenerative cell treatment begins</li>
<li>Realistic outcomes are set out plainly before your doctor recommends a procedure</li>
<li>Clear pricing is confirmed before your first session, with no surprises</li>
</ul>

<h2>Book Stem Cell Therapy in Dubai</h2>
<p>Book a stem cell therapy consultation at Brockwell Healthcare in Dubai. Your doctor reviews your condition, explains whether the treatment suits you, walks you through the process and confirms the cost before anything begins.</p>
"""

FAQS = [
    ("What can stem cell treatment help with?",
     "Stem cell treatment in Dubai may help with joint pain, cartilage damage, tendon and ligament injuries, sports recovery and early osteoarthritis. It does not suit every condition, so your doctor assesses your case and reviews your scans and history first."),
    ("What should I do before a session?",
     "Follow the preparation guidance from your team. That may mean fasting, pausing certain medications, bringing recent scans and avoiding anti-inflammatories in the days before your appointment."),
    ("How many sessions will I need?",
     "Many patients need only one, though it depends on the condition and how your body responds. Your doctor explains the recommended plan after your consultation and assessment."),
    ("What side effects can occur?",
     "Temporary soreness, swelling or bruising at the harvest or injection site are the most common effects, and they usually settle within a few days. Serious complications are uncommon when the team follows proper protocols."),
    ("Is mesenchymal stem cell therapy safe?",
     "Yes. MSC therapy is considered safe when qualified doctors carry it out with proper screening and sterile technique."),
    ("Is the treatment painful?",
     "You may feel mild discomfort during harvesting, which happens under local anaesthetic, and some pressure during the injection. Most patients cope well, and any soreness afterwards eases within a few days."),
    ("How long does one session take?",
     "A full session covering harvesting, processing and injection usually runs two to three hours. The consultation and preparation happen earlier, on a separate visit."),
    ("Can it be combined with PRP or other treatments?",
     "Yes. A regenerative medicine plan at Brockwell can pair stem cell treatment with PRP, hyaluronic acid, physiotherapy or other options, depending on what your case needs."),
    ("What does stem cell therapy cost in Dubai?",
     "Cost depends on the cell source, treatment area, protocol and number of sessions. You receive clear pricing and a full estimate before any treatment starts."),
    ("Who should consider stem cell therapy?",
     "It may suit patients with ongoing joint pain, cartilage wear, early osteoarthritis, or tendon, ligament and sports injuries that have not responded well to other care."),
    ("Who should avoid it, or check with a doctor first?",
     "Stem cell treatment does not suit patients with an active infection near the treatment area, blood-clotting disorders, active cancer, uncontrolled diabetes or serious illness. Pregnant patients need medical clearance first."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    svc = Service.objects.filter(region="uae", slug="stem-cells").first()
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
        ("services", "0013_red_light_therapy_content"),
        ("core", "0010_remove_oscar_tellez"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
