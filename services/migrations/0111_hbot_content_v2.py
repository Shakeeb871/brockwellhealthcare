"""Refresh the Hyperbaric Oxygen Therapy service with the user's doctor-led,
honest-evidence copy: reworked section set (What is / How HBOT works / What we use
HBOT for [card grid] / How it fits with our other services / What to expect / The
treatment process / Why patients choose) and a 10-item FAQ. Prose-led. Keeps the hero
and a single inline content image.
Hero: static/img/services/hyperbaric-oxygen-therapy-hero.webp;
inline: static/img/services/hyperbaric-oxygen-therapy-content.webp."""

from django.db import migrations

SLUG = "hyperbaric-oxygen-therapy"

SEO_TITLE = "Hyperbaric Oxygen Therapy in Dubai | Doctor-Led HBOT | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led hyperbaric oxygen therapy in Dubai at Brockwell Healthcare for recovery, "
    "wound healing, performance and longevity. Screened, protocol-driven, with honest "
    "expectations."
)
HERO_HEADING = "Hyperbaric oxygen therapy in Dubai"
SUMMARY = (
    "Doctor-led HBOT for recovery, wound healing, performance and longevity, screened and "
    "protocol-driven, with honest expectations."
)

DESCRIPTION = """
<p>Hyperbaric oxygen therapy at Brockwell Healthcare is a doctor-led treatment in which you breathe pure oxygen inside a pressurised chamber. Every course starts with a consultation with a qualified doctor, and treatment only goes ahead if the assessment shows it is suitable for you.</p>

<h2>What is hyperbaric oxygen therapy at Brockwell Healthcare?</h2>
<p>Under normal conditions, almost all the oxygen in your blood is carried by red blood cells, and they are close to fully loaded already. Inside a hyperbaric chamber, the increased pressure dissolves extra oxygen directly into the plasma, the liquid part of your blood. That dissolved oxygen reaches tissues that red blood cells struggle to supply properly, including injured tissue, areas of poor circulation and tissue under repair.</p>
<p>HBOT is an old, well-studied treatment. Hospitals have used it for decades for conditions such as non-healing wounds, decompression sickness in divers and tissue damage after radiotherapy. The wellness world has picked it up more recently for recovery, energy and healthy ageing, and the evidence for those newer uses is younger than the evidence for the hospital indications. We are upfront about that difference, and your doctor tells you at the consultation where your goal sits on that spectrum.</p>
<p>What HBOT is not is an oxygen bar or a quick spa add-on. Pressure, oxygen concentration, session length and the number of sessions all change what the treatment does, which is why the protocol at Brockwell Healthcare is set by a doctor, not picked off a menu.</p>

<h2>How HBOT works</h2>
<p>You sit or lie in the chamber while the pressure rises, similar to the pressure change you feel on a descending flight. Once at treatment pressure, you breathe normally for the rest of the session. Sessions typically run sixty to ninety minutes, and most people read, listen to something or sleep through them.</p>
<p>The extra oxygen does a few things that matter for healing. It supports the energy production cells need for repair, it stimulates the growth of new small blood vessels in tissue with poor supply, and it has effects on inflammation and on the stem cell activity involved in tissue regeneration. These effects accumulate over a course of sessions, which is why HBOT is almost always prescribed as a series instead of a single visit.</p>
<p>The most common side effect is ear pressure during the pressure change, the same as flying, and equalising your ears handles it for most people. Not everyone is a candidate. Certain lung conditions, recent ear surgery, some chemotherapy drugs and untreated pneumothorax rule the treatment out, and your doctor screens for all of these before your first session.</p>

<img src="/static/img/services/hyperbaric-oxygen-therapy-content.webp" alt="Doctor-led hyperbaric oxygen therapy (HBOT) chamber session at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>What we use HBOT for</h2>
<h3>Recovery and tissue healing</h3>
<p>This is the closest to HBOT's traditional medical territory. Patients recovering from surgery, injury or stubborn wounds use HBOT to support the healing process, because repairing tissue consumes far more oxygen than resting tissue does. Your doctor reviews the injury or wound first, coordinates with your surgeon or treating doctor where there is one, and sets a protocol matched to the stage of healing you are at.</p>
<h3>Sports recovery and physical performance</h3>
<p>Athletes and serious gym-goers use HBOT between training blocks and after competition to support recovery from muscle damage and soft-tissue strain. The research here is promising in places and mixed in others, and we say so. What we can do is assess your training load, recovery quality and any nagging injuries, and set a protocol with a defined goal so you can judge whether it is earning its place in your routine.</p>
<h3>Energy and persistent fatigue</h3>
<p>Some patients try HBOT for fatigue that has not responded to anything else. Before anyone books a course for this, we test. Fatigue usually has a measurable cause, and our functional medicine work covers thyroid, iron, vitamin D, blood sugar and cortisol rhythm. It makes no sense to sit in a chamber for ten sessions when the actual problem is a ferritin level of 12. Where the work-up comes back clean, or where an identified problem is already being treated, HBOT can be added as a supportive layer.</p>
<h3>Longevity and healthy ageing</h3>
<p>HBOT has attracted attention in longevity circles, partly from research suggesting effects on cellular ageing markers after intensive protocols. That research is genuinely interesting and still early, and the intensive protocols used in the studies involve dozens of sessions. If longevity is your goal, HBOT here sits inside a wider longevity medicine plan alongside hormonal, metabolic and lifestyle work, because no single therapy carries healthy ageing on its own.</p>
<h3>Skin and aesthetic support</h3>
<p>Better tissue oxygenation supports collagen production and skin repair, which is why HBOT is sometimes paired with aesthetic and regenerative skin treatments, including after procedures. Where it is relevant to a treatment plan, your doctor explains what it adds and when in the sequence it belongs.</p>

<h2>How HBOT fits with our other services</h2>
<p>Most of the goals people bring to HBOT overlap with things we already test and treat. Fatigue overlaps with functional medicine. Performance and drive overlap with male wellness and hormonal health. Healthy ageing overlaps with the longevity programme, and tissue repair overlaps with our regenerative treatments such as PRP and peptide therapy. Because all of this runs under one roof, your doctor can combine HBOT with the right supporting work instead of selling it as a standalone fix, and can also tell you when the supporting work alone would get you there.</p>

<h2>What to expect from a course</h2>
<p>The number of sessions depends entirely on the goal. Recovery support after a procedure might need a short series, while the intensive protocols used in longevity research run much longer. Your doctor sets the number at your assessment, explains the reasoning, and reviews progress partway through instead of waiting until the end.</p>
<p>Effects build across the course. Some patients notice better sleep or energy within the first few sessions, while tissue healing benefits work on the timescale that healing itself does. Your doctor tells you before you start what a realistic outcome looks like for your goal, and if we do not think HBOT is the right tool for it, we will tell you that instead.</p>

<h2>The treatment process</h2>
<p>It starts with booking, where you contact Brockwell Healthcare to arrange your HBOT consultation, and you see the doctor before you see the chamber. At the assessment, your doctor reviews your goal, medical history, medications and the contraindication list, and where blood work would explain part of the picture, especially for fatigue or longevity goals, it is offered at this stage. If HBOT is suitable, your doctor sets the protocol, meaning the pressure, session length and number of sessions for your goal, and confirms the full cost before you start. The sessions themselves run sixty to ninety minutes each, during which you wear comfortable cotton clothing, leave phones and electronics outside, and equalise your ears as the pressure changes, and after that the time is yours. Finally, your response is reviewed during the course and the protocol is adjusted if it needs to be.</p>

<h2>Why patients choose Brockwell Healthcare for HBOT</h2>
<p>Chambers are easy to buy, and plenty of places in Dubai have one. The difference is what happens around the chamber. At Brockwell Healthcare a qualified doctor screens every patient against the contraindication list, protocols are set for a defined clinical goal, and blood work is available when the symptoms suggest the real problem lies elsewhere. We are honest about where the evidence for HBOT is established and where it is still emerging, we coordinate with your existing doctors when you have them, and full pricing is confirmed before your first session.</p>

<h2>Book a hyperbaric oxygen therapy consultation in Dubai</h2>
<p>Book a hyperbaric oxygen therapy consultation in Dubai at Brockwell Healthcare. Your doctor will assess whether HBOT suits your goal, set the right protocol if it does, and confirm the cost before anything begins.</p>
"""

