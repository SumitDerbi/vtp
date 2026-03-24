# Wagtail Website Build — Planning Guidelines

> **Purpose:** Provide this document when asking AI to plan a Wagtail CMS website.
> It ensures consistent, high-quality planning across projects by encoding proven patterns, phase structure, and lessons learned.

---

## How to Use This Document

1. Copy this file into your new project folder
2. Fill in **Section 1 (Project Brief)** with your specific requirements
3. Provide both this document + your filled brief to AI with the prompt:
   _"Read the guidelines document and my project brief. Create a phased build plan with individual prompts following the structure and patterns defined in the guidelines."_

---

## Section 1 — Project Brief Template

> _Fill this section for each new project. Delete the example values._

```
COMPANY NAME:        [e.g., Vinsat Precision Technologies]
TAGLINE:             [e.g., Precision Tooling Solutions]
INDUSTRY:            [e.g., CNC Manufacturing]
WEBSITE TYPE:        [e.g., Corporate/Catalog — few products, professional look]

PAGES NEEDED:
- Home
- About
- [List all pages...]

PRODUCTS/SERVICES:   [List all with names. Few = simple catalog, Many = filterable index]

SPECIAL FEATURES:
- [ ] Contact form with email notification
- [ ] Product enquiry form (linked to product)
- [ ] Blog
- [ ] Downloads section (PDFs, catalogs)
- [ ] WhatsApp widget
- [ ] Image gallery / lightbox
- [ ] Testimonials
- [ ] Team members section
- [ ] Newsletter signup
- [ ] [Other...]

ADMIN PANEL NEEDS:
- [ ] Contact form submissions listing
- [ ] Product enquiry listing
- [ ] [Other admin listings...]

SITE SETTINGS FIELDS:
- [ ] Logo (PNG + SVG)
- [ ] Favicon
- [ ] Contact details (phone, email, address)
- [ ] Social media links
- [ ] WhatsApp number
- [ ] Google Analytics ID
- [ ] [Other...]

THEME PREFERENCES:
- Base color:    [e.g., White #FFFFFF]
- Primary:      [e.g., Sky Blue #0284C7]
- Secondary:    [e.g., Dark Navy #1E3A5F]
- Accent:       [e.g., Amber #F59E0B]
- Font:         [e.g., Inter from Google Fonts]

DEPLOYMENT:
- Dev database:  SQLite
- Prod database: [MySQL with PyMySQL / PostgreSQL]
- Hosting:       [Docker + Nginx / VPS / Cloud]
- Need deployment scripts: [Yes/No]
- Need Docker setup:       [Yes/No]

REFERENCE PROJECT: [Path to existing project to use as reference, if any]
```

---

## Section 2 — Proven Phase Structure

Always follow this phase order. Each phase builds on the previous one. Never skip phases.

### Phase 1 — Project Setup & Foundation (Prompts 01–06)

**What:** Project skeleton, settings, apps, URLs, first migration.

| Prompt | Task                                       | Key Details                                                                     |
| ------ | ------------------------------------------ | ------------------------------------------------------------------------------- |
| 01     | Create Django/Wagtail project structure    | `django-admin startproject`, folder layout, `apps/` directory                   |
| 02     | Configure settings (base, dev, production) | Split settings: `settings/base.py`, `settings/dev.py`, `settings/production.py` |
| 03     | Setup database connection                  | SQLite for dev, PyMySQL for production (no C compiler deps)                     |
| 04     | Create all Django apps (empty shells)      | One `startapp` per feature: home, products, contact, blog, etc.                 |
| 05     | Configure URLs and installed apps          | Register all apps in `INSTALLED_APPS`, main `urls.py`                           |
| 06     | First migration & superuser                | `migrate`, `createsuperuser`                                                    |

**Critical Rules:**

- Always use split settings (`base.py` / `dev.py` / `production.py`)
- Put apps inside `apps/` directory with proper `AppConfig.name = "apps.appname"`
- Use PyMySQL instead of mysqlclient for production (avoids C compiler dependency)
- Create `.env.example` with all environment variables documented

