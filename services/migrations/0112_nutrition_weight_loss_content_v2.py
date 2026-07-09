"""Refresh the Nutrition & Weight Loss service with the user's doctor-led, blood-test-first
copy: reworked section set (What is / How the assessment works / What we address [card grid]
/ How this fits / What to expect / The programme process / Why patients choose) and a 10-item
FAQ. Prose-led. Keeps the hero and a single inline content image.
Hero: static/img/services/nutrition-weight-loss-hero.webp;
inline: static/img/services/nutrition-weight-loss-content.webp."""

from django.db import migrations

SLUG = "nutrition-weight-loss"

SEO_TITLE = (
    "Nutrition & Weight Loss in Dubai | Doctor-Led, Blood-Test First | Brockwell Healthcare"
)
SEO_DESCRIPTION = (
    "Doctor-led nutrition and weight loss in Dubai at Brockwell Healthcare. Blood work first "
    "to find why the weight is stuck, then a plan built on your results, with GLP-1 where "
    "appropriate."
)
HERO_HEADING = "Nutrition and weight loss in Dubai"
SUMMARY = (
    "Doctor-led, blood-test-first weight loss that finds why the weight is stuck, then builds "
    "the plan on your results, with GLP-1 where appropriate."
)

DESCRIPTION = """
<p>The nutrition and weight loss programme at Brockwell Healthcare is led by a qualified doctor and built for people whose weight has stopped responding to the usual advice. Before any plan is written, you have a consultation and blood work, and the point of the blood work is to find out why the weight is there in the first place.</p>

<h2>What is the nutrition and weight loss programme at Brockwell Healthcare?</h2>
<p>Most patients who come to us have already tried. They have done the diets, sometimes several of them, lost weight, regained it, and are now heavier than when they started. Or they are eating carefully and training regularly and the scale has simply stopped moving. Telling these patients to eat less and move more does not help, because that is what they have already been doing.</p>
<p>Weight that resists a reasonable effort usually has a reason. It might be insulin resistance, which changes how the body stores fat, or a thyroid running slow. In men, falling testosterone changes body composition, and in women the hormonal shifts of perimenopause or PCOS do the same. Poor sleep and high cortisol push appetite up, and several common medications cause weight gain as a side effect. A diet plan on its own does not check for any of this.</p>
<p>So the programme starts with testing, and the plan is built around what the tests find. One patient's plan is mostly nutritional. Another needs a thyroid or hormonal problem treated first, or a prescription for weight loss medication alongside the food changes. Your doctor explains the reasoning at every step.</p>

<h2>How the assessment works</h2>
<p>The first appointment goes through your weight history in detail, meaning what you have tried, what happened each time, and how your weight has moved over the years. We also ask about eating patterns, sleep, stress, training, any medications and your family history. Someone who has lost and regained the same weight three times needs different testing than someone whose weight has crept up slowly over a decade.</p>
<p>Blood work typically covers insulin and glucose regulation, thyroid function, a lipid profile, inflammatory markers, and the hormone panels relevant to your situation. Body composition is measured as well, because two people can weigh the same with very different amounts of muscle and visceral fat, and their plans should not look the same.</p>
<p>When the results are back, your doctor goes through them with you and connects them to your history. A fasting insulin at the top of the range often explains years of stubborn weight, and finding it changes the whole plan.</p>

<img src="/static/img/services/nutrition-weight-loss-content.webp" alt="Doctor-led, blood-test-first nutrition and weight loss consultation at Brockwell Healthcare in Dubai" loading="lazy" decoding="async">

<h2>What we address</h2>
<h3>Weight that will not shift</h3>
<p>This is the most common reason people come to us. The diet is reasonable and the training is consistent, but nothing changes on the scale. Blood work in these patients very often turns up insulin resistance, an underperforming thyroid or a hormonal shift that was never tested for, and once the finding is treated, the nutrition plan is built to support that correction.</p>
<h3>Insulin resistance and pre-diabetes</h3>
<p>Insulin resistance sits behind a large share of adult weight gain, and it develops years before blood sugar looks abnormal on a standard test. Day to day it shows up as weight around the middle and energy crashes after meals, with cravings usually part of the picture too. It responds well to a structured plan, and catching it at this stage also lowers your risk of developing diabetes later.</p>
<h3>Hormonal weight gain</h3>
<p>Weight gain during perimenopause, after pregnancy, alongside PCOS or with falling testosterone has hormonal causes, and calorie restriction on its own usually does not work against it. We test the relevant hormones and treat what needs treating, then adjust the nutrition and training approach to fit.</p>
<h3>Appetite, cravings and eating patterns</h3>
<p>Constant hunger and cravings usually have physical drivers. Blood sugar swings, poor sleep, stress hormones and certain deficiencies all push appetite upward, and correcting them makes eating well much easier. Where eating patterns suggest something that needs specialist support, such as a possible eating disorder, we say so and refer you to the right care instead of putting you on a weight loss plan that could do harm.</p>
<h3>Medical weight loss treatment</h3>
<p>Prescription weight loss medication, including GLP-1 based treatment, has changed the options available to many patients, and we prescribe it where the assessment supports it. Your doctor screens for the situations where these medications are a bad idea, and pairs the prescription with a nutrition plan that protects muscle while the weight comes off. Follow-up matters here, because the dose changes over time and side effects and food intake both need watching.</p>
<h3>Nutrition and deficiency correction</h3>
<p>Some patients need nutritional work more than weight loss. Low vitamin D, B12, iron and magnesium are common findings, and they affect energy, mood, training recovery and appetite regulation. Deficiencies found in your blood work are corrected as part of the programme, with retesting to confirm the correction worked.</p>
<h3>Muscle, strength and body composition</h3>
<p>On an aggressive diet, part of what you lose is muscle, and muscle is what keeps your metabolism and blood sugar control working as you age. Your plan includes protein and training guidance matched to your starting point, and body composition is retested during the programme so we can confirm the loss is coming from fat.</p>

<h2>How this fits with our other services</h2>
<p>Weight is connected to almost everything else we treat. Insulin resistance and thyroid problems sit inside our functional medicine work. Testosterone and weight are tightly linked in men, which is where the male wellness service comes in. Patients thinking past the weight itself often move into the longevity programme, where body composition and metabolic health are core markers. Because it all runs under one roof, your weight loss plan draws on whichever of these your results say you need.</p>

<h2>What to expect</h2>
<p>Lasting weight loss tends to be steady. Most patients who follow their plan lose at a sustainable rate that protects muscle, and the early weeks are often more about sleep and appetite settling down than about big movement on the scale. Patients on weight loss medication typically lose faster, and the follow-up structure exists to keep that loss healthy.</p>
<p>Your doctor tells you at the results appointment what a realistic outcome looks like for your situation and your timeline. If you have a significant amount to lose, you will hear a straight answer on how long that takes to do properly.</p>

<h2>The programme process</h2>
<p>It starts with booking, where you contact Brockwell Healthcare to arrange your consultation and the team books you with the doctor first. At the assessment, your doctor takes a detailed weight and health history, followed by blood work and body composition testing selected for your situation. At the results and plan appointment, your doctor goes through every finding with you and builds the plan from the results, covering nutrition, training guidance, treatment for anything the blood work found, and medication where it is appropriate, with costs confirmed before anything starts. Follow-up then reviews your progress at set intervals, with body composition retested and blood work repeated where needed, and plans adjusted as your weight and results change. The final stage is maintenance, keeping the weight off, which is planned with the same care as the loss itself, including how any medication is tapered where it was used.</p>

<h2>Why patients choose Brockwell Healthcare</h2>
<p>Plenty of weight loss programmes never run a single blood test. At Brockwell Healthcare the blood work comes first, so the plan rests on your own results. A qualified doctor leads the programme, prescription treatment is available when your results support it, and patients whose situation needs specialist care are referred on instead of kept in the programme. Muscle and long-term metabolic health are protected throughout, and you know the full price before your first session.</p>

<h2>Book a nutrition and weight loss consultation in Dubai</h2>
<p>Book a nutrition and weight loss consultation in Dubai at Brockwell Healthcare. Your doctor will work out why the weight is not moving and build the plan from your results, and you will know the cost before anything begins.</p>
"""

