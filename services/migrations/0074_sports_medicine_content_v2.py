"""Update the existing Sports Medicine service with the user's restructured, narrative
copy. Prose-led with no card grid, timeline or lists, a reworked section set and a
6-item FAQ. Keeps the hero and inline content images. Supersedes the previous content.
Hero: static/img/services/sports-medicine-hero.webp;
inline: static/img/services/sports-medicine-content.webp."""

from django.db import migrations

SLUG = "sports-medicine"

SEO_TITLE = "Sports Medicine in Dubai | Injury & Return to Play | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Sports medicine in Dubai at Brockwell Healthcare for the diagnosis, treatment and "
    "rehabilitation of sports injuries, with a clear, staged path back to the activity you "
    "care about."
)
HERO_HEADING = "Sports medicine in Dubai"
SUMMARY = (
    "Diagnosis, treatment and rehabilitation of sports and activity injuries, with a clear, "
    "staged path back to the activity you care about."
)

DESCRIPTION = """
<p>Sports medicine is the care of injuries and performance problems that come from physical activity, in athletes and in anyone active. It covers the whole arc of an injury, from working out exactly what is wrong, through treatment, to a properly staged return to sport. At Brockwell Healthcare our sports medicine service in Dubai is built around that arc, because getting someone back to running or lifting safely matters as much as settling the pain in the first place.</p>

<h2>What a sports medicine doctor actually does</h2>
<p>A sports medicine doctor diagnoses and manages injuries of muscles, tendons, ligaments, joints and bones, and guides the return to activity. The work splits into two broad kinds of injury. Acute injuries happen in a moment, a rolled ankle or a torn hamstring, while overuse injuries build slowly from repeated load, such as runner's knee or a tendinopathy. The two need different thinking, and telling them apart is the first real job.</p>

<h2>Getting the diagnosis right</h2>
<p>Everything downstream depends on an accurate diagnosis, so this comes first and properly. Our doctor takes a detailed history of how the injury happened and examines the area, then uses imaging where it adds something. Diagnostic ultrasound is particularly useful for tendons, muscles and ligaments because it shows them moving in real time, while an MRI is reserved for deeper or more complex problems such as a suspected cartilage or ligament tear. The aim is a specific diagnosis, for example a grade two hamstring strain and not simply "a pulled muscle", because the grade changes the timeline and the plan.</p>

<img src="/static/img/services/sports-medicine-content.webp" alt="Sports medicine doctor assessing an injury with diagnostic ultrasound at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>How injuries are treated now</h2>
<p>Sports injury care has moved on, and it is worth knowing how. The old advice to rest and ice everything has largely given way to an approach summed up as PEACE and LOVE, which protects the injury early but then reintroduces movement and load sooner, because tissue heals better when it is gradually challenged than when it is wrapped in cotton wool. Treatment might combine hands-on rehabilitation, a structured loading programme, and where useful the clinic's other tools, such as shockwave therapy for a stubborn tendon or an ultrasound-guided injection. The thread running through all of it is load managed intelligently, not activity avoided.</p>

<h2>The part most clinics skip: returning to sport</h2>
<p>Coming back too early is how injuries turn into recurring injuries, so the return is treated as its own stage and not an afterthought. The return to sport is guided by what you can actually do, so instead of a date on a calendar you meet clear physical milestones for strength, movement and control before progressing. Our team plans a graded build back to training and then to competition, so the tissue is ready for the demands you are about to put on it. Done well, this is what stops the same hamstring going twice in a season.</p>
"""

FAQS = [
    ("What does a sports medicine doctor do?",
     "A sports medicine doctor diagnoses and treats injuries of muscles, tendons, ligaments, joints and bones from physical activity, and guides a safe, staged return to sport. The role covers both sudden injuries and gradual overuse problems, without necessarily involving surgery."),
    ('Is the old "RICE" advice outdated?',
     "Largely, yes. Resting and icing everything has given way to approaches like PEACE and LOVE, which protect an injury early but then reintroduce movement and load sooner, because controlled loading generally helps tissue heal better than prolonged rest."),
    ("Do I always need an MRI?",
     "No. Many sports injuries are diagnosed from the examination and diagnostic ultrasound, which shows soft tissue moving in real time. An MRI is used for deeper or more complex problems, such as a suspected ligament or cartilage tear."),
    ("How long until I can play again?",
     "It depends on the injury and its grade, which is why an accurate diagnosis matters so much. The return is guided by meeting strength and movement milestones, not a fixed date, so you come back when the tissue is genuinely ready."),
    ("Do sports injuries need surgery?",
     "Most do not. The majority are managed with rehabilitation, load management and, where useful, treatments like shockwave or guided injections, with surgery reserved for specific structural injuries that need it."),
    ("Can you treat non-athletes?",
     "Yes. The same principles apply to anyone active, whether that is a weekend runner, a gym-goer or someone whose job is physical, and the plan is built around your goals."),
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
        ("services", "0073_regenerative_orthopedics_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
