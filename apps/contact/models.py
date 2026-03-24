from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtailmetadata.models import MetadataPageMixin


class ContactPage(MetadataPageMixin, Page):
    max_count = 1
    parent_page_types = ["home.HomePage"]
    subpage_types = []

    def serve(self, request):
        from django.template.response import TemplateResponse

        from .forms import ContactForm

        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                submission = form.save()
                self.send_notification_email(submission)
                from django.shortcuts import redirect
                return redirect(self.url + "?submitted=true")
        else:
            form = ContactForm()

        context = self.get_context(request)
        context["form"] = form
        context["submitted"] = request.GET.get("submitted") == "true"

        return TemplateResponse(
            request,
            self.get_template(request),
            context,
        )

    def send_notification_email(self, submission):
        from django.core.mail import send_mail

        recipient = self.notification_email or self.email
        if recipient:
            send_mail(
                subject=f"New Contact Form: {submission.subject or 'No Subject'}",
                message=(
                    f"Name: {submission.name}\n"
                    f"Email: {submission.email}\n"
                    f"Phone: {submission.phone}\n"
                    f"Company: {submission.company}\n\n"
                    f"Message:\n{submission.message}"
                ),
                from_email=None,
                recipient_list=[recipient],
                fail_silently=True,
            )

    intro = RichTextField(blank=True)
    address = models.TextField(
        blank=True, help_text="Overrides SiteSettings address if filled"
    )
    phone = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    google_maps_embed = models.TextField(
        blank=True, help_text="Paste Google Maps embed iframe code"
    )
    form_heading = models.CharField(
        max_length=255, default="Send us a Message"
    )
    success_message = models.TextField(
        default="Thank you for contacting us. We will get back to you shortly."
    )
    notification_email = models.EmailField(
        blank=True, help_text="Email to receive form submissions"
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        MultiFieldPanel(
            [
                FieldPanel("address"),
                FieldPanel("phone"),
                FieldPanel("email"),
                FieldPanel("google_maps_embed"),
            ],
            heading="Contact Details",
        ),
        MultiFieldPanel(
            [
                FieldPanel("form_heading"),
                FieldPanel("success_message"),
                FieldPanel("notification_email"),
            ],
            heading="Form Settings",
        ),
    ]


class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.subject or 'No Subject'} ({self.created_at:%Y-%m-%d})"
