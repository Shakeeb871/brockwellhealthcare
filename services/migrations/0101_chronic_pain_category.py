"""Replace the 'Emsculpt for Pain' core-service category with 'Chronic Pain'.

The old Emsculpt-for-Pain category (id kept) is repurposed in place: renamed to
Chronic Pain, re-slugged to ``chronic-pain`` and given the user's doctor-led,
root-cause chronic pain copy. Rendered through the professional category layout
(``content_sections``): 'Conditions we treat' becomes a card grid, the benefits
list a list section, and the remaining prose sections alternate text + image.
Plus an 11-item FAQ. Section/hero images live under
static/img/services/categories/chronic-pain/ (placeholders until supplied)."""

from django.db import migrations

OLD_SLUG = "emsculpt-for-pain"
NEW_SLUG = "chronic-pain"

NAME = "Chronic Pain"
HERO_HEADING = "Chronic pain treatment in Dubai"
SEO_TITLE = (
    "Chronic Pain Treatment in Dubai | Doctor-Led Pain Management | Brockwell Healthcare"
)
SEO_DESCRIPTION = (
    "Doctor-led chronic pain treatment in Dubai at Brockwell Healthcare for persistent "
    "joint, nerve, back and tendon pain, fibromyalgia and complex pain, with a root-cause "
    "clinical plan."
)
SUMMARY = (
    "Doctor-led treatment for persistent joint, nerve, back and tendon pain, fibromyalgia "
    "and complex pain, built around a root-cause clinical plan."
)

