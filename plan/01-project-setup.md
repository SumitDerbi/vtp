# Prompt 01 — Create Django/Wagtail Project Structure

## Goal

Create the initial Django/Wagtail project with the correct folder structure.

## Prompt

```
Create a new Wagtail CMS project for "Vinsat Precision Technologies" website.

Project name: vtp
Root directory: vtp/ (current workspace root)

Create THIS exact folder structure:

vtp/
├── manage.py
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   └── production.txt
├── vtp/                            # Main project config
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── production.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   └── __init__.py
├── static/
│   ├── css/
│   │   └── .gitkeep
│   ├── js/
│   │   └── .gitkeep
│   └── images/
│       └── .gitkeep
├── media/
│   └── .gitkeep
└── templates/
    └── .gitkeep

For requirements/base.txt include:
wagtail>=6.0,<7.0
Django>=5.0,<6.0
PyMySQL
wagtail-metadata
django-recaptcha
whitenoise
gunicorn
Pillow
cryptography

For requirements/dev.txt:
-r base.txt
django-debug-toolbar
django-extensions

For requirements/production.txt:
-r base.txt

Create manage.py pointing to vtp.settings.dev as default.
Create basic wsgi.py and asgi.py pointing to vtp.settings.production.

DO NOT create settings files yet (that's the next step).
DO NOT create any app models yet.
```

## Verification

1. Check folder structure exists
2. Verify `manage.py` exists and has correct settings module
3. Verify `requirements/base.txt` has all packages listed (PyMySQL, not mysqlclient)

## Expected Result

- Clean project skeleton with all folders created
- No errors when checking file structure
- `manage.py` file with proper Django configuration
