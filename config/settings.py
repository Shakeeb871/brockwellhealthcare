"""
Django settings for the Stem Cell multi-region website.

Production-ready, environment-driven configuration. All secrets and
environment-specific values are read from environment variables so the
same codebase runs safely in local development and in production
(e.g. Render, Railway, any WSGI host) with zero code changes.
"""

from pathlib import Path
import os

import dj_database_url
from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Load variables from a local .env file when present (development).
load_dotenv(BASE_DIR / ".env")


def env_bool(key: str, default: bool = False) -> bool:
    return os.getenv(key, str(default)).strip().lower() in {"1", "true", "yes", "on"}


def env_list(key: str, default: str = "") -> list[str]:
    raw = os.getenv(key, default)
    return [item.strip() for item in raw.split(",") if item.strip()]


# --------------------------------------------------------------------------- #
# Core security
# --------------------------------------------------------------------------- #
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-dev-only-key-change-me-in-production-0000000000",
)

DEBUG = env_bool("DEBUG", True)

# Hosts. In production set ALLOWED_HOSTS="yourbrand.com,www.yourbrand.com".
ALLOWED_HOSTS = env_list("ALLOWED_HOSTS", "localhost,127.0.0.1,0.0.0.0")

# Render and most PaaS hosts inject the external hostname automatically.
RENDER_EXTERNAL_HOSTNAME = os.getenv("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

CSRF_TRUSTED_ORIGINS = env_list("CSRF_TRUSTED_ORIGINS")
if RENDER_EXTERNAL_HOSTNAME:
    CSRF_TRUSTED_ORIGINS.append(f"https://{RENDER_EXTERNAL_HOSTNAME}")


# --------------------------------------------------------------------------- #
# Applications
# --------------------------------------------------------------------------- #
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    # Third-party
    "adminsortable2",
    "tinymce",
    # Local apps
    "core",
    "services",
    "events",
    "payments",
    "team",
    "blog",
]

# Rich-text editor (TinyMCE) used in the admin for long-form content fields.
TINYMCE_DEFAULT_CONFIG = {
    "license_key": "gpl",
    "height": 480,
    "menubar": "edit view insert format tools table",
    "plugins": (
        "advlist autolink lists link image charmap preview anchor "
        "searchreplace visualblocks code fullscreen insertdatetime "
        "media table help wordcount"
    ),
    "toolbar": (
        "undo redo | blocks | bold italic underline forecolor | "
        "alignleft aligncenter alignright alignjustify | "
        "bullist numlist outdent indent | link image media table | "
        "removeformat code fullscreen preview | help"
    ),
    "block_formats": (
        "Paragraph=p; Heading 2=h2; Heading 3=h3; Heading 4=h4; "
        "Quote=blockquote; Preformatted=pre"
    ),
    "branding": False,
    "promotion": False,
    "convert_urls": False,
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # WhiteNoise serves compressed static files efficiently in production.
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Defence-in-depth response headers (CSP, Permissions-Policy, COOP, …).
    "core.middleware.SecurityHeadersMiddleware",
    # Detects the active region (UAE/US) for every request.
    "core.middleware.RegionMiddleware",
    # Adds X-Robots-Tag: noindex on every response while SITE_NOINDEX is on.
    "core.middleware.NoIndexMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Exposes brand + region + SEO defaults to every template.
                "core.context_processors.site_context",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# --------------------------------------------------------------------------- #
# Database
# --------------------------------------------------------------------------- #
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        conn_health_checks=True,
    )
}


# --------------------------------------------------------------------------- #
# Password validation
# --------------------------------------------------------------------------- #
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# --------------------------------------------------------------------------- #
# Internationalization
# --------------------------------------------------------------------------- #
LANGUAGE_CODE = "en"
TIME_ZONE = os.getenv("TIME_ZONE", "Asia/Dubai")
USE_I18N = True
USE_TZ = True


# --------------------------------------------------------------------------- #
# Static & media files (WhiteNoise compressed, hashed)
# --------------------------------------------------------------------------- #
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# --------------------------------------------------------------------------- #
# Production security hardening (only active when DEBUG is off)
# --------------------------------------------------------------------------- #
if not DEBUG:
    SECURE_SSL_REDIRECT = env_bool("SECURE_SSL_REDIRECT", True)
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
    X_FRAME_OPTIONS = "DENY"
    SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin"
    # Cookies not readable by JavaScript and not sent on cross-site requests.
    SESSION_COOKIE_HTTPONLY = True
    CSRF_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    CSRF_COOKIE_SAMESITE = "Lax"

    # Fail closed: never boot production on the shipped development SECRET_KEY.
    if SECRET_KEY.startswith("django-insecure-"):
        raise ImproperlyConfigured(
            "SECRET_KEY is unset in production — set a strong SECRET_KEY env var."
        )


# --------------------------------------------------------------------------- #
# Brand / Site configuration
#   Change BRAND_NAME (and friends) here or via environment variables.
#   These flow into every page's titles, footer, and SEO structured data.
# --------------------------------------------------------------------------- #
BRAND_NAME = os.getenv("BRAND_NAME", "Brockwell Healthcare")
BRAND_TAGLINE = os.getenv(
    "BRAND_TAGLINE", "Advanced Regenerative & Stem Cell Therapies"
)
SITE_DOMAIN = os.getenv("SITE_DOMAIN", "brockwellhealthcare.com")
# Pre-rendered 1200x630 JPEG so link previews actually render. SVG is unsupported by
# social/chat crawlers, and webp is unreliable for link previews (WhatsApp/Facebook),
# so the shared og:image cards under img/og/ are JPEG.
DEFAULT_OG_IMAGE = "img/og/default.jpg"

