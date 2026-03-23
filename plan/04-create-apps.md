# Prompt 04 — Create All Django Apps

## Goal

Create all the Django apps needed for the VTP website as empty shells.

## Prompt

```
Create the following Django apps inside the apps/ directory for VTP:

1. apps/home/         — HomePage
2. apps/products/     — ProductIndexPage, ProductPage
3. apps/contact/      — ContactPage, ContactFormSubmission
4. apps/enquiry/      — EnquiryFormSubmission (linked to products)
5. apps/blog/         — BlogIndexPage, BlogPost
6. apps/downloads/    — DownloadIndexPage, DownloadItem
7. apps/common/       — SiteSettings, shared utilities

For each app:
- Create __init__.py
- Create apps.py with proper AppConfig (label and name using 'apps.xxx')
- Create models.py (empty, just imports)
- Create admin.py (empty)
- Create views.py (empty)
- Create urls.py (empty)
- Create templates/ directory with .gitkeep

DO NOT create any models yet — just the app structure.
Make sure each AppConfig has the correct name = 'apps.appname' format.
```

## Verification

1. All 7 app directories exist under `apps/`
2. Each has `apps.py` with correct AppConfig
3. No import errors

## Expected Result

- 7 empty Django app shells ready for models
