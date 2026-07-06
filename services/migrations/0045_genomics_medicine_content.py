"""Load the full Genomics Medicine content into the existing sub-service:
keyword-rich H1 (full, with tagline), SEO meta, styled rich-text sections
('Covers' → card grid, process → numbered timeline via the enhance pipeline)
and the FAQ set. Photos are added later."""

from django.db import migrations

SEO_TITLE = "Genomics Medicine in Dubai | DNA & Genetic Testing | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Book a genomics medicine consultation in Dubai at Brockwell Healthcare for genetic "
    "health assessment, disease risk screening, personalised treatment planning and "
    "longevity support. Doctor-led genomic testing with clinical interpretation."
)
HERO_HEADING = "Genomics Medicine in Dubai | Doctor-Led DNA & Genetic Testing"
SLUG = "genomics-medicine"
SUMMARY = (
    "Doctor-led genomics medicine in Dubai for genetic health assessment, disease risk "
    "screening, personalised treatment planning and longevity support."
)

DESCRIPTION = """
<p>Doctor-led genomics at Brockwell Healthcare uses genetic information to inform clinical decisions with more precision than standard testing alone can achieve. It suits patients who want to understand their inherited health risks, how their body processes medications and nutrients, and how their genetic profile can shape a more personalised approach to treatment, prevention and longevity planning.</p>

<h2>What Is Genomics Medicine?</h2>
<p>Genomics medicine is a clinical approach that uses information from a patient's DNA to inform health decisions. Clinical DNA health testing provides information that can help personalise prevention, treatment planning and long-term health management. A standard blood test reflects how the body is functioning at a particular moment. A genetic assessment reflects how the body is built, which predispositions it carries and how it is likely to respond to specific treatments, nutrients or lifestyle changes over time.</p>
<p>At Brockwell Healthcare, we use genomic testing in Dubai as a clinical tool, not a consumer or ancestry service. It builds a more precise, personalised understanding of a patient's health. Every genomic assessment begins with a proper clinical consultation that determines which genetic panels are relevant to your specific symptoms, history and goals. A doctor then reviews the results and translates the findings into actionable clinical guidance, so you are never left to interpret raw data on your own.</p>

<h2>How Does Genomics Medicine Work?</h2>
<p>Genomic testing analyses specific regions of a patient's DNA to identify variants, known as single-nucleotide polymorphisms or SNPs, that may be associated with health risks, physiological traits or treatment responses. Most clinical genomic panels do not sequence the whole genome. Instead, they examine targeted regions clinically relevant to the specific questions being asked, whether that is cardiovascular risk, metabolic function, hormonal processing, drug sensitivity, inflammation regulation or nutrient metabolism.</p>
<p>Your clinician collects a sample, usually through a simple saliva swab or blood draw. A certified genomics laboratory then processes it and returns a report showing which variants you carry. At Brockwell Healthcare, your doctor reviews these findings in the context of your full clinical picture, your symptoms, family history, lifestyle and current health, before making any recommendations. A genetic variant is not a diagnosis. It is one piece of information, most useful when interpreted alongside everything else known about a patient. This is how genomics supports personalised medicine, by combining genetic findings with your clinical history, lifestyle and current health.</p>

<h2>What Genomics Medicine Covers</h2>
<p>The specific genetic panels used depend on your symptoms, clinical history and goals. Brockwell Healthcare selects the most clinically relevant testing for your situation.</p>
<h3>Cardiovascular and Metabolic Risk</h3>
<p>Genetic variants associated with cardiovascular disease risk, lipid metabolism, blood-pressure regulation and metabolic function. This may be relevant for patients with a family history of heart disease, high cholesterol or metabolic conditions, or those who want a fuller picture of their long-term cardiovascular risk alongside standard blood testing.</p>
<h3>Cancer Risk Screening</h3>
<p>Selected genetic panels that identify variants associated with elevated risk for certain hereditary cancers, including breast, ovarian, colorectal and prostate cancer. Your doctor discusses this carefully during the consultation. A positive finding does not mean cancer will develop. It means risk is elevated, and more frequent surveillance or preventive strategies may be appropriate.</p>
<h3>Pharmacogenomics</h3>
<p>An assessment of how your genetic profile affects your response to specific medications, including antidepressants, pain medications, anticoagulants, statins and other commonly prescribed drugs. This may help you avoid medications likely to be ineffective or to carry an elevated side-effect risk for your genetic profile.</p>
<h3>Nutrigenomics</h3>
<p>An assessment of genetic variants affecting how your body processes and responds to specific nutrients, including folate, Vitamin D, omega-3 fatty acids, caffeine and others. Nutrigenomic findings can inform more targeted nutritional guidance suited to your individual profile.</p>
<h3>Hormonal and Endocrine Genetics</h3>
<p>Variants affecting oestrogen metabolism, testosterone processing, cortisol regulation and thyroid function may be relevant to patients with hormonal symptoms that standard blood panels have not fully explained.</p>
<h3>Inflammatory Regulation</h3>
<p>Genetic variants affecting inflammatory pathways may help explain why some patients carry elevated chronic inflammation despite a reasonable lifestyle. This can inform targeted anti-inflammatory approaches within a wider regenerative or longevity plan.</p>
<h3>Longevity and Healthspan Genetics</h3>
<p>Selected panels relevant to biological ageing, including mitochondrial function, DNA-repair capacity, telomere-related variants and other longevity-associated markers. Longevity genetics and biological age genetics add useful information when interpreted alongside lifestyle, biomarkers and other longevity assessments. It is only one component of a broader longevity medicine strategy, and your doctor always interprets it alongside clinical findings.</p>

<h2>Benefits of Doctor-Led Genomics Medicine</h2>
<p>Genomics medicine may offer several potential benefits when findings are properly interpreted and applied within a clinical plan. Results vary with which variants are identified and how they interact with lifestyle, environment and other health factors.</p>
<p>Possible benefits include:</p>
<ul>
<li>Genetically elevated disease risks identified before symptoms develop, allowing earlier, more targeted prevention</li>
<li>Treatment decisions matched more closely to how your body is built</li>
<li>Medication selection better informed by pharmacogenomic findings, reducing trial-and-error prescribing</li>
<li>More targeted nutritional guidance where nutrigenomic findings apply</li>
<li>Better understanding of hormonal symptoms that standard testing has not explained</li>
<li>A genetic baseline to help track and interpret health changes within a longevity or healthspan plan</li>
<li>More personalised, evidence-informed decisions across treatment, prevention and lifestyle</li>
</ul>
<p>Results are not guaranteed to predict outcomes. A genetic variant indicates a tendency or a risk, not a certainty. A thorough clinical discussion at Brockwell Healthcare makes sure genomic findings are interpreted appropriately and never overstated.</p>

<h2>The Genomics Medicine Process at Brockwell Healthcare</h2>
<p>Every genomics medicine assessment at Brockwell Healthcare follows a structured clinical process, and your doctor recommends testing only when a proper consultation confirms it is likely to provide clinically useful information.</p>
<h3>Step 1: Booking</h3>
<p>Get in touch with Brockwell Healthcare to arrange your genomics medicine Dubai consultation. The team helps you choose the right appointment for your main concern, whether that is disease risk, medication sensitivity, nutritional genetics, hormonal assessment or longevity planning.</p>
<h3>Step 2: Pre-Test Clinical Consultation</h3>
<p>Your genetic health assessment begins with a detailed review of your medical history, symptoms and family history before your doctor selects the appropriate testing panels. This step, a form of pre-test counselling, determines which genetic panels are likely to provide clinically useful information for your situation. Your doctor discusses the potential implications of possible findings before any testing begins, including how a positive finding would be interpreted and what the clinical response would be.</p>
<h3>Step 3: Sample Collection</h3>
<p>Your clinician collects a saliva swab or blood sample, depending on the panel. Collection is straightforward and usually takes only a few minutes, and the team sends the sample to a certified genomics laboratory for analysis.</p>
<h3>Step 4: Laboratory Analysis</h3>
<p>The laboratory processes and analyses the sample for the specific genetic variants in the selected panels. Turnaround time varies with the panels and laboratory involved, and your doctor advises on the expected timeline when your testing is arranged.</p>
<h3>Step 5: Results Review and Clinical Interpretation</h3>
<p>Once results are available, your doctor reviews them with you in full, explaining each finding in plain language and in the context of your full clinical picture. A variant is not a verdict. Your doctor explains what each finding means, how significant it is alongside your other health information, and what, if anything, it suggests for clinical action.</p>
<h3>Step 6: Clinical Plan</h3>
<p>From the genomic findings and the broader clinical picture, your doctor recommends the most appropriate next steps. That may include targeted treatment, preventive strategies, surveillance, nutritional adjustments, medication review, specialist referral, or integrating the findings into an ongoing longevity or healthspan plan. Your doctor confirms the cost before anything begins.</p>

<h2>Why Choose Brockwell Healthcare for Genomics Medicine</h2>
<ul>
<li>A DHA-licensed doctor leads every assessment and interprets findings in clinical context.</li>
<li>Panel selection follows your specific clinical history and goals.</li>
<li>Your doctor explains results in plain language, with an honest account of what they do and do not mean.</li>
<li>Genomic findings feed into a wider clinical plan, never delivered as standalone data.</li>
<li>The potential implications of any findings are discussed before testing, so you decide with full information.</li>
<li>Upfront pricing is confirmed before any testing begins, with no surprises.</li>
</ul>
"""

