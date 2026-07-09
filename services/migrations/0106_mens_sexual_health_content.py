"""Rename the Sexual Health service to Men's Sexual Health and load the user's
doctor-led, root-cause copy: reworked section set (What is / How treatment works /
Conditions we assess and treat [card grid] / Treatments we may use / What treatment
may offer [list] / How the consultation works / Why patients choose) and an 11-item
FAQ. Prose-led. Slug is kept as ``sexual-health`` so the URL does not change. Keeps
the hero and a single inline content image.
Hero: static/img/services/sexual-health-hero.webp;
inline: static/img/services/sexual-health-content.webp."""

from django.db import migrations

SLUG = "sexual-health"

NAME = "Men's Sexual Health"
SEO_TITLE = (
    "Men's Sexual Health in Dubai | Doctor-Led ED & Sexual Wellness | Brockwell Healthcare"
)
SEO_DESCRIPTION = (
    "Doctor-led men's sexual health in Dubai at Brockwell Healthcare for erectile "
    "dysfunction, low libido, testosterone concerns and premature ejaculation. Private, "
    "root-cause treatment."
)
HERO_HEADING = "Men's sexual health in Dubai"
SUMMARY = (
    "Doctor-led, private treatment for erectile dysfunction, low libido, testosterone "
    "concerns and premature ejaculation, built around a root-cause assessment."
)