### Phase 2 — Tailwind, Base Templates & Site Settings (Prompts 07–12)

**What:** Frontend framework, base layout, header/footer, site-wide settings model.

| Prompt | Task                             | Key Details                                                     |
| ------ | -------------------------------- | --------------------------------------------------------------- |
| 07     | Install & configure Tailwind CSS | `package.json`, `tailwind.config.js`, `input.css`, `output.css` |
| 08     | Create `base.html` template      | DOCTYPE, meta tags, font, CSS link, Alpine.js CDN, blocks       |
| 09     | Create header with navigation    | Responsive hamburger menu, Alpine.js for mobile toggle          |
| 10     | Create footer template           | Company info, quick links, social icons, copyright              |
| 11     | Create SiteSettings model        | Logo, contact, social media, WhatsApp, analytics fields         |
| 12     | Create common includes           | Breadcrumbs, CTA banner, other reusable partials                |

**Critical Rules:**

- Tailwind content paths must include BOTH `./templates/**/*.html` AND `./apps/**/templates/**/*.html`
- Theme colors defined in `tailwind.config.js` extend section — use semantic names (`primary`, `secondary`, `accent`)
- Alpine.js loaded via CDN `defer` script at bottom of body (not head)
- Header must work on mobile — use Alpine.js `x-data`, `x-show`, `@click` for menu toggle
- Load `wagtailsettings_tags` in templates that need SiteSettings access

### Phase 3 — Page Models (Prompts 13–18)

**What:** All Wagtail page models, one prompt per model group.

| Prompt | Task              | Model Pattern                                                       |
| ------ | ----------------- | ------------------------------------------------------------------- |
| 13     | HomePage model    | Hero fields, featured section, CTA fields                           |
| 14     | Product models    | ProductIndexPage (parent) + ProductPage (child) + gallery orderable |
| 15     | ContactPage model | Form fields embedded in page, `serve()` method for POST             |
| 16     | Enquiry model     | Separate model linked to product via ForeignKey                     |
| 17     | Blog models       | BlogIndexPage + BlogPost with date/author/excerpt/body              |
| 18     | Downloads model   | DownloadIndexPage + DownloadItem as Wagtail snippet                 |

**Critical Rules:**

- Every page model must inherit `MetadataPageMixin, Page` (for SEO — install `wagtail-metadata`)
- Use `content_panels`, `promote_panels`, and `MetadataPageMixin.promote_panels` properly
- Set `max_count = 1` on singleton pages (HomePage, ContactPage, AboutPage)
- Set `parent_page_types` and `subpage_types` to enforce page tree structure
- Use `Orderable` + `InlinePanel` for galleries and repeating content
- ContactPage should override `serve()` with `TemplateResponse` (not `self.render()`)
- Run `makemigrations` + `migrate` after every model change

### Phase 4 — Templates for All Pages (Prompts 19–25)

**What:** HTML templates for every page model.

**Critical Rules:**

- Template location: `apps/<appname>/templates/<appname>/page_name.html` (Django convention)
- Exception: pages in `home` app can use `templates/home/page_name.html` (project-level)
- Every template extends `base.html`
- Use `{% load wagtailcore_tags wagtailimages_tags %}` at top
- Use `{% image ... fill-WxH as img %}` for Wagtail image renditions — never raw `image.url`
- Add `loading="lazy"` to all images EXCEPT the hero/above-fold image
- Use Tailwind responsive classes: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`
- Use semantic HTML: `<article>`, `<section>`, `<nav>`, `<main>`
- Add focus states on all interactive elements: `focus:ring-2 focus:ring-primary focus:outline-none`

### Phase 5 — Forms, Admin & Features (Prompts 26–29)

**What:** Form processing, admin panel listings, widgets.

| Prompt | Task                            | Key Details                                                     |
| ------ | ------------------------------- | --------------------------------------------------------------- |
| 26     | Contact form processing         | POST handler, save to DB, email notification, PRG redirect      |
| 27     | Enquiry form processing         | POST-only view, linked to product, email notification           |
| 28     | Admin listings                  | `ViewSetGroup` for wagtail admin, list columns, search, filters |
| 29     | WhatsApp widget & scroll-to-top | Fixed position, Alpine.js, accessibility                        |

**Critical Rules:**

- Forms use POST-Redirect-GET (PRG) pattern — never re-render on POST success
- Use Django's `messages` framework or query params for success feedback
- Admin listings use `ModelViewSet` in `wagtail_hooks.py` (not Django admin)
- Add `inspect_view_enabled = True` for read-only detail views
- WhatsApp widget uses `https://wa.me/{number}` format

