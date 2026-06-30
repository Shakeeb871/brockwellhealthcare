"""Seed professional placeholder content for the UAE region.

Run with:  python manage.py seed_demo
Idempotent — safe to run repeatedly (updates by slug). All content is fully
editable from the admin afterwards.
"""

from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.text import slugify

from core.models import FAQ, Page
from events.models import Event
from services.models import Service, ServiceCategory
from team.models import Doctor

REGION = "uae"

# (name, icon, summary, [sub-services]) — order preserved.
CATEGORIES = [
    (
        "Regenerative Wellness", "🌿",
        "Restore vitality and balance with therapies that support your body's natural healing.",
        [
            "Detox Therapy", "Hydrodissection & Injections", "Exomind TMS Wellness",
            "Hyperbaric Oxygen Therapy", "IV Laser Therapy", "Male Wellness",
            "Sexual Health", "Nutrition & Weight Loss", "PEMF Therapy",
            "Red Light Therapy", "Shock Wave Therapy", "Stress Management",
            "Urology Services",
        ],
    ),
    (
        "Regenerative Medicine", "💠",
        "Advanced biological therapies that repair, restore and rebuild from within.",
        [
            "Regenerative Orthopedics", "Biological Integrative Medicine", "Sports Medicine",
            "Exosome Therapy", "Functional Medicine", "Genomics Medicine", "Physiotherapy",
        ],
    ),
    (
        "Longevity | Healthspan", "⏳",
        "Science-led programmes to extend healthspan and optimise how you age.",
        [
            "Healthspan", "Longevity Medicine", "Stem Cells",
            "Stress Reset", "Ketamine Therapy", "Longevity IVs",
        ],
    ),
    (
        "Anti-Aging Aesthetics", "✨",
        "Natural-looking aesthetic treatments that rejuvenate and restore confidence.",
        ["Pure Plasma", "Emsella", "Emsculpt NEO"],
    ),
    (
        "Advanced Diagnostics", "🔬",
        "Precise, modern diagnostics to guide truly personalised care.",
        ["Ultrasound Diagnostics"],
    ),
    (
        "Emsculpt For Pain", "⚡",
        "Non-invasive electromagnetic therapy for muscle recovery and pain relief.",
        [],
    ),
]

# Short, tailored summaries for each sub-service.
SERVICE_SUMMARIES = {
    "Detox Therapy": "Cleanse and reset your system with guided, medically-supervised detox protocols.",
    "Hydrodissection & Injections": "Precision ultrasound-guided injections to relieve nerve and joint pain.",
    "Exomind TMS Wellness": "Non-invasive transcranial stimulation to support mood, focus and mental wellbeing.",
    "Hyperbaric Oxygen Therapy": "Oxygen-rich therapy that accelerates healing and boosts cellular recovery.",
    "IV Laser Therapy": "Intravenous laser treatment to enhance circulation, energy and immunity.",
    "Male Wellness": "Comprehensive men's health programmes for hormones, energy and vitality.",
    "Sexual Health": "Confidential, evidence-based treatments to restore sexual health and confidence.",
    "Nutrition & Weight Loss": "Personalised nutrition and medical weight-management plans that last.",
    "PEMF Therapy": "Pulsed electromagnetic field therapy to reduce pain and support recovery.",
    "Red Light Therapy": "Therapeutic red and near-infrared light for skin, recovery and energy.",
    "Shock Wave Therapy": "Acoustic wave therapy to treat chronic pain and stimulate tissue repair.",
    "Stress Management": "Holistic, clinically-guided programmes to manage stress and build resilience.",
    "Urology Services": "Specialist urological assessment and treatment in a discreet setting.",
    "Regenerative Orthopedics": "Non-surgical regenerative treatments for joints, tendons and ligaments.",
    "Biological Integrative Medicine": "Whole-body, root-cause care combining biological and integrative therapies.",
    "Sports Medicine": "Performance, injury and recovery care for active people and athletes.",
    "Exosome Therapy": "Next-generation cellular signalling therapy to support tissue regeneration.",
    "Functional Medicine": "Root-cause medicine that addresses the 'why' behind your symptoms.",
    "Genomics Medicine": "Personalised insights from your DNA to guide prevention and treatment.",
    "Physiotherapy": "Expert physiotherapy to restore movement, strength and function.",
    "Healthspan": "Programmes designed to maximise the years you live in great health.",
    "Longevity Medicine": "Proactive, data-driven medicine focused on healthy longevity.",
    "Stem Cells": "Regenerative stem cell therapies delivered to the highest clinical standards.",
    "Stress Reset": "Targeted protocols to rebalance your nervous system and recover from burnout.",
    "Ketamine Therapy": "Supervised ketamine therapy for mood, pain and mental wellbeing.",
    "Longevity IVs": "Tailored intravenous nutrient therapies to support energy and longevity.",
    "Pure Plasma": "Platelet-rich plasma treatments for natural skin and tissue rejuvenation.",
    "Emsella": "Non-invasive pelvic floor strengthening for bladder control and confidence.",
    "Emsculpt NEO": "Build muscle and reduce fat simultaneously — no surgery, no downtime.",
    "Ultrasound Diagnostics": "High-resolution diagnostic ultrasound for accurate, real-time assessment.",
}

