from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page


class ProductIndexPage(Page):
    max_count = 1
    parent_page_types = ["home.HomePage"]
    subpage_types = ["products.ProductPage"]

    heading = models.CharField(max_length=255, default="Our Products")
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("heading"),
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["products"] = (
            ProductPage.objects.live().child_of(self).order_by("title")
        )
        return context


class ProductPage(Page):
    parent_page_types = ["products.ProductIndexPage"]
    subpage_types = []

    short_description = models.TextField(
        blank=True, help_text="Brief description for cards/listings"
    )
    description = RichTextField(
        blank=True, help_text="Full product description"
    )
    main_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    specifications = RichTextField(
        blank=True, help_text="Technical specifications table or list"
    )
    features = RichTextField(
        blank=True, help_text="Key features and benefits"
    )

    content_panels = Page.content_panels + [
        FieldPanel("short_description"),
        FieldPanel("main_image"),
        FieldPanel("description"),
        FieldPanel("specifications"),
        FieldPanel("features"),
        InlinePanel("gallery_images", label="Product Gallery", max_num=10),
    ]


class ProductGalleryImage(Orderable):
    page = ParentalKey(ProductPage, related_name="gallery_images")
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.CASCADE,
        related_name="+",
    )
    caption = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel("image"),
        FieldPanel("caption"),
    ]