FAQS = [
    ("Can genomic testing diagnose conditions?",
     "No. Genetic variants indicate a tendency or elevated risk, not a certainty or a diagnosis. Genomic testing in Dubai at Brockwell Healthcare provides information that can inform clinical decisions, but it does not replace clinical assessment, imaging or standard diagnostic testing."),
    ("What is pharmacogenomics?",
     "Pharmacogenomics assesses how a patient's genetic profile affects their response to specific medications. It may help identify medications less likely to work, or more likely to cause side effects, for a particular patient, which supports more precise prescribing."),
    ("What is nutrigenomics?",
     "Nutrigenomics assesses genetic variants affecting how the body processes and responds to specific nutrients. Findings can inform more targeted nutritional guidance based on your individual genetic profile."),
    ("Can genomics medicine help with hormonal symptoms?",
     "Genetic variants affecting oestrogen metabolism, testosterone processing, cortisol regulation and thyroid function may help explain hormonal symptoms that standard blood panels have not fully accounted for. This is one component of a hormonal assessment, not a replacement for it."),
    ("Is cancer risk genetic testing available at Brockwell Healthcare?",
     "Selected panels identifying variants associated with elevated hereditary cancer risk are available and discussed during the pre-test consultation. A positive finding does not mean cancer will develop. It indicates elevated risk and informs decisions about surveillance frequency and preventive strategies."),
    ("How long does genomic testing take?",
     "Sample collection takes only a few minutes. Laboratory turnaround varies with the panels selected and typically ranges from one to three weeks. Your doctor advises on the expected timeline when your testing is arranged."),
    ("Is genomic testing safe?",
     "Yes. Genomic testing involves only a saliva swab or standard blood draw and carries no physical risk. The main consideration beforehand is making sure you understand the potential implications of possible findings and have had the chance to discuss them with a clinician before proceeding."),
    ("How are genomic findings integrated into a treatment plan?",
     "Your doctor reviews genomic findings in the context of your full clinical picture and translates them into actionable recommendations. These might include targeted treatment, preventive strategies, nutritional adjustments, medication review or integration into an ongoing longevity plan. Findings are never delivered as standalone data without clinical context."),
    ("Can genomics medicine support longevity planning?",
     "Yes. Selected genetic panels relevant to biological ageing, including mitochondrial function, DNA-repair capacity and inflammation regulation, may be used as one component within a longevity medicine or healthspan plan at Brockwell Healthcare. Genetic information is most useful when interpreted alongside clinical markers, lifestyle assessment and treatment response over time."),
    ("What is the cost of genomics medicine in Dubai?",
     "The cost depends on the specific panels selected and the scope of the assessment. Brockwell Healthcare provides clear pricing and a full cost estimate before any testing begins."),
    ("Do I need a consultation before genomic testing in Dubai?",
     "Yes. A pre-test clinical consultation is required before any genomic testing in Dubai at Brockwell Healthcare. It confirms which panels are relevant, prepares you for the potential implications of possible findings and makes sure results are interpreted in proper clinical context, so nothing begins without it."),
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
        ("services", "0044_peptide_therapy_content"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
