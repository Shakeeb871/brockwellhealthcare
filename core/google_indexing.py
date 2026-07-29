"""Google Indexing API client — request an immediate crawl of a URL.

This is the mechanism the commercial "instant indexer" services use. It talks
to ``https://indexing.googleapis.com/v3/urlNotifications:publish``, which puts
a URL straight into Google's crawl queue instead of waiting for it to be
rediscovered. Typical effect is a crawl within seconds to minutes.

Honest caveat: the API guarantees *crawling*, not *indexing*. Google still
decides whether to index a page. Nothing can force that — any service claiming
otherwise is really selling this same crawl request.

Setup (one time, ~10 minutes — see SEO-INDEXING.md):
  1. Google Cloud console → new project → enable "Indexing API".
  2. Create a service account → add a JSON key → download it.
  3. Search Console → Settings → Users and permissions → add the service
     account's ``client_email`` as an **Owner**.
  4. Put the JSON on the server and set ``GOOGLE_INDEXING_CREDENTIALS`` to its
     path (or paste the JSON straight into that env var).

Auth is implemented directly against the OAuth2 JWT-bearer flow using the pure
Python ``rsa`` package, so there is nothing to compile on shared hosting.
"""

from __future__ import annotations

import base64
import json
import logging
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Iterable

from django.conf import settings

log = logging.getLogger(__name__)

TOKEN_URI = "https://oauth2.googleapis.com/token"
PUBLISH_URI = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPE = "https://www.googleapis.com/auth/indexing"

# Google's documented per-project quota for the Indexing API.
DAILY_QUOTA = 200

_token_cache: dict[str, tuple[str, float]] = {}


# --------------------------------------------------------------------------- #
# Credentials
# --------------------------------------------------------------------------- #
def _load_credentials() -> dict | None:
    """Service-account dict from ``GOOGLE_INDEXING_CREDENTIALS``.

    Accepts either a path to the JSON key file or the raw JSON itself, so it
    works with a file on disk or a single env var.
    """
    raw = (getattr(settings, "GOOGLE_INDEXING_CREDENTIALS", "") or "").strip()
    if not raw:
        return None
    try:
        if raw.startswith("{"):
            data = json.loads(raw)
        else:
            with open(raw, "r", encoding="utf-8") as fh:
                data = json.load(fh)
    except Exception as exc:
        log.warning("Google Indexing: cannot read credentials (%s)", exc)
        return None
    if not data.get("client_email") or not data.get("private_key"):
        log.warning("Google Indexing: credentials missing client_email/private_key")
        return None
    return data


def is_configured() -> bool:
    return _load_credentials() is not None


def service_account_email() -> str:
    creds = _load_credentials()
    return creds.get("client_email", "") if creds else ""


# --------------------------------------------------------------------------- #
# Minimal PKCS#8 -> PKCS#1 unwrap (service-account keys are PKCS#8)
# --------------------------------------------------------------------------- #
def _der_read_len(data: bytes, i: int) -> tuple[int, int]:
    n = data[i]
    i += 1
    if n < 0x80:
        return n, i
    count = n & 0x7F
    return int.from_bytes(data[i:i + count], "big"), i + count


def _pkcs8_to_pkcs1(pem: str) -> bytes:
    """Extract the inner PKCS#1 RSA key from a PKCS#8 PEM.

    A PKCS#8 body is ``SEQUENCE { INTEGER version, SEQUENCE algorithm,
    OCTET STRING privateKey }`` where ``privateKey`` is the PKCS#1 blob. We
    walk those three fields rather than pull in an ASN.1 dependency.
    """
    body = "".join(
        line for line in pem.strip().splitlines() if "-----" not in line
    )
    der = base64.b64decode(body)
    if der[0] != 0x30:                                  # outer SEQUENCE
        raise ValueError("not a DER SEQUENCE")
    _, i = _der_read_len(der, 1)
    for _ in range(2):                                  # version, algorithm
        i += 1                                          # tag
        length, i = _der_read_len(der, i)
        i += length
    if der[i] != 0x04:                                  # OCTET STRING
        raise ValueError("expected OCTET STRING with the private key")
    i += 1
    length, i = _der_read_len(der, i)
    return der[i:i + length]


def _private_key(pem: str):
    import rsa

    pem = pem.replace("\\n", "\n")
    if "BEGIN RSA PRIVATE KEY" in pem:
        return rsa.PrivateKey.load_pkcs1(pem.encode())
    return rsa.PrivateKey._load_pkcs1_der(_pkcs8_to_pkcs1(pem))


# --------------------------------------------------------------------------- #
# OAuth2 JWT-bearer access token
# --------------------------------------------------------------------------- #
def _b64(data: bytes) -> bytes:
    return base64.urlsafe_b64encode(data).rstrip(b"=")


def _access_token() -> str | None:
    creds = _load_credentials()
    if not creds:
        return None

    email = creds["client_email"]
    cached = _token_cache.get(email)
    if cached and cached[1] > time.time() + 60:
        return cached[0]

    import rsa

    now = int(time.time())
    header = _b64(json.dumps({"alg": "RS256", "typ": "JWT"}).encode())
    claims = _b64(json.dumps({
        "iss": email,
        "scope": SCOPE,
        "aud": creds.get("token_uri", TOKEN_URI),
        "iat": now,
        "exp": now + 3600,
    }).encode())
    signing_input = header + b"." + claims

    try:
        signature = rsa.sign(signing_input, _private_key(creds["private_key"]), "SHA-256")
    except Exception as exc:
        log.warning("Google Indexing: cannot sign JWT (%s)", exc)
        return None

    assertion = (signing_input + b"." + _b64(signature)).decode()
    payload = urllib.parse.urlencode({
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": assertion,
    }).encode()

    req = urllib.request.Request(
        creds.get("token_uri", TOKEN_URI), data=payload,
        headers={"Content-Type": "application/x-www-form-urlencoded"}, method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.loads(r.read().decode())
        token = data.get("access_token")
        if token:
            _token_cache[email] = (token, now + int(data.get("expires_in", 3600)))
        return token
    except urllib.error.HTTPError as exc:
        log.warning("Google Indexing token error %s: %s", exc.code, exc.read()[:400])
    except Exception as exc:
        log.warning("Google Indexing token request failed: %s", exc)
    return None


# --------------------------------------------------------------------------- #
# Publish
# --------------------------------------------------------------------------- #
def publish(url: str, deleted: bool = False) -> tuple[int, str]:
    """Ask Google to (re)crawl ``url``. Returns ``(http_status, message)``.

    ``deleted=True`` reports the URL as removed instead of updated.
    """
    token = _access_token()
    if not token:
        return 0, "Google Indexing API not configured (or credentials invalid)"

    payload = json.dumps({
        "url": url,
        "type": "URL_DELETED" if deleted else "URL_UPDATED",
    }).encode()
    req = urllib.request.Request(
        PUBLISH_URI, data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }, method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read().decode("utf-8", "ignore")
            return r.status, body[:400]
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "ignore")
        try:
            detail = json.loads(detail).get("error", {}).get("message", detail)
        except Exception:
            pass
        log.warning("Google Indexing publish %s for %s: %s", exc.code, url, detail[:400])
        return exc.code, detail[:400]
    except Exception as exc:
        log.warning("Google Indexing publish failed for %s: %s", url, exc)
        return 0, str(exc)[:400]


def publish_many(urls: Iterable[str]) -> list[tuple[str, int, str]]:
    """Publish several URLs, returning ``(url, status, message)`` for each."""
    return [(u, *publish(u)) for u in urls]
