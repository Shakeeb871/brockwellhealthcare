# Getting pages indexed — setup & operating guide

This site has a built-in indexing pusher: **Core → Index submissions → “+ Submit
URLs for indexing”** in the admin. It sends URLs to

| Target | What it does | Limit |
|---|---|---|
| **Google Indexing API** | Puts the URL straight into Google’s crawl queue. Normally crawled within minutes. This is the same mechanism paid “instant indexer” services use. | 200 URLs/day |
| **IndexNow** | Instant push to Bing, Yandex, Seznam, Naver. Google also picks up discovery signals from Bing’s crawl. | unlimited |

**Set expectations honestly:** these APIs guarantee *crawling*, not *indexing*.
Google decides whether to keep a page. No tool or paid service can override
that — they all call the same API. What they can do (and what this does) is
remove the discovery delay, which on a new domain is the biggest bottleneck.

---

## 1. Google Indexing API — one-time setup (~10 minutes)

1. **Create a project** — <https://console.cloud.google.com/projectcreate>
2. **Enable the API** — APIs & Services → *Library* → search **Indexing API** →
   **Enable**.
3. **Create a service account** — APIs & Services → *Credentials* →
   **Create credentials** → **Service account** → give it any name → Done.
4. **Download a key** — open the service account → **Keys** tab →
   *Add key* → *Create new key* → **JSON** → it downloads a `.json` file.
5. **Grant it ownership in Search Console** — this step is the one people miss:
   - <https://search.google.com/search-console> → your property
   - *Settings* → **Users and permissions** → **Add user**
   - Paste the service account’s `client_email` (looks like
     `something@your-project.iam.gserviceaccount.com`, it’s inside the JSON)
   - Permission: **Owner** (not Full — it must be Owner)

   Without this you get `Permission denied. Failed to verify the URL ownership.`
6. **Upload the key to cPanel** — see the walkthrough below.

### Uploading the JSON in cPanel (step by step)

The file must sit **outside `public_html`** so nobody can download it from the
web. The home folder is the right place.

1. Rename the downloaded file to something simple — e.g.
   **`google-indexing.json`** (Google names it something like
   `brockwell-seo-3f9a2c1b7d4e.json`).
2. cPanel → **File Manager**.
3. In the left tree click **`/home/USERNAME`** — the very top level, the folder
   that *contains* `public_html`. **Do not** open `public_html`.
4. Toolbar → **Upload** → choose the JSON → wait for 100% → click
   *Go Back to …* .
5. Confirm it's listed next to `public_html` (not inside it).
6. Note the full path — it is `/home/USERNAME/google-indexing.json` with your
   real cPanel username. (File Manager shows the current folder in the path bar
   at the top.)
7. Now edit `.env` (File Manager → your app folder → enable
   *Settings → Show Hidden Files* → right-click `.env` → **Edit**) and add:

   ```
   GOOGLE_INDEXING_CREDENTIALS=/home/USERNAME/google-indexing.json
   ```

8. **Set permissions to 600** (owner-only) — right-click the JSON →
   *Change Permissions* → untick everything for Group and World → Save.
9. Redeploy: `bash ~/brockwellhealthcare/deploy.sh`
10. Verify:

    ```bash
    python manage.py seostatus
    ```

    You want to see:

    ```
    Instant indexing
      Google Indexing API  READY   xxx@yyy.iam.gserviceaccount.com
    ```

    If it says `BROKEN (file not found)` the path in `.env` doesn't match where
    the file actually is — re-check the username and filename, both are
    case-sensitive.

**No File Manager / prefer the terminal?** Upload via SFTP to your home folder,
or paste the JSON straight into the env var instead of using a file:
`GOOGLE_INDEXING_CREDENTIALS={"type":"service_account",...}` (all on one line —
keep the `\n` sequences inside `private_key` exactly as they are).

## 2. IndexNow — one-time setup (~1 minute)

```bash
python -c "import secrets; print(secrets.token_hex(16))"
```

Put the result in `.env`:

```
INDEXNOW_KEY=<the 32-character string>
```

The site then serves the verification file automatically at
`https://brockwellhealthcare.com/<key>.txt`.

## 3. Make sure the site is actually indexable

```
SITE_NOINDEX=False
SEO_INDEX_REGIONS=uae        # add ,us when the US site should be indexed too
```

Then redeploy:

```bash
bash ~/brockwellhealthcare/deploy.sh
```

Check it took effect:

```bash
python manage.py seostatus
```

---

## Using it

### From the admin (normal way)

**Core → Index submissions → “+ Submit URLs for indexing”**

- Paste URLs, one per line. Bare paths like `/uae/services/` work too.
- Or click **Load all N sitemap URLs** / **Load first 200 (Google daily limit)**.
- Tick which targets to use, hit **Submit for indexing**.
- Every URL is logged with its engine, HTTP status and response.

### From the command line

```bash
# everything in the sitemaps (respects Google's 200/day)
python manage.py submiturls --all

# only URLs never accepted by Google before — ideal for a daily cron
python manage.py submiturls --all --new-only

# specific URLs
python manage.py submiturls /uae/services/ /uae/team/

# see the plan without sending anything
python manage.py submiturls --all --dry-run
```

### Daily cron (optional, keeps pushing new content)

cPanel → *Cron Jobs* → daily:

```
cd /home/USER/brockwellhealthcare && /home/USER/virtualenv/brockwellhealthcare/3.11/bin/python manage.py submiturls --all --new-only >> /home/USER/indexing.log 2>&1
```

---

## Also do these — they matter more than any API on a new domain

1. **Search Console → Sitemaps** → submit `https://brockwellhealthcare.com/sitemap.xml`.
2. **Search Console → URL Inspection** → paste a URL → **Request indexing**.
   Do your 10–15 most important pages (Google allows roughly 10/day). This is
   Google’s own manual push and it carries more weight than the API.
3. **Search Console → Pages** → read “Why pages aren’t indexed” after a few
   days. It tells you exactly what Google decided — *Crawled – currently not
   indexed*, *Discovered – currently not indexed*, etc. Act on what it says
   rather than guessing.
4. **Get real external links.** A brand-new domain with zero inbound links is
   the single biggest reason Google crawls slowly. Google Business Profile,
   LinkedIn company page, medical directories, professional associations,
   partner and supplier sites. Even a handful changes the crawl rate.
5. **Bing Webmaster Tools** — add the site there too and import from Search
   Console. Bing indexes new sites far faster, and IndexNow feeds it directly.

## Troubleshooting

| Response | Meaning | Fix |
|---|---|---|
| `Permission denied. Failed to verify the URL ownership.` | Service account isn’t an Owner in Search Console | Step 1.5 above |
| `Invalid grant: account not found` | Credentials JSON is wrong/stale | Re-download the key |
| `Indexing API has not been used in project … before or it is disabled` | API not enabled | Step 1.2 |
| `Quota exceeded` | Past 200 URLs today | Continue tomorrow, or use `--new-only` |
| Everything logs `skipped` | `SITE_NOINDEX=True` | Step 3 |
