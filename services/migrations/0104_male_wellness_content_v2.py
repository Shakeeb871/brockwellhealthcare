"""Refresh the Male Wellness service with the user's doctor-led, root-cause copy:
reworked section set (What is / How the assessment works / Conditions we assess and
treat [card grid] / Regenerative approaches / What it may offer [list] / How the
consultation works / Why patients choose) and an 11-item FAQ. Prose-led. Keeps the
hero and a single inline content image.
Hero: static/img/services/male-wellness-hero.webp;
inline: static/img/services/male-wellness-content.webp."""

from django.db import migrations

SLUG = "male-wellness"

SEO_TITLE = "Male Wellness in Dubai | Men's Health & Hormones | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Doctor-led male wellness in Dubai at Brockwell Healthcare for testosterone, sexual "
    "health, prostate, metabolic and energy concerns, with private, root-cause assessment "
    "and honest plans."
)
HERO_HEADING = "Male wellness in Dubai"
SUMMARY = (
    "Doctor-led men's health for testosterone, sexual health, prostate, metabolic and "
    "energy concerns, with private, root-cause assessment and honest plans."
)

DESCRIPTION = """
<p>Male wellness at Brockwell Healthcare is a doctor-led clinical service focused on the biological, hormonal and physical health concerns that affect men across adult life. It suits men who want a thorough, private and clinically grounded assessment, not a rushed appointment where concerns are managed superficially or brushed off.</p>

<h2>What is male wellness at Brockwell Healthcare?</h2>
<p>Male wellness here covers the full range of hormonal, sexual, metabolic, urological and general wellness concerns that affect men. It is not a single-symptom service. It is a clinical framework that looks at how these systems interact and addresses them together, instead of treating each one in isolation.</p>
<p>Many men put off seeking help for far longer than they should. Fatigue, low libido, mood changes, erectile difficulty, urinary symptoms and weight gain are often written off as stress or ageing and left alone, when they frequently reflect identifiable, treatable biological changes. A proper clinical assessment shows what is actually driving them, instead of leaving you to guess or cope alone. As with everything we do, male wellness is approached with a root-cause philosophy, and every assessment begins with a thorough clinical review before any investigation or treatment is discussed.</p>

<h2>How the assessment works</h2>
<p>An effective male wellness assessment starts with a detailed clinical history covering your current symptoms, how long they have been present, how they affect daily life, your relevant medical and family history, lifestyle, medications and goals.</p>
<p>From there, your doctor chooses the investigations most likely to give clinically useful information for your situation. That might include a hormonal panel covering testosterone, LH, FSH, oestrogen, SHBG and other markers, a metabolic and cardiovascular panel, inflammatory markers, thyroid function, and a prostate assessment including PSA where appropriate, along with other tests your history and symptoms point to. Results are then read in the context of your full clinical picture, not in isolation. A testosterone level sitting inside a reference range is not always clinically normal for a given individual, so your doctor interprets findings against your symptoms, age, lifestyle and overall health, instead of comparing your numbers to a population average and stopping there.</p>

<img src="/static/img/services/male-wellness-content.webp" alt="Doctor-led male wellness assessment and consultation at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>Conditions we assess and treat</h2>
<p>Each concern below needs individual clinical assessment before any treatment is recommended, and suitability depends on the diagnosis, severity, duration and your overall health.</p>
<h3>Testosterone and hormonal health</h3>
<p>Low testosterone affects energy, libido, mood, body composition, muscle mass, bone density and general wellbeing, and its symptoms are often gradual and mistaken for normal ageing. Assessment covers testosterone, LH, FSH, SHBG and other hormone markers, and any treatment options are explained clearly, with an honest discussion of benefits, risks and alternatives. Low testosterone treatment is only discussed once symptoms, examination findings and blood results have been reviewed together.</p>
<h3>Erectile dysfunction</h3>
<p>Erectile dysfunction is among the most under-reported men's health concerns despite being very common, and it may involve vascular, hormonal, neurological or psychological factors. Assessment identifies which of these are relevant before any treatment is recommended, and care may include hormonal optimisation, low-intensity shockwave therapy where a vascular cause is found, PRP in selected cases, and lifestyle guidance alongside clinical treatment.</p>
<h3>Prostate health</h3>
<p>Urinary symptoms such as frequency, urgency, weak flow, waking to pass urine and incomplete emptying are often linked to the prostate. A prostate assessment covers BPH management, evaluation for prostatitis and a discussion of prostate cancer risk, including PSA testing and ultrasound where appropriate. Men over 40 with any urinary symptoms, and men over 50 without symptoms, should discuss prostate assessment with a doctor.</p>
<h3>Metabolic health and weight</h3>
<p>Insulin resistance, raised cardiovascular risk markers, an abnormal lipid profile and weight that will not shift with reasonable diet and exercise are all common presentations. Assessment identifies the underlying metabolic contributors before a targeted plan is built.</p>
<h3>Energy and recovery</h3>
<p>Persistent fatigue that does not lift with rest may reflect hormonal decline, mitochondrial issues, nutritional deficiencies, disrupted sleep or inflammatory burden, well beyond simply being tired. A full assessment works out which of these are contributing before any treatment is recommended.</p>
<h3>Mood and mental health</h3>
<p>Low mood, irritability, anxiety, lost motivation and cognitive fogging are common in men and less often talked about. They may reflect hormonal, inflammatory, sleep or metabolic contributors that can be identified and addressed clinically. Where mental health support is the primary need, appropriate referral is arranged alongside clinical management.</p>
<h3>Sexual health</h3>
<p>Testing and referral for sexually transmitted infections, fertility-related concerns, ejaculatory dysfunction and general sexual health questions are all handled confidentially and without judgement during a consultation.</p>
<h3>Hair loss</h3>
<p>Male hair loss treatment begins by assessing the pattern, rate and likely cause of thinning before any therapy is recommended. Androgenetic alopecia in men is driven by genetic and hormonal factors, and options may include PRP scalp therapy, peptide therapy for hormonal support, or finasteride or minoxidil where clinically appropriate, sometimes in combination.</p>

<h2>Regenerative approaches in male wellness</h2>
<p>Where it is clinically appropriate, the clinic's wider regenerative medicine expertise is brought into male wellness. Peptide therapy may support hormonal signalling, energy regulation and recovery in men dealing with age-related hormonal decline, considered alongside a full hormonal assessment and only where the assessment confirms it fits. Low-intensity shockwave therapy may support vascular function in erectile tissue in selected men where a vascular component has been identified, though it does not suit every cause of erectile dysfunction and suitability is confirmed at review. PRP may be considered in selected applications, including sexual health support and scalp treatment for thinning hair, again only after a proper assessment. And men who want a proactive approach to their physical and mental performance as they age may benefit from a structured longevity or healthspan plan that pulls hormonal, metabolic and regenerative support into one coordinated framework.</p>

<h2>What doctor-led male wellness care may offer</h2>
<p>When assessment and treatment are properly structured around your specific clinical picture, this care may offer real benefits, though results depend on the condition, its severity and how you respond. Read the points below as what a well-built plan works towards.</p>
<ul>
<li>hormonal imbalances such as low testosterone identified and addressed, instead of written off as normal ageing without investigation</li>
<li>erectile dysfunction improving when the specific underlying cause is assessed and treated, instead of managed generically</li>
<li>energy, mood and physical performance improving as hormonal and metabolic contributors are addressed</li>
<li>prostate concerns caught early, when the range of management options is wider and outcomes are generally better</li>
<li>metabolic risk factors managed sooner, when they are found through proper assessment instead of late</li>
<li>sexual health and fertility concerns properly investigated, instead of left unmanaged</li>
<li>hair loss slowed when treatment starts before significant follicle loss has happened</li>
</ul>
<p>Results depend on the specific condition, its severity and individual response, and a clinical assessment is what determines what is realistic before any plan begins.</p>

<h2>How the consultation works</h2>
<p>Every consultation follows a clear clinical process, and nothing is recommended until your doctor has a thorough picture of your health, symptoms and goals.</p>
<p>It begins with booking, where the team helps you choose the right appointment for your main concern, whether that is hormonal health, sexual function, prostate assessment, energy, a metabolic review, hair loss or a general check. Then comes the history and examination, where your doctor takes a detailed history of your symptoms, their duration and impact, your medical and family history, medications, lifestyle and goals, with a focused physical examination where clinically appropriate. Based on that, your doctor selects the investigations most relevant to you, which may include a hormonal panel, metabolic and cardiovascular markers, inflammatory markers, PSA and prostate assessment, thyroid function, nutritional markers and other tests fitting your presentation.</p>
<p>Once results are in, your doctor reviews them with you in context, explaining each finding, what it means for your health and what the options are, and builds a plan around what your biology actually shows instead of a standard protocol, with the cost confirmed before anything begins. Because hormonal, metabolic and prostate concerns do better with continuity, follow-up appointments then track your response, repeat investigations where needed and adjust the plan as your health changes.</p>

<h2>Why patients choose Brockwell Healthcare for male wellness</h2>
<p>Several things shape our men's health care. Every consultation is carried out by a licensed doctor with clinical experience in hormonal, sexual and metabolic health in men. Investigations are chosen around your specific symptoms and history, not a fixed standard panel, and hormonal findings are read in the context of your full clinical picture instead of against a population reference range alone. Regenerative approaches, including shockwave, PRP and peptide therapy, are available where clinically appropriate. Sensitive concerns, from sexual health and erectile dysfunction to mental health, are handled privately and without judgement. Realistic outcomes are discussed honestly before any treatment starts, and full pricing is confirmed before your first session, with no surprises.</p>

<h2>Book a male wellness consultation in Dubai</h2>
<p>Book a male wellness consultation in Dubai at Brockwell Healthcare for a root-cause approach. Our team will review your symptoms and biology thoroughly, explain your options honestly and confirm the cost before anything begins.</p>
"""

