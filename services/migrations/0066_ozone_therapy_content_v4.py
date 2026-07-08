"""Replace the Ozone Therapy service content with the user's restructured, narrative,
safety-first copy. Prose-led: only 'What ozone is explored for' carries a list; the
remaining sections are paragraphs, with no card grid or timeline. New meta title and a
shorter (7-item) FAQ. Supersedes 0058. Images added later."""

from django.db import migrations

SLUG = "ozone-therapy"

SEO_TITLE = "Ozone Therapy in Dubai | Medical Ozone | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led medical ozone therapy in Dubai for recovery, inflammation, immune "
    "wellbeing and circulation support. Sterile, closed-system delivery built around "
    "careful screening."
)
HERO_HEADING = "Ozone therapy in Dubai"
SUMMARY = (
    "Doctor-led medical ozone therapy for recovery, inflammation, immune wellbeing and "
    "circulation, delivered by sterile, closed-system methods and built around careful "
    "screening."
)

DESCRIPTION = """
<p>Ozone is oxygen with an extra atom. Ordinary oxygen is two atoms bonded together, and ozone is three, which makes it unstable and highly reactive. That reactivity is exactly why it is useful, because a small, controlled dose can prompt a response that plain oxygen cannot. Medical ozone is made fresh from medical-grade oxygen through a generator and used within moments, since it cannot be stored. At Brockwell Healthcare our doctors deliver it across several methods in Dubai, and with a treatment this reactive, two things drive everything, which are careful screening and correct technique.</p>

<h2>What is ozone therapy?</h2>
<p>Ozone therapy is the medical use of a precise mixture of oxygen and ozone. Passing medical-grade oxygen through a generator produces a set concentration, measured in micrograms per millilitre, and different methods call for different concentrations. The gas is produced and used in the same moment, never bottled and stored.</p>

<h2>Why safety comes first with ozone</h2>
<p>Most treatment pages leave safety until the end. With ozone it belongs at the front, because two points genuinely govern whether it can be done at all. The first is simple and absolute. Ozone gas must never be inhaled, since it is harmful to the lungs, which is why every medical method delivers it by another route entirely, into the blood, into a body cavity, or onto the skin.</p>
<p>The second is about who ozone suits. People with G6PD deficiency, a condition where red blood cells break down easily, are at real risk from the oxidative nature of ozone, so a simple blood test for it is often done before treatment. Ozone is also avoided in clotting disorders, hyperthyroidism, active cancer without clearance, serious uncontrolled heart disease, and during pregnancy without clearance. Screening for these is not a formality. It is the difference between a safe treatment and a dangerous one.</p>

<h2>How a small, controlled dose works</h2>
<p>The mechanism is almost counterintuitive. A measured dose of ozone creates a brief, mild burst of oxidative stress, and the body answers by switching on its own antioxidant defences. This deliberate, low-level challenge is sometimes called oxidative eustress, and it is thought to activate a cellular pathway called Nrf2, which raises protective enzymes such as superoxide dismutase, glutathione peroxidase and catalase. When ozone is used in the blood, it also interacts with red cells and plasma, and researchers have looked at whether this helps oxygen reach the tissues more readily and whether it influences inflammatory and immune signalling. How much of this helps depends on the method, the dose and the person.</p>

<h2>The methods, from gentle to intensive</h2>
<p>Ozone can be given in several ways, and the right one depends on your goal. Major autohemotherapy, the most common blood-based method, draws roughly a hundred to two hundred millilitres of your blood into a sterile system, mixes it with a measured ozone dose and returns it. EBOO, which stands for extracellular blood oxygenation and ozonation and is sometimes called the ten-pass, cycles a larger volume through a filter for a more intensive session. Minor autohemotherapy uses only a few millilitres given back into muscle. Away from the blood, rectal insufflation is a gentle and well-established route, with vaginal and ear insufflation used for local purposes. Prolozone combines ozone with a local anaesthetic and nutrients around a joint, and ozonated oils and water are used on the skin. A session can run from a few minutes for insufflation to around ninety minutes for EBOO.</p>

<h2>What ozone is explored for</h2>
<p>When the right method is matched to the right concern, ozone therapy is studied for several possibilities, none of them guaranteed and all of them dependent on the person:</p>
<ul>
<li>support for recovery after illness, exertion or sustained stress</li>
<li>a role in how efficiently red blood cells release oxygen to the tissues</li>
<li>help with the body's response to chronic, low-grade inflammation</li>
<li>support for immune wellbeing and for recurrent infections</li>
<li>better circulation, including support for slow-healing wounds</li>
</ul>
<p>The evidence is stronger for some of these than others, and our doctors are clear about where that line sits and not blurring it.</p>

<h2>What a session and a course look like</h2>
<p>Before a first session, you and your doctor go through your history, medications and blood results, settle on the method and concentration that suit your goal, and map out the plan. A blood test for G6PD is often part of that. On the day, a blood-based session feels much like a standard IV, carried out with sealed, sterile equipment while your comfort is watched, whereas insufflation and topical routes are quicker and gentler. Most plans then run as a course over several weeks, because a single session is rarely the whole story, with spaced maintenance added later where it helps.</p>
"""

FAQS = [
    ("What is the difference between MAH and EBOO?",
     "Both are blood-based but differ in scale. Major autohemotherapy draws around a hundred to two hundred millilitres of blood, ozonates it in a closed system and returns it, while EBOO cycles a much larger volume through a filter for a more intensive session."),
    ("Can ozone gas be inhaled?",
     "No, and it is the most important safety point of all. Ozone gas must never be inhaled because it harms the lungs. Every medical method is designed to deliver it by another route entirely."),
    ("Why test for G6PD deficiency?",
     "Because ozone works through mild oxidative stress, and people with G6PD deficiency have red cells prone to breaking down under it. A simple blood test rules this out beforehand, which is central to doing ozone safely."),
    ("What is prolozone?",
     "Prolozone is a joint-focused method that mixes ozone with a local anaesthetic and nutrients, injected around a joint or soft tissue. Your doctor advises whether it fits your case."),
    ("Does ozone therapy hurt?",
     "Most methods involve little more than a needle for blood access or a gentle insufflation, and a blood-based session feels similar to a routine IV."),
    ("How many sessions are usual?",
     "Most plans run as a course over several weeks, with the exact number depending on the method and your response, reviewed as you go."),
    ("Is ozone therapy safe?",
     "In trained hands, with proper screening and sterile technique, ozone can be delivered within a controlled plan. It does not suit everyone, and the screening beforehand, especially for G6PD deficiency, is what keeps it safe."),
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
        ("services", "0065_peptide_therapy_content_v5"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
