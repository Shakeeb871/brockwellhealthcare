"""
SEO / AEO / GEO helpers.

Builds the metadata and schema.org structured data that make pages rank in
search engines AND get cited accurately by answer engines / LLMs:

* ``build_meta``      -> title, description, canonical, hreflang, OG/Twitter.
* schema builders     -> JSON-LD for Organization (MedicalBusiness), Website,
                         Service, Event, FAQPage and BreadcrumbList.

Everything is region-aware so the UAE and (future) US sites each expose their
own canonical URLs, locale and contact details.
"""

from django.conf import settings

from .regions import enabled_regions, region_absolute, region_path


def absolute(path: str) -> str:
    if path.startswith("http"):
        return path
    if not path.startswith("/"):
        path = "/" + path
    return f"https://{settings.SITE_DOMAIN}{path}"


def build_meta(request, *, title, description, path, image=None, robots="index, follow", og_type="website"):
    """Assemble the full <head> metadata bundle for a page.

    ``path`` is the region-relative path WITHOUT the region prefix, e.g.
    ``/services/`` — hreflang/canonical are derived per region from it.
    """
    region_code = getattr(request, "region_code", settings.DEFAULT_REGION)
    canonical = absolute(f"/{region_code}{path}")

    # hreflang alternates: one per enabled region + an x-default.
    alternates = []
    for region in enabled_regions():
        alternates.append(
            {
                "hreflang": region["locale"],
                "href": absolute(f"/{region['code']}{path}"),
            }
        )
    alternates.append(
        {"hreflang": "x-default", "href": absolute(f"/{settings.DEFAULT_REGION}{path}")}
    )

    brand = settings.BRAND_NAME
    full_title = title if brand in title else f"{title} | {brand}"

    return {
        "title": full_title,
        "description": description,
        "canonical": canonical,
        "robots": robots,
        "og_type": og_type,
        "image": absolute(settings.STATIC_URL + (image or settings.DEFAULT_OG_IMAGE)),
        "alternates": alternates,
    }


# --------------------------------------------------------------------------- #
# JSON-LD schema builders
# --------------------------------------------------------------------------- #
def organization_schema(region):
    """MedicalBusiness/Organization — the foundational entity for GEO."""
    return {
        "@context": "https://schema.org",
        "@type": "MedicalBusiness",
        "@id": f"https://{settings.SITE_DOMAIN}/{region['code']}/#organization",
        "name": settings.BRAND_NAME,
        "description": settings.BRAND_TAGLINE,
        "url": f"https://{settings.SITE_DOMAIN}/{region['code']}/",
        "telephone": region["phone"],
        "email": region["email"],
        "medicalSpecialty": "RegenerativeMedicine",
        "areaServed": region["name"],
        "address": {
            "@type": "PostalAddress",
            "addressCountry": region["short"],
            "streetAddress": region["address"],
        },
        "priceRange": "$$$",
    }


def website_schema(region):
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": f"https://{settings.SITE_DOMAIN}/{region['code']}/#website",
        "name": settings.BRAND_NAME,
        "url": f"https://{settings.SITE_DOMAIN}/{region['code']}/",
        "inLanguage": region["locale"],
        "publisher": {"@id": f"https://{settings.SITE_DOMAIN}/{region['code']}/#organization"},
    }


def breadcrumb_schema(items):
    """items: list of (name, absolute_url) tuples."""
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                "item": url,
            }
            for i, (name, url) in enumerate(items)
        ],
    }


def service_schema(service, region):
    data = {
        "@context": "https://schema.org",
        "@type": "MedicalProcedure",
        "name": service.name,
        "description": service.summary,
        "url": region_absolute(region["code"], "services:detail", slug=service.slug),
        "provider": {"@id": f"https://{settings.SITE_DOMAIN}/{region['code']}/#organization"},
        "areaServed": region["name"],
    }
    if service.price:
        data["offers"] = {
            "@type": "Offer",
            "price": str(service.price),
            "priceCurrency": region["currency"],
        }
    return data


def event_schema(event, region):
    data = {
        "@context": "https://schema.org",
        "@type": "Event",
        "name": event.title,
        "description": event.summary,
        "startDate": event.start.isoformat(),
        "eventStatus": "https://schema.org/EventScheduled",
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "url": region_absolute(region["code"], "events:detail", slug=event.slug),
        "location": {
            "@type": "Place",
            "name": event.location,
            "address": region["address"],
        },
        "organizer": {
            "@type": "Organization",
            "name": settings.BRAND_NAME,
            "url": f"https://{settings.SITE_DOMAIN}/{region['code']}/",
        },
    }
    if event.end:
        data["endDate"] = event.end.isoformat()
    data["offers"] = {
        "@type": "Offer",
        "price": str(event.price),
        "priceCurrency": region["currency"],
        "availability": "https://schema.org/InStock"
        if not event.is_sold_out
        else "https://schema.org/SoldOut",
        "url": region_absolute(region["code"], "events:detail", slug=event.slug),
    }
    return data


def faq_schema(faqs):
    if not faqs:
        return None
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": faq.question,
                "acceptedAnswer": {"@type": "Answer", "text": faq.answer},
            }
            for faq in faqs
        ],
    }