# Social media profiles (shown in the header). Override any via .env; leave a
# value blank to hide that icon.
SOCIAL_LINKS = [
    {"name": "Facebook", "icon": "facebook",
     "url": os.getenv("SOCIAL_FACEBOOK", "https://www.facebook.com/profile.php?id=61572848905268")},
    {"name": "Instagram", "icon": "instagram",
     "url": os.getenv("SOCIAL_INSTAGRAM", "https://www.instagram.com/brockwellhealthcare")},
    {"name": "YouTube", "icon": "youtube",
     "url": os.getenv("SOCIAL_YOUTUBE", "https://www.youtube.com/@Brockwellhealthcare")},
    {"name": "TikTok", "icon": "tiktok",
     "url": os.getenv("SOCIAL_TIKTOK", "https://www.tiktok.com/@brockwellhealthcare")},
    {"name": "LinkedIn", "icon": "linkedin",
     "url": os.getenv("SOCIAL_LINKEDIN", "https://www.linkedin.com/company/brockwell-healthcare")},
]

# Google rating shown on the home page. AggregateRating schema is only emitted
# when GOOGLE_REVIEW_COUNT is set (> 0) so we never publish an unverifiable
# review count. Set it to your real Google review count to enable the markup.
GOOGLE_RATING_VALUE = os.getenv("GOOGLE_RATING_VALUE", "4.91")
GOOGLE_REVIEW_COUNT = int(os.getenv("GOOGLE_REVIEW_COUNT", "0") or 0)

# Site-wide search-engine indexing switch.
#   True  -> the whole site is de-indexed: every page sends `noindex` via a
#            <meta> tag AND an X-Robots-Tag response header. robots.txt still
#            allows crawling (so engines can see the noindex and drop pages)
#            but withholds the sitemap.
#   False -> normal indexing resumes.
# Flip this by setting SITE_NOINDEX=False in the environment (.env) when ready
# to go live in search engines. Currently defaults to de-indexed.
SITE_NOINDEX = env_bool("SITE_NOINDEX", True)

# Region configuration. The bare domain opens on the US site by default; UAE
# visitors are routed to /uae/ (by geo-detection), and /uae/ is always reachable
# directly. Change DEFAULT_REGION to flip which region the root serves.
DEFAULT_REGION = "us"
REGIONS = {
    "uae": {
        "code": "uae",
        "name": "United Arab Emirates",
        "short": "UAE",
        "city": "Dubai",
        # Location phrasing used in shared templates (region-neutral wording keeps
        # the US pages location-light with a single country mention).
        "in_loc": " in Dubai",
        "h1_loc": "in Dubai",
        "across": "across the UAE",
        "area": "the UAE",
        "dot_city": " · Dubai",
        "enabled": True,
        "currency": "AED",
        "currency_symbol": "AED",
        "stripe_currency": "aed",
        "locale": "en-AE",
        "phone": os.getenv("UAE_PHONE", "+971 50 193 1763"),
        "email": os.getenv("UAE_EMAIL", "info@brockwellhealthcare.com"),
        "address": os.getenv("UAE_ADDRESS", "Dubai, United Arab Emirates"),
    },
    "us": {
        "code": "us",
        "name": "United States",
        "short": "USA",
        "city": "Philadelphia",
        # US pages stay location-light: no city in body copy, country mentioned
        # sparingly (only the home/hero H1 via ``h1_loc``).
        "in_loc": "",
        "h1_loc": "in the USA",
        "across": "nationwide",
        "area": "the US",
        "dot_city": "",
        "enabled": env_bool("US_ENABLED", True),
        "currency": "USD",
        "currency_symbol": "$",
        "stripe_currency": "usd",
        "locale": "en-US",
        "phone": os.getenv("US_PHONE", "+1 (262) 302-1216"),
        "email": os.getenv("US_EMAIL", "info@brockwellhealthcare.com"),
        "address": os.getenv("US_ADDRESS", "Philadelphia, PA, United States"),
    },
}


# --------------------------------------------------------------------------- #
# Stripe (test keys by default; set live keys via environment in production)
# --------------------------------------------------------------------------- #
STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY", "")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "")

# Where booking/payment notifications are sent (the clinic's admin inbox).
EVENT_NOTIFY_EMAIL = os.getenv("EVENT_NOTIFY_EMAIL", "info@brockwellhealthcare.com")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "Brockwell Healthcare <info@brockwellhealthcare.com>")
SERVER_EMAIL = os.getenv("SERVER_EMAIL", DEFAULT_FROM_EMAIL)

# Email delivery. Set EMAIL_HOST (+ user/password) via environment to send for
# real over SMTP; without it we fall back to the console backend so nothing
# crashes and messages are logged during development.
EMAIL_HOST = os.getenv("EMAIL_HOST", "")
if EMAIL_HOST:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
    EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "1") == "1"
    EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL", "0") == "1"
    EMAIL_TIMEOUT = int(os.getenv("EMAIL_TIMEOUT", "20"))
else:
    EMAIL_BACKEND = os.getenv(
        "EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend"
    )


# --------------------------------------------------------------------------- #
# Logging — surface errors clearly, never leak them to visitors.
# --------------------------------------------------------------------------- #
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": os.getenv("LOG_LEVEL", "INFO")},
}
