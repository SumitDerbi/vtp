# Prompt 18 — DownloadIndexPage & DownloadItem Models

## Goal

Create the downloads section where admin can add files with title and description.

## Prompt

```
Create the Downloads models for VTP.

File: apps/downloads/models.py

1. DownloadIndexPage(Page):
   - max_count = 1
   - parent_page_types = ['home.HomePage']
   - subpage_types = []

   Fields:
   - intro = RichTextField(blank=True)
   - heading = CharField(max_length=255, default="Downloads")

   content_panels = Page.content_panels + [
       FieldPanel('heading'),
       FieldPanel('intro'),
   ]

   def get_context(self, request):
       context = super().get_context(request)
       context['downloads'] = DownloadItem.objects.all().order_by('-created_at')
       return context

2. DownloadItem(Model):     ← NOT a Page, it's a Wagtail Snippet
   - title = CharField(max_length=255)
   - description = TextField(blank=True)
   - file = ForeignKey('wagtaildocs.Document', on_delete=CASCADE, related_name='+')
   - thumbnail = ForeignKey('wagtailimages.Image', null=True, blank=True,
       on_delete=SET_NULL, related_name='+',
       help_text="Optional thumbnail/preview image")
   - category = CharField(max_length=100, blank=True,
       help_text="e.g., Brochure, Catalog, Technical Sheet")
   - created_at = DateTimeField(auto_now_add=True)
   - is_active = BooleanField(default=True)

   panels = [
       FieldPanel('title'),
       FieldPanel('description'),
       FieldPanel('file'),
       FieldPanel('thumbnail'),
       FieldPanel('category'),
       FieldPanel('is_active'),
   ]

   class Meta:
       ordering = ['-created_at']

   def __str__(self):
       return self.title

Register DownloadItem as a Wagtail Snippet using @register_snippet decorator.
This way admin can manage downloads from Wagtail admin → Snippets → Downloads.

Admin can add title, description, and upload files (PDF, docs, etc.).
The DownloadIndexPage template will list all active DownloadItems.

Run: python manage.py makemigrations downloads && python manage.py migrate
```

## Verification

1. Migrations run
2. DownloadIndexPage can be created under Home
3. Wagtail admin → Snippets → Download Items appears
4. Can add downloads with title, description, file
5. DownloadIndexPage context includes all active downloads

## Expected Result

- Downloads managed as Wagtail Snippets (no page tree clutter)
- Admin adds title + description + file upload
- DownloadIndexPage lists all downloads
