# Prompt 13 — HomePage Model with Hero Section

## Goal

Create the HomePage model with hero section, featured products, and about snippet.

## Prompt

```
Create the HomePage model for VTP.

File: apps/home/models.py

1. HomePage(Page):
   - max_count = 1
   - subpage_types = ['products.ProductIndexPage', 'contact.ContactPage',
                       'blog.BlogIndexPage', 'downloads.DownloadIndexPage']

   Fields:
   # Hero Section
   - hero_title = CharField(max_length=255, default="Precision Tooling Solutions")
   - hero_subtitle = TextField(default="Manufacturing excellence in tube bending dies and tooling")
   - hero_image = ForeignKey('wagtailimages.Image', null=True, blank=True,
       on_delete=SET_NULL, related_name='+')
   - hero_cta_text = CharField(max_length=100, default="View Our Products")
   - hero_cta_link = ForeignKey('wagtailcore.Page', null=True, blank=True,
       on_delete=SET_NULL, related_name='+')

   # About Snippet on Home
   - about_heading = CharField(max_length=255, default="About VPT")
   - about_text = RichTextField(blank=True)
   - about_image = ForeignKey('wagtailimages.Image', null=True, blank=True,
       on_delete=SET_NULL, related_name='+')

   # CTA Section
   - cta_heading = CharField(max_length=255, default="Need Custom Tooling?")
   - cta_text = TextField(default="Contact us for precision-engineered solutions")
   - cta_button_text = CharField(max_length=100, default="Get in Touch")
   - cta_link = ForeignKey('wagtailcore.Page', null=True, blank=True,
       on_delete=SET_NULL, related_name='+')

   content_panels = Page.content_panels + [
       MultiFieldPanel([
           FieldPanel('hero_title'),
           FieldPanel('hero_subtitle'),
           FieldPanel('hero_image'),
           FieldPanel('hero_cta_text'),
           FieldPanel('hero_cta_link'),
       ], heading="Hero Section"),
       InlinePanel('featured_products', label="Featured Products", max_num=6),
       MultiFieldPanel([
           FieldPanel('about_heading'),
           FieldPanel('about_text'),
           FieldPanel('about_image'),
       ], heading="About Section"),
       MultiFieldPanel([
           FieldPanel('cta_heading'),
           FieldPanel('cta_text'),
           FieldPanel('cta_button_text'),
           FieldPanel('cta_link'),
       ], heading="Call to Action"),
   ]

2. FeaturedProduct(Orderable):
   - page = ParentalKey(HomePage, related_name='featured_products')
   - product_page = ForeignKey('wagtailcore.Page', on_delete=CASCADE, related_name='+')

   panels = [PageChooserPanel('product_page')]

Run: python manage.py makemigrations home && python manage.py migrate
```

## Verification

1. Migrations run
2. Wagtail admin → can edit HomePage
3. Hero section fields appear
4. Featured products inline works
5. About section fields appear
6. CTA section fields appear

## Expected Result

- HomePage model with hero, featured products, about snippet, and CTA