DESCRIPTION = """
<p>Chronic pain management at Brockwell Healthcare is a doctor-led clinical service that sets out to find what is actually driving persistent pain and builds a structured plan around it. It suits people who have lived with pain for months or years without enough relief, and who want a more thorough, targeted approach than managing the symptom alone can offer.</p>

<h2>What is chronic pain?</h2>
<p>Chronic pain is pain that lasts beyond the expected healing period, generally defined as longer than three months. Acute pain is a direct signal of tissue damage, but chronic pain often involves changes in how the nervous system processes and amplifies pain signals, so it can carry on, and even intensify, after the original injury has healed or gone quiet.</p>
<p>It is not a single condition. It is a presentation that can come from many underlying causes, including ongoing tissue damage or inflammation, nerve sensitisation, central sensitisation where the nervous system itself becomes the driver of amplified pain, hormonal and metabolic contributors, psychological stress and disrupted sleep. Effective management depends on working out which of these matter most for you as an individual, instead of applying one protocol to everyone. At Brockwell Healthcare, chronic pain is treated as a root-cause clinical problem, not a symptom to be suppressed, and every plan begins with a thorough assessment before any treatment is recommended.</p>

<h2>How chronic pain management works</h2>
<p>Chronic pain is rarely driven by one thing. Most people with long-term pain have a mix of structural contributors, inflammatory processes, nerve sensitisation, lifestyle factors and psychological components, all interacting. Treating only one of these in isolation is why many standard approaches bring temporary relief without lasting change.</p>
<p>Doctor-led management here begins by mapping the contributors to your specific pain. That means reviewing the structural and diagnostic findings, the inflammatory and hormonal picture from blood work, the nervous system's role in amplifying pain, the effect of sleep and stress on how pain is felt, and the movement and lifestyle patterns that keep the cycle going. Treatment is then built around what the assessment actually shows, which might be regenerative approaches for structural tissue damage, nerve-focused treatments to reduce sensitisation, systemic anti-inflammatory support, sleep and stress work, movement rehabilitation, or several of these combined in one coordinated plan.</p>

<h2>Conditions we treat</h2>
<p>The treatments included in a plan depend on the drivers found during assessment. The presentations below are the ones seen most often.</p>
<h3>Chronic joint and musculoskeletal pain</h3>
<p>Persistent pain in the knees, hips, shoulders, back, elbows and ankles, where structural change, inflammation and surrounding muscle weakness are all contributing. Depending on how much structural involvement there is, a plan may combine regenerative therapies, rehabilitation and anti-inflammatory support.</p>
<h3>Chronic back and spinal pain</h3>
<p>Lower back pain, neck pain, disc-related pain and facet joint pain that have been present for months or longer. Assessment pins down the specific structural and non-structural contributors before anything is planned, and treatment may include regenerative injections, rehabilitation, nerve-focused therapies and systemic support.</p>
<h3>Nerve pain and neuropathic conditions</h3>
<p>Nerve entrapment, peripheral neuropathy and radiculopathy, where the nerve itself is generating or amplifying pain. Ultrasound-guided hydrodissection and other targeted approaches may be considered alongside systemic nerve support.</p>
<h3>Fibromyalgia and widespread pain</h3>
<p>Fibromyalgia brings widespread musculoskeletal pain, fatigue, disrupted sleep and cognitive symptoms. Management focuses on the central sensitisation component, on improving sleep and recovery, on reducing inflammatory burden and on supporting overall function, instead of chasing individual pain sites one by one.</p>
<h3>Chronic tendon and soft-tissue pain</h3>
<p>Persistent tendon pain, including Achilles, rotator cuff and patellar tendinopathy and tennis elbow, that has not settled with rest or physiotherapy. Regenerative options such as PRP and shockwave therapy may form part of a wider tendon rehabilitation plan.</p>
<h3>Post-injury and post-surgical pain</h3>
<p>Pain that outlasts the expected healing period after an injury or an operation. Scar tissue, nerve sensitisation, movement compensations or unresolved inflammation may all be involved, and assessment identifies what is keeping the pain going before any treatment is recommended.</p>
<h3>Complex regional pain and central sensitisation</h3>
<p>Where central sensitisation has become a major driver, management addresses the nervous system component alongside any structural contributors. This calls for a carefully paced, comprehensive approach, and deliberately avoids aggressive structural intervention.</p>

<h2>Treatments we may use</h2>
<p>The treatment chosen depends on the type of pain, the structures involved and what the assessment shows. Our doctors select the most appropriate approach, or combination, after reviewing your case in full.</p>
<p>Regenerative injection therapy, covering PRP, hyaluronic acid injection and prolotherapy, may be considered where structural tissue damage is contributing, and every injection is placed under ultrasound guidance. Where a nerve is entrapped or compressed, hydrodissection delivers fluid precisely alongside it to release it from the surrounding tissue and reduce its part in the pain. For chronic tendon and soft-tissue problems that have not improved with rest and physiotherapy, shockwave therapy can reset a stalled repair process.</p>
<p>Beyond these, ozone therapy may support anti-inflammatory processes where chronic inflammation is a driver, PEMF therapy may support cellular function and pain modulation where it fits the plan, and targeted IV anti-inflammatory and recovery support may help where systemic inflammation, oxidative stress or nutrient depletion are involved. Red light and photobiomodulation therapy may support tissue repair in localised areas. Underpinning most plans, structured physiotherapy addresses movement quality, strength and load, and because pain and poor sleep feed each other in a cycle that medication alone rarely breaks, sleep, stress and lifestyle contributors are addressed directly when the assessment flags them.</p>

<h2>What chronic pain management may help with</h2>
<p>When assessment and treatment are properly structured around your specific drivers, chronic pain management may offer real benefits, though results depend on the type and duration of pain, the treatments involved and how you respond. Read the points below as what a well-built plan works towards.</p>
<ul>
<li>identifying the underlying drivers of persistent pain through proper assessment, so treatment is not guesswork</li>
<li>addressing structural contributors such as tissue damage, joint degeneration and nerve entrapment directly, instead of masking them with medication</li>
<li>reducing pain intensity over a course of treatment as both structural and systemic contributors are worked through</li>
<li>improving functional movement and physical capacity as pain eases and rehabilitation progresses</li>
<li>better sleep, since easing pain lifts the nocturnal burden that keeps people awake</li>
<li>less reliance on long-term pain medication once the underlying cause is being treated</li>
<li>more meaningful, sustained improvement from a coordinated plan across several approaches than from any one in isolation</li>
</ul>
<p>Outcomes are not guaranteed and vary a great deal with the type, duration and complexity of the condition. A thorough assessment is what determines which parts of chronic pain treatment are appropriate for your situation.</p>

<h2>How the process works</h2>
<p>Every plan follows a clear clinical process, and nothing is recommended until your doctor has a full picture of your pain, its drivers and your wider health.</p>
<p>It starts with booking, where the team helps you choose the right appointment for your main concern, whether that is joint, back, nerve, tendon or widespread pain. Next comes a comprehensive pain assessment, where your doctor takes a detailed history of the location, character, duration, severity and behaviour of your pain, what eases or worsens it, its effect on sleep and daily life, and all previous investigations and treatments, then reviews relevant blood work and imaging and arranges any further investigation needed before the plan is finalised. From there your doctor builds a personalised plan around the specific drivers found, explaining each recommended option, why it was chosen, what the sessions involve, how many are likely and what realistic outcomes look like, with the cost confirmed before anything begins.</p>
<p>Treatment is then delivered in a clinical setting by a licensed doctor or supervised clinical team, using medical-grade equipment and sterile protocols, with every session following the protocol agreed at your assessment. Finally, because chronic pain responds best to an ongoing clinical relationship, review and adjustment appointments track your pain, function, sleep and response over time, and the plan is refined as you progress, since the goal is sustained improvement and not a brief reprieve.</p>

<h2>Why patients choose Brockwell Healthcare</h2>
<p>Several things set our chronic pain care apart. Every plan is built from a comprehensive assessment by a licensed doctor, not a one-size symptom-management protocol. Several treatment approaches sit under one clinical framework, so a plan can address all the relevant drivers at once, and regenerative, nerve-focused, systemic and rehabilitation methods can be combined within a single coordinated course. We discuss realistic outcomes honestly before anything starts, including the limits of what each approach can do, and we review progress at regular follow-ups and adjust as your response tells us more. The focus throughout stays on the cause of the pain, not on suppressing the symptom indefinitely, and full pricing is confirmed before your first session, with no surprises.</p>

<h2>Book a chronic pain consultation in Dubai</h2>
<p>Book a chronic pain consultation in Dubai at Brockwell Healthcare for a root-cause approach. Our team will assess your pain thoroughly, work out what is driving it, explain your options and confirm the cost before anything begins.</p>
"""

