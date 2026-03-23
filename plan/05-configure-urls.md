# Prompt 05 — Configure URLs and Installed Apps

## Goal

Register all apps in settings and configure URL routing.

## Prompt

```
1. Update vtp/settings/base.py INSTALLED_APPS to include all our apps:
   - 'apps.home',
   - 'apps.products',
   - 'apps.contact',
   - 'apps.enquiry',
   - 'apps.blog',
   - 'apps.downloads',
   - 'apps.common',

2. Create vtp/urls.py with:
   - Django admin at /django-admin/
   - Wagtail admin at /admin/
   - Wagtail documents at /documents/
   - Wagtail search (if needed)
   - Serve media files in DEBUG mode
   - Wagtail page serving at / (catch-all, must be last)

Make sure the URL patterns follow Wagtail's recommended setup.
Include static/media URL serving for development.
```

## Verification

1. `python manage.py check` — passes
2. No import errors for any app

## Expected Result

- All apps registered in INSTALLED_APPS
- URL routing configured correctly