### Phase 6 — Setup Command & Docs (Prompts 30–32)

**What:** Management command for page tree, image requirements doc, content verification.

**Critical Rules:**

- `setup_pages` command must be **idempotent** — safe to run multiple times
- Use Wagtail's `parent.add_child(instance=page)` pattern, then `page.save_revision().publish()`
- Call `Page.fix_tree()` after deleting any pages (Wagtail uses treebeard)
- Create `doc/image-requirements.md` listing every image needed with dimensions
- Verify every page renders without errors before moving to next phase

### Phase 7 — Additional Pages (If needed)

**What:** Any pages not in the original plan that were discovered during requirements review.

**Rule:** Always review the requirements document at planning time and list ALL pages. Missing pages mid-build is costly — they require model + template + setup_pages update + nav update.

### Phase 8 — SEO, Deployment & Go-Live (Final prompts)

| Prompt             | Task                                        | Key Details                                                       |
| ------------------ | ------------------------------------------- | ----------------------------------------------------------------- |
| SEO                | Meta tags, sitemap, robots.txt              | `wagtail-metadata`, `WagtailSitemap`, `robots.txt` template       |
| Responsive & Perf  | Audit all templates                         | Lazy loading, focus states, ARIA attributes, semantic HTML        |
| Deployment scripts | `deployment.sh`, `deployment_first_time.sh` | Git pull, pip install, npm build, migrate, collectstatic, restart |
| Docker             | Dockerfile, docker-compose.yml, nginx       | Python slim, gunicorn, MySQL, nginx reverse proxy                 |
| Go-live checklist  | Verification document                       | Pre-launch, SEO, production, performance, post-launch checks      |

---

## Section 3 — Prompt Writing Rules

### Structure of Each Prompt File

```markdown
# Prompt XX — [Short Title]

## Goal

One sentence describing what this prompt achieves.

## Prompt

The exact instructions to execute. Be specific about:

- File paths (where to create/edit)
- Model fields (names, types, defaults)
- Template structure (sections, layout)
- Any dependencies on previous prompts

## Expected Result

- What should work after this prompt
- How to verify (URL to visit, command to run)
```

### Prompt Rules

1. **One concept per prompt** — don't mix model creation with template creation
2. **Self-contained** — each prompt should work independently given prior prompts are done
3. **Specific over vague** — say "CharField max_length=255" not "a text field"
4. **Include verification** — every prompt should say how to test the result
5. **State dependencies** — if prompt 14 needs prompt 13 done, say so
6. **Include file paths** — always specify where files should be created/edited

---

## Section 4 — Tech Stack & Architecture Decisions

### Mandatory Stack

| Component    | Choice                          | Rationale                                                 |
| ------------ | ------------------------------- | --------------------------------------------------------- |
| Backend      | Django + Wagtail                | CMS with admin panel, page tree, image handling           |
| Frontend CSS | Tailwind CSS 3.x                | Utility-first, no custom CSS files needed                 |
| Frontend JS  | Alpine.js (CDN)                 | Lightweight interactivity without build step              |
| Font         | Google Fonts (Inter or similar) | Professional, readable, free                              |
| Dev DB       | SQLite                          | Zero config for development                               |
| Prod DB      | MySQL + PyMySQL                 | No C compiler deps, reliable                              |
| Static files | WhiteNoise                      | Serve static files in production without nginx for static |
| SEO          | wagtail-metadata                | OG/Twitter meta tags, search image, search description    |
| Deployment   | Docker + gunicorn + nginx       | Standard production setup                                 |

