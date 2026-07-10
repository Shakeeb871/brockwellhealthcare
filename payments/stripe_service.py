"""Thin wrapper around the Stripe API.

Keeps Stripe specifics in one place so views stay clean and the integration
is easy to test or swap. Live behaviour activates automatically once real
keys are set in the environment; until then ``is_configured`` is False and
the UI shows a friendly "payments coming soon" state instead of erroring.
"""

from decimal import Decimal

from django.conf import settings

import stripe


def is_configured() -> bool:
    return bool(settings.STRIPE_SECRET_KEY)


def _client():
    stripe.api_key = settings.STRIPE_SECRET_KEY
    return stripe


def create_checkout_session(*, request, registration, event, region, success_url, cancel_url):
    """Create a Stripe Checkout session for an event registration.

    Amounts are converted to the smallest currency unit (fils/cents).
    """
    client = _client()
    amount_minor = int((Decimal(event.price) * 100).to_integral_value())

    session = client.checkout.Session.create(
        mode="payment",
        success_url=success_url,
        cancel_url=cancel_url,
        customer_email=registration.email,
        client_reference_id=str(registration.id),
        metadata={
            "registration_id": str(registration.id),
            "event_id": str(event.id),
            "region": region["code"],
        },
        line_items=[
            {
                "quantity": 1,
                "price_data": {
                    "currency": region["stripe_currency"],
                    "unit_amount": amount_minor,
                    "product_data": {
                        "name": event.title,
                        "description": event.summary[:300],
                    },
                },
            }
        ],
    )
    return session


def create_package_checkout_session(*, event, package, region, success_url, cancel_url):
    """Create a Stripe Checkout session for a specific event package tier.

    The amount comes from ``package.amount`` (server-side, from the database) —
    never from the browser. Stripe collects the buyer's email and card on its
    own hosted page; the webhook then records the paid registration.
    """
    client = _client()
    amount_minor = int((Decimal(package.amount) * 100).to_integral_value())

    session = client.checkout.Session.create(
        mode="payment",
        success_url=success_url,
        cancel_url=cancel_url,
        metadata={
            "event_id": str(event.id),
            "package_id": str(package.id),
            "package_name": package.name,
            "region": region["code"],
        },
        line_items=[
            {
                "quantity": 1,
                "price_data": {
                    "currency": region["stripe_currency"],
                    "unit_amount": amount_minor,
                    "product_data": {
                        "name": f"{event.title} — {package.name}",
                        "description": event.summary[:300],
                    },
                },
            }
        ],
    )
    return session


def construct_webhook_event(payload, signature):
    """Verify and parse an incoming Stripe webhook."""
    return stripe.Webhook.construct_event(
        payload, signature, settings.STRIPE_WEBHOOK_SECRET
    )