# (name, photo). Details (title/bio/specialties) are placeholder; edit in admin.
DOCTORS = [
    ("Dr. Hasnain Haider-Shah", "/static/img/dr-shah-brockwell-health-care.webp"),
    ("Dr. Nigel Beejay", ""),
    ("Dr. Adeel Khan, MD", ""),
    ("Dr. Sabine Hazan, MD", ""),
    ("Dr. Salman Gilani", ""),
    ("Shirley D'Souza", ""),
    ("Jean-Francois Tremblay", ""),
    ("Shahnawaz Hussein Khan, PhD", ""),
    ("Dr. Nameer Haider", ""),
    ("Prof. Dato' Sri Dr. Mike Chan", ""),
    ("Dr. Rozina Badal Munir", ""),
    ("Dr. Summer Beattie", ""),
    ("Rachel Tan Garcia", ""),
    ("Oscar Tellez", ""),
    ("Dr Don Buford", ""),
]

LEGAL_PAGES = [
    (
        "privacy-policy", "Privacy Policy",
        "Introduction:\n\nThis Privacy Policy explains how {brand} collects, uses and protects "
        "your personal information when you use our website and services. We are committed to "
        "safeguarding your privacy.\n\n"
        "Information We Collect:\n\nWe may collect your name, contact details and any information "
        "you provide through our enquiry or booking forms.\n\n"
        "How We Use Your Information:\n\nWe use your information to respond to enquiries, provide "
        "our services, and improve your experience. We do not sell your personal data.\n\n"
        "Contact Us:\n\nFor any privacy questions, please contact us at the details on our Contact page.\n\n"
        "Please note: this is a placeholder policy and should be reviewed by a qualified legal professional before publication.",
    ),
    (
        "terms-conditions", "Terms & Conditions",
        "Agreement:\n\nBy accessing and using the {brand} website, you agree to these Terms & "
        "Conditions.\n\n"
        "Use of the Website:\n\nThe content on this website is for general information and educational "
        "purposes only and does not constitute medical advice.\n\n"
        "Bookings & Payments:\n\nAppointments and event bookings are subject to availability and our "
        "cancellation policy.\n\n"
        "Limitation of Liability:\n\n{brand} is not liable for any decisions made solely on the basis "
        "of information on this website.\n\n"
        "Please note: this is a placeholder document and should be reviewed by a qualified legal professional before publication.",
    ),
    (
        "cookies", "Cookies Policy",
        "About Cookies:\n\nOur website uses cookies to ensure you get the best experience and to help "
        "us understand how the site is used.\n\n"
        "Types of Cookies:\n\nWe use essential cookies for site functionality and, where permitted, "
        "analytics cookies to improve our services.\n\n"
        "Managing Cookies:\n\nYou can control and delete cookies through your browser settings at any time.\n\n"
        "Please note: this is a placeholder document and should be reviewed by a qualified legal professional before publication.",
    ),
]

FAQS = [
    ("What conditions do you treat at Brockwell Healthcare?",
     "We offer regenerative wellness, regenerative medicine, longevity, anti-aging aesthetics and "
     "advanced diagnostics. The best starting point is a consultation, where we assess your needs and "
     "recommend the right programme."),
    ("Are your treatments safe?",
     "Patient safety is our highest priority. All treatments follow rigorous clinical protocols and are "
     "delivered by experienced specialists in accredited facilities."),
    ("How do I book an appointment?",
     "You can call us, email our team, or complete the enquiry form on our Contact page. We'll respond "
     "promptly to arrange your visit."),
    ("Where are you located?",
     "We are based in Dubai, United Arab Emirates, and welcome patients from across the UAE. Please "
     "contact us to arrange a convenient appointment."),
    ("Do you offer personalised treatment plans?",
     "Yes. Every plan is tailored to your individual health goals following a thorough assessment with "
     "our specialists."),
]