FAQS = [
    ("How is this different from standard pain management?",
     "Doctor-led chronic pain management here identifies the specific structural, inflammatory, neurological and lifestyle drivers of your pain through a full assessment before any plan is built. Standard pain management often focuses on suppressing the symptom with medication without addressing what is keeping the pain going."),
    ("What causes chronic pain?",
     "It can come from ongoing tissue damage, inflammation, nerve sensitisation, central sensitisation where the nervous system amplifies pain, hormonal and metabolic factors, disrupted sleep and psychological stress. Most people have several of these interacting at once, which is why a thorough assessment comes before any treatment planning."),
    ("Can chronic pain be treated without surgery?",
     "Many chronic pain conditions can be managed without surgery, using regenerative injection therapy, nerve hydrodissection, shockwave therapy, physiotherapy and IV anti-inflammatory support. A clinical assessment confirms which non-surgical approaches suit your specific condition."),
    ("Can regenerative treatments help with chronic pain?",
     "Regenerative approaches such as PRP, hydrodissection, prolotherapy and shockwave may support chronic pain management by addressing structural tissue damage, nerve compression and tendon degeneration, and not the symptom alone. Suitability depends on the condition and is confirmed at assessment."),
    ("Can nerve pain be treated here?",
     "Yes. Nerve pain from entrapment, compression or sensitisation may be addressed through ultrasound-guided hydrodissection, nerve release and systemic support. The right approach depends on where the nerve involvement is, what is causing it and what else is contributing."),
    ("How long does chronic pain treatment take?",
     "It depends a great deal on the type, duration and complexity of the pain, the treatments involved and your response. Some people notice meaningful improvement over a structured course of sessions, while others need a longer ongoing plan with regular reviews. Your doctor gives an honest estimate after the assessment."),
    ("Can chronic pain ever be fully resolved?",
     "That depends on the underlying cause and how long the pain has been present. Conditions where structural drivers are addressed early tend to respond better than long-standing pain with significant central sensitisation. Your doctor discusses realistic expectations honestly and does not overpromise."),
    ("What does chronic pain treatment cost in Dubai?",
     "The cost depends on the treatments selected, the number of sessions and the clinical protocol. We provide clear pricing and a full estimate before any treatment begins."),
    ("Who should consider chronic pain management here?",
     "It may suit people who have had pain for longer than three months, who have not found lasting relief through standard approaches, who want to understand what is actually driving their pain, or who want a coordinated plan that addresses several contributors under one clinical framework."),
    ("Do I need a referral first?",
     "No formal referral is needed. You can contact Brockwell Healthcare directly to book, and the team will help you choose the right appointment and advise on what to bring, including any relevant imaging or previous results."),
]


def load_content(apps, schema_editor):
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    cat = ServiceCategory.objects.filter(
        region="uae", slug__in=[OLD_SLUG, NEW_SLUG]
    ).first()
    if not cat:
        return

    cat.name = NAME
    cat.slug = NEW_SLUG
    cat.hero_heading = HERO_HEADING
    cat.summary = SUMMARY
    cat.description = DESCRIPTION.strip()
    cat.seo_title = SEO_TITLE
    cat.seo_description = SEO_DESCRIPTION
    cat.icon = ""
    cat.is_published = True
    cat.save()

    ct, _ = ContentType.objects.get_or_create(
        app_label="services", model="servicecategory"
    )
    FAQItem.objects.filter(content_type=ct, object_id=cat.id).delete()
    for i, (question, answer) in enumerate(FAQS):
        FAQItem.objects.create(
            content_type=ct, object_id=cat.id,
            question=question, answer=answer, order=i, is_published=True,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0100_tpe_inline_image"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
