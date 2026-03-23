# Prompt 23 — BlogIndexPage & BlogPost Templates

## Goal

Create blog listing and detail templates.

## Prompt

```
Create the Blog templates for VTP.

1. File: apps/blog/templates/blog/blog_index_page.html

   {% extends "base.html" %}
   {% load wagtailcore_tags wagtailimages_tags %}

   Sections:
   - Breadcrumbs
   - Page header: "Blog" heading + intro
   - Blog post grid: lg:grid-cols-3, md:grid-cols-2, grid-cols-1
   - Each post card:
     - Featured image (fill-400x250, fallback gray)
     - Date (text-sm, text-steel)
     - Title (font-semibold, text-secondary)
     - Excerpt (text-gray-600, line-clamp-3)
     - "Read More" link (text-primary)
   - Card: white bg, rounded-xl, shadow
   - Empty state: "No blog posts yet"

2. File: apps/blog/templates/blog/blog_post.html

   {% extends "base.html" %}
   {% load wagtailcore_tags wagtailimages_tags %}

   Sections:
   - Breadcrumbs
   - Article header:
     - Title (text-4xl, font-bold, text-secondary)
     - Meta: date + author (text-steel)
   - Featured image (full-width, rounded-lg, max-h-96 object-cover)
   - Article body (prose-like styling, max-w-3xl mx-auto)
     - RichTextField with proper typography
     - Images responsive
   - Back to blog link
   - CTA banner at bottom

   Content container: max-w-4xl mx-auto px-4

Clean, readable blog layout. Good typography for long-form content.
```

## Verification

1. Blog index shows post grid
2. Blog post renders with full content
3. Images display correctly
4. Responsive
5. Empty state handled

## Expected Result

- Clean blog section with listing and detail pages
