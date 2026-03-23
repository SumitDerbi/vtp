# Prompt 11 — Create SiteSettings Model

## Goal

Create global site settings editable from Wagtail admin, available in all templates.

## Prompt

```
Create the SiteSettings model for VTP.

File: apps/common/models.py

Create a Wagtail SiteSetting model using BaseSiteSetting:

from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

@register_setting
class SiteSettings(BaseSiteSetting):
    # Company Info
    company_name = CharField(max_length=255, default='Vinsat Precision Technologies')
    tagline = CharField(max_length=255, default='Precision Tooling Solutions')

    # Logo — support both PNG and SVG
    logo = ForeignKey('wagtailimages.Image', null=True, blank=True,
        on_delete=SET_NULL, related_name='+', help_text="PNG/JPG logo")
    logo_svg = FileField(upload_to='logos/', blank=True,
        help_text="SVG logo (preferred). Upload SVG file here.")
    favicon = ForeignKey('wagtailimages.Image', null=True, blank=True,
        on_delete=SET_NULL, related_name='+')

    # Contact
    phone_primary = CharField(max_length=50, blank=True)
    phone_secondary = CharField(max_length=50, blank=True)
    email = EmailField(blank=True)
    address = TextField(blank=True)

    # Social Media
    linkedin_url = URLField(blank=True)
    facebook_url = URLField(blank=True)
    instagram_url = URLField(blank=True)
    youtube_url = URLField(blank=True)
    twitter_url = URLField(blank=True)

    # WhatsApp
    whatsapp_number = CharField(max_length=20, blank=True,
        help_text="Include country code, e.g., 919876543210")

    # Analytics
    google_analytics_id = CharField(max_length=50, blank=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('company_name'),
            FieldPanel('tagline'),
            FieldPanel('logo'),
            FieldPanel('logo_svg'),
            FieldPanel('favicon'),
        ], heading="Company"),
        MultiFieldPanel([
            FieldPanel('phone_primary'),
            FieldPanel('phone_secondary'),
            FieldPanel('email'),
            FieldPanel('address'),
        ], heading="Contact"),
        MultiFieldPanel([
            FieldPanel('linkedin_url'),
            FieldPanel('facebook_url'),
            FieldPanel('instagram_url'),
            FieldPanel('youtube_url'),
            FieldPanel('twitter_url'),
            FieldPanel('whatsapp_number'),
        ], heading="Social Media"),
        MultiFieldPanel([
            FieldPanel('google_analytics_id'),
        ], heading="Analytics"),
    ]

Ensure 'wagtail.contrib.settings' is in INSTALLED_APPS.
Ensure 'wagtail.contrib.settings.context_processors.settings' is in TEMPLATES context processors.

Run: python manage.py makemigrations common && python manage.py migrate
```

## Verification

1. Migrations run without errors
2. Wagtail admin → Settings → Site Settings appears
3. Can fill in all fields and save
4. Settings accessible in templates via {{ settings.common.SiteSettings.company_name }}

## Expected Result

- SiteSettings model with logo (PNG + SVG support), contact, social media
