# Prompt 02 — Configure Settings (base, dev, production)

## Goal

Create proper Django/Wagtail settings files split into base, dev, and production.

## Prompt

```
Create the Django/Wagtail settings files for the VTP project.

File: vtp/settings/base.py
- Set PROJECT_DIR and BASE_DIR correctly
- INSTALLED_APPS should include:
  - Django defaults (auth, contenttypes, sessions, messages, staticfiles)
  - Wagtail apps (wagtail.contrib.forms, wagtail.contrib.redirects, wagtail.embeds,
    wagtail.sites, wagtail.users, wagtail.snippets, wagtail.documents,
    wagtail.images, wagtail.search, wagtail.admin, wagtail)
  - wagtail.contrib.settings
  - Third party: wagtail_metadata
  - Our apps placeholder: (empty for now, will add later)
  - taggit, modelcluster
- MIDDLEWARE: standard Django + wagtail.contrib.redirects.middleware.RedirectMiddleware
- TEMPLATES: configured for templates/ directory with context processors
  - Include 'wagtail.contrib.settings.context_processors.settings'
- STATIC_URL = '/static/'
- STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
- STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
- MEDIA_URL = '/media/'
- MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
- WAGTAIL_SITE_NAME = 'Vinsat Precision Technologies'
- DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
- AUTH_PASSWORD_VALIDATORS (standard Django set)

File: vtp/settings/dev.py
- Import from .base
- DEBUG = True
- ALLOWED_HOSTS = ['*']
- SECRET_KEY = 'dev-secret-key-change-in-production'
- DATABASE: SQLite for development (db.sqlite3)
- WAGTAILADMIN_BASE_URL = 'http://localhost:8000'
- EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

File: vtp/settings/production.py
- Import from .base
- DEBUG = False
- SECRET_KEY from environment variable
- ALLOWED_HOSTS from environment variable
- DATABASE: MySQL configuration using PyMySQL
  Add at top of file:
  import pymysql
  pymysql.install_as_MySQLdb()
  (NAME, USER, PASSWORD, HOST, PORT from os.environ)
- WAGTAILADMIN_BASE_URL from environment variable
- WhiteNoise for static files in MIDDLEWARE
- SECURE settings (HSTS, secure cookies, etc.)

File: vtp/settings/__init__.py
- Leave empty

Make sure all imports are correct and files are syntactically valid Python.
```

## Verification

1. `python manage.py check --settings=vtp.settings.dev`
   Should show "System check identified no issues"

## Expected Result

- Three settings files properly configured
- Dev uses SQLite, Production uses MySQL via PyMySQL
- `python manage.py check` passes with no errors
