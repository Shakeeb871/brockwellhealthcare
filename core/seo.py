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

from .regions import enabled_regions, region_absolute, region_path, region_prefix


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
    canonical = absolute(f"{region_prefix(region_code)}{path}")

    # hreflang alternates: one per enabled region + an x-default.
    alternates = []
    for region in enabled_regions():
        alternates.append(
            {
                "hreflang": region["locale"],
                "href": absolute(f"{region_prefix(region['code'])}{path}"),
            }
        )
    alternates.append(
        {"hreflang": "x-default",
         "href": absolute(f"{region_prefix(settings.DEFAULT_REGION)}{path}")}
    )

    brand = settings.BRAND_NAME
    full_title = title if brand in title else f"{title} | {brand}"

    # ``image`` may be: a media/absolute URL (starts with "/" or "http", e.g. an
    # uploaded blog/event image) used as-is, a static-relative path prefixed with
    # STATIC_URL, or None → the brand default. Always emitted as an absolute URL so
    # link previews (WhatsApp, Facebook, X, LinkedIn) resolve it.
    if image and (image.startswith("http") or image.startswith("/")):
        og_image = image
    else:
        og_image = settings.STATIC_URL + (image or settings.DEFAULT_OG_IMAGE)

    return {
        "title": full_title,
        "description": description,
        "canonical": canonical,
        "robots": robots,
        "og_type": og_type,
        "image": absolute(og_image),
        # Dimensions/type of the standard 1200x630 JPEG cards. Views that override
        # ``image`` with an uploaded media file (blog/events) also override these.
        "image_w": 1200,
        "image_h": 630,
        "image_type": "image/jpeg",
        "alternates": alternates,
    }


# --------------------------------------------------------------------------- #
# JSON-LD schema builders
# --------------------------------------------------------------------------- #
def _postal_address(region):
    """Build a PostalAddress. Uses split street/locality/region/postal fields
    when a region provides them (better local SEO), otherwise falls back to the
    single free-text address string."""
    addr = {"@type": "PostalAddress", "addressCountry": region["short"]}
    if region.get("street"):
        addr["streetAddress"] = region["street"]
        if region.get("locality"):
            addr["addressLocality"] = region["locality"]
        if region.get("state"):
            addr["addressRegion"] = region["state"]
        if region.get("postal"):
            addr["postalCode"] = region["postal"]
    else:
        addr["streetAddress"] = region["address"]
    return addr


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
        # `medicalSpecialty` only accepts schema.org's fixed MedicalSpecialty
        # enumeration (no "RegenerativeMedicine" member), so the clinic's focus is
        # expressed with `knowsAbout`, which accepts free text and validates cleanly.
        "knowsAbout": [
            "Regenerative Medicine",
            "Stem Cell Therapy",
            "Longevity Medicine",
            "Functional Medicine",
            "Chronic Pain Management",
        ],
        "areaServed": region["name"],
        "address": _postal_address(region),
        "priceRange": "$$$",
    }


EMIRATES = [
    "Dubai", "Abu Dhabi", "Sharjah", "Ajman",
    "Ras Al Khaimah", "Fujairah", "Umm Al Quwain",
]


def medical_clinic_schema(region):
    """Richer home-page organization node: MedicalClinic with logo, social
    profiles, the emirates served and (optionally) an AggregateRating."""
    from django.templatetags.static import static

    org = organization_schema(region)
    org["@type"] = ["MedicalBusiness", "MedicalClinic"]
    org["logo"] = absolute(static("img/brockwell-healthcare-logo.png"))
    org["image"] = absolute(static("img/brockwell-healthcare.webp"))
    org["sameAs"] = [s["url"] for s in settings.SOCIAL_LINKS if s.get("url")]
    # The emirate list only makes sense for the UAE clinic; other regions serve
    # their own country.
    if region["code"] == "uae":
        org["areaServed"] = [{"@type": "AdministrativeArea", "name": e} for e in EMIRATES]
    else:
        org["areaServed"] = {"@type": "Country", "name": region["short"]}
    # Only publish a rating if a real, verifiable review count is configured.
    if getattr(settings, "GOOGLE_REVIEW_COUNT", 0):
        org["aggregateRating"] = {
            "@type": "AggregateRating",
            "ratingValue": settings.GOOGLE_RATING_VALUE,
            "bestRating": "5",
            "ratingCount": settings.GOOGLE_REVIEW_COUNT,
        }
    return org


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


def category_schema(category, region):
    """A main service area — MedicalSpecialty/CollectionPage entry point."""
    return {
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "name": category.name,
        "description": category.summary,
        "url": region_absolute(region["code"], "services:category", category=category.slug),
        "about": {"@type": "MedicalSpecialty", "name": category.name},
        "provider": {"@id": f"https://{settings.SITE_DOMAIN}/{region['code']}/#organization"},
    }


def service_schema(service, region):
    data = {
        "@context": "https://schema.org",
        "@type": "MedicalProcedure",
        "name": service.name,
        "description": service.summary,
        "url": region_absolute(
            region["code"], "services:detail",
            category=service.category.slug, slug=service.slug,
        ),
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


def doctor_schema(doctor, region):
    # An individual doctor is a Person (schema.org's `Physician` is an
    # organization type, so `jobTitle`/`worksFor` warn on it). `hasOccupation`
    # keeps the physician signal without any invalid property.
    data = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": doctor.name,
        "description": doctor.short_bio,
        "url": region_absolute(region["code"], "team:detail", slug=doctor.slug),
        "jobTitle": doctor.title,
        "worksFor": {"@id": f"https://{settings.SITE_DOMAIN}/{region['code']}/#organization"},
        "hasOccupation": {"@type": "Occupation", "name": "Physician"},
    }
    if doctor.photo:
        data["image"] = doctor.photo
    if doctor.specialty_list:
        data["knowsAbout"] = doctor.specialty_list
    return data


def page_schema(page, region):
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": page.title,
        "url": absolute(f"/{region['code']}/{page.slug}/"),
        "publisher": {"@id": f"https://{settings.SITE_DOMAIN}/{region['code']}/#organization"},
    }


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
        "availability": "https://schema.org/InStock",
        "url": region_absolute(region["code"], "events:detail", slug=event.slug),
    }
    return data


def article_schema(post, region):
    if post.image:
        images = [absolute(post.image.url)]
    else:
        images = [absolute(settings.STATIC_URL + settings.DEFAULT_OG_IMAGE)]
    return {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": post.title,
        "description": post.excerpt,
        "image": images,
        "datePublished": post.published_at.isoformat(),
        "dateModified": post.updated_at.isoformat(),
        "author": {"@type": "Organization", "name": post.author},
        "publisher": {
            "@type": "Organization",
            "name": settings.BRAND_NAME,
            "url": f"https://{settings.SITE_DOMAIN}/{region['code']}/",
        },
        "mainEntityOfPage": region_absolute(region["code"], "blog:entry", slug=post.slug),
        "articleSection": post.category.name if post.category_id else "Insights",
    }


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
