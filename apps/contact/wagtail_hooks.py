from wagtail import hooks
from wagtail.admin.panels import FieldPanel
from wagtail.admin.ui.tables import BooleanColumn, DateColumn
from wagtail.admin.viewsets.model import ModelViewSet

from .models import ContactFormSubmission


class ContactSubmissionViewSet(ModelViewSet):
    model = ContactFormSubmission
    icon = "mail"
    menu_label = "Contact Responses"
    menu_order = 100
    add_to_admin_menu = True
    list_display = [
        "name",
        "email",
        "subject",
        DateColumn("created_at", label="Date"),
        BooleanColumn("is_read", label="Read"),
    ]
    list_filter = ["is_read", "created_at"]
    search_fields = ["name", "email", "subject", "message"]
    ordering = ["-created_at"]
    inspect_view_enabled = True
    form_fields = ["name", "email", "phone", "company", "subject", "message", "is_read"]
    panels = [
        FieldPanel("name", read_only=True),
        FieldPanel("email", read_only=True),
        FieldPanel("phone", read_only=True),
        FieldPanel("company", read_only=True),
        FieldPanel("subject", read_only=True),
        FieldPanel("message", read_only=True),
        FieldPanel("is_read"),
    ]


@hooks.register("register_admin_viewset")
def register_contact_submission_viewset():
    return ContactSubmissionViewSet("contact_submissions")