### Project Structure Convention

```
project_root/
├── apps/                    # All Django apps here
│   ├── __init__.py
│   ├── home/                # HomePage, AboutPage, FacilityPage (singleton pages)
│   ├── products/            # Product catalog
│   ├── blog/                # Blog posts
│   ├── contact/             # Contact form
│   ├── enquiry/             # Product enquiries (separate from contact)
│   ├── downloads/           # Downloadable files
│   └── common/              # SiteSettings, shared models
├── templates/               # Project-level templates
│   ├── base.html
│   ├── robots.txt
│   ├── includes/            # Header, footer, widgets
│   └── home/                # Templates for home app pages
├── static/
│   ├── css/
│   │   ├── input.css        # Tailwind directives
│   │   └── output.css       # Built CSS (gitignored in some setups)
│   ├── images/
│   └── js/
├── requirements/
│   ├── base.txt             # Shared deps
│   ├── dev.txt              # Dev-only (debug toolbar, etc.)
│   └── production.txt       # Prod-only (gunicorn, whitenoise, pymysql)
├── doc/                     # Documentation
├── plan/                    # Build plan and prompt files
├── nginx/                   # Nginx config for Docker
├── project_name/            # Django project config
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── production.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── Dockerfile
├── docker-compose.yml
├── package.json
├── tailwind.config.js
├── .env.example
├── .gitignore
├── .prettierignore          # Prevent formatter from breaking Django templates
└── manage.py
```

### Settings Split Pattern

**base.py** — Shared settings:

- INSTALLED_APPS (all apps, wagtail apps, third-party)
- MIDDLEWARE
- TEMPLATES config
- Static/media file paths
- Wagtail settings (WAGTAIL_SITE_NAME, etc.)
- Console email backend (dev default)

**dev.py** — Dev overrides:

- `DEBUG = True`
- SQLite database
- Django Debug Toolbar
- `ALLOWED_HOSTS = ["*"]`

**production.py** — Production overrides:

- `DEBUG = False`
- MySQL via PyMySQL with `pymysql.install_as_MySQLdb()`
- WhiteNoise middleware + staticfiles storage
- Security settings (HSTS, SSL redirect, secure cookies, CSRF)
- SMTP email backend
- `SECRET_KEY` from environment variable
- `ALLOWED_HOSTS` from environment variable

---

## Section 5 — Common Patterns & Code Snippets

### Page Model Pattern

```python
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtailmetadata.models import MetadataPageMixin

class MyPage(MetadataPageMixin, Page):
    # Fields
    heading = models.CharField(max_length=255)
    intro = models.TextField(blank=True)
    body = RichTextField(blank=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("heading"),
        FieldPanel("intro"),
        FieldPanel("body"),
        FieldPanel("banner_image"),
    ]

    promote_panels = MetadataPageMixin.promote_panels

    max_count = 1  # For singleton pages
    parent_page_types = ["home.HomePage"]
    subpage_types = []
```

### Gallery Orderable Pattern

```python
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable

class GalleryImage(Orderable):
    page = ParentalKey("MyPage", related_name="gallery_images")
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+",
    )
    caption = models.CharField(max_length=255, blank=True)

    panels = [FieldPanel("image"), FieldPanel("caption")]
```

### ContactPage serve() Pattern (PRG)

```python
from django.template.response import TemplateResponse

class ContactPage(MetadataPageMixin, Page):
    def serve(self, request):
        from .forms import ContactForm
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                submission = form.save()
                # Send email notification here
                return redirect(self.url + "?success=true")
        else:
            form = ContactForm()
        return TemplateResponse(request, self.get_template(request), {
            "page": self, "self": self, "form": form,
        })
```

### Admin Listing Pattern (wagtail_hooks.py)

