# Prompt 32 — Upload Sample Content & Verify

## Goal

Upload sample content to all pages and verify everything works end-to-end.

## Prompt

```
Verify the complete VTP website by adding content:

1. Via Wagtail admin, fill in:
   - SiteSettings (company name, contact, social links)
   - HomePage hero content
   - Product pages — add descriptions and upload product images
     (use the images from doc/WhatsApp folder as initial product photos)
   - Contact page — fill address, phone, email
   - Create 1-2 sample blog posts
   - Add 1-2 sample download items (upload a test PDF)

2. Test all pages:
   - Homepage renders with hero, products, about, CTA
   - Products grid shows all 6 products
   - Product detail shows gallery, specs, enquiry form
   - Contact form submits and saves
   - Enquiry form submits and links to product
   - Blog listing shows posts
   - Blog post renders with full content
   - Downloads page shows files
   - Download links work

3. Test responsive:
   - Mobile (375px)
   - Tablet (768px)
   - Desktop (1280px+)

4. Test admin:
   - Contact responses appear in admin
   - Product enquiries appear in admin
   - Downloads manageable from snippets

This is a manual verification step — no code changes.
```

## Verification

- All pages render correctly
- All forms work
- All admin listings work
- Responsive on all breakpoints

## Expected Result

- **MILESTONE: Complete working website with sample content!**
