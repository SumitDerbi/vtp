"""
Passenger WSGI entry point for cPanel Python Application (Phusion Passenger).

Passenger looks for:
  - Startup file: passenger_wsgi.py  (set in cPanel → Setup Python App)
  - Entry point:  application        (WSGI callable)

On cPanel the layout is:
  ~/vtp/                     ← APP_DIR (this file lives here)
  ~/virtualenv/vtp/3.11/     ← virtualenv managed by cPanel
  ~/vtp.com/                  ← domain document root (static/media symlinks)
  ~/deploy_config/vtp/vtp.env ← .env copied here by deploy.sh
"""

import os
import sys

# ── Path Setup ──────────────────────────────────────────────────────────
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

# ── Virtualenv site-packages (fallback if Passenger doesn't activate it) ─
# cPanel usually activates the venv via its own wrapper, but some edge
# cases (restart race, SSH-based test) may skip it.  This block is a
# safety net — it's harmless if the packages are already on sys.path.
VENV_SITE = os.path.expanduser("~/virtualenv/vtp/3.11/lib/python3.11/site-packages")
if os.path.isdir(VENV_SITE) and VENV_SITE not in sys.path:
    sys.path.insert(0, VENV_SITE)

# ── Django Settings ─────────────────────────────────────────────────────
os.environ["DJANGO_SETTINGS_MODULE"] = "vtp.settings.production"

# ── Load .env ───────────────────────────────────────────────────────────
# Check local .env first, then fall back to deploy_config location.
try:
    from dotenv import load_dotenv

    local_env = os.path.join(CURRENT_DIR, ".env")
    deploy_env = os.path.expanduser("~/deploy_config/vtp/vtp.env")

    if os.path.isfile(local_env):
        load_dotenv(local_env)
    elif os.path.isfile(deploy_env):
        load_dotenv(deploy_env)
except ImportError:
    pass  # python-dotenv not installed — env vars must be set externally

# ── WSGI Application ───────────────────────────────────────────────────
from django.core.wsgi import get_wsgi_application  # noqa: E402

application = get_wsgi_application()
