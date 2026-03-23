# Prompt 10 — Create Footer Template

## Goal

Create a professional footer with company info, quick links, and contact details.

## Prompt

```
Create the footer for the VTP website.

File: templates/includes/footer.html

Design — 3-section footer:

1. MAIN FOOTER (bg-secondary / dark navy background, white text):
   - Column 1: Company logo + short description + social media icons
   - Column 2: "Quick Links" — Home, Products, Blog, Downloads, Contact
   - Column 3: "Contact Us" — phone, email, address from SiteSettings
   - Grid: lg:grid-cols-3, md:grid-cols-2, grid-cols-1

2. BOTTOM BAR (slightly darker bg):
   - "© 2026 Vinsat Precision Technologies. All rights reserved."
   - Right side: "Designed by" credit (optional)

Social media links from SiteSettings (LinkedIn, Facebook, Instagram, YouTube).
Use {% load wagtailsettings_tags %} {% get_settings %}.
Font: readable size (text-sm to text-base).
Links: text-gray-300 hover:text-primary-light transition.
```

## Verification

1. Footer renders on all pages
2. Contact info shows from SiteSettings (after model is created)
3. Social icons link correctly
4. Responsive layout

## Expected Result

- Professional dark footer with company information