```python
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail import hooks

class MySubmissionViewSet(SnippetViewSet):
    model = MySubmission
    menu_label = "Submissions"
    menu_order = 100
    list_display = ["name", "email", "date", "read"]
    search_fields = ["name", "email"]
    list_filter = ["read", "date"]
    inspect_view_enabled = True
    add_to_admin_menu = True

@hooks.register("register_snippet_viewsets")
def register_viewsets():
    return [MySubmissionViewSet]
```

### SiteSettings Access in Templates

```html
{% load wagtailsettings_tags %} {{ settings.common.SiteSettings.company_name }}
{{ settings.common.SiteSettings.phone_primary }} {% if
settings.common.SiteSettings.whatsapp_number %}...{% endif %}
```

### Tailwind Config Pattern

```javascript
module.exports = {
  content: [
    "./templates/**/*.html",
    "./apps/**/templates/**/*.html",
    "./static/js/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        primary: { DEFAULT: "#0284C7", light: "#38BDF8", dark: "#0369A1" },
        secondary: "#1E3A5F",
        accent: "#F59E0B",
        surface: "#F0F9FF",
      },
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"],
      },
    },
  },
};
```

---

## Section 6 — Lessons Learned & Pitfalls

### Things That Go Wrong

| Problem                                    | Cause                                                                  | Solution                                                                                           |
| ------------------------------------------ | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `self.render()` crashes on ContactPage     | Wagtail Page.render() doesn't accept request properly in serve()       | Use `TemplateResponse(request, template, context)` instead                                         |
| Page tree corruption after deleting pages  | Wagtail uses treebeard (materialized path)                             | Always call `Page.fix_tree()` after manual page deletion                                           |
| Tailwind classes not applying              | Content paths in tailwind.config.js don't cover all template locations | Include BOTH `./templates/**/*.html` AND `./apps/**/templates/**/*.html`                           |
| Prettier/formatter breaks Django templates | HTML formatters don't understand `{% %}` and `{{ }}` tags              | Create `.prettierignore` with `*.html`                                                             |
| Missing pages discovered mid-build         | Requirements not fully analyzed before planning                        | Review ALL pages at planning time. Each missing page = model + template + nav + setup_pages update |
| Template tags not loading                  | Forgot to add `{% load %}` at top, or wrong tag library                | Always specify exact loads: `{% load wagtailcore_tags wagtailimages_tags wagtailsettings_tags %}`  |
| Images broken in production                | Using `image.file.url` instead of Wagtail renditions                   | Always use `{% image obj fill-WxH as img %}` then `{{ img.url }}`                                  |
| Google Analytics not injecting             | Field exists in SiteSettings but no script in base.html                | Must add `{% if %}` conditional gtag.js script block in `<head>`                                   |
| Favicon not rendering                      | SiteSettings has favicon field but no `<link>` tag in HTML             | Must add explicit `<link rel="icon">` tags using `{% image %}` renditions                          |
| Deploy check warnings in dev               | `manage.py check --deploy` flags dev settings                          | Expected — production.py has all security settings properly configured                             |

### Performance Checklist

- [ ] `loading="lazy"` on all images EXCEPT hero/above-fold
- [ ] Tailwind CSS built with `--minify` flag
- [ ] Google Fonts loaded with `display=swap`
- [ ] Font preconnect hints in `<head>`
- [ ] Alpine.js loaded with `defer`
- [ ] Images served via Wagtail renditions (auto-resized)

### Accessibility Checklist

- [ ] `focus:ring-2 focus:ring-primary focus:outline-none` on all interactive elements
- [ ] ARIA labels on modals, lightboxes, hamburger menu
- [ ] Semantic HTML tags (`<article>`, `<section>`, `<nav>`, `<main>`)
- [ ] `role="dialog"` and `aria-modal="true"` on modals
- [ ] Keyboard navigation for lightbox (Escape, ArrowLeft, ArrowRight)
- [ ] Skip-to-content link (optional but recommended)

### SEO Checklist

