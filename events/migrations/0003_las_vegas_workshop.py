"""Create the USA flagship event: the Advanced Regenerative Medicine &
Interventional Injection Training Workshop in Las Vegas (July 24-25, 2026).

Rich, section-based description rendered through the ``enhance`` filter (Why
Attend / Faculty / Pricing groups become card grids, the learning outcomes a
CSS icon list). Region-aware images live under
static/img/us/events/regenerative-injection-training-las-vegas-{hero,card}.webp."""

from datetime import datetime

from django.db import migrations
from django.utils.timezone import make_aware

SLUG = "regenerative-injection-training-las-vegas"

SEO_TITLE = (
    "Regenerative Medicine & Injection Training Workshop — Las Vegas, July 2026 "
    "| Brockwell Healthcare"
)
SEO_DESCRIPTION = (
    "A two-day, hands-on regenerative and interventional injection training workshop in "
    "Las Vegas, July 24-25, 2026. Small-group, instructor-led, limited to 25 seats. "
    "Register now."
)
SUMMARY = (
    "A two-day, hands-on regenerative and interventional injection training workshop — "
    "small-group, instructor-led and strictly limited to 25 seats."
)

DESCRIPTION = """
<h2>Overview</h2>
<p>Brockwell Healthcare invites physicians, physician assistants, nurse practitioners and allied healthcare professionals to a two-day intensive training workshop in Las Vegas focused on regenerative and interventional injection medicine.</p>
<p>This is not a lecture-based conference. It is a hands-on, practice-focused programme where participants train directly under expert faculty in small-group, instructor-led sessions, and leave with clinical skills they can apply immediately in their practice.</p>

<img src="/static/img/events/regenerative-injection-training-las-vegas-card.webp" alt="Hands-on interventional injection training at the Brockwell Healthcare workshop in Las Vegas" loading="lazy" decoding="async">

<h2>What you will learn</h2>
<ul>
<li>Advanced interventional injection techniques with live, hands-on clinical training</li>
<li>Practical applications of regenerative and longevity medicine in modern patient care</li>
<li>Ultrasound-guided injection protocols and procedural best practices</li>
<li>How to integrate regenerative treatment pathways into your existing practice</li>
</ul>

<h2>Why attend</h2>
<h3>Expert-led training</h3>
<p>Learn directly from practitioners shaping modern regenerative medicine, in a programme built around clinical judgement and real technique.</p>
<h3>Hands-on experience</h3>
<p>Interactive clinical sessions built for real-world impact, not passive lectures — you practise the procedures yourself under supervision.</p>
<h3>Small cohort</h3>
<p>Enrolment is limited to just 25 seats to preserve the quality of instructor-led training and give every participant real hands-on time.</p>
<h3>Professional network</h3>
<p>Connect with forward-thinking clinicians from around the world and build relationships that continue well beyond the workshop.</p>

<h2>Meet the faculty</h2>
<h3>Dr. Syed Hasnain Haider-Shah — MD, CM (McGill), FINR, FICA</h3>
<p>Lead Faculty and Program Director, and Founder of Brockwell Healthcare. A McGill-trained international neurointerventional specialist and regenerative medicine physician, internationally recognised for translational work in cerebrovascular regeneration, photobiomodulation integration and executive longevity medicine.</p>
<h3>Aaron Kuehl — PA-C</h3>
<p>Lead Faculty and Board-Certified Physician Associate, co-leading the hands-on clinical training, with a practice focus on regenerative and interventional injection medicine.</p>
<h3>Rachel Ann Garcia — AGACNP-BC, APRN</h3>
<p>Speaker and Trainer. An Adult-Gerontology Acute Care Nurse Practitioner with ICU leadership experience across the Middle East and the United States, focusing on IV infusion therapy, peptide-based recovery protocols and clinical workflow design for regenerative practice.</p>
<h3>Karolina Balkenbush — RDN, LDN, CDCES</h3>
<p>Speaker and Trainer. A Registered Dietitian Nutritionist and Certified Diabetes Care and Education Specialist, bringing clinical nutrition expertise to regenerative and longevity patient care.</p>
<h3>Nurse Chap — Aesthetics Specialist</h3>
<p>Speaker and Trainer, contributing hands-on expertise in aesthetic and regenerative treatment applications.</p>
<h3>Natalie Nicole — Founder, Dulsa Life</h3>
<p>Speaker and Trainer. Founder of Dulsa Life, contributing expertise in wellness and lifestyle-driven approaches to patient care.</p>

<h2>Registration and pricing</h2>
<p>Seats are strictly limited to 25 participants, and registration is offered across several tiers so you can choose the level of access that fits your goals.</p>
<h3>Early Registration — $1,495</h3>
<p>First 10 registrants only. Full access to lectures, training sessions, course materials, a certificate of attendance and networking opportunities.</p>
<h3>Standard Registration — $1,995</h3>
<p>Full conference access, hands-on training sessions, educational materials, a certificate of attendance and networking access.</p>
<h3>VIP Mentorship Package — $2,995</h3>
<p>Everything in Standard Registration, plus priority seating, small-group mentorship, direct Q&amp;A with faculty, exclusive VIP resource materials and post-event guidance and support.</p>
<h3>Observer Registration — $995</h3>
<p>Lecture and observation only. Access to didactic sessions, live demonstrations, observation areas and general course materials. Hands-on participation is not included.</p>
<p><strong>Group practice discounts are available</strong> — special pricing for teams registering from the same practice. To register or ask about group rates, call <strong>725-312-2125</strong> or email <strong>fathima@brockwellhealthcare.com</strong>.</p>
"""


def create_event(apps, schema_editor):
    Event = apps.get_model("events", "Event")

    # The US region was seeded by cloning the UAE events; those Dubai seminars are
    # not real US events, so hide them and let the US site show its own workshops.
    Event.objects.filter(
        region="us",
        slug__in=["regenerative-medicine-seminar-dubai", "longevity-healthspan-masterclass"],
    ).update(is_published=False)

    Event.objects.update_or_create(
        region="us", slug=SLUG,
        defaults=dict(
            title="Advanced Regenerative Medicine & Interventional Injection Training Workshop",
            summary=SUMMARY,
            description=DESCRIPTION.strip(),
            start=make_aware(datetime(2026, 7, 24, 9, 0)),
            end=make_aware(datetime(2026, 7, 25, 17, 0)),
            location="Las Vegas, Nevada, USA",
            # Multiple registration tiers ($995–$2,995) are shown in the content;
            # the sidebar takes a reservation and the team confirms tier and payment.
            price=0,
            capacity=25,
            is_published=True,
            seo_title=SEO_TITLE,
            seo_description=SEO_DESCRIPTION,
        ),
    )


def remove_event(apps, schema_editor):
    Event = apps.get_model("events", "Event")
    Event.objects.filter(region="us", slug=SLUG).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0002_event_image"),
    ]

    operations = [migrations.RunPython(create_event, remove_event)]
