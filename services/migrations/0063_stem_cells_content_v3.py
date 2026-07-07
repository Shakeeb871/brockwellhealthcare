"""Refresh the Stem Cells service with the user's revised, more narrative copy.
This version is prose-led: the 'Types', 'Your patient journey' and 'Why choose'
sections are single paragraphs (no card grid or timeline), and only the Benefits
section carries a list. Keeps the hero and inline content images. Supersedes the
previous stem cell content (0052 / 0053)."""

from django.db import migrations

SLUG = "stem-cells"

SEO_TITLE = "Stem Cell Therapy in Dubai | Regenerative Medicine | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led stem cell therapy in Dubai at Brockwell Healthcare for joint, tendon and "
    "soft-tissue concerns. Honest, assessment-first regenerative care using your own cells."
)
HERO_HEADING = "Stem cell therapy in Dubai"
SUMMARY = (
    "Doctor-led, assessment-first regenerative care for joint, tendon and soft-tissue "
    "concerns, using mesenchymal cells from your own bone marrow or fat."
)

DESCRIPTION = """
<p>Stem cell therapy works with a particular kind of cell that has not yet committed to a single job in the body. In regenerative orthopaedics the cells used are almost always mesenchymal stem cells, usually shortened to MSCs, drawn from your own bone marrow or fat. There is a common misunderstanding that these cells simply replace worn tissue. In practice, most of their effect comes from the signals they release into the area around them, which is a more interesting and more useful thing. Our doctors at Brockwell Healthcare work with them for worn joints and stubborn soft-tissue injuries, and because the science here is genuinely mixed, every plan starts with an honest look at whether it is worth doing for you at all.</p>

<h2>What is stem cell therapy?</h2>
<p>Stem cell therapy is a branch of regenerative medicine built around mesenchymal stem cells. There is an agreed definition for these cells, set out by the International Society for Cellular Therapy, and it is more specific than most people expect. To count as an MSC, a cell has to stick to plastic in culture, carry the surface markers CD73, CD90 and CD105 while lacking blood-cell markers such as CD34 and CD45, and be able to turn into bone, cartilage and fat cells under the right conditions. That last ability, the trilineage potential, is what makes them interesting for worn joints and tendons.</p>
<p>One point of honesty matters up front. Many experts now prefer the term mesenchymal stromal cells, because the cells prepared for treatment are a mixed population and only a small fraction behave as true stem cells. It is a small distinction on paper and a meaningful one in practice, and it is the kind of thing we would rather explain than gloss over.</p>

<h2>How does stem cell therapy work?</h2>
<p>The interesting part is how these cells talk to the tissue around them. MSCs work mainly through what is called paracrine signalling, meaning they release a steady stream of growth factors and other molecules into their surroundings. Among these are vascular endothelial growth factor, or VEGF, which encourages new blood vessels to form, and transforming growth factor beta, which has a hand in tissue repair. They also release their own tiny signalling packets, and they help calm down local inflammation.</p>
<p>So the cells act less like spare parts and more like coordinators. They are studied for the way they may shift a stalled, inflamed area back towards repair, partly by improving its blood supply and partly by settling the immune activity that keeps a tendon or joint irritated. There is even evidence that MSCs can hand over healthy mitochondria to struggling cells, which is a genuinely surprising mechanism and still being worked out. How much of this helps any one person is uncertain, and it depends heavily on the tissue and the problem, which is exactly why a careful assessment comes before anything else.</p>

<img src="/static/img/services/stem-cells-content.webp" alt="Doctor preparing a stem cell therapy treatment under ultrasound guidance at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>Types of stem cell therapy</h2>
<p>The right preparation depends on your case, so your doctor confirms it after examining you. Autologous therapy uses cells from your own body, which keeps the risk of rejection very low and is the usual route in joint and tendon work. Where those cells come from makes a practical difference. Bone marrow is drawn from the back of the pelvis, at the posterior iliac crest, then spun in a centrifuge to produce bone marrow concentrate, often called BMAC, which brings the cells and growth factors together in a smaller volume. Fat is the other common source, taken from the abdomen through a small liposuction-style harvest, and gram for gram it tends to yield far more MSCs than marrow does, which is one reason adipose-derived preparations have become popular. Whichever source is chosen, the cells are prepared under sterile conditions and, in most cases, placed back the same day.</p>

<h2>Benefits of stem cell therapy</h2>
<p>Everything stem cell therapy is explored for comes back to supporting the body's own repair, so the effects are gradual, they differ from person to person, and none of them is a promise. The points below describe what the research looks into, not what you are guaranteed to feel.</p>
<p>Within a properly assessed plan, the approach is studied and explored for:</p>
<ul>
<li>support for worn cartilage and irritated tendon or ligament tissue</li>
<li>a possible easing of the pain and stiffness of joint degeneration</li>
<li>better local blood supply, since the cells release VEGF and related factors</li>
<li>a calming effect on the low-grade inflammation that keeps a joint sore</li>
<li>use of your own cells, which keeps rejection risk very low</li>
<li>a minimally invasive option worth weighing before surgery, in suitable cases</li>
</ul>
<p>It is worth being straight about the evidence too. Results across trials have been inconsistent, and the field has had high-profile disappointments, such as the Prochymal stem cell product missing its main goals in a large graft-versus-host-disease trial. Whether the approach suits your particular joint is something only an assessment can judge, and our doctors will tell you where the evidence is reasonable and where it is still thin.</p>

<h2>Who is stem cell therapy for?</h2>
<p>Most people who ask about this are living with a musculoskeletal problem that has ground on for months or years. In practice it is considered most often for knee osteoarthritis, meniscal and ligament injuries, rotator cuff and other shoulder or hip trouble, ankle and elbow complaints, tendon problems such as tendinopathy, and pain from the sacroiliac joint. Many have already been through rest, physiotherapy, anti-inflammatories or standard cortisone injections, and they want to understand their non-surgical options properly before agreeing to an operation.</p>
<p>Screening comes first, because this is not right for everyone. Our doctor reviews your history and sets stem cell therapy aside where there is active cancer or an active infection, among other situations that make it unsafe or unsuitable. There is a good reason for the caution. Because these cells influence blood-vessel growth and immune activity, they are best kept well away from anything where that influence could do harm, and the assessment is where all of that is worked through.</p>

<h2>What to expect from stem cell therapy in Dubai</h2>
<p>Your first visit is a consultation, not a procedure. Our doctor takes a full history, examines the joint or tendon, looks over any scans, and gives you a frank account of what the treatment might and might not do for your specific problem.</p>
<p>If treatment does go ahead, most of it happens in a single visit. The cells are collected, whether from marrow or fat, prepared on the same day under sterile conditions, and then placed back into the target area. Ultrasound guides that final injection, so the preparation reaches the exact spot inside a joint or alongside a tendon. Because your own cells are used, the after-effects are usually minor and short-lived, most often a little swelling, bruising or soreness at the harvest and injection sites for a day or two. Our clinician talks you through each step and stays with you throughout.</p>

<h2>Stem cell therapy recovery timeline and what to expect over time</h2>
<p>Regenerative repair runs on biology, not on the timetable anyone would prefer, so any real change tends to build slowly. Some people notice a difference over a few weeks, others over several months, and a proportion notice very little, which we say plainly at the start.</p>
<p>The days right after treatment usually bring the mild soreness described above, and normal daily activity resumes quickly. From there, any genuine benefit tends to develop gradually as the tissue responds to the signalling the cells have set off, and it is often supported by a course of physiotherapy to protect and build on it. Because the biology varies so much between people, our doctors keep the expectations grounded and review how you are actually doing instead of promising a fixed timeline.</p>

<h2>Tailored stem cell therapy programmes for your lifestyle</h2>
<p>A regenerative plan only earns its place when it fits how you actually live, so we build it around your goals and your daily demands. For active people and those recovering from a sports injury, we time the treatment around training and rest and plan a graded return to the movements that matter to you, since loading a treated tendon too early tends to undo the point of it.</p>
<p>For anyone managing a long-standing joint problem alongside work and family, the treatment is arranged around a realistic schedule and paired with the physiotherapy that holds any gains in place. Either way, you will know how each step fits your week and how it works with the rest of your care.</p>

<h2>Why consider stem cell therapy?</h2>
<p>The appeal is reasonably clear. It uses your own cells, it is minimally invasive, and for the right person it is worth exploring before committing to surgery on a worn joint. Having a considered regenerative option to weigh up is, for many people, reason enough to look into it.</p>
<p>The honest side carries just as much weight. This is a developing field, the evidence is stronger for some uses than others, individual responses vary a great deal, and it works best as one part of a broader plan that still includes the basics of load management and rehabilitation. Our doctors go through all of it plainly, because a decision made with the full picture in front of you is the only kind worth making here.</p>

<h2>Your patient journey</h2>
<p>The path here runs in four clear stages. It begins with a consultation, where our doctor takes a history, examines the area, reviews any imaging and says honestly whether stem cell therapy suits your case. Next comes your personalised plan, where we agree the cell source, the preparation and a realistic view of what it can achieve. If treatment goes ahead, the cells are collected, concentrated on the same day and placed under ultrasound guidance in a sterile setting. After that we handle recovery and review, with clear aftercare and a course of rehabilitation folded into your wider plan.</p>

<h2>Why choose Brockwell Healthcare for stem cell therapy</h2>
<p>A few things shape how we work. Our doctors lead every case and confirm the diagnosis and your suitability before anything starts, because this is never a first, casual step. We favour autologous preparations that use your own bone marrow or fat, which keeps the risk of rejection low and the process straightforward. We are honest about a developing field, clear about where the evidence holds up and where it does not, and we will happily explain the details most clinics skip over. And every injection is placed under ultrasound guidance in a sterile setting, with your plan and its pricing set out plainly before you begin.</p>
"""

