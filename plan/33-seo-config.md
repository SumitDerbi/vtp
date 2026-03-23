# Prompt 33 — SEO Meta Tags, Sitemap, Robots.txt

## Goal

Add SEO essentials — meta tags, sitemap, and robots.txt.

## Prompt

```
Add SEO configuration for VTP website.

1. Add wagtail-metadata support to all page models:
   - All page models should inherit from MetadataPageMixin
   - Provides OG tags, Twitter cards, meta description
   - Update base.html <head> to include:
     {% load wagtailmetadata_tags %}
     {% meta_tags %}

2. Create sitemap configuration:
   - Add 'django.contrib.sitemaps' to INSTALLED_APPS
   - Add Wagtail sitemap URL in urls.py:
     from wagtail.contrib.sitemaps import Sitemap as WagtailSitemap
     path('sitemap.xml', sitemap_views.sitemap, {'sitemaps': {'wagtail': WagtailSitemap}})

3. Create robots.txt:
   - Template: templates/robots.txt
   - Allow all crawlers
   - Sitemap: https://yourdomain.com/sitemap.xml
   - Disallow: /admin/
   - Add URL in urls.py:
     path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'))

4. Update base.html:
   - Add canonical URL
   - Add structured data (JSON-LD) for Organization
```

## Verification

1. View page source — OG tags present
2. /sitemap.xml — lists all published pages
3. /robots.txt — correct content
4. Meta descriptions editable in Wagtail admin

## Expected Result

- SEO-ready website with meta tags, sitemap, robots.txt
