"""
Django/Wagtail settings for VTP project — development.
"""

from .base import *  # noqa: F401, F403

DEBUG = True

SECRET_KEY = "dev-secret-key-change-in-production"

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

WAGTAILADMIN_BASE_URL = "http://localhost:8000"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Debug toolbar
INSTALLED_APPS += ["debug_toolbar", "django_extensions"]  # noqa: F405
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")  # noqa: F405
INTERNAL_IPS = ["127.0.0.1"]
