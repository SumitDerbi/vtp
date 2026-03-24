# Prompt 35 — Facility Page (Model + Template)

## Goal

Create the Facility page — model, template, and add to page tree.

## Prompt

```
Create the Facility page for VTP.

1. Model (apps/home/models.py — reuse home app):
   - FacilityPage(MetadataPageMixin, Page)
   - parent_page_types = ["home.HomePage"]
   - subpage_types = []
   - Fields:
     - heading (CharField, max_length=255, default="Our Facility")
     - intro (TextField, blank=True — short intro paragraph)
     - body (RichTextField — main content describing manufacturing facility)
     - banner_image (ForeignKey to wagtailimages.Image, blank=True, null=True)
   - FacilityGalleryImage (Orderable, ParentalKey to FacilityPage):
     - image (ForeignKey to wagtailimages.Image)
     - caption (CharField, max_length=255, blank=True)
   - content_panels with FieldPanel for each field + InlinePanel("gallery_images")
   - max_count = 1

2. Template (templates/home/facility_page.html):
   - Extends base.html
   - Hero/banner section with banner_image and heading
   - Intro paragraph
   - Body content (rich text)
   - Image gallery grid (responsive — 2 cols mobile, 3 cols desktop)
     - Alpine.js lightbox/modal on click (similar to product gallery)
   - Breadcrumbs

3. Update setup_pages command:
   - Add FacilityPage as child of HomePage (title="Our Facility")

4. Update header navigation:
   - Add "Facility" link in header.html nav (after About)
```

## Verification

1. /facility/ page renders correctly
2. Facility link visible in navigation
3. Gallery images display in grid with lightbox
4. Content editable in Wagtail admin
5. Responsive layout

## Expected Result

- Facility showcase page with image gallery highlighting manufacturing capabilities
