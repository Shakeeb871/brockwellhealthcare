# Brockwell Healthcare — working notes

Django 5 multi-region, multi-location clinic site. Python 3.11, SQLite (switchable
to Postgres/MySQL via `DATABASE_URL`), Django templates + vanilla CSS/JS (no
frontend framework), WhiteNoise, Stripe, deployed on cPanel/Passenger.

## Standing rules

**1. Everything country-scoped must be per-country. Always.**
This site serves multiple countries and will serve many more, each with many
locations. Anything that varies by market gets its own per-country version by
default — never one blended artefact, and never ask whether it should be:

- Technical SEO files: sitemaps (`/sitemap-<country>.xml` index + per-section
  `/sitemap-<country>-<section>.xml`), `llms.txt` (`/uae/llms.txt`), canonical,
  hreflang, JSON-LD.
- Content, addresses, phone numbers, currency, opening hours, doctors, locations.
- Indexing rules (`SEO_INDEX_REGIONS`), analytics, structured data.

`robots.txt` is the one exception the standard forces: it is a per-HOST file, so
there is a single one — but it must list **every** country's sitemap.

**2. Nothing country-specific may be hard-coded.**
New countries/locations are added as data (settings `REGIONS`, the `Location`
model) and their pages, sitemaps and SEO artefacts must appear automatically
with no code change. Same for states — they are derived by grouping locations.

**3. Never delete, change or remove previously approved work without asking.**
Do exactly what was requested. If something looks wrong, say so — don't silently
"fix" it.

**4. No fabricated claims.** This is a medical site. Never invent partner brands,
accreditations, media features, ratings or outcomes. Placeholders get truthful
replacements, not invented ones.

## Search-engine indexing

Two settings, both from the environment (`.env`):

| Setting | Meaning |
|---|---|
| `SITE_NOINDEX` | Master kill-switch. `True` (default) = whole site de-indexed. Set `False` to go live. |
| `SEO_INDEX_REGIONS` | Which regions may be indexed. Defaults to `uae`. Use `uae,us` for both. |

A region that isn't indexable sends `noindex` via **both** a meta tag and an
`X-Robots-Tag` header, and is excluded from hreflang and every sitemap.
Crawling is always allowed (a `noindex` only works if the page can be fetched).

Check the live state at any time:

    bash ~/brockwellhealthcare/manage.sh seostatus   # on the server
    python manage.py seostatus                       # locally

## Technical SEO endpoints

    /robots.txt                       host-level; lists every country's sitemap
    /sitemap.xml                      master index (all populated sections)
    /sitemap-<country>.xml            per-country index (submit per market in GSC)
    /sitemap-<country>-<section>.xml  main | services | events | blog | team | locations
    /llms.txt, /<country>/llms.txt    per-country LLM manifest (GEO)

## Deploying

    bash ~/brockwellhealthcare/deploy.sh

Pulls, installs, migrates, **collectstatic**, restarts, then prints `seostatus`.
CSS/JS/image changes do **not** go live without `collectstatic` — the site uses
hashed static filenames (`CompressedManifestStaticFilesStorage`).

`.env`, `db.sqlite3` and `media/` are gitignored, so deploys never touch them.

## Apps

`core` (home/about/contact, SEO, regions) · `services` · `events` · `team` ·
`blog` · `locations` (clinics) · `payments` (Stripe) · `clinic` (patient &
clinic management backend: patients, appointments, encounters, invoices)

## Conventions

- Region-aware URLs in templates: `{% rurl 'app:name' %}` (not `{% url %}`).
- Region-aware images: `{% region_img %}` / `region_asset_rel` — per-region
  overrides live in `static/img/<code>/` and fall back to the shared file.
- Site buttons are square (`border-radius: 0`) — don't add pill radii.
- Forms post via AJAX (`data-ajax`) and show toasts; no page reload.
