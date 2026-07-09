# Region-specific images

Images are resolved **region-aware with fallback**:

1. First the site looks for the current region's own file under
   `static/img/<region>/…`  (e.g. `static/img/us/…`, `static/img/uae/…`)
2. If that is missing, it falls back to the **shared** file under `static/img/…`

So you only need to place an image in a region folder when that region should
look *different*. Everything else stays shared automatically — no duplication.

## Structure (mirror the shared layout inside each region folder)

```
static/img/
├── <shared files>                         ← used by every region unless overridden
├── us/                                     ← USA-only overrides
│   ├── services/<slug>-hero.webp
│   ├── services/<slug>-content.webp
│   ├── services/<slug>-card.webp
│   ├── services/categories/<cat>.webp
│   ├── services/categories/<cat>/hero.webp
│   ├── services/categories/<cat>/<section>.webp
│   ├── og/svc-<slug>.jpg   og/cat-<cat>.jpg   og/default.jpg   og/about.jpg
│   ├── doctors/<name>.jpg
│   └── brockwell-healthcare.webp  (home hero) …
└── uae/                                    ← UAE-only overrides (same layout)
```

Example: to give the US "Male Wellness" page its own hero, drop
`static/img/us/services/male-wellness-hero.webp`. The UAE keeps the shared one.
