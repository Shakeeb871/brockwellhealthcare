"""
Passenger entry point for cPanel "Setup Python App" hosting.

cPanel/Phusion Passenger looks for this file in the application root and
serves the WSGI ``application`` callable it exposes. It simply hands off to
Django's real WSGI app in ``config/wsgi.py``.
"""

import os
import sys

# This file lives in the project root; make sure that root is importable.
sys.path.insert(0, os.path.dirname(__file__))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from config.wsgi import application  # noqa: E402  (import after sys.path setup)