DESCRIPTION = """
<p>Men's sexual health at Brockwell Healthcare is a doctor-led clinical service that assesses and treats the biological, hormonal and vascular contributors to sexual dysfunction and reduced sexual wellbeing. It suits men who want a proper clinical assessment of what is actually driving their concern, not a generic prescription or a conversation that feels rushed and uncomfortable.</p>

<h2>What is men's sexual health?</h2>
<p>Men's sexual health covers the physical, hormonal and vascular factors behind sexual function, desire and satisfaction. When any of these are compromised, whether through age, hormonal change, cardiovascular factors, neurological contributors, medication side effects or psychological stress, the result can be erectile dysfunction, reduced libido, premature ejaculation, changes in performance or a general dissatisfaction that affects confidence and relationships.</p>
<p>Sexual health is approached here with the same clinical rigour applied across the clinic. The aim is to identify the specific biological drivers of your concern and build a plan around them, instead of offering one solution without understanding the cause, and every assessment begins with a proper clinical review before any treatment is discussed.</p>

<h2>How treatment works</h2>
<p>Sexual function in men depends on a cascade of connected systems working together. Adequate testosterone supports desire and arousal. Healthy vascular function supports blood flow to erectile tissue. Neurological integrity supports sensation and response. Hormonal balance affects energy, mood and drive. When any part of that cascade is disrupted, the effect on sexual function can be significant, and it often involves more than one contributing factor at once.</p>
<p>Doctor-led assessment begins by working out which of these systems matter most for your specific concern. That involves a detailed clinical history, relevant blood work covering testosterone and associated hormonal markers, a cardiovascular risk assessment, and imaging to assess vascular function where relevant. Treatment is then matched to what the assessment actually shows, instead of a standard approach applied to every man.</p>

<img src="/static/img/services/sexual-health-content.webp" alt="Private, doctor-led men's sexual health consultation at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>Conditions we assess and treat</h2>
<p>The assessment and treatments included depend on the concern and what the clinical review finds. The presentations below are the most frequent reasons men book a consultation.</p>
<h3>Erectile dysfunction</h3>
<p>Erectile dysfunction is one of the most common and under-reported men's health concerns, and it may reflect vascular, hormonal, neurological or psychological contributors, often more than one together. Assessment identifies the specific drivers before any treatment is discussed, and options depend on the cause, ranging from medication and hormonal support to regenerative approaches and lifestyle guidance.</p>
<h3>Low testosterone and androgen deficiency</h3>
<p>Testosterone falls naturally with age, but it can also drop through stress, poor sleep, metabolic dysfunction and obesity, affecting energy, libido, mood, body composition, muscle strength, sleep and sexual performance. A proper assessment covers symptoms, blood markers including total and free testosterone, LH, FSH and other hormones, and the contributing factors, and low testosterone treatment is only discussed once symptoms, examination and blood results have been reviewed together.</p>
<h3>Low libido and reduced drive</h3>
<p>Reduced interest in sex may reflect hormonal change, medication side effects, relationship stress, psychological contributors, poor sleep or a general decline in health. A clinical assessment identifies what is most likely contributing before any treatment is recommended.</p>
<h3>Premature ejaculation</h3>
<p>Premature ejaculation is common and rarely discussed openly, and it may involve neurological sensitivity, psychological contributors or a combination. Assessment identifies the likely mechanism before treatment options are discussed.</p>
<h3>Sexual performance concerns</h3>
<p>General concerns about sexual confidence, stamina or performance that are affecting quality of life or relationships are assessed in a private, non-judgemental setting, with the specific biological contributors identified where relevant and options discussed honestly.</p>
<h3>Sexual function after prostate surgery</h3>
<p>Men dealing with changes to sexual function following prostate surgery may benefit from a structured assessment of vascular, neurological and hormonal factors, and a targeted plan to support recovery of function where possible.</p>

<h2>Treatments we may use</h2>
<p>The treatment chosen depends on the concern, the underlying drivers and what the assessment shows, and our doctors select the most appropriate approach after reviewing your case.</p>
<p>Where medication is clinically appropriate, your doctor can prescribe and monitor within a supervised framework, including PDE5 inhibitors once a cardiovascular assessment confirms they are safe, and hormonal support where blood markers and symptoms support it. Low-intensity shockwave therapy delivers acoustic energy to penile tissue to support neovascularisation, the formation of new blood vessels, and may be considered for selected men where a vascular component to erectile dysfunction has been identified, with suitability confirmed through clinical and vascular assessment. PRP delivers concentrated growth factors to targeted tissue to support vascular health and tissue function, and may form part of a wider plan where a doctor confirms it fits your assessment. Where hormonal support is appropriate, targeted treatment including peptide therapy for hormonal signalling may be discussed. Because cardiovascular health, sleep, body composition, alcohol intake, stress and activity all directly affect sexual function, a review of these is part of every assessment, with targeted guidance where relevant. And where psychological contributors such as performance anxiety, relationship stress or depression are significant, referral to appropriate psychological or counselling support is arranged alongside any clinical treatment.</p>

<h2>What treatment may offer</h2>
<p>When assessment and treatment are properly structured around your specific drivers, sexual health treatment may offer real benefits, though results depend on the underlying cause, the treatments involved and how you respond. Read the points below as what a well-built plan works towards.</p>
<ul>
<li>identifying the specific biological drivers of sexual dysfunction through proper assessment, instead of symptom-based management alone</li>
<li>improving erectile function when vascular, hormonal or neurological contributors are appropriately addressed</li>
<li>easing testosterone-related symptoms such as fatigue, low libido and mood changes when hormonal support is confirmed appropriate and properly monitored</li>
<li>reducing performance and confidence concerns as the underlying contributors are addressed</li>
<li>recovering libido when hormonal, sleep and lifestyle contributors are identified and managed</li>
<li>better sexual function over time as cardiovascular and metabolic health improve with lifestyle work</li>
<li>care delivered privately and without judgement in a professional clinical setting</li>
</ul>
<p>Results are not guaranteed and vary with the cause, duration and complexity of the concern. A thorough assessment is what determines what is realistic and appropriate before any treatment begins.</p>

<h2>How the consultation works</h2>
<p>Every plan follows a clear, private clinical process, and nothing is recommended until your doctor understands your concern and what is driving it.</p>
<p>It begins with booking, which is entirely private and confidential, where the team helps you choose the right appointment for your main concern. Then comes the clinical assessment, where your doctor takes a detailed history of your concern, its duration, severity and impact, your medical history, medications, lifestyle, sleep, stress and relationship context where relevant, arranges blood work covering testosterone and associated hormonal markers, metabolic and cardiovascular markers and other relevant tests, and carries out a physical examination where clinically appropriate. Based on that, your doctor builds a personalised plan around the specific drivers of your concern, which may be one approach or a combination, explaining what each involves, what realistic outcomes look like and what the cost will be before anything begins.</p>
<p>Treatment is then delivered in a clinical setting by a licensed doctor, following the protocol confirmed at your assessment, and may include medication, low-intensity shockwave therapy, PRP, hormonal support and lifestyle optimisation depending on the cause. Because this care often needs tracking over time, follow-up appointments review your response, adjust doses, revisit lifestyle changes and refine the plan where needed.</p>

<h2>Why patients choose Brockwell Healthcare for men's sexual health</h2>
<p>Several things shape this service. Every assessment is carried out by a licensed doctor in a fully private and confidential setting. The specific biological drivers of sexual dysfunction are identified through proper clinical assessment before any treatment is recommended. Treatment options are discussed honestly, including realistic expectations, limitations and the evidence behind each approach. Regenerative options such as shockwave therapy for erectile dysfunction and PRP are available where assessment confirms they fit, and hormonal assessment and support are integrated where relevant instead of treated in isolation. Where psychological or relationship factors are contributing, referral is arranged, and full pricing is confirmed before your first session, with no surprises.</p>

<h2>Book a men's sexual health consultation in Dubai</h2>
<p>Book a men's sexual health consultation in Dubai at Brockwell Healthcare for a root-cause approach. Our team will assess your concern thoroughly, identify what is driving it, explain your options honestly and confirm the cost before anything begins. Everything is handled in complete confidence.</p>
"""

