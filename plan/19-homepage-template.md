# Prompt 19 — HomePage Template

## Goal

Create a professional homepage template with hero, product showcase, about section, and CTA.

## Prompt

```
Create the HomePage template for VTP.

File: apps/home/templates/home/home_page.html

{% extends "base.html" %}
{% load wagtailcore_tags wagtailimages_tags %}

Sections:

1. HERO SECTION:
   - Full-width, min-height h-[500px] (h-[350px] mobile)
   - Background image with dark overlay for text readability
   - Hero title in white, large (text-4xl lg:text-6xl), font-bold
   - Subtitle in text-gray-200, text-xl
   - CTA button (btn-primary, large)
   - If no hero_image, use gradient bg (from primary to primary-dark)

2. FEATURED PRODUCTS SECTION:
   - Section heading: "Our Products" (section-heading class)
   - bg-surface (light sky blue tint)
   - Grid of product cards (lg:grid-cols-3, md:grid-cols-2, grid-cols-1)
   - Each card: product image (fill-400x300), title, short_description
   - Card hover: shadow increase + slight scale
   - "View Details" link on each card
   - "View All Products" button at bottom

3. ABOUT SNIPPET SECTION:
   - White background
   - Two columns (lg:grid-cols-2): image left, text right
   - about_heading, about_text (RichTextField rendered)
   - about_image with rounded corners

4. STATS/WHY US SECTION (hardcoded for now):
   - bg-secondary (dark navy) with white text
   - 3-4 items: "Precision Engineering", "Quality Assurance", "On-Time Delivery", "Custom Solutions"
   - Icon + title + short text for each

5. CTA SECTION:
   - Use cta_heading, cta_text, cta_button_text from model
   - Gradient bg (primary to primary-dark), white text
   - Centered, prominent button

Use {% image %} tag for all images with appropriate renditions.
Fully responsive. Clean white + sky blue theme.
```

## Verification

1. Homepage renders with all sections
2. Hero with image/gradient
3. Featured products grid
4. About section
5. CTA at bottom
6. Mobile responsive

## Expected Result

- Professional manufacturing company homepage