- [ ] `wagtail-metadata` installed, `MetadataPageMixin` on ALL page models
- [ ] `{% meta_tags %}` in base.html `<head>`
- [ ] `<link rel="canonical">` on every page
- [ ] JSON-LD Organization schema in base.html
- [ ] `/sitemap.xml` via `WagtailSitemap`
- [ ] `/robots.txt` with proper Allow/Disallow rules + Sitemap reference
- [ ] Google Analytics conditional injection in base.html

---

## Section 7 — Naming Conventions

| Item                | Convention                         | Example                                                                 |
| ------------------- | ---------------------------------- | ----------------------------------------------------------------------- |
| App names           | Lowercase, singular or descriptive | `home`, `products`, `blog`, `contact`, `enquiry`, `downloads`, `common` |
| Page models         | PascalCase, ends with `Page`       | `HomePage`, `ProductPage`, `ContactPage`                                |
| Index pages         | PascalCase, ends with `IndexPage`  | `ProductIndexPage`, `BlogIndexPage`                                     |
| Snippet models      | PascalCase, descriptive            | `DownloadItem`, `SiteSettings`                                          |
| Submission models   | PascalCase, ends with `Submission` | `ContactFormSubmission`, `EnquiryFormSubmission`                        |
| Orderable models    | PascalCase, descriptive            | `ProductGalleryImage`, `FeaturedProduct`                                |
| Template files      | snake_case matching model          | `home_page.html`, `product_page.html`                                   |
| URL slugs           | kebab-case                         | `about-us`, `bend-dies`, `contact-us`                                   |
| CSS classes         | Tailwind utilities                 | No custom CSS classes unless absolutely necessary                       |
| Management commands | snake_case                         | `setup_pages`                                                           |

---

## Section 8 — Dependencies (requirements files)

### base.txt

```
Django>=5.2,<6.0
wagtail>=6.4,<7.0
wagtail-metadata>=5.0
```

### dev.txt

```
-r base.txt
django-debug-toolbar
```

### production.txt

```
-r base.txt
gunicorn
whitenoise
PyMySQL
```

---

## Section 9 — Context Window Optimization

When working with AI on a multi-prompt build plan:

1. **Conversation summary is your friend** — after ~10 prompts, the AI uses summarized context. Key facts must be in the plan document, not just conversation history.

2. **Master plan as source of truth** — the `00-master-plan.md` file should contain:
   - Company context (1-2 lines)
   - Phase table
   - All prompts with checkbox status
   - Tech stack reference

3. **Each prompt file should be self-contained** — include enough context that the AI can execute it without reading 5 other files.

4. **Mark completed prompts** — `[x]` in master plan so AI knows current position.

5. **State the current prompt** — always say "next prompt" or "execute prompt XX" to maintain sequential order.

6. **Don't mix planning and execution** — plan all prompts first (Phase 0), then execute one at a time.

7. **Course corrections** — if you need to add pages mid-build:
   - Create new prompt files
   - Renumber subsequent prompts
   - Update master plan phase table
   - Remember: each new page needs model + template + setup_pages + nav update

---

## Section 10 — Go-Live Verification Template

Before going live, verify:

### Code Complete

- [ ] All page models created and migrated
- [ ] All templates rendering without errors
- [ ] All forms processing and saving to DB
- [ ] Admin listings registered for all submission types
- [ ] `setup_pages` command creates full page tree
- [ ] Navigation links to all pages (desktop + mobile)

### Content Ready

- [ ] All product/service content entered
- [ ] Images uploaded (logo, favicon, product images, banners)
- [ ] Contact information filled in SiteSettings
- [ ] Social media links configured
- [ ] Blog has at least 1 post
- [ ] Downloads section has at least 1 file

### Production Config

- [ ] `SECRET_KEY` changed from default
- [ ] `DEBUG = False`
- [ ] `ALLOWED_HOSTS` set to domain
- [ ] Database configured
- [ ] `collectstatic` run
- [ ] Email SMTP configured
- [ ] HTTPS enabled

### Post-Launch

- [ ] Submit sitemap to Google Search Console
- [ ] Test all forms on production
- [ ] Set up error monitoring
- [ ] Set up database backups
- [ ] Monitor server logs
