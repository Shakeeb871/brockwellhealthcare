"""IndexNow protocol client.

IndexNow (https://www.indexnow.org/) lets us tell Bing, Yandex, Seznam and
Naver about new/changed URLs the moment they're published — no waiting for
those engines to re-crawl. Google does NOT support it directly but reads Bing
signals, and the other engines together are a meaningful traffic source.

The site publishes a verification key at ``/<key>.txt`` and pings the shared
IndexNow endpoint whenever content is saved. Set ``INDEXNOW_KEY`` in the
environment to enable it; without a key we no-op silently.
"""

from __future__ import annotations

import json
import logging
import urllib.request
from typing import Iterable

from django.conf import settings

log = logging.getLogger(__name__)

ENDPOINT = "https://api.indexnow.org/IndexNow"


def _key() -> str:
    return getattr(settings, "INDEXNOW_KEY", "") or ""


def is_enabled() -> bool:
    """Only ping when we have a key AND indexing itself is on for something."""
    return bool(_key() and not getattr(settings, "SITE_NOINDEX", True))


def submit(urls: Iterable[str]) -> tuple[int, str]:
    """Submit up to 10,000 URLs in one call. Returns (status, body). No-op if
    IndexNow isn't configured or the site is de-indexed."""
    if not is_enabled():
        return 0, "disabled"
    urls = [u for u in urls if u]
    if not urls:
        return 0, "no urls"

    payload = json.dumps({
        "host": settings.SITE_DOMAIN,
        "key": _key(),
        "keyLocation": f"https://{settings.SITE_DOMAIN}/{_key()}.txt",
        "urlList": list(urls)[:10000],
    }).encode()

    req = urllib.request.Request(
        ENDPOINT,
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            body = r.read().decode("utf-8", "ignore")
            log.info("IndexNow: %s -> %s", r.status, body[:120])
            return r.status, body
    except Exception as exc:                 # never let a ping break a save
        log.warning("IndexNow submit failed: %s", exc)
        return 0, str(exc)


def submit_one(url: str) -> tuple[int, str]:
    return submit([url])