FAQS = [
    ("What is the difference between stem cell therapy and PRP?",
     "They are related but not the same. PRP uses concentrated platelets and growth factors spun from your own blood, while stem cell approaches work with cells taken from bone marrow or fat. Both are regenerative, they are sometimes used together, and our doctor explains which one fits your situation better."),
    ('Are these really "stem cells"?',
     "Partly. The preparations are a mixed population of cells, and only a fraction behave as true stem cells, which is why many specialists call them mesenchymal stromal cells. They still carry the recognised MSC markers and release the signalling factors that make the approach worth studying, and we are upfront about that nuance."),
    ("Where do the cells come from?",
     "From your own body, usually bone marrow taken from the back of the pelvis or fat taken from the abdomen. Fat generally yields more cells for its volume, while marrow is long established, and your doctor recommends the source that suits your case."),
    ("What conditions is stem cell therapy used for?",
     "It is considered most often for knee osteoarthritis, meniscal and ligament injuries, rotator cuff and other shoulder or hip problems, ankle and elbow complaints, tendinopathy and sacroiliac joint pain, usually once conservative care has not done enough, with suitability confirmed at assessment."),
    ("Is stem cell therapy painful?",
     "Most people feel the discomfort of the harvest and the injection, usually eased with local anaesthetic, and any soreness afterwards is mild and settles within a few days. Our clinician explains what to expect at each step."),
    ("How long until I might notice a difference?",
     "Because it works with your body's own repair, any change tends to build over weeks to months, and it varies a great deal between people, which is why we keep expectations grounded."),
    ("Is stem cell therapy safe?",
     "Using your own cells keeps the risks low, and most after-effects are minor and short-lived. It is not suitable for everyone, and the screening at assessment, including for active cancer or infection, is there precisely because these cells influence blood-vessel growth and the immune system."),
    ("Can stem cell therapy help me avoid surgery?",
     "For some suitable joint and tendon problems it is worth exploring first, though it is not right for every case and it is not guaranteed to work. Our doctor gives you an honest read on where it sits for your particular condition."),
    ("How much does stem cell therapy cost in Dubai?",
     "The cost depends on the cell source, the area treated and the number of sessions, and we explain your pricing clearly before anything begins."),
    ("Do I need a consultation first?",
     "You do. A proper assessment confirms the diagnosis, checks the treatment is safe for you and shapes the plan around your particular joint or injury, so it always comes first."),
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
        ("services", "0062_shock_wave_therapy_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
