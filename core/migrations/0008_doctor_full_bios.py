"""Full approved doctor titles + bios for the home "Our Doctors" section
(and the individual profile pages, kept in sync)."""

from django.db import migrations


# slug -> (title, bio)
DOCTORS = {
    "dr-hasnain-haider-shah": (
        "Founder & Lead Specialist | Neurointerventional Surgery & Regenerative Medicine",
        "Dr. Hasnain Haider-Shah founded Brockwell Healthcare and leads its clinical vision. "
        "American Board-trained and DHA-licensed, he holds a dual specialisation in "
        "neurointerventional surgery and regenerative medicine. His experience spans "
        "neurointervention, interventional oncology and pain management, which he combines with "
        "biologic and functional therapies. He focuses on restoring function, improving "
        "performance and achieving lasting results without unnecessary surgery. Patients value "
        "his clear, evidence-led thinking, and every protocol he designs is proactive, "
        "personalised and built around long-term health."),
    "dr-nigel-beejay": (
        "Consultant Physician, Gastroenterologist & Digital Health Expert",
        "With more than twenty years of global clinical experience, Dr. Nigel Beejay specialises "
        "in advanced gastrointestinal care, diagnostic endoscopy and digital health. His "
        "expertise covers colon cancer screening, chronic digestive disorders, liver disease "
        "management and clinical informatics. Known for pairing clinical excellence with "
        "innovation, he has led large-scale healthcare improvements and digital transformation "
        "programmes across the UK and UAE. At Brockwell, he brings a precise, systems-driven "
        "approach to gut health and complex internal medicine."),
    "dr-adeel-khan-md": (
        "Regenerative Medicine & Longevity Physician",
        "A pioneer in advanced biologics, Dr. Adeel Khan focuses on stem cell therapies, Muse "
        "cell innovation and human performance optimisation. His work centres on slowing "
        "biological ageing, treating complex chronic pain and helping patients avoid surgery "
        "through modern regenerative solutions. He works at the forefront of longevity science, "
        "always with a firm emphasis on measurable, real-world outcomes. For Brockwell patients, "
        "he designs regenerative plans focused on recovery, resilience and healthier, more "
        "active ageing."),
    "dr-sabine-hazan-md": (
        "Gastroenterology & Microbiome Specialist",
        "Dr. Sabine Hazan is a recognised leader in microbiome research and clinical trials. She "
        "specialises in gut health, digestive disorders and advanced therapeutic approaches that "
        "link the microbiome to overall wellbeing. Her work bridges everyday clinical medicine "
        "with research-driven innovation, studying how the balance of gut bacteria shapes both "
        "health and disease. She guides diagnostics and treatment for Brockwell patients whose "
        "recovery and long-term wellbeing depend on restoring a healthy, balanced internal "
        "environment."),
    "dr-salman-gilani": (
        "Regenerative Medicine Specialist",
        "Dr. Salman Gilani is an expert in stem cell therapy, precision diagnostics and "
        "technology-integrated care. As a specialist in next-generation regenerative medicine, "
        "he favours treatments that are scientifically grounded and closely tailored to each "
        "patient. His approach helps move care from reactive to proactive, improving both "
        "clinical outcomes and the overall patient experience. Within the Brockwell team, he "
        "supports patients facing pain, injury and age-related decline through carefully "
        "planned, closely monitored regenerative treatment."),
    "shirley-dsouza": (
        "Functional Nutritionist & Precision Health Coach",
        "Shirley D'Souza brings deep expertise in metabolic health, gut health and personalised "
        "nutrition. She works on root-cause healing through targeted lifestyle and nutritional "
        "strategies, integrating peptides, supplementation and functional nutrition into every "
        "plan. Her focus is long-term health, hormonal balance and sustainable weight management "
        "for patients who want lasting change. Her role at Brockwell is to turn complex health "
        "goals into practical, personalised nutrition and lifestyle programmes that patients can "
        "actually understand and follow."),
    "shahnawaz-hussein-khan-phd": (
        "Regenerative & Nutritional Science Expert",
        "Dr. Shahnawaz Hussein Khan specialises in systems-based therapeutic frameworks and the "
        "science of how the body heals. His work examines how a person's biological environment "
        "influences repair and regeneration, drawing together precision diagnostics, nutritional "
        "science and regenerative therapies. From this, he builds structured, individualised "
        "protocols for patients with complex, long-standing conditions. His research-led "
        "perspective strengthens how each Brockwell treatment plan is designed, sequenced and "
        "measured over time, so nothing is left to guesswork."),
    "dr-nameer-haider": (
        "Pain Medicine & Interventional Specialist",
        "With over twenty-five years of experience, Dr. Nameer Haider is a leader in minimally "
        "invasive pain management, neuromodulation and advanced spinal treatments. He has "
        "developed innovative procedures for difficult chronic pain conditions and continues to "
        "work at the forefront of interventional pain medicine and medical technology. For "
        "Brockwell patients, he helps reduce pain, restore movement and rebuild daily function "
        "through precise, image-guided techniques, offering a safe and considered alternative to "
        "open, invasive surgery."),
    "prof-dato-sri-dr-mike-chan": (
        "Global Leader in Biotechnology & Regenerative Medicine",
        "Prof. Dato' Sri Dr. Mike Chan is a global authority in biotechnology and regenerative "
        "medicine, with more than four decades of experience. A pioneer in stem cell research "
        "and peptide therapeutics, he has founded several research institutions, authored "
        "numerous scientific publications and helped advance regenerative medicine worldwide. "
        "His work continues to shape modern biologic therapy. His scientific leadership informs "
        "Brockwell's most advanced regenerative and longevity protocols, keeping the clinic "
        "aligned with the latest evidence."),
    "dr-rozina-badal-munir": (
        "Ultrasound Diagnostics Specialist | Global Development Director, ABRM",
        "Dr. Rozina Badal Munir serves as Global Development Director for the American Board of "
        "Regenerative Medicine. She is an ultrasound diagnostics specialist certified across "
        "musculoskeletal ultrasound, echocardiography, vascular interpretation and emergency "
        "point-of-care imaging. She leads regenerative medicine education across more than "
        "twenty-five countries, with a strong focus on diagnostic precision and procedural "
        "reproducibility. Her imaging expertise ensures Brockwell treatments are accurately "
        "guided, safely placed and reliably repeatable for every patient, on every visit."),
    "dr-summer-beattie": (
        "Photobiomodulation Specialist | Regenerative & Neuro-Restoration Medicine",
        "Dr. Summer Beattie is a naturopathic doctor and clinical instructor in regenerative and "
        "neuro-restoration medicine, with deep specialisation in photobiomodulation. Her "
        "clinical work spans intravenous laser therapy, Weber Endolaser platforms, cranial "
        "photobiomodulation and Class IV therapeutic laser systems, integrated into wider "
        "regenerative protocols. She brings light-based therapy into personalised Brockwell "
        "treatment plans, supporting recovery, cellular health and neurological function for "
        "patients dealing with a wide range of complex conditions and individual recovery goals."),
    "rachel-tan-garcia": (
        "Adult-Gerontology Acute Care Nurse Practitioner",
        "Rachel Tan Garcia is an Adult-Gerontology Acute Care Nurse Practitioner with ICU "
        "leadership experience across the Middle East and internationally. Her practice focuses "
        "on IV infusion therapy, peptide-based recovery protocols and clinical workflow design "
        "for regenerative and longevity medicine. She combines critical-care precision with a "
        "genuinely patient-centred approach to recovery. At Brockwell, she oversees safe, "
        "well-structured infusion and recovery care, making sure every protocol runs smoothly "
        "from initial preparation through to careful follow-up."),
    "dr-don-buford": (
        "Orthopedic Surgeon & Regenerative Medicine Specialist",
        "Dr. Don Buford provides concierge care for joint pain, sports injuries and back pain, "
        "combining evidence-based orthopedic surgery with regenerative medicine. Across "
        "twenty-six years, he has performed thousands of shoulder and knee arthroscopic "
        "procedures alongside orthobiologic treatments using PRP and bone marrow concentrate. "
        "His protocols rest on proven clinical evidence rather than passing trends. He helps "
        "active Brockwell patients recover from injury and joint pain, while avoiding surgery "
        "wherever it is realistic to do so."),
    "jean-francois-tremblay": (
        "Founder, Canlab | Diagnostics & Laboratory Innovation",
        "Jean-Francois Tremblay brings specialist expertise in clinical systems, laboratory "
        "innovation and healthcare infrastructure. As founder of Canlab, his work supports "
        "advanced diagnostics and precision-medicine frameworks, helping bridge the gap between "
        "research, testing and real-world patient care. His focus is building the reliable "
        "diagnostic backbone that modern regenerative medicine depends on. That expertise "
        "underpins accurate testing, sound diagnosis and evidence-based treatment planning "
        "across every stage of care at Brockwell, from first test to final follow-up."),
}


def load(apps, schema_editor):
    Doctor = apps.get_model("team", "Doctor")
    for slug, (title, bio) in DOCTORS.items():
        Doctor.objects.filter(region="uae", slug=slug).update(
            title=title, short_bio=bio, full_bio=f"<p>{bio}</p>",
        )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_homepage_content_revisions"),
        ("team", "0003_seed_real_doctors"),
    ]

    operations = [migrations.RunPython(load, migrations.RunPython.noop)]
