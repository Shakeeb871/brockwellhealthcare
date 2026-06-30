#!/usr/bin/env bash
# Manual deploy helper for cPanel.
# Pulls the latest code from GitHub, applies DB migrations, rebuilds static
# files, and restarts the app. Safe to run as many times as you like.
#
# Run it with:   bash ~/brockwellhealthcare/deploy.sh
set -e

cd "$(dirname "$0")"

echo "==> Pulling latest code from GitHub..."
git fetch origin main
git reset --hard origin/main

# Find this app's virtualenv python (any Python version).
PYBIN=$(ls -d "$HOME"/virtualenv/brockwellhealthcare/*/bin/python 2>/dev/null | head -1)
[ -z "$PYBIN" ] && PYBIN=python

echo "==> Installing/updating Python dependencies..."
"$PYBIN" -m pip install -r requirements.txt

echo "==> Applying database migrations..."
"$PYBIN" manage.py migrate --noinput

echo "==> Collecting static files..."
"$PYBIN" manage.py collectstatic --noinput

echo "==> Restarting the app..."
mkdir -p tmp && touch tmp/restart.txt

echo "✅ Done! Your live site is now updated."
