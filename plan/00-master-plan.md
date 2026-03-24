# Vinsat Precision Technologies — Wagtail Website Build Plan

## Jai Shree Ram

> **Strategy:** Small, independent, testable steps. Each prompt is self-contained.
> Execute one prompt → Test → Verify → Move to next.

---

## Company Context

**Vinsat Precision Technologies (VPT)** — Precision CNC manufacturing company.
Products: Tube bending tooling — Bend Dies, Clamp Dies, Pressure Dies, Wiper Inserts, Mandrels, Accessories.
Few products, clean catalog. White + Sky Blue theme. Professional manufacturing look.

---

## Phase Overview

| Phase       | Focus                      | Prompts |
| ----------- | -------------------------- | ------- |
| **Phase 1** | Project Setup & Foundation | 01–06   |
| **Phase 2** | Tailwind, Base Templates   | 07–12   |
| **Phase 3** | Page Models (all)          | 13–18   |
| **Phase 4** | Templates for All Pages    | 19–25   |
| **Phase 5** | Forms, Admin & Features    | 26–29   |
| **Phase 6** | Setup Command & Content    | 30–32   |
| **Phase 7** | SEO, Deployment & Go-Live  | 33–37   |

---

## Prompt Execution Rules

1. **One prompt at a time** — don't skip ahead
2. **Test after each prompt** — run `python manage.py runserver` and verify
3. **Run migrations** — after any model change: `makemigrations` → `migrate`
4. **Commit after each prompt** — small git commits for easy rollback
5. **Mark done** — check off each prompt below as you complete it

---

## All Prompts (Quick Reference)

### Phase 1 — Project Setup & Foundation

- [x] `01` — Create Django/Wagtail project structure
- [x] `02` — Configure settings (base, dev, production)
- [x] `03` — Setup database connection (SQLite dev, MySQL prod with PyMySQL)
- [x] `04` — Create all Django apps (empty shells)
- [x] `05` — Configure URLs and installed apps
- [x] `06` — First migration & superuser creation

### Phase 2 — Tailwind, Base Templates & Site Settings

- [x] `07` — Install and configure Tailwind CSS (white + sky blue theme)
- [x] `08` — Create base.html template
- [x] `09` — Create header with navigation
- [x] `10` — Create footer template
- [x] `11` — Create SiteSettings model (logo, contact, social)
- [x] `12` — Create common includes (breadcrumbs, CTA banner)

### Phase 3 — Page Models

- [x] `13` — HomePage model with hero section
- [x] `14` — ProductIndexPage & ProductPage models
- [x] `15` — ContactPage & ContactFormSubmission models
- [x] `16` — EnquiryFormSubmission model (linked to product)
- [x] `17` — BlogIndexPage & BlogPost models
- [x] `18` — DownloadIndexPage & DownloadItem models

### Phase 4 — Templates for All Pages

- [x] `19` — HomePage template (hero + product showcase + CTA)
- [x] `20` — ProductIndexPage template (product grid)
- [x] `21` — ProductPage template (detail with enquiry button)
- [x] `22` — ContactPage template with form
- [x] `23` — BlogIndexPage & BlogPost templates
- [x] `24` — DownloadIndexPage template
- [x] `25` — Enquiry modal/form template (product-linked)

### Phase 5 — Forms, Admin Listings & Features

- [x] `26` — Contact form processing with email notification
- [x] `27` — Product enquiry form processing
- [x] `28` — Admin listings (contact responses, enquiries, downloads)
- [x] `29` — WhatsApp widget & scroll-to-top

### Phase 6 — Setup Command & Content

- [x] `30` — Management command: setup_pages (create default page tree)
- [x] `31` — Image requirements document
- [x] `32` — Upload sample content & verify all pages

### Phase 7 — SEO, Deployment & Go-Live

- [ ] `33` — SEO meta tags, sitemap, robots.txt
- [ ] `34` — Responsive testing & performance
- [ ] `35` — deployment.sh script
- [ ] `36` — Docker & production configuration
- [ ] `37` — Final build & go-live checklist

---

## Tech Stack

- **Backend:** Django 5.x + Wagtail 6.x
- **Database:** SQLite (dev), MySQL with PyMySQL (prod)
- **Frontend:** Tailwind CSS 3.x, Alpine.js
- **Theme:** White base (#FFFFFF) + Sky Blue (#0EA5E9) + accents
- **Font:** Inter (Google Fonts)
- **Deployment:** Docker + Nginx + Gunicorn + deployment.sh
- **Admin:** Wagtail CMS admin panel

---

## Page Tree Structure

```
Root
└── Home (HomePage)
    ├── Products (ProductIndexPage)
    │   ├── Bend Dies (ProductPage)
    │   ├── Clamp Dies (ProductPage)
    │   ├── Pressure Dies (ProductPage)
    │   ├── Wiper Inserts (ProductPage)
    │   ├── Mandrels (ProductPage)
    │   └── Accessories (ProductPage)
    ├── Contact Us (ContactPage)
    ├── Blog (BlogIndexPage)
    │   └── Blog Post 1... (BlogPost)
    └── Downloads (DownloadIndexPage)
```

Enquiry form is a modal/inline form on ProductPage — not a separate page.
