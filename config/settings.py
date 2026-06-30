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
    # Local apps
    "core",
    "services",
    "events",
    "payments",
]

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
    # Detects the active region (UAE/US) for every request.
    "core.middleware.RegionMiddleware",
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


# --------------------------------------------------------------------------- #
# Brand / Site configuration
#   Change BRAND_NAME (and friends) here or via environment variables.
#   These flow into every page's titles, footer, and SEO structured data.
# --------------------------------------------------------------------------- #
BRAND_NAME = os.getenv("BRAND_NAME", "Brockwell Healthcare")
BRAND_TAGLINE = os.getenv(
    "BRAND_TAGLINE", "Advanced Regenerative & Stem Cell Therapies"
)
SITE_DOMAIN = os.getenv("SITE_DOMAIN", "yourbrand.com")
DEFAULT_OG_IMAGE = "img/og-default.svg"

# Region configuration. UAE is live now; US is reserved and plugs in later
# by simply flipping ``enabled`` to True (no code changes required).
DEFAULT_REGION = "uae"
REGIONS = {
    "uae": {
        "code": "uae",
        "name": "United Arab Emirates",
        "short": "UAE",
        "enabled": True,
        "currency": "AED",
        "currency_symbol": "AED",
        "stripe_currency": "aed",
        "locale": "en-AE",
        "phone": os.getenv("UAE_PHONE", "+971 4 000 0000"),
        "email": os.getenv("UAE_EMAIL", "hello@yourbrand.com"),
        "address": os.getenv(
            "UAE_ADDRESS", "Dubai Healthcare City, Dubai, United Arab Emirates"
        ),
    },
    "us": {
        "code": "us",
        "name": "United States",
        "short": "USA",
        "enabled": env_bool("US_ENABLED", False),
        "currency": "USD",
        "currency_symbol": "$",
        "stripe_currency": "usd",
        "locale": "en-US",
        "phone": os.getenv("US_PHONE", "+1 000 000 0000"),
        "email": os.getenv("US_EMAIL", "hello@yourbrand.com"),
        "address": os.getenv("US_ADDRESS", "United States"),
    },
}


# --------------------------------------------------------------------------- #
# Stripe (test keys by default; set live keys via environment in production)
# --------------------------------------------------------------------------- #
STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY", "")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "")


# --------------------------------------------------------------------------- #
# Logging — surface errors clearly, never leak them to visitors.
# --------------------------------------------------------------------------- #
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": os.getenv("LOG_LEVEL", "INFO")},
}