FAQS = [
    ("What does an HBOT session feel like?",
     "Mostly uneventful, which surprises people. You feel pressure in your ears as the chamber pressurises, the same as a descending flight, and equalising handles it. After that you sit or lie comfortably for sixty to ninety minutes and breathe normally, and many patients sleep."),
    ("How many sessions do I need?",
     "It depends on the goal. A short series can support recovery after a procedure, while the protocols used in longevity research run to dozens of sessions. Your doctor sets the number at your assessment and explains why."),
    ("Is HBOT safe?",
     "It has a long safety record when patients are screened properly, and the screening is the point. Certain lung conditions, untreated pneumothorax, recent ear surgery and some chemotherapy drugs rule it out, which is why every course here starts with a doctor's assessment."),
    ("Will HBOT give me more energy?",
     "Sometimes, and it depends on why your energy is low. Fatigue usually has a measurable cause, so we test before we treat. If blood work finds low iron or a thyroid problem, fixing that will do more than any chamber. Where the work-up is clean, HBOT can be a reasonable supportive option."),
    ("Is HBOT good for anti-ageing?",
     "The longevity research on HBOT is interesting and still early, and the studies used long, intensive protocols. We offer it as part of a wider longevity plan instead of a standalone anti-ageing treatment, and your doctor gives you an honest read on what to expect."),
    ("Can I use my phone in the chamber?",
     "No. Electronics stay outside for safety reasons. You can read, rest or sleep, and the session tends to pass faster than people expect."),
    ("Can HBOT be combined with other treatments?",
     "Yes, and it often is. It pairs with recovery from procedures, with regenerative treatments such as PRP, and with functional medicine or longevity plans. Your doctor sequences everything so the treatments support each other."),
    ("Who should not have HBOT?",
     "Anyone with untreated pneumothorax, and people with certain lung conditions, recent ear surgery or specific medications need careful review first. Your doctor goes through the full screening list at your assessment."),
    ("What does HBOT cost in Dubai?",
     "It depends on the protocol and the number of sessions. You get the full cost at your assessment, before any session is booked, and nothing is added without your agreement."),
    ("Do I need a referral?",
     "No. Contact the clinic directly and the team will book your assessment. If another doctor is already treating you for the condition involved, bring their notes or reports, because your doctor here will want to coordinate with them."),
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
        ("services", "0110_exomind_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
