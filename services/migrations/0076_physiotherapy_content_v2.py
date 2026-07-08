"""Update the existing Physiotherapy service with the user's restructured, narrative,
assessment-and-exercise-led copy. Prose-led with no card grid, timeline or lists, a
reworked section set and a 6-item FAQ. Supersedes the previous content (0046). Images
added later (no physiotherapy image is present yet)."""

from django.db import migrations

SLUG = "physiotherapy"

SEO_TITLE = "Physiotherapy in Dubai | Assessment-Led Rehab | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Physiotherapy in Dubai at Brockwell Healthcare for back pain, sports injuries, "
    "post-surgical recovery and mobility, built on accurate assessment and active, "
    "evidence-based rehabilitation."
)
HERO_HEADING = "Physiotherapy in Dubai"
SUMMARY = (
    "Assessment-led, exercise-based physiotherapy for back pain, sports injuries, "
    "post-surgical recovery and mobility, built on an accurate diagnosis and an active plan."
)

DESCRIPTION = """
<p>Physiotherapy is the treatment of pain, injury and movement problems through assessment, hands-on care and, above all, targeted exercise. It is one of the best-evidenced treatments in musculoskeletal care, which is worth saying at the start, because it does the quiet, unglamorous work of getting a body moving properly again. At Brockwell Healthcare our physiotherapy service in Dubai is built around an accurate diagnosis and an active plan, since the fastest way through most injuries is rarely rest alone.</p>

<h2>What a physiotherapist actually does</h2>
<p>A physiotherapist assesses how you move, works out what is driving your pain or restriction, and treats it with a mix of manual therapy and prescribed exercise. The job is as much detective work as treatment, because knee pain might come from the hip, and back pain might come from how you load, not from any single damaged part. Getting that cause right is what makes the plan work.</p>

<h2>Why the exercise matters more than the couch</h2>
<p>There is a common picture of physiotherapy as massage and machines, and that misses the point. The hands-on part, the manual therapy that eases a stiff joint or a tight muscle, is genuinely useful, but it mostly opens a window. The lasting change comes from loading the tissue in a graded, progressive way, because muscle, tendon and bone all get stronger by being asked to do a little more over time. A good physiotherapist spends less effort doing things to you and more effort building the exercise plan that does the real work, which is why your input between sessions matters so much.</p>

<h2>What physiotherapy treats</h2>
<p>Physiotherapy helps with a wide span of problems, and it is the first-line treatment for most of them. It is used for lower back and neck pain, sports injuries such as hamstring and ankle strains, tendon problems like tennis elbow and Achilles tendinopathy, shoulder conditions, post-surgical recovery after a joint operation, and the gradual loss of strength and mobility that comes with age or inactivity. In our clinic it often runs alongside other treatments, so a stubborn tendon might have shockwave therapy while physiotherapy rebuilds the strength around it.</p>

<h2>What to expect, from first visit to discharge</h2>
<p>Your first appointment is a proper assessment, where the physiotherapist takes a history, watches how you move and tests the area to reach a working diagnosis. From there you get a plan, usually a combination of some hands-on treatment and a set of specific exercises to do between sessions, with clear goals. As you improve, the exercises are progressed, made harder in a controlled way, so the tissue keeps adapting, and the aim throughout is to get you independent, not reliant on appointments. Being discharged with a body that works is the goal, not an endless run of visits.</p>
"""

FAQS = [
    ("What does a physiotherapist do?",
     "A physiotherapist diagnoses and treats pain, injury and movement problems using assessment, manual therapy and prescribed exercise. The work focuses on finding the real cause of a problem and building a plan, mostly exercise-based, that restores strength, movement and function."),
    ("Does physiotherapy actually work?",
     "Yes, and it is one of the best-evidenced treatments in musculoskeletal care. It is the recommended first-line approach for most back pain, sports injuries and tendon problems, and it works best when you also do the prescribed exercises between sessions."),
    ("How many sessions will I need?",
     "It varies with the problem, from a few sessions for a simple strain to a longer course for post-surgical recovery. A good physiotherapist aims to make you independent with a home programme, not to keep you coming back indefinitely."),
    ("Is physiotherapy painful?",
     "Some treatment and exercise can be mildly uncomfortable, particularly early on, but it should never be about pushing through severe pain. Your physiotherapist works within what your tissue can handle and progresses it sensibly."),
    ("Should I rest my injury or move it?",
     "For most injuries, controlled movement beats prolonged rest, because tissue heals and strengthens by being gradually loaded. Your physiotherapist guides how much and how soon, which is the skilled part."),
    ("What is the difference between physiotherapy and a chiropractor?",
     "Physiotherapy is broad and heavily exercise-based, treating a wide range of injuries and rehabilitation needs, and it is what most guidelines recommend first for musculoskeletal pain. Your doctor can advise which suits your particular problem."),
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
        ("services", "0075_pemf_therapy_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
