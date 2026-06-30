"""Seed professional placeholder content for the UAE region.

Run with:  python manage.py seed_demo
Idempotent — safe to run multiple times (updates existing records by slug).
All content is client-editable from the admin afterwards.
"""

from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import FAQ
from events.models import Event
from services.models import Service

REGION = "uae"

SERVICES = [
    {
        "slug": "stem-cell-therapy",
        "icon": "🧬",
        "name": "Stem Cell Therapy",
        "summary": "Personalised regenerative treatments that harness your body's own healing potential.",
        "price": "5000.00",
        "order": 1,
        "description": (
            "Stem cell therapy uses specialised cells to support the body's natural repair "
            "processes. At our UAE clinic, treatments are tailored to your individual condition "
            "and delivered under strict clinical supervision.\n\n"
            "Our specialists assess your suitability through a comprehensive consultation, "
            "ensuring every plan is grounded in current clinical evidence and the highest "
            "standards of safety."
        ),
        "benefits": (
            "Personalised to your condition and goals\n"
            "Delivered in accredited, modern facilities\n"
            "Overseen by experienced regenerative specialists\n"
            "Supported by thorough follow-up care"
        ),
    },
    {
        "slug": "regenerative-medicine",
        "icon": "💠",
        "name": "Regenerative Medicine",
        "summary": "Advanced therapies designed to restore function and improve quality of life.",
        "price": "3500.00",
        "order": 2,
        "description": (
            "Regenerative medicine focuses on repairing and restoring damaged tissues using "
            "cutting-edge biological therapies.\n\n"
            "We combine the latest scientific advances with rigorous clinical protocols to offer "
            "treatments that are both innovative and safe."
        ),
        "benefits": (
            "Evidence-based treatment protocols\n"
            "Focus on long-term wellbeing\n"
            "Tailored to each patient's needs"
        ),
    },
    {
        "slug": "specialist-consultation",
        "icon": "🩺",
        "name": "Specialist Consultation",
        "summary": "A thorough one-to-one assessment with our regenerative medicine experts.",
        "price": "500.00",
        "order": 3,
        "description": (
            "Every journey begins with understanding. Our specialist consultation gives you a "
            "detailed assessment of your health, a clear explanation of your options, and an "
            "honest view of what regenerative therapies can offer.\n\n"
            "There is no obligation — just expert guidance to help you make an informed decision."
        ),
        "benefits": (
            "Comprehensive health assessment\n"
            "Clear, honest guidance\n"
            "Personalised treatment recommendations"
        ),
    },
    {
        "slug": "cord-blood-banking",
        "icon": "🏦",
        "name": "Cord Blood Banking",
        "summary": "Secure preservation of cord blood stem cells for your family's future health.",
        "price": None,
        "order": 4,
        "description": (
            "Cord blood is a rich source of stem cells that can be safely collected at birth and "
            "stored for potential future use.\n\n"
            "Our banking service offers secure, accredited storage and complete peace of mind for "
            "families across the UAE."
        ),
        "benefits": (
            "Accredited, secure long-term storage\n"
            "Simple, safe collection at birth\n"
            "A valuable resource for your family's future"
        ),
    },
]

EVENTS = [
    {
        "slug": "regenerative-medicine-seminar-dubai",
        "title": "Regenerative Medicine Seminar — Dubai",
        "summary": "An introductory evening seminar on stem cell and regenerative therapies.",
        "location": "Dubai Healthcare City, Dubai",
        "price": "0.00",
        "days_ahead": 21,
        "capacity": 100,
        "description": (
            "Join our specialists for an informative evening exploring the science and "
            "possibilities of regenerative medicine.\n\n"
            "This free seminar is ideal for anyone curious about how stem cell therapies work and "
            "whether they may be suitable. Light refreshments will be served."
        ),
    },
    {
        "slug": "stem-cell-masterclass-abu-dhabi",
        "title": "Stem Cell Masterclass — Abu Dhabi",
        "summary": "An in-depth masterclass with leading regenerative medicine clinicians.",
        "location": "Abu Dhabi",
        "price": "250.00",
        "days_ahead": 45,
        "capacity": 40,
        "description": (
            "A focused, half-day masterclass for those who want a deeper understanding of "
            "regenerative therapies.\n\n"
            "Includes detailed presentations, case discussions, and a live Q&A with our "
            "specialists. Places are limited."
        ),
    },
]

FAQS = [
    {
        "question": "What is stem cell therapy?",
        "answer": (
            "Stem cell therapy uses specialised cells to support the body's natural ability to "
            "repair and regenerate tissue. Treatments are tailored to each patient and delivered "
            "under strict clinical supervision."
        ),
        "order": 1,
    },
    {
        "question": "Is stem cell treatment safe?",
        "answer": (
            "Patient safety is our highest priority. All treatments follow rigorous clinical "
            "protocols and are carried out in accredited facilities by experienced specialists. "
            "Your suitability is carefully assessed during consultation."
        ),
        "order": 2,
    },
    {
        "question": "How do I know if I'm a suitable candidate?",
        "answer": (
            "The best way to find out is through a specialist consultation. Our team will review "
            "your medical history, assess your condition, and give you honest, evidence-based "
            "guidance on your options."
        ),
        "order": 3,
    },
    {
        "question": "Where are you located in the UAE?",
        "answer": (
            "Our clinic is based in Dubai, and we host events and consultations across the UAE. "
            "Please contact us to arrange an appointment at a convenient location."
        ),
        "order": 4,
    },
    {
        "question": "How can I book a consultation?",
        "answer": (
            "You can book a consultation by calling us, emailing our team, or completing the "
            "enquiry form on our contact page. We'll respond promptly to arrange your visit."
        ),
        "order": 5,
    },
]


class Command(BaseCommand):
    help = "Seed professional placeholder content for the UAE region."

    def handle(self, *args, **options):
        now = timezone.now()

        for data in SERVICES:
            Service.objects.update_or_create(
                region=REGION,
                slug=data["slug"],
                defaults={
                    "name": data["name"],
                    "icon": data["icon"],
                    "summary": data["summary"],
                    "description": data["description"],
                    "benefits": data["benefits"],
                    "price": data["price"],
                    "order": data["order"],
                    "is_published": True,
                },
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(SERVICES)} services."))

        for data in EVENTS:
            Event.objects.update_or_create(
                region=REGION,
                slug=data["slug"],
                defaults={
                    "title": data["title"],
                    "summary": data["summary"],
                    "description": data["description"],
                    "location": data["location"],
                    "price": data["price"],
                    "capacity": data["capacity"],
                    "start": now + timedelta(days=data["days_ahead"], hours=18),
                    "end": now + timedelta(days=data["days_ahead"], hours=20),
                    "is_published": True,
                },
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(EVENTS)} events."))

        for data in FAQS:
            FAQ.objects.update_or_create(
                region=REGION,
                question=data["question"],
                defaults={"answer": data["answer"], "order": data["order"], "is_published": True},
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(FAQS)} FAQs."))
        self.stdout.write(self.style.SUCCESS("Demo content ready."))
