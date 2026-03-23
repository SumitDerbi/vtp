# Prompt 09 — Create Header with Navigation

## Goal

Create a responsive header with logo, navigation, and mobile menu.

## Prompt

```
Create the header navigation for VTP website.

File: templates/includes/header.html

Design:
- White background, subtle bottom shadow
- Left: Logo (from SiteSettings, fallback to text "VPT")
- Center/Right: Navigation links:
  - Home
  - Products
  - Blog
  - Downloads
  - Contact Us
  - "Send Enquiry" button (sky blue, links to contact page)
- Mobile: Hamburger menu with slide-down nav (Alpine.js)

Use Wagtail tags: {% load wagtailcore_tags wagtailimages_tags %}
Get settings: {% load wagtailsettings_tags %}{% get_settings %}

Navigation should:
- Highlight active page (use request.path matching)
- Be sticky on scroll (sticky top-0 z-50)
- Links in text-secondary color, hover:text-primary
- "Send Enquiry" as btn-primary (sky blue button)
- Mobile responsive — hamburger below lg breakpoint

Keep it clean and professional. Manufacturing company feel.
Readable font size (text-base or text-lg for nav items).
```

## Verification

1. Header renders on all pages
2. Logo shows (or fallback text)
3. Navigation links work
4. Mobile hamburger menu opens/closes
5. Active page highlighted

## Expected Result

- Professional sticky header with responsive navigation