FAQS = [
    ("What causes erectile dysfunction?",
     "It most often reflects vascular contributors affecting blood flow to erectile tissue, hormonal contributors including low testosterone, neurological factors, medication side effects or psychological contributors such as performance anxiety and stress. Most men have more than one factor at play, and a proper assessment identifies which are most relevant before treatment is discussed."),
    ("Can erectile dysfunction be treated without medication?",
     "Selected men with a confirmed vascular component may suit low-intensity shockwave therapy, which aims to support new blood vessel formation in the erectile tissue, and PRP may also be considered where clinically appropriate. Lifestyle changes such as exercise, better sleep, weight management and reducing alcohol can meaningfully improve function where metabolic and cardiovascular contributors are present."),
    ("Can low testosterone be treated at Brockwell Healthcare?",
     "Yes. Where blood markers and clinical assessment confirm hormonal support is appropriate, options including hormonal optimisation and peptide therapy for hormonal signalling are discussed. Testosterone treatment is always considered in the context of your full health profile, instead of prescribed on symptoms alone."),
    ("Is low libido always linked to testosterone?",
     "No. Low testosterone is a common contributor, but poor sleep, high stress, depression, relationship difficulties, medication side effects and a general decline in health can all reduce sexual drive independently of testosterone. A proper assessment identifies which factors are most relevant before any treatment."),
    ("Is shockwave therapy effective for erectile dysfunction?",
     "Low-intensity shockwave therapy may support vascular function in the erectile tissue of selected men where a vascular component has been identified. It does not suit every cause of erectile dysfunction, and suitability is confirmed through clinical and vascular assessment before it is recommended."),
    ("How is premature ejaculation assessed and treated?",
     "It is assessed through a detailed clinical history that identifies the likely mechanism, whether primarily neurological, psychological or a combination, and options are discussed based on the findings, which may include medical management, behavioural strategies or psychological support referral."),
    ("Is the consultation completely confidential?",
     "Yes. All consultations are conducted in a fully private and confidential setting, and your medical information is handled in line with applicable patient confidentiality standards and is not shared without your consent."),
    ("What blood tests are included?",
     "Blood work typically covers total and free testosterone, LH, FSH, SHBG, oestradiol, prolactin, thyroid function, metabolic markers and cardiovascular risk indicators, depending on your clinical picture. Your doctor selects the most relevant markers for your symptoms and history, instead of applying a fixed panel to everyone."),
    ("Can lifestyle changes improve sexual health?",
     "Yes. Cardiovascular fitness, sleep quality, body composition, alcohol intake and stress management all directly affect sexual function, so clinical guidance on these is part of every assessment, with targeted recommendations where relevant."),
    ("What does a consultation cost in Dubai?",
     "The cost depends on the assessment required, the investigations selected and any treatment recommended. We provide clear pricing and a full estimate before any investigation or treatment begins."),
    ("Do I need a referral first?",
     "No formal referral is needed. You can contact Brockwell Healthcare directly to book, and the team will help you choose the right appointment and advise on what to prepare before your visit."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if not svc:
        return

    svc.name = NAME
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
        ("services", "0105_unpublish_tpe"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
