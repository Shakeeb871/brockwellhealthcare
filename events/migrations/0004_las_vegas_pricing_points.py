"""Rewrite the Las Vegas workshop pricing so each package's inclusions are
bullet points (rendered as a checklist on the pricing cards) instead of a
single paragraph. Everything else in the description is unchanged."""

from django.db import migrations

SLUG = "regenerative-injection-training-las-vegas"

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
<ul>
<li>First 10 registrants only</li>
<li>Full access to all lectures and training sessions</li>
<li>Complete course materials</li>
<li>Certificate of attendance</li>
<li>Networking opportunities</li>
</ul>
<h3>Standard Registration — $1,995</h3>
<ul>
<li>Full conference and training access</li>
<li>Hands-on training sessions</li>
<li>Educational materials</li>
<li>Certificate of attendance</li>
<li>Networking access</li>
</ul>
<h3>VIP Mentorship Package — $2,995</h3>
<ul>
<li>Everything in Standard Registration</li>
<li>Priority seating</li>
<li>Small-group mentorship</li>
<li>Direct Q&amp;A with faculty</li>
<li>Exclusive VIP resource materials</li>
<li>Post-event guidance and support</li>
</ul>
<h3>Observer Registration — $995</h3>
<ul>
<li>Lecture and observation only</li>
<li>Access to all didactic sessions</li>
<li>Live procedure demonstrations</li>
<li>Observation areas</li>
<li>General course materials</li>
<li>Hands-on participation not included</li>
</ul>
<p><strong>Group practice discounts are available</strong> — special pricing for teams registering from the same practice. To register or ask about group rates, call <strong>725-312-2125</strong> or email <strong>fathima@brockwellhealthcare.com</strong>.</p>
"""


def set_description(apps, schema_editor):
    Event = apps.get_model("events", "Event")
    Event.objects.filter(region="us", slug=SLUG).update(description=DESCRIPTION.strip())


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0003_las_vegas_workshop"),
    ]

    operations = [migrations.RunPython(set_description, noop)]
