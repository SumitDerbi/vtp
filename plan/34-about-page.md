# Prompt 34 — About Page (Model + Template)

## Goal

Create the About page — model, template, and add to page tree.

## Prompt

```
Create the About page for VTP.

1. Model (apps/home/models.py — reuse home app):
   - AboutPage(MetadataPageMixin, Page)
   - parent_page_types = ["home.HomePage"]
   - subpage_types = []
   - Fields:
     - heading (CharField, max_length=255, default="About Us")
     - intro (TextField, blank=True — short intro paragraph)
     - body (RichTextField — main content)
     - mission_heading (CharField, max_length=255, blank=True)
     - mission_text (TextField, blank=True)
     - vision_heading (CharField, max_length=255, blank=True)
     - vision_text (TextField, blank=True)
     - banner_image (ForeignKey to wagtailimages.Image, blank=True, null=True)
   - content_panels with FieldPanel for each field
   - max_count = 1

2. Template (templates/home/about_page.html):
   - Extends base.html
   - Hero/banner section with banner_image and heading
   - Intro paragraph in a readable centered layout
   - Body content (rich text)
   - Mission & Vision side-by-side cards (if filled)
   - CTA banner include at bottom
   - Breadcrumbs

3. Update setup_pages command:
   - Add AboutPage as child of HomePage (title="About Us")

4. Update header navigation:
   - Add "About" link in header.html nav
```

## Verification

1. /about/ page renders correctly
2. About link visible in navigation
3. Content editable in Wagtail admin
4. Responsive layout

## Expected Result

- Professional About page with mission/vision sections
