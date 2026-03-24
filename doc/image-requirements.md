# VTP — Image Requirements

All images needed for the Vinsat Precision Technologies website.

---

## 1. Logo

| Variant | Dimensions     | Format | Notes                                    |
| ------- | -------------- | ------ | ---------------------------------------- |
| Primary | 300×100 px min | PNG    | Transparent background                   |
| Vector  | Scalable       | SVG    | Preferred for header (crisp at any size) |

**Used in:** Header, Footer, Wagtail Admin (via SiteSettings)

---

## 2. Favicon

| Dimensions | Format  | Notes            |
| ---------- | ------- | ---------------- |
| 32×32 px   | PNG/ICO | Browser tab icon |

**Used in:** Browser tab (set via SiteSettings → favicon)

---

## 3. Hero Image

| Dimensions      | Aspect Ratio | Format | Notes                                                 |
| --------------- | ------------ | ------ | ----------------------------------------------------- |
| 1920×600 px min | ~3.2:1       | JPG    | High quality, shows manufacturing/precision equipment |

**Used in:** Homepage hero section (full-width background)

---

## 4. Product Images

Each of the 6 products needs:

| Type    | Dimensions      | Aspect Ratio | Format | Notes                                 |
| ------- | --------------- | ------------ | ------ | ------------------------------------- |
| Main    | 800×600 px min  | 4:3          | JPG    | White or neutral background preferred |
| Gallery | 800×600 px each | 4:3          | JPG    | Up to 10 per product                  |

### Products

1. **Bend Dies** — main image + gallery
2. **Clamp Dies** — main image + gallery
3. **Pressure Dies** — main image + gallery
4. **Wiper Inserts** — main image + gallery
5. **Mandrels** — main image + gallery
6. **Accessories** — main image + gallery

**Total:** 6 main images + up to 60 gallery images

> **Note:** Client already has product photos (WhatsApp images in `doc/` folder). These may need cropping/resizing to 4:3 ratio.

---

## 5. About Section Image

| Dimensions     | Aspect Ratio | Format | Notes                                   |
| -------------- | ------------ | ------ | --------------------------------------- |
| 800×600 px min | 4:3          | JPG    | Manufacturing facility / workshop photo |

**Used in:** Homepage "About" section (image-left layout)

---

## 6. Blog Post Images

| Type     | Dimensions  | Aspect Ratio | Format | Notes                           |
| -------- | ----------- | ------------ | ------ | ------------------------------- |
| Featured | 1200×630 px | ~1.9:1       | JPG    | Social share friendly (OG size) |

**Used in:** Blog listing cards (cropped to 400×250) and blog post header

---

## 7. Open Graph / Social Sharing

| Dimensions  | Format  | Notes                                               |
| ----------- | ------- | --------------------------------------------------- |
| 1200×630 px | PNG/JPG | Default image when pages are shared on social media |

**Used in:** Meta tags for Facebook, LinkedIn, Twitter/X

---

## 8. Download Thumbnails (Optional)

| Dimensions | Format | Notes                            |
| ---------- | ------ | -------------------------------- |
| 200×280 px | PNG    | Document preview / catalog cover |

**Used in:** Downloads listing page (optional thumbnail per item)

---

## Summary

| Category          | Count      | Priority |
| ----------------- | ---------- | -------- |
| Logo (PNG + SVG)  | 2 files    | High     |
| Favicon           | 1 file     | High     |
| Hero image        | 1 file     | High     |
| Product images    | 6–36 files | High     |
| About image       | 1 file     | Medium   |
| Blog images       | As needed  | Low      |
| OG / Social image | 1 file     | Medium   |
| Download thumbs   | As needed  | Low      |

**Minimum to launch:** Logo + Favicon + Hero + 6 product main images = **~10 files**
