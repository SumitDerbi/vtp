from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page


class HomePage(Page):
    max_count = 1

    # Hero Section
    hero_title = models.CharField(max_length=255, default="Precision Tooling Solutions")
    hero_subtitle = models.TextField(
        default="Manufacturing excellence in tube bending dies and tooling"
    )
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hero_cta_text = models.CharField(max_length=100, default="View Our Products")
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    # About Snippet on Home
    about_heading = models.CharField(max_length=255, default="About VPT")
    about_text = RichTextField(blank=True)
    about_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    # CTA Section
    cta_heading = models.CharField(max_length=255, default="Need Custom Tooling?")
    cta_text = models.TextField(default="Contact us for precision-engineered solutions")
    cta_button_text = models.CharField(max_length=100, default="Get in Touch")
    cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("hero_title"),
                FieldPanel("hero_subtitle"),
                FieldPanel("hero_image"),
                FieldPanel("hero_cta_text"),
                FieldPanel("hero_cta_link"),
            ],
            heading="Hero Section",
        ),
        InlinePanel("featured_products", label="Featured Products", max_num=6),
        MultiFieldPanel(
            [
                FieldPanel("about_heading"),
                FieldPanel("about_text"),
                FieldPanel("about_image"),
            ],
            heading="About Section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("cta_heading"),
                FieldPanel("cta_text"),
                FieldPanel("cta_button_text"),
                FieldPanel("cta_link"),
            ],
            heading="Call to Action",
        ),
    ]


class FeaturedProduct(Orderable):
    page = ParentalKey(HomePage, related_name="featured_products")
    product_page = models.ForeignKey(
        "wagtailcore.Page", on_delete=models.CASCADE, related_name="+"
    )

    panels = [FieldPanel("product_page")]
