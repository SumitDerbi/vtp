# Prompt 22 — ContactPage Template with Form

## Goal

Create the contact page template with contact info, map, and contact form.

## Prompt

```
Create the ContactPage template for VTP.

File: apps/contact/templates/contact/contact_page.html

{% extends "base.html" %}
{% load wagtailcore_tags wagtailimages_tags %}

Sections:

1. BREADCRUMBS:
   {% include "includes/breadcrumbs.html" %}

2. PAGE HEADER:
   - bg-surface strip
   - "Contact Us" heading
   - intro text

3. MAIN CONTENT — two-column layout:
   LEFT COLUMN (lg:w-1/2):
   - form_heading
   - Contact form with fields:
     - Name* (text input)
     - Email* (email input)
     - Phone (text input)
     - Company (text input)
     - Subject (text input)
     - Message* (textarea, 5 rows)
   - Submit button (btn-primary)
   - All inputs: Tailwind styled with focus:ring-2 focus:ring-primary
   - Success message shown after submission (from success_message field)

   RIGHT COLUMN (lg:w-1/2):
   - Contact Info Card (bg-white, rounded-xl, shadow):
     - Address (with map pin icon)
     - Phone (with phone icon)
     - Email (with email icon)
   - Google Maps embed (if google_maps_embed is filled)
     - Responsive iframe, rounded-lg

4. Form uses POST method with CSRF token
   Action handled by serve() method (Prompt 26)

Clean, professional layout. White bg, sky blue accents.
Form inputs readable size.
Use simple SVG icons for contact info (inline or heroicons).
```

## Verification

1. Contact page renders
2. Form displays with all fields
3. Contact info card shows
4. Google Maps embed works
5. Responsive layout
6. Success message after submission

## Expected Result

- Professional contact page with form and info
