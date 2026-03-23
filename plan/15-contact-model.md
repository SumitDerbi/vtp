# Prompt 15 — ContactPage & ContactFormSubmission Models

## Goal

Create the Contact page with form submission storage.

## Prompt

```
Create the Contact models for VTP.

File: apps/contact/models.py

1. ContactPage(Page):
   - max_count = 1
   - parent_page_types = ['home.HomePage']
   - subpage_types = []

   Fields:
   - intro = RichTextField(blank=True)
   - address = TextField(blank=True, help_text="Overrides SiteSettings address if filled")
   - phone = CharField(max_length=100, blank=True)
   - email = EmailField(blank=True)
   - google_maps_embed = TextField(blank=True,
       help_text="Paste Google Maps embed iframe code")
   - form_heading = CharField(max_length=255, default="Send us a Message")
   - success_message = TextField(
       default="Thank you for contacting us. We will get back to you shortly.")
   - notification_email = EmailField(blank=True,
       help_text="Email to receive form submissions")

   content_panels = Page.content_panels + [
       FieldPanel('intro'),
       MultiFieldPanel([
           FieldPanel('address'),
           FieldPanel('phone'),
           FieldPanel('email'),
           FieldPanel('google_maps_embed'),
       ], heading="Contact Details"),
       MultiFieldPanel([
           FieldPanel('form_heading'),
           FieldPanel('success_message'),
           FieldPanel('notification_email'),
       ], heading="Form Settings"),
   ]

2. ContactFormSubmission(Model):
   - name = CharField(max_length=255)
   - email = EmailField()
   - phone = CharField(max_length=50, blank=True)
   - company = CharField(max_length=255, blank=True)
   - subject = CharField(max_length=255, blank=True)
   - message = TextField()
   - created_at = DateTimeField(auto_now_add=True)
   - is_read = BooleanField(default=False)

   class Meta:
       ordering = ['-created_at']

   def __str__(self):
       return f"{self.name} — {self.subject or 'No Subject'} ({self.created_at:%Y-%m-%d})"

Run: python manage.py makemigrations contact && python manage.py migrate
```

## Verification

1. Migrations run
2. ContactPage can be created under Home
3. ContactFormSubmission model exists in DB

## Expected Result

- ContactPage model with configurable form settings
- ContactFormSubmission stored in database for admin listing
