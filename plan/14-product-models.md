# Prompt 14 — ProductIndexPage & ProductPage Models

## Goal

Create the product catalog models — index page and individual product pages.

## Prompt

```
Create the Product models for VTP.

File: apps/products/models.py

1. ProductIndexPage(Page):
   - max_count = 1
   - parent_page_types = ['home.HomePage']
   - subpage_types = ['products.ProductPage']

   Fields:
   - intro = RichTextField(blank=True)
   - heading = CharField(max_length=255, default="Our Products")

   content_panels = Page.content_panels + [
       FieldPanel('heading'),
       FieldPanel('intro'),
   ]

   def get_context(self, request):
       context = super().get_context(request)
       context['products'] = ProductPage.objects.live().child_of(self).order_by('title')
       return context

2. ProductPage(Page):
   - parent_page_types = ['products.ProductIndexPage']
   - subpage_types = []

   Fields:
   - short_description = TextField(blank=True, help_text="Brief description for cards/listings")
   - description = RichTextField(blank=True, help_text="Full product description")
   - main_image = ForeignKey('wagtailimages.Image', on_delete=SET_NULL,
       null=True, blank=True, related_name='+')
   - specifications = RichTextField(blank=True,
       help_text="Technical specifications table or list")
   - features = RichTextField(blank=True, help_text="Key features and benefits")

   content_panels = Page.content_panels + [
       FieldPanel('short_description'),
       FieldPanel('main_image'),
       FieldPanel('description'),
       FieldPanel('specifications'),
       FieldPanel('features'),
       InlinePanel('gallery_images', label="Product Gallery", max_num=10),
   ]

3. ProductGalleryImage(Orderable):
   - page = ParentalKey(ProductPage, related_name='gallery_images')
   - image = ForeignKey('wagtailimages.Image', on_delete=CASCADE, related_name='+')
   - caption = CharField(max_length=255, blank=True)

   panels = [
       FieldPanel('image'),
       FieldPanel('caption'),
   ]

Run: python manage.py makemigrations products && python manage.py migrate

Products are simple — few items, each with image gallery, description, specs.
No categories needed (client has few products).
```

## Verification

1. Migrations run
2. Can create ProductIndexPage under Home
3. Can create ProductPage under ProductIndex
4. Gallery images inline works
5. Product listing shows in context

## Expected Result

- Clean product catalog: index page + individual product pages with gallery
