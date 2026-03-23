# Prompt 17 — BlogIndexPage & BlogPost Models

## Goal

Create the blog section with index and post pages.

## Prompt

```
Create the Blog models for VTP.

File: apps/blog/models.py

1. BlogIndexPage(Page):
   - max_count = 1
   - parent_page_types = ['home.HomePage']
   - subpage_types = ['blog.BlogPost']

   Fields:
   - intro = RichTextField(blank=True)

   content_panels = Page.content_panels + [
       FieldPanel('intro'),
   ]

   def get_context(self, request):
       context = super().get_context(request)
       posts = BlogPost.objects.live().child_of(self).order_by('-date')
       context['posts'] = posts
       return context

2. BlogPost(Page):
   - parent_page_types = ['blog.BlogIndexPage']
   - subpage_types = []

   Fields:
   - date = DateField("Post date")
   - excerpt = TextField(blank=True, help_text="Short summary for listings")
   - body = RichTextField()
   - featured_image = ForeignKey('wagtailimages.Image', null=True, blank=True,
       on_delete=SET_NULL, related_name='+')
   - author = CharField(max_length=255, blank=True)

   content_panels = Page.content_panels + [
       FieldPanel('date'),
       FieldPanel('author'),
       FieldPanel('featured_image'),
       FieldPanel('excerpt'),
       FieldPanel('body'),
   ]

Run: python manage.py makemigrations blog && python manage.py migrate
```

## Verification

1. Migrations run
2. BlogIndexPage can be created under Home
3. BlogPost can be created under BlogIndex
4. Posts ordered by date (newest first)

## Expected Result

- Simple blog with index and post pages