class Command(BaseCommand):
    help = "Seed professional placeholder content for the UAE region."

    def handle(self, *args, **options):
        now = timezone.now()

        # Service categories + sub-services
        n_cat = n_sub = 0
        for order, (name, icon, summary, subs) in enumerate(CATEGORIES, start=1):
            cat, _ = ServiceCategory.objects.update_or_create(
                region=REGION, slug=slugify(name),
                defaults={
                    "name": name, "icon": icon, "summary": summary, "order": order,
                    "description": (
                        f"At Brockwell Healthcare, our {name} services are delivered by experienced "
                        f"clinicians using the latest evidence-based approaches.\n\n"
                        f"Every programme is personalised to your individual needs and goals. "
                        f"Book a consultation to find out how we can help."
                    ),
                    "is_published": True,
                },
            )
            n_cat += 1
            for s_order, s_name in enumerate(subs, start=1):
                s_summary = SERVICE_SUMMARIES.get(s_name, f"{s_name} tailored to your health goals.")
                Service.objects.update_or_create(
                    region=REGION, slug=slugify(s_name),
                    defaults={
                        "category": cat, "name": s_name, "summary": s_summary, "order": s_order,
                        "description": (
                            f"{s_summary}\n\n"
                            f"Our {s_name} programme is part of our {name} services and is delivered by "
                            f"specialists at Brockwell Healthcare in Dubai. After a thorough assessment, "
                            f"we create a plan tailored specifically to you.\n\n"
                            f"To learn whether {s_name} is right for you, book a consultation with our team."
                        ),
                        "benefits": "Personalised to your needs\nDelivered by experienced specialists\nEvidence-based and patient-centred",
                        "is_published": True,
                    },
                )
                n_sub += 1
        self.stdout.write(self.style.SUCCESS(f"Seeded {n_cat} categories and {n_sub} sub-services."))

        # Doctors
        Doctor.objects.filter(region=REGION).delete()
        for order, (name, photo) in enumerate(DOCTORS, start=1):
            Doctor.objects.create(
                region=REGION, slug=slugify(name), name=name, title="Specialist",
                photo=photo, order=order, is_published=True,
                short_bio="Part of the expert medical team at Brockwell Healthcare.",
                full_bio=(
                    "Part of the expert medical team at Brockwell Healthcare. "
                    "(Add this specialist's full profile, specialties and photo in the admin.)"
                ),
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(DOCTORS)} doctors."))

        # Legal pages
        for slug, title, body in LEGAL_PAGES:
            Page.objects.update_or_create(
                region=REGION, slug=slug,
                defaults={"title": title, "body": body.format(brand="Brockwell Healthcare"), "is_published": True},
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(LEGAL_PAGES)} legal pages."))

        # FAQs
        FAQ.objects.filter(region=REGION).delete()
        for order, (q, a) in enumerate(FAQS, start=1):
            FAQ.objects.create(region=REGION, question=q, answer=a, order=order, is_published=True)
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(FAQS)} FAQs."))

        # Events
        events = [
            ("Regenerative Medicine Seminar — Dubai",
             "An introductory evening seminar on regenerative and longevity therapies.",
             "Dubai, United Arab Emirates", "0.00", 21, 100),
            ("Longevity & Healthspan Masterclass",
             "An in-depth masterclass with our longevity specialists.",
             "Dubai, United Arab Emirates", "250.00", 45, 40),
        ]
        for title, summary, location, price, days, capacity in events:
            Event.objects.update_or_create(
                region=REGION, slug=slugify(title),
                defaults={
                    "title": title, "summary": summary, "location": location, "price": price,
                    "capacity": capacity, "start": now + timedelta(days=days, hours=18),
                    "end": now + timedelta(days=days, hours=20), "is_published": True,
                    "description": (
                        f"{summary}\n\nJoin our specialists for an informative session at Brockwell "
                        f"Healthcare. Places are limited — reserve yours today."
                    ),
                },
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(events)} events."))
        self.stdout.write(self.style.SUCCESS("All demo content ready."))
