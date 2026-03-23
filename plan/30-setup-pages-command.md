# Prompt 30 — Management Command: setup_pages

## Goal

Create a management command to set up the initial page tree structure in Wagtail.

## Prompt

```
Create a Django management command to set up the initial Wagtail page tree for VTP.

File: apps/home/management/__init__.py (empty)
File: apps/home/management/commands/__init__.py (empty)
File: apps/home/management/commands/setup_pages.py

This command should:

1. Delete the default Wagtail "Welcome to your new Wagtail site!" page
2. Create the HomePage as the root page with:
   - Title: "Vinsat Precision Technologies"
   - slug: "home"
   - Hero defaults filled in

3. Under HomePage, create these child pages (in order):
   a. ProductIndexPage — title: "Products", slug: "products"
   b. BlogIndexPage — title: "Blog", slug: "blog"
   c. DownloadIndexPage — title: "Downloads", slug: "downloads"
   d. ContactPage — title: "Contact Us", slug: "contact"
      - Pre-fill form_heading, success_message

4. Under ProductIndexPage, create product pages:
   a. ProductPage — "Bend Dies", slug: "bend-dies"
   b. ProductPage — "Clamp Dies", slug: "clamp-dies"
   c. ProductPage — "Pressure Dies", slug: "pressure-dies"
   d. ProductPage — "Wiper Inserts", slug: "wiper-inserts"
   e. ProductPage — "Mandrels", slug: "mandrels"
   f. ProductPage — "Accessories", slug: "accessories"

5. Set the default site to point to the new HomePage

6. Publish all pages

7. Create default SiteSettings:
   - company_name: "Vinsat Precision Technologies"
   - tagline: "Precision Tooling Solutions"

Command usage:
python manage.py setup_pages

The command should be IDEMPOTENT — check if pages exist before creating.
Print progress: "Creating Products page... ✓"

Use Page.add_child(instance=page) for tree structure.
Set the Site's root_page to HomePage.
```

## Verification

1. Run: `python manage.py setup_pages`
2. All pages created without errors
3. Wagtail admin → Pages shows correct hierarchy
4. Run command again — no duplicates (idempotent)
5. Site configured to serve from HomePage

## Expected Result

- Complete page tree set up programmatically
- **MILESTONE: Full page tree ready for content!**
