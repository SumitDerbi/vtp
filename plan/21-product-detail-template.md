# Prompt 21 — ProductPage Template (Detail with Enquiry)

## Goal

Create the individual product detail page with image gallery and enquiry button.

## Prompt

```
Create the ProductPage template for VTP.

File: apps/products/templates/products/product_page.html

{% extends "base.html" %}
{% load wagtailcore_tags wagtailimages_tags %}

Sections:

1. BREADCRUMBS:
   {% include "includes/breadcrumbs.html" %}

2. PRODUCT DETAIL — two-column layout (lg):
   LEFT COLUMN (lg:w-1/2):
   - Main product image (large, rounded-lg, shadow)
   - Gallery thumbnails below (horizontal scroll or grid)
   - Clicking thumbnail shows it as main image (Alpine.js)

   RIGHT COLUMN (lg:w-1/2):
   - Product title (text-3xl, font-bold, text-secondary)
   - short_description (text-lg, text-steel)
   - "Send Enquiry" button (btn-primary, prominent)
     → Opens enquiry modal or scrolls to enquiry form section
   - Description (RichTextField rendered)

3. SPECIFICATIONS SECTION (if filled):
   - Full-width section below
   - Heading: "Specifications"
   - Table/list from specifications RichTextField
   - bg-surface, clean layout

4. FEATURES SECTION (if filled):
   - Heading: "Features & Benefits"
   - features RichTextField rendered
   - White background

5. ENQUIRY FORM SECTION:
   - Anchor: id="enquiry"
   - bg-surface strip
   - Heading: "Enquire About This Product"
   - Form fields: name, email, phone, company, quantity, message
   - Product name pre-filled and shown (read-only display)
   - Submit button (btn-primary)

6. RELATED PRODUCTS:
   - Show other products (siblings) — up to 3
   - Small cards with image + title + link

7. CTA BANNER at bottom

Gallery should use Alpine.js for thumbnail click → main image swap.
Enquiry form posts to a view (handled in Prompt 27).
```

## Verification

1. Product detail renders
2. Image gallery with thumbnail click
3. Enquiry form visible with product name
4. Specs and features sections conditional
5. Related products show
6. Responsive

## Expected Result

- Professional product detail page with gallery and inline enquiry form
