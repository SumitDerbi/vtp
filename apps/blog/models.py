from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtailmetadata.models import MetadataPageMixin


class BlogIndexPage(MetadataPageMixin, Page):
    max_count = 1
    parent_page_types = ["home.HomePage"]
    subpage_types = ["blog.BlogPost"]

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        posts = BlogPost.objects.live().child_of(self).order_by("-date")
        context["posts"] = posts
        return context


class BlogPost(MetadataPageMixin, Page):
    parent_page_types = ["blog.BlogIndexPage"]
    subpage_types = []

    date = models.DateField("Post date")
    excerpt = models.TextField(blank=True, help_text="Short summary for listings")
    body = RichTextField()
    featured_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    author = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("author"),
        FieldPanel("featured_image"),
        FieldPanel("excerpt"),
        FieldPanel("body"),
    ]
