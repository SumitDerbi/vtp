# Prompt 20 — ProductIndexPage Template

## Goal

Create the products listing page showing all products in a professional grid.

## Prompt

```
Create the ProductIndexPage template for VTP.

File: apps/products/templates/products/product_index_page.html

{% extends "base.html" %}
{% load wagtailcore_tags wagtailimages_tags %}

Sections:

1. PAGE HEADER:
   - bg-surface (light sky blue) strip
   - heading (from model), centered
   - intro text below heading

2. BREADCRUMBS:
   {% include "includes/breadcrumbs.html" %}

3. PRODUCT GRID:
   - Container max-w-7xl mx-auto px-4 py-12
   - Grid: lg:grid-cols-3, md:grid-cols-2, grid-cols-1, gap-8
   - Each product card:
     - Product main_image (fill-400x300, with fallback placeholder)
     - Product title (font-semibold, text-secondary)
     - short_description (text-steel, truncated 2 lines)
     - "View Details" link (text-primary, hover underline)
     - "Send Enquiry" small button (btn-outline, small)
   - Card: white bg, rounded-xl, shadow, hover:shadow-lg transition
   - Clean gaps, generous padding

4. CTA BANNER at bottom:
   {% include "includes/cta_banner.html" %}

If no products: show "No products available yet" message.
Make it visually appealing — manufacturing products look premium.
```

## Verification

1. Page renders with product grid
2. Product images display correctly
3. Links to individual product pages work
4. Responsive grid layout
5. Empty state handled

## Expected Result

- Clean product catalog grid page
