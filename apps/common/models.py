from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting
class SiteSettings(BaseSiteSetting):
    # Company Info
    company_name = models.CharField(max_length=255, default="Vinsat Precision Technologies")
    tagline = models.CharField(max_length=255, default="Precision Tooling Solutions")

    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="PNG/JPG logo",
    )
    logo_svg = models.FileField(upload_to="logos/", blank=True, help_text="SVG logo (preferred)")
    favicon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    # Contact
    phone_primary = models.CharField(max_length=50, blank=True)
    phone_secondary = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    # Social Media
    linkedin_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)

    # WhatsApp
    whatsapp_number = models.CharField(
        max_length=20, blank=True, help_text="Include country code, e.g., 919876543210"
    )

    # Analytics
    google_analytics_id = models.CharField(max_length=50, blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("company_name"),
                FieldPanel("tagline"),
                FieldPanel("logo"),
                FieldPanel("logo_svg"),
                FieldPanel("favicon"),
            ],
            heading="Company",
        ),
        MultiFieldPanel(
            [
                FieldPanel("phone_primary"),
                FieldPanel("phone_secondary"),
                FieldPanel("email"),
                FieldPanel("address"),
            ],
            heading="Contact",
        ),
        MultiFieldPanel(
            [
                FieldPanel("linkedin_url"),
                FieldPanel("facebook_url"),
                FieldPanel("instagram_url"),
                FieldPanel("youtube_url"),
                FieldPanel("twitter_url"),
                FieldPanel("whatsapp_number"),
            ],
            heading="Social Media",
        ),
        MultiFieldPanel(
            [
                FieldPanel("google_analytics_id"),
            ],
            heading="Analytics",
        ),
    ]

    class Meta:
        verbose_name = "Site Settings"
