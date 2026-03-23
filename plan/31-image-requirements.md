# Prompt 31 — Image Requirements Document

## Goal

Create a document listing all image requirements for the website.

## Prompt

```
Create an image requirements document for VTP.

File: doc/image-requirements.md

List ALL images needed for the website with:
- Purpose / Where used
- Recommended dimensions (pixels)
- Aspect ratio
- Format (JPG/PNG/SVG)
- Notes

Images needed:

1. LOGO
   - PNG: 300x100px minimum (transparent background)
   - SVG: vector version (preferred for header)
   - Used: Header, Footer, Admin

2. FAVICON
   - 32x32px PNG or ICO
   - Used: Browser tab

3. HERO IMAGE
   - 1920x600px minimum
   - JPG, high quality
   - Used: Homepage hero section
   - Should show manufacturing/precision equipment

4. PRODUCT IMAGES (per product):
   - Main: 800x600px minimum (4:3 ratio)
   - Gallery: 800x600px each, up to 10 per product
   - JPG, white or neutral background preferred
   - Products: Bend Dies, Clamp Dies, Pressure Dies, Wiper Inserts, Mandrels, Accessories
   - *Client already has product photos (WhatsApp images in doc/ folder)*

5. ABOUT SECTION IMAGE
   - 800x600px minimum
   - Manufacturing facility / workshop photo

6. BLOG POST IMAGES
   - Featured: 1200x630px (social share friendly)
   - JPG

7. OPEN GRAPH / SOCIAL SHARING
   - 1200x630px default share image
   - PNG/JPG

8. DOWNLOAD THUMBNAILS (optional)
   - 200x280px (document preview)
   - PNG

TOTAL IMAGES NEEDED:
- 1 Logo (PNG + SVG)
- 1 Favicon
- 1 Hero background
- ~6-30 Product photos (1 main + gallery per product)
- 1 About image
- Blog images (as needed)
- 1 OG image
```

## Expected Result

- Clear image requirements document for client/designer
