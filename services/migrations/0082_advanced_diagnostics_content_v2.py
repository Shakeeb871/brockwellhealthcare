"""Update the Advanced Diagnostics category with the user's restructured, narrative copy,
rendered through the professional category (homepage-style) layout as alternating
text + image sections. Hero, lead (intro) and the first two section images are supplied
under static/img/services/categories/advanced-diagnostics/. Plus a 7-item FAQ.
Supersedes the previous category content (0043)."""

from django.db import migrations

SEO_TITLE = "Advanced Diagnostics in Dubai | Comprehensive Health Check | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Advanced diagnostics in Dubai at Brockwell Healthcare, going beyond a standard check "
    "with detailed biomarkers and imaging, interpreted properly to find what actually "
    "matters for your health."
)
HERO_HEADING = "Advanced diagnostics in Dubai"
SUMMARY = (
    "In-depth health assessment beyond a standard check, using detailed biomarkers and "
    "targeted imaging, interpreted properly to find what actually matters."
)

DESCRIPTION = """
<p>A standard health check tells you whether anything is obviously wrong today. Advanced diagnostics tries to answer a more useful question, which is where your health is heading and what you can change while it still counts. It does that by measuring more, and more precisely, than a routine panel. At Brockwell Healthcare our advanced diagnostics in Dubai are built to find the signals worth acting on early, and, just as importantly, to avoid drowning you in numbers that do not matter.</p>

<h2>What is advanced diagnostics?</h2>
<p>Advanced diagnostics is detailed health assessment that goes beyond the basic blood test and physical, using a broader set of biomarkers and, where useful, imaging, to build a fuller picture of how your body is actually working. The point is not to run every test that exists. It is to measure the things that genuinely predict future health, then interpret them together and not one line at a time.</p>

<h2>Beyond the standard blood test</h2>
<p>The difference from a routine panel is in the depth and the choice of markers. A standard test might check cholesterol and blood sugar. A more advanced assessment looks underneath those. It might measure hs-CRP, a sensitive marker of the low-grade inflammation tied to many chronic diseases, or HbA1c and fasting insulin together, which reveal how your metabolism is coping years before diabetes would show up on a simple glucose test. It often includes ApoB, which counts the actual number of harmful particles behind cardiovascular risk more accurately than standard cholesterol, alongside a proper look at hormones, thyroid function and key micronutrients such as vitamin D. Each of these earns its place by telling you something you can act on.</p>
<p>Blood is only part of the story, so the picture is often completed with imaging and functional testing chosen for the individual. That might mean ultrasound to look at soft tissue or blood vessels without any radiation, measures of cardiovascular and metabolic fitness, or body-composition analysis that distinguishes muscle from fat far better than weight alone. The aim is always the same, to gather the specific information that changes a decision, and to leave out the rest.</p>

<h2>The honest side: more testing is not automatically better</h2>
<p>This is the part serious diagnostics gets right and the marketing gets wrong. Testing has a downside as well as an upside, because scanning and measuring everything inevitably turns up incidental findings, harmless quirks that lead to more tests, more worry and occasionally more harm than the original finding ever would have caused. Good advanced diagnostics is therefore selective on purpose. Our doctor chooses tests that answer a real question for you and interprets the results in context, so a slightly out-of-range number is understood, not chased. Measuring well is a skill, and measuring everything is not the same thing.</p>

<h2>Who it suits</h2>
<p>Advanced diagnostics suits people who want to be proactive about their health, who are building a longevity or prevention plan, or who simply want a clearer baseline than a basic check provides. It is most powerful when it is repeated over time, because a single snapshot tells you where you are, while a trend tells you where you are going. Our doctor uses it as the foundation of a plan, not as an end in itself.</p>
"""

FAQS = [
    ("What is advanced diagnostics?",
     "Advanced diagnostics is in-depth health assessment that goes beyond a standard blood test, using a wider set of meaningful biomarkers and targeted imaging to show how your body is really working and where your health is heading, all interpreted together by a doctor."),
    ("What tests are included?",
     "It varies with the person, but it often adds markers like hs-CRP for inflammation, HbA1c and fasting insulin for metabolic health, ApoB for cardiovascular risk, plus hormones, thyroid and micronutrients, alongside imaging such as ultrasound where useful."),
    ("Is more testing always better?",
     "No. Testing everything turns up harmless incidental findings that can lead to unnecessary worry and further tests. Good diagnostics is selective, choosing tests that answer a real question and interpreting them in context."),
    ("How is this different from a normal health check?",
     "A normal check looks for obvious current problems, while advanced diagnostics measures more sensitive markers that predict future risk, often years earlier, and focuses on trends you can act on instead of a single pass or fail."),
    ("Do I need to prepare or fast beforehand?",
     "Some markers, such as fasting glucose, insulin and certain lipids, are best measured after an overnight fast, while others need no preparation at all. Our team tells you exactly what to do before your specific panel."),
    ("How often should I do it?",
     "Because trends matter more than a single reading, it is usually repeated periodically, with the interval set by your doctor around your age, risks and goals."),
    ("What happens after the tests?",
     "The results are interpreted together into a clear picture and a practical plan, with anything that needs attention followed up. The tests are the start of the conversation, not the end."),
]


def load_content(apps, schema_editor):
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    cat = ServiceCategory.objects.filter(region="uae", slug="advanced-diagnostics").first()
    if not cat:
        return

    cat.hero_heading = HERO_HEADING
    cat.summary = SUMMARY
    cat.description = DESCRIPTION.strip()
    cat.seo_title = SEO_TITLE
    cat.seo_description = SEO_DESCRIPTION
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
        ("services", "0081_genomics_medicine_inline_image"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
