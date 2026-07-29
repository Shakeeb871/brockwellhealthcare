#!/usr/bin/env bash
# Run any Django management command without remembering paths.
#
# On cPanel `python manage.py ...` fails from your home folder because manage.py
# lives in the app folder and the app has its own virtualenv. This wrapper cd's
# to the right place and picks the correct python for you.
#
# Usage:
#   bash ~/brockwellhealthcare/manage.sh seostatus
#   bash ~/brockwellhealthcare/manage.sh submiturls --all --new-only
#   bash ~/brockwellhealthcare/manage.sh migrate
set -e

cd "$(dirname "$0")"

# This app's virtualenv python (any Python version), else whatever is on PATH.
PYBIN=$(ls -d "$HOME"/virtualenv/*/*/bin/python 2>/dev/null | grep -i "$(basename "$PWD")" | head -1)
[ -z "$PYBIN" ] && PYBIN=$(ls -d "$HOME"/virtualenv/*/*/bin/python 2>/dev/null | head -1)
[ -z "$PYBIN" ] && PYBIN=$(command -v python3 || command -v python)

if [ -z "$PYBIN" ]; then
  echo "Could not find a python interpreter." >&2
  exit 1
fi

if [ $# -eq 0 ]; then
  echo "Usage: bash $0 <command> [args]"
  echo
  echo "Common commands:"
  echo "  seostatus                      show indexing status & credentials"
  echo "  submiturls --all               push every sitemap URL to Google/IndexNow"
  echo "  submiturls --all --new-only    push only URLs not yet accepted"
  echo "  migrate                        apply database migrations"
  echo "  collectstatic --noinput        rebuild CSS/JS/images"
  echo
  echo "Using python: $PYBIN"
  exit 0
fi

exec "$PYBIN" manage.py "$@"