FAQS = [
    ("How is this different from seeing a nutritionist?",
     "Mainly the diagnostic step. A nutritionist can build you a good meal plan, but if the reason your weight is stuck is insulin resistance or a thyroid problem, the meal plan alone will keep failing. Here a doctor tests first, treats what needs treating, and the nutrition plan is built on top of that."),
    ("I eat well and train regularly but my weight will not move. Can you help?",
     "This is the most common situation we see, and the programme was designed around it. There is usually a measurable reason, and blood work finds it. Once that reason is treated, diet and training start producing results again."),
    ("Do you prescribe weight loss injections like GLP-1 medications?",
     "Yes, where the assessment shows they are clinically appropriate. Your doctor screens for suitability, pairs the prescription with a plan that protects your muscle, and follows you up through the course, including how it eventually gets tapered."),
    ("Will I be put on a very low calorie diet?",
     "No. Aggressive restriction costs you muscle and slows your metabolism, and it usually ends in regain. Most of our patients have been through that cycle before. Plans are built to be sustainable, with enough food to train and function well."),
    ("How fast will I lose weight?",
     "It depends on your starting point, your results and whether medication is part of the plan. Your doctor gives you a realistic rate at the results appointment."),
    ("Do I have to give up my normal food?",
     "The plan is built around how you live and eat, including eating out, which is hard to avoid in Dubai. If parts of it are not working for you, we adjust them at follow-up."),
    ("What tests are included?",
     "Typically insulin and glucose markers, thyroid function, a lipid profile, inflammatory markers and relevant hormone panels, plus body composition testing. The exact panel is selected for your history, and each test is explained before it is ordered."),
    ("Can you help with weight gain caused by my medication?",
     "Often, yes. Some common medications drive weight gain, and the approach depends on which one and why you take it. We never stop or change a medication without proper clinical review and coordination with your prescribing doctor."),
    ("What does the programme cost?",
     "It depends on the testing, the plan and whether medication is involved. You get a clear cost estimate at your assessment, before anything is booked, and nothing is added without your agreement."),
    ("Do I need a referral?",
     "No. Contact the clinic directly and the team will book your assessment. Bring any recent blood results you have, so you are not paying to repeat tests that were already done."),
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
        ("services", "0111_hbot_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, migrations.RunPython.noop)]
