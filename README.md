# Stem Cell — Multi-Region Website (UAE live, USA ready)

A professional, SEO/AEO/GEO-optimised, server-rendered website for a stem cell &
regenerative medicine clinic. Built with **Python + Django**. The UAE region is
live now; the USA region plugs in later with no code changes.

## Highlights

- **Multi-region** from one codebase — `/uae/` is live, `/us/` is reserved.
  Visitors are auto-routed to the right region; each region has its own
  currency, contact details, canonical URLs and `hreflang` targeting.
- **SEO / AEO / GEO built-in** — per-page titles & meta, canonical + hreflang,
  Open Graph & Twitter cards, JSON-LD structured data (Organization /
  MedicalBusiness, Service, Event, FAQPage, BreadcrumbList, WebSite), an XML
  sitemap, `robots.txt` (welcomes GPTBot, PerplexityBot, ClaudeBot, etc.) and an
  `llms.txt` manifest for answer engines.
- **Server-side rendered** — full content in the HTML, so search engines and
  LLMs read everything and there are no client-render issues.
- **Stripe payments** — region-aware currency (AED / USD), Checkout + webhook.
- **Admin-managed content** — services, events, FAQs and leads are all editable
  from the Django admin (no coding needed).
- **Deploy-ready** — WhiteNoise static files, gunicorn, `render.yaml`, `Procfile`.

## Quick start (local)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env            # then edit values
python manage.py migrate
python manage.py seed_demo      # loads UAE demo content
python manage.py createsuperuser
python manage.py runserver
```

Open <http://127.0.0.1:8000/> — you'll be redirected to `/uae/`.
Admin: <http://127.0.0.1:8000/admin/>

## Going live

1. Set environment variables (see `.env.example`): `SECRET_KEY`, `DEBUG=False`,
   `ALLOWED_HOSTS`, `SITE_DOMAIN`, `BRAND_NAME`, and Stripe keys.
2. Deploy. On **Render**, the included `render.yaml` provisions the web service
   and a PostgreSQL database automatically.
3. Add your Stripe webhook endpoint: `https://yourbrand.com/stripe/webhook/`.

## Enabling the USA site later

Set `US_ENABLED=True` (env var) — the `/us/` region, sitemap entries, hreflang
alternates and region switcher all activate automatically. Then add US-region
content in the admin.

## Project structure

```
config/        Django project (settings, urls, wsgi)
core/          Regions, middleware, SEO helpers, home/about/contact, sitemaps
services/      Stem cell services (model, views, templates)
events/        Events + registrations (Stripe-enabled)
payments/      Stripe checkout, success/cancel, webhook
templates/     Server-rendered HTML (base + partials + pages)
static/        CSS design system + images
```

> Medical disclaimer: site content is for educational purposes and is not a
> substitute for professional medical advice.
