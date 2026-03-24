from wagtail import hooks
from wagtail.admin.panels import FieldPanel
from wagtail.admin.ui.tables import BooleanColumn, DateColumn
from wagtail.admin.viewsets.model import ModelViewSet

from .models import EnquiryFormSubmission


class EnquirySubmissionViewSet(ModelViewSet):
    model = EnquiryFormSubmission
    icon = "clipboard-list"
    menu_label = "Product Enquiries"
    menu_order = 200
    add_to_admin_menu = True
    list_display = [
        "name",
        "product_name",
        "email",
        DateColumn("created_at", label="Date"),
        BooleanColumn("is_read", label="Read"),
    ]
    list_filter = ["is_read", "product_name", "created_at"]
    search_fields = ["name", "email", "product_name", "message"]
    ordering = ["-created_at"]
    inspect_view_enabled = True
    form_fields = [
        "product_name",
        "name",
        "email",
        "phone",
        "company",
        "quantity",
        "message",
        "is_read",
    ]
    panels = [
        FieldPanel("product_name", read_only=True),
        FieldPanel("name", read_only=True),
        FieldPanel("email", read_only=True),
        FieldPanel("phone", read_only=True),
        FieldPanel("company", read_only=True),
        FieldPanel("quantity", read_only=True),
        FieldPanel("message", read_only=True),
        FieldPanel("is_read"),
    ]


@hooks.register("register_admin_viewset")
def register_enquiry_submission_viewset():
    return EnquirySubmissionViewSet("enquiry_submissions")
