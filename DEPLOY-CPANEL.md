# Deploying Brockwell Healthcare to cPanel

This Django site runs on cPanel using the built-in **Setup Python App**
feature (Phusion Passenger). Static files are served by WhiteNoise, so no
extra Apache config is needed.

> **Prerequisite:** your hosting's cPanel must have **"Setup Python App"**
> (cPanel → *Software* section) with **Python 3.10 or 3.11** available.
> Most CloudLinux / LiteSpeed hosts have this. If your host only offers
> Python 3.9 or has no Python App tool, tell your developer — the site can
> be pinned to Django 4.2 for 3.9, or hosted on Render instead.

---

## Step 1 — Create the Python App
1. cPanel → **Setup Python App** → **Create Application**.
2. **Python version:** 3.11 (or 3.10).
3. **Application root:** e.g. `brockwell` (a folder in your home dir).
4. **Application URL:** select your domain `brockwellhealthcare.com` (or a subdomain to test first, e.g. `staging.brockwellhealthcare.com`).
5. **Application startup file:** `passenger_wsgi.py`
6. **Application Entry point:** `application`
7. Click **Create**. cPanel makes a virtual environment and shows a command like:
   `source /home/USER/virtualenv/brockwell/3.11/bin/activate && cd /home/USER/brockwell`
   — **copy that line**, you'll need it in Step 4.

## Step 2 — Put the code in the Application root
**Option A — Git (recommended):** cPanel → **Git Version Control** →
*Create* → Clone URL `https://github.com/Shakeeb871/brockwellhealthcare.git`
into your Application root folder. (For private repos use a deploy token.)

**Option B — File Manager:** download the repo as a ZIP from GitHub
(*Code → Download ZIP*), upload it into the Application root via cPanel
**File Manager**, and **Extract**. Make sure the files (manage.py,
passenger_wsgi.py, config/, …) sit **directly** in the Application root,
not inside a sub-folder.

## Step 3 — passenger_wsgi.py
Already included in this repo at the project root — no action needed. (If
cPanel created its own placeholder `passenger_wsgi.py`, let this repo's
version overwrite it.)

## Step 4 — Environment variables (the `.env` file)
In **File Manager**, inside the Application root, create a file named
**`.env`** with these values (edit to your real values):

```
SECRET_KEY=paste-a-long-random-string-here
DEBUG=False
ALLOWED_HOSTS=brockwellhealthcare.com,www.brockwellhealthcare.com
SITE_DOMAIN=brockwellhealthcare.com
CSRF_TRUSTED_ORIGINS=https://brockwellhealthcare.com,https://www.brockwellhealthcare.com
TIME_ZONE=Asia/Dubai

BRAND_NAME=Brockwell Healthcare
UAE_PHONE=+971 50 193 1763
UAE_EMAIL=info@brockwellhealthcare.com
UAE_ADDRESS=Dubai, United Arab Emirates

# Stripe — add later when ready (leave blank for now)
STRIPE_PUBLISHABLE_KEY=
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
```

> Tip for `SECRET_KEY`: use any long random mix of 50+ letters/numbers.
> (You can also set these as **Environment variables** in the Setup Python
> App screen instead of a `.env` file — either works.)

## Step 5 — Install & set up (Terminal)
Open cPanel → **Terminal** (or SSH). Paste the **activate** command from
Step 1, then run:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py seed_demo          # loads the demo content (optional)
python manage.py createsuperuser    # create your admin login
```

> No Terminal access? Use **Setup Python App → Execute python script** /
> the pip + "Run" buttons in that screen to run `migrate` and
> `collectstatic`. Ask your host to enable Terminal if needed.

## Step 6 — Restart
cPanel → **Setup Python App** → your app → **Restart**.
Visit **https://brockwellhealthcare.com/** — it should load and redirect to
`/uae/`. Admin panel: **/admin/**.

---

## Database
- **Default = SQLite** — works out of the box, no setup, good for launch and
  light traffic. The `db.sqlite3` file lives in the Application root.
- **MySQL (optional, for scale):** create a MySQL DB + user in cPanel, then
  add to `.env`:
  `DATABASE_URL=mysql://DBUSER:DBPASS@localhost/DBNAME`
  and tell your developer to add a MySQL driver (`mysqlclient`) to
  requirements. Then re-run `migrate`.

## Static files
Handled automatically by WhiteNoise after `collectstatic` — no Apache rules
needed. Re-run `collectstatic` and **Restart** whenever CSS/images change.

## Auto-deploy (Cron — no terminal needed)
Make the live site pull the latest code from GitHub automatically. In cPanel →
**Cron Jobs**, add a job (e.g. every 10 minutes: `*/10 * * * *`) with this
command (paths shown for user `carpente`, app `brockwellhealthcare`, Python
3.11 — adjust if different):

```
( cd /home/carpente/brockwellhealthcare && git fetch -q origin main && git reset -q --hard origin/main && /home/carpente/virtualenv/brockwellhealthcare/3.11/bin/python manage.py migrate --noinput && /home/carpente/virtualenv/brockwellhealthcare/3.11/bin/python manage.py collectstatic --noinput && mkdir -p tmp && touch tmp/restart.txt ) >> /home/carpente/deploy.log 2>&1
```

It force-syncs the working tree to `origin/main` (so it never hits merge
conflicts), runs migrations + collectstatic, and restarts Passenger by
touching `tmp/restart.txt`. `.env`, `db.sqlite3`, `staticfiles/` and `media/`
are git-ignored, so they are never touched. Progress/errors are logged to
`~/deploy.log`. Content edited in the admin is live instantly and is
unaffected by deploys.

## Updating the site later
```bash
# in the Application root, with the venv activated:
git pull origin main          # (if you used Git)
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
# then Restart the app in Setup Python App
```

## Troubleshooting
- **500 error / "Internal Server Error":** check the app's `stderr.log`
  (Application root) — usually a missing env var or a dependency not
  installed. Confirm `pip install -r requirements.txt` ran in the venv.
- **CSS missing / unstyled page:** run `collectstatic` and Restart.
- **"DisallowedHost" / 400:** add your exact domain to `ALLOWED_HOSTS` in `.env`.
- **Static 404s:** ensure `DEBUG=False` and `collectstatic` was run.
- **Python version error installing Django 5:** your host's Python is < 3.10;
  ask your developer to pin Django 4.2.

## Pointing the domain
`brockwellhealthcare.com` must point (DNS A record / nameservers) to this
cPanel server, and the domain must be added in cPanel (Domains). If the
domain currently shows another site, deploying here will replace it once DNS
resolves to this server.
