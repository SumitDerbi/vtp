from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


class DownloadIndexPage(Page):
    max_count = 1
    parent_page_types = ["home.HomePage"]
    subpage_types = []

    heading = models.CharField(max_length=255, default="Downloads")
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("heading"),
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["downloads"] = DownloadItem.objects.filter(
            is_active=True
        ).order_by("-created_at")
        return context


@register_snippet
class DownloadItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.ForeignKey(
        "wagtaildocs.Document",
        on_delete=models.CASCADE,
        related_name="+",
    )
    thumbnail = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Optional thumbnail/preview image",
    )
    category = models.CharField(
        max_length=100,
        blank=True,
        help_text="e.g., Brochure, Catalog, Technical Sheet",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("file"),
        FieldPanel("thumbnail"),
        FieldPanel("category"),
        FieldPanel("is_active"),
    ]

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
