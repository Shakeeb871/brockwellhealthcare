"""Refresh the Stem Cells service with the user's condensed, narrative copy: reworked
section set (What is / How it works / The cell sources / What it is studied for / Who it
suits / What treatment involves) and a 7-item FAQ. Prose-led, no card grid, timeline or
lists. Keeps the hero and inline content images. Supersedes 0063 / 0053.
Hero: static/img/services/stem-cells-hero.webp;
inline: static/img/services/stem-cells-content.webp."""

from django.db import migrations

SLUG = "stem-cells"

SEO_TITLE = "Stem Cell Therapy in Dubai | Regenerative Medicine | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led stem cell therapy in Dubai at Brockwell Healthcare for joint, tendon and "
    "soft-tissue concerns, using your own cells, with honest evidence and assessment first."
)
HERO_HEADING = "Stem cell therapy in Dubai"
SUMMARY = (
    "Doctor-led stem cell therapy for joint, tendon and soft-tissue concerns, using your "
    "own cells, with honest evidence and assessment first."
)

DESCRIPTION = """
<p>Stem cell therapy works with cells that have not yet committed to a single job in the body, using them to support repair in worn joints and stubborn soft-tissue injuries. There is a common misunderstanding that these cells simply replace damaged tissue, when in practice most of their effect comes from the signals they release into the area around them. Our doctors at Brockwell Healthcare offer stem cell therapy in Dubai as one part of regenerative care, and because the science here is genuinely mixed, every plan begins with an honest look at whether it suits you.</p>

<h2>What is stem cell therapy?</h2>
<p>Stem cell therapy is a branch of regenerative medicine built around mesenchymal stem cells, usually shortened to MSCs. There is an agreed definition for these cells, set by the International Society for Cellular Therapy, and it is more specific than most people expect. To count as an MSC, a cell has to stick to plastic in culture, carry the surface markers CD73, CD90 and CD105 while lacking blood-cell markers such as CD34 and CD45, and be able to turn into bone, cartilage and fat cells. That last ability, the trilineage potential, is what makes them interesting for joints and tendons. One honest note belongs here, which is that many experts now prefer the term mesenchymal stromal cells, because the prepared cells are a mixed population and only a fraction behave as true stem cells.</p>

<h2>How it works</h2>
<p>The interesting part is how these cells talk to the tissue around them. MSCs work mainly through paracrine signalling, meaning they release a steady stream of growth factors and other molecules into their surroundings. Among these are vascular endothelial growth factor, or VEGF, which encourages new blood vessels, and transforming growth factor beta, which has a hand in repair, and they also help calm local inflammation. So the cells act less like spare parts and more like coordinators, studied for the way they may shift a stalled, inflamed area back towards repair. There is even evidence that MSCs can hand over healthy mitochondria to struggling cells, a genuinely surprising mechanism still being worked out.</p>

<img src="/static/img/services/stem-cells-content.webp" alt="Doctor preparing a stem cell therapy treatment under ultrasound guidance at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>The cell sources</h2>
<p>The right preparation depends on your case. Autologous therapy uses cells from your own body, which keeps the risk of rejection very low and is the usual route in joint and tendon work. Where those cells come from makes a practical difference. Bone marrow is drawn from the back of the pelvis, at the posterior iliac crest, then spun in a centrifuge to produce bone marrow concentrate, often called BMAC, which brings cells and growth factors together in a smaller volume. Fat is the other common source, taken from the abdomen through a small liposuction-style harvest, and gram for gram it tends to yield far more MSCs than marrow, which is why adipose-derived preparations have become popular.</p>

<h2>What it is studied for, and the honest evidence</h2>
<p>Everything stem cell therapy is explored for comes back to supporting the body's own repair, so the effects are gradual, vary between people, and are never guaranteed. It is studied for worn cartilage and irritated tendon or ligament tissue, for easing the pain and stiffness of joint degeneration, and, through the VEGF it releases, for better local blood supply, all while using your own cells to keep rejection risk low. The honest side matters just as much. Results across trials have been inconsistent, and the field has had high-profile disappointments, such as the Prochymal product missing its main goals in a large graft-versus-host-disease trial. We tell you where the evidence is reasonable and where it is still thin.</p>

<h2>Who it suits, and the screening first</h2>
<p>Most people who ask about this have a musculoskeletal problem that has ground on for months or years, most often knee osteoarthritis, meniscal and ligament injuries, rotator cuff and other shoulder or hip trouble, tendinopathy, or sacroiliac joint pain, usually after rest, physiotherapy and standard injections have not done enough. Screening comes first, because it is not right for everyone. Our doctor sets stem cell therapy aside where there is active cancer or infection, among other situations, and there is good reason for the caution, since these cells influence blood-vessel growth and immune activity and are best kept away from anything that influence could worsen.</p>

<h2>What treatment involves</h2>
<p>If treatment goes ahead, most of it happens in a single visit. The cells are collected, whether from marrow or fat, prepared on the same day under sterile conditions, and placed back into the target area with ultrasound guidance so they reach the exact spot inside a joint or alongside a tendon. Because your own cells are used, after-effects are usually minor and short-lived, most often a little swelling, bruising or soreness for a day or two. Any real benefit then builds gradually over weeks to months as the tissue responds, usually supported by physiotherapy to protect the result.</p>
"""

FAQS = [
    ("What is the difference between stem cell therapy and PRP?",
     "They are related but not the same. PRP uses concentrated platelets and growth factors spun from your own blood, while stem cell approaches work with cells taken from bone marrow or fat. Both are regenerative, they are sometimes used together, and our doctor explains which fits your situation."),
    ('Are these really "stem cells"?',
     "Partly. The preparations are a mixed population, and only a fraction behave as true stem cells, which is why many specialists call them mesenchymal stromal cells. They still carry the recognised MSC markers and release the signalling factors that make the approach worth studying."),
    ("What conditions is it used for?",
     "Most often knee osteoarthritis, meniscal and ligament injuries, rotator cuff and other shoulder or hip problems, tendinopathy and sacroiliac joint pain, usually once conservative care has not done enough, with suitability confirmed at assessment."),
    ("Does it hurt?",
     "Most people feel the discomfort of the harvest and the injection, usually eased with local anaesthetic, and any soreness afterwards is mild and settles within a few days."),
    ("How long until I might notice a difference?",
     "Because it works with your own repair, change tends to build over weeks to months and varies a great deal between people, which is why we keep expectations grounded."),
    ("Is stem cell therapy safe?",
     "Using your own cells keeps the risks low, and most after-effects are minor. It is not suitable for everyone, and the screening at assessment, including for active cancer or infection, is there precisely because these cells influence blood-vessel growth and the immune system."),
    ("Can it help me avoid surgery?",
     "For some suitable joint and tendon problems it is worth exploring first, though it is not right for every case and is not guaranteed. Our doctor gives an honest read on where it sits for your condition."),
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
    svc.benefits = ""
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
        ("services", "0093_regenerative_wellness_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