FAQS = [
    ("What does a male wellness consultation involve?",
     "It involves a detailed clinical history, a focused physical examination where appropriate, and a carefully chosen panel of investigations based on your specific symptoms. Results are reviewed in context, and a treatment plan is built around what your biology actually shows instead of a standard protocol."),
    ("When should a man get a testosterone assessment?",
     "Any man with persistent fatigue, reduced libido, mood changes, erectile difficulty, muscle loss or body-composition changes not explained by lifestyle alone should discuss a testosterone assessment with a doctor. Assessing earlier gives more treatment options and a clearer baseline for tracking changes over time."),
    ("Can erectile dysfunction be treated without medication?",
     "Treatment here identifies the specific contributing factors before anything is recommended. Where vascular factors are found, low-intensity shockwave therapy may be considered, and where hormonal factors contribute, hormonal optimisation may be the better first step. Many cases do well by addressing the underlying cause instead of relying on medication alone."),
    ("When should a man get a prostate assessment?",
     "Men over 40 with any urinary symptoms, and men over 50 without symptoms, should discuss a prostate assessment with a doctor, and earlier if there is a family history of prostate cancer. It typically includes PSA testing, a clinical examination and ultrasound where indicated."),
    ("Can low testosterone be treated at Brockwell Healthcare?",
     "Yes. Assessment covers your symptoms, blood markers and overall clinical picture before any treatment is discussed, and the options are explained clearly with an honest account of benefits, risks and alternatives, including lifestyle approaches, peptide therapy and hormonal support where appropriate."),
    ("Can hair loss be treated through a male wellness consultation?",
     "Yes. A clinical assessment identifies the pattern, rate and likely cause of hair loss before treatment is discussed, and options may include PRP scalp therapy, peptide therapy, finasteride or minoxidil where clinically appropriate. Treatment tends to work better when started before significant follicle loss has occurred."),
    ("Is a male wellness consultation confidential?",
     "Yes. All consultations are conducted privately and confidentially, and sensitive concerns including sexual health, erectile function and mental health are handled without judgement in a discreet clinical setting."),
    ("Can male wellness care be integrated with a longevity plan?",
     "Yes. Men who want to maintain physical and mental performance as they age may benefit from a structured longevity or healthspan plan that brings hormonal, metabolic and regenerative support into one coordinated framework."),
    ("What does a male wellness consultation cost in Dubai?",
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
        ("services", "0103_category_order"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
