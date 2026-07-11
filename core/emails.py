"""Transactional emails — booking/payment confirmations and admin notifications.

Every send is fail-safe: a failed email must never break a booking, payment or
enquiry. If SMTP isn't configured the console backend logs the message instead.
"""

import logging

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.templatetags.static import static
from django.utils.html import strip_tags

logger = logging.getLogger(__name__)


def _region(region_code):
    return settings.REGIONS.get(region_code) or settings.REGIONS.get(settings.DEFAULT_REGION)


def _abs_static(path):
    """Absolute https URL for a static asset (email clients need full URLs)."""
    try:
        url = static(path)
    except Exception:
        url = settings.STATIC_URL + path
    if url.startswith("http"):
        return url
    if not url.startswith("/"):
        url = "/" + url
    return f"https://{settings.SITE_DOMAIN}{url}"


def _send(subject, to, template, context, reply_to=None):
    """Render ``emails/<template>.html`` (+ optional ``.txt``) and send it.
    Returns True/False; never raises."""
    to_list = [a for a in ([to] if isinstance(to, str) else list(to or [])) if a]
    if not to_list:
        return False
    ctx = {
        "brand": settings.BRAND_NAME,
        "site_domain": settings.SITE_DOMAIN,
        "site_url": f"https://{settings.SITE_DOMAIN}",
        "logo_url": _abs_static("img/brockwell-healthcare-logo.png"),
        "hero_url": _abs_static("img/email/email-hero.jpg"),
        **context,
    }
    try:
        html = render_to_string(f"emails/{template}.html", ctx)
        try:
            text = render_to_string(f"emails/{template}.txt", ctx)
        except Exception:
            text = strip_tags(html)
        msg = EmailMultiAlternatives(
            subject=subject,
            body=text,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=to_list,
            reply_to=[reply_to] if reply_to else None,
        )
        msg.attach_alternative(html, "text/html")
        msg.send(fail_silently=False)
        return True
    except Exception:
        logger.exception("Email send failed (template=%s to=%s)", template, to_list)
        return False


def notify_admin(*, region_code, subject, title, rows, reply_to=None):
    """Send an internal notification to the clinic inbox."""
    return _send(
        subject, settings.EVENT_NOTIFY_EMAIL, "admin_notice",
        {"region": _region(region_code), "title": title, "rows": rows},
        reply_to=reply_to,
    )


def acknowledge(*, region_code, to, subject, heading, intro, rows=None, cta_label=None, cta_url=None):
    """Send a branded acknowledgement to the customer."""
    region = _region(region_code)
    return _send(
        subject, to, "customer_notice",
        {"region": region, "heading": heading, "intro": intro,
         "rows": rows or [], "cta_label": cta_label, "cta_url": cta_url},
        reply_to=region.get("email"),
    )


# --- High-level flows ------------------------------------------------------- #

def paid_booking(reg):
    """Online (Stripe-paid) booking → customer confirmation + admin notice."""
    region_code = reg.event.region
    tier = reg.package.name if reg.package_id else "—"
    amount = f"{reg.currency} {reg.amount:,.0f}"
    date = reg.event.start.strftime("%d %b %Y") if reg.event.start else ""
    notify_admin(
        region_code=region_code,
        subject=f"New paid booking — {reg.name} ({tier})",
        title="New paid booking",
        rows=[("Name", reg.name), ("Email", reg.email), ("Phone", reg.phone or "—"),
              ("Event", reg.event.title), ("Package", tier), ("Amount", amount)],
        reply_to=reg.email,
    )
    acknowledge(
        region_code=region_code, to=reg.email,
        subject=f"Your booking is confirmed — {reg.event.title}",
        heading="Your booking is confirmed",
        intro=(f"Thank you, {reg.name}. We've received your payment and reserved your "
               f"place at {reg.event.title}. Our team will be in touch with the details."),
        rows=[("Event", reg.event.title), ("Package", tier),
              ("Amount paid", amount), ("Date", date)],
    )


def event_registration(reg):
    """Form-based event registration (free or reserved) → admin + customer ack."""
    region_code = reg.event.region
    date = reg.event.start.strftime("%d %b %Y") if reg.event.start else ""
    notify_admin(
        region_code=region_code,
        subject=f"New event registration — {reg.name}",
        title="New event registration",
        rows=[("Name", reg.name), ("Email", reg.email), ("Phone", reg.phone or "—"),
              ("Event", reg.event.title), ("Paid", "Yes" if reg.paid else "No")],
        reply_to=reg.email,
    )
    acknowledge(
        region_code=region_code, to=reg.email,
        subject=f"We've received your registration — {reg.event.title}",
        heading="Registration received",
        intro=(f"Thank you, {reg.name}. We've received your registration for "
               f"{reg.event.title} and our team will be in touch shortly."),
        rows=[("Event", reg.event.title), ("Date", date)],
    )


def contact_lead(lead):
    """Contact / booking / newsletter enquiry → admin notice + customer ack."""
    is_newsletter = (lead.subject or "").lower().startswith("newsletter")
    notify_admin(
        region_code=lead.region,
        subject=(f"New newsletter signup — {lead.email}" if is_newsletter
                 else f"New enquiry — {lead.name}"),
        title="Newsletter signup" if is_newsletter else "New website enquiry",
        rows=[("Name", lead.name), ("Email", lead.email), ("Phone", lead.phone or "—"),
              ("Subject", lead.subject or "—"), ("Message", lead.message)],
        reply_to=lead.email,
    )
    if is_newsletter:
        acknowledge(
            region_code=lead.region, to=lead.email,
            subject=f"You're subscribed — {settings.BRAND_NAME}",
            heading="You're subscribed",
            intro="Thanks for subscribing to our newsletter. You'll now receive our "
                  "latest health updates and event news.",
        )
    else:
        acknowledge(
            region_code=lead.region, to=lead.email,
            subject=f"Thank you for contacting {settings.BRAND_NAME}",
            heading="Thank You for Contacting Us",
            intro=(f"Dear {lead.name}, thank you for reaching out to {settings.BRAND_NAME}. "
                   "We have received your enquiry and a member of our team will get back to "
                   "you within 24 hours. We appreciate your interest in our regenerative "
                   "medicine and longevity care."),
            rows=[("Your message", lead.message)] if lead.message else None,
            cta_label="Visit Our Website",
            cta_url=f"https://{settings.SITE_DOMAIN}",
        )
