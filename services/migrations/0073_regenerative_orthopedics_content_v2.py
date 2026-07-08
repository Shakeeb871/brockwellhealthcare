"""Update the existing Regenerative Orthopedics service with the user's restructured,
narrative copy (British 'orthopaedics' spelling in the visible text). Prose-led with no
card grid, timeline or lists, a reworked section set and a 7-item FAQ. Keeps the hero and
inline content images. Supersedes the previous content.
Hero: static/img/services/regenerative-orthopedics-hero.webp;
inline: static/img/services/regenerative-orthopedics-content.webp."""

from django.db import migrations

SLUG = "regenerative-orthopedics"

SEO_TITLE = "Regenerative Orthopaedics in Dubai | Non-Surgical | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Regenerative orthopaedics in Dubai at Brockwell Healthcare, using PRP, stem cells, "
    "prolotherapy and shockwave to treat joint, tendon and ligament problems without "
    "surgery where possible."
)
HERO_HEADING = "Regenerative orthopaedics in Dubai"
SUMMARY = (
    "Non-surgical, ultrasound-guided orthobiologic care, PRP, stem cells, prolotherapy, "
    "hydrodissection and shockwave, for joint, tendon and ligament problems."
)

DESCRIPTION = """
<p>Regenerative orthopaedics is the part of orthopaedic care that tries to help a joint, tendon or ligament heal instead of replacing or operating on it. It brings together a set of treatments, known collectively as orthobiologics, that use your own biology to support repair. At Brockwell Healthcare our doctors offer regenerative orthopaedics in Dubai for the worn joints and stubborn soft-tissue injuries that sit between conservative care and surgery, and every plan begins by working out whether these approaches genuinely suit your problem.</p>

<h2>What is regenerative orthopaedics?</h2>
<p>Regenerative orthopaedics is a non-surgical approach to musculoskeletal problems that aims to stimulate the body's own repair and not remove or replace damaged tissue. The treatments involved are called orthobiologics, because they use biological materials such as your blood, bone marrow or fat, alongside techniques that release trapped nerves or trigger healing in stalled tissue. The whole point is to sit in the gap between rest and physiotherapy on one side and an operation on the other.</p>

<h2>The treatments under one roof</h2>
<p>What makes this a field and not a single procedure is the toolkit, and choosing between the tools is most of the skill. Platelet-rich plasma, or PRP, concentrates the growth factors from your own blood and injects them into an injured tendon or joint. Bone marrow and fat-derived preparations bring mesenchymal stem cells into the same work, which is covered in detail on our stem cell therapy page. Prolotherapy uses a mild irritant solution to prompt a healing response in loose or painful ligaments. Hydrodissection frees a compressed nerve with fluid under ultrasound, and shockwave therapy uses acoustic energy to restart repair in a chronic tendon. Most of these are placed with ultrasound guidance, so the material reaches the exact structure that needs it.</p>

<h2>How these treatments work</h2>
<p>The common thread is biology, not hardware. Orthobiologics work by delivering the body's own repair signals, the growth factors, cells and messengers that drive healing, straight to the tissue that has stopped mending on its own. PRP, for instance, carries a concentrated dose of platelet growth factors, while stem cell preparations add cells that release their own signalling molecules and help calm inflammation. Techniques like shockwave and prolotherapy take a different route to the same end, provoking a controlled, low-level stimulus that wakes a stalled repair process back up. Ultrasound guidance runs through all of it, because a growth factor placed a few millimetres off target does little good.</p>

<img src="/static/img/services/regenerative-orthopedics-content.webp" alt="Doctor performing an ultrasound-guided regenerative orthopaedics injection at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>What regenerative orthopaedics is used for</h2>
<p>These treatments are considered most often for knee osteoarthritis, meniscal and ligament injuries, rotator cuff and other shoulder problems, hip and gluteal tendon pain, tennis and golfer's elbow, Achilles and patellar tendinopathy, plantar fasciitis, and sacroiliac joint pain. Many people arrive having already tried rest, physiotherapy and anti-inflammatories, and they want to understand what sits between that and surgery. None of these treatments is guaranteed, the evidence is stronger for some uses than others, and our doctors are honest about which of your problems is a reasonable candidate and which is not.</p>

<h2>Who it suits, and where its limits are</h2>
<p>Regenerative orthopaedics tends to suit people with a clear musculoskeletal diagnosis who would rather explore biological repair before committing to an operation, and who hold realistic expectations about gradual, variable results. It is not a fit for everyone. Advanced, bone-on-bone joint damage may be beyond what these treatments can help, some conditions genuinely need surgery, and screening sets aside anyone with active infection, certain cancers or other specific contraindications. A proper assessment, including imaging, is what separates a good candidate from a poor one, and it is where every plan starts.</p>
"""

FAQS = [
    ("What is regenerative orthopaedics?",
     "It is a non-surgical branch of orthopaedic care that uses your own biology, through treatments called orthobiologics such as PRP and stem cells, to support the repair of joints, tendons and ligaments. It aims to sit between conservative care and surgery for suitable problems."),
    ("Is it a real alternative to surgery?",
     "For some suitable problems it is worth exploring before an operation, though it is not right for every case and cannot rebuild a severely damaged joint. Our doctor gives an honest view of where it fits for your specific condition after examining you and your imaging."),
    ("What conditions does it treat?",
     "Most often knee osteoarthritis, tendon problems such as tendinopathy, rotator cuff injuries, ligament issues, tennis elbow, plantar fasciitis and sacroiliac pain, usually once conservative care has not done enough."),
    ("Which treatment would I have?",
     "That depends on the diagnosis. PRP, stem cell preparations, prolotherapy, hydrodissection and shockwave each suit different problems, and often a plan combines them. Your doctor matches the tool to the tissue."),
    ("Is it painful?",
     "Most involve an injection, often with local anaesthetic, and any soreness afterwards is usually mild and short-lived. Your clinician explains what to expect for the specific treatment."),
    ("How many sessions will I need?",
     "It varies by treatment and condition, from a single injection to a short course, and your doctor sets a plan after the assessment and reviews it as you respond."),
    ("How much does regenerative orthopaedics cost in Dubai?",
     "The cost depends on which treatments are used and how many sessions are needed, and we set out the pricing in full before you go ahead."),
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
        ("services", "0072_red_light_therapy_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
