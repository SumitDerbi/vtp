# Prompt 28 — Admin Listings (Contact, Enquiry, Downloads)

## Goal

Create Wagtail admin listings for contact responses, product enquiries, and downloads management.

## Prompt

```
Create Wagtail admin panel listings for VTP.

Use wagtail.contrib.modeladmin or wagtail_modeladmin (Wagtail 6.x) or
Wagtail's built-in ModelViewSet (preferred for Wagtail 6+).

1. File: apps/contact/wagtail_hooks.py

   Register ContactFormSubmission in Wagtail admin:
   - List display: name, email, subject, created_at, is_read
   - List filter: is_read, created_at
   - Search: name, email, subject, message
   - Menu label: "Contact Responses"
   - Menu icon: "mail"
   - Ordering: -created_at
   - Read-only detail view showing all fields
   - Ability to mark as read

2. File: apps/enquiry/wagtail_hooks.py

   Register EnquiryFormSubmission in Wagtail admin:
   - List display: name, product_name, email, created_at, is_read
   - List filter: is_read, product_name, created_at
   - Search: name, email, product_name, message
   - Menu label: "Product Enquiries"
   - Menu icon: "clipboard-list"
   - Ordering: -created_at
   - Show which product the enquiry is about

3. Downloads are already managed via Snippets (from Prompt 18).
   Optionally add a ModelAdmin entry too for better visibility:

   File: apps/downloads/wagtail_hooks.py
   - Menu label: "Downloads"
   - Menu icon: "download"
   - List display: title, category, is_active, created_at

Group all under a "Submissions" menu group in Wagtail sidebar:
- Contact Responses
- Product Enquiries

Use Wagtail 6.x ModelViewSet approach:
  from wagtail.snippets.views.snippets import SnippetViewSet
  or from wagtail.admin.viewsets.model import ModelViewSet
```

## Verification

1. Wagtail admin sidebar shows "Submissions" group
2. Contact Responses listing works with search/filter
3. Product Enquiries listing shows product name
4. Downloads manageable from Snippets
5. Can mark items as read

## Expected Result

- Admin can view, filter, and manage all form submissions
