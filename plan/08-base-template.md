# Prompt 08 — Create base.html Template

## Goal

Create the base HTML template that all pages will extend.

## Prompt

```
Create the base template for the VTP website.

File: templates/base.html

This should be a complete HTML5 template with:

1. DOCTYPE html, lang="en"
2. <head> section:
   - meta charset, viewport, description
   - {% block title %}{{ self.seo_title|default:self.title }} | Vinsat Precision Technologies{% endblock %}
   - Google Fonts: Inter (400, 500, 600, 700)
   - Link to /static/css/output.css (Tailwind)
   - {% block extra_css %}{% endblock %}
   - Favicon from SiteSettings (with fallback)

3. <body> with Tailwind classes (bg-white text-gray-800 font-sans antialiased):
   - {% include "includes/header.html" %}
   - {% block breadcrumbs %}{% endblock %}
   - <main>{% block content %}{% endblock %}</main>
   - {% include "includes/footer.html" %}
   - Alpine.js CDN script
   - {% block extra_js %}{% endblock %}

4. Use Wagtail template tags:
   {% load static wagtailcore_tags wagtailuserbar %}
   - Include {% wagtailuserbar %} for logged-in admin users

5. Create EMPTY placeholder files:
   - templates/includes/header.html (just <!-- Header placeholder -->)
   - templates/includes/footer.html (just <!-- Footer placeholder -->)

Include these blocks:
- title, meta_description, extra_css, breadcrumbs, content, extra_js

Clean, semantic HTML. White background default.
```

## Verification

1. `templates/base.html` exists
2. Includes exist
3. `python manage.py runserver` — no template errors

## Expected Result

- Base template ready for child templates to extend
- Alpine.js loaded for interactive components
