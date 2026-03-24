from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.core.mail import send_mail

from .forms import EnquiryForm


@require_POST
def submit_enquiry(request):
    form = EnquiryForm(request.POST)
    if form.is_valid():
        submission = form.save(commit=False)
        product_page_id = request.POST.get("product_page_id")
        if product_page_id:
            from wagtail.models import Page

            try:
                submission.product_page = Page.objects.get(id=product_page_id)
            except Page.DoesNotExist:
                pass
        submission.product_name = request.POST.get("product_name", "")
        submission.save()
        send_enquiry_notification(submission)
        referer = request.META.get("HTTP_REFERER", "/")
        separator = "&" if "?" in referer else "?"
        return redirect(f"{referer}{separator}enquiry_sent=true")

    return redirect(request.META.get("HTTP_REFERER", "/"))


def send_enquiry_notification(submission):
    from apps.common.models import SiteSettings
    from wagtail.models import Site

    site = Site.objects.filter(is_default_site=True).first()
    if not site:
        return
    settings = SiteSettings.for_site(site)
    recipient = settings.email
    if recipient:
        send_mail(
            subject=f"Product Enquiry: {submission.product_name}",
            message=(
                f"Product: {submission.product_name}\n"
                f"Name: {submission.name}\n"
                f"Email: {submission.email}\n"
                f"Phone: {submission.phone}\n"
                f"Company: {submission.company}\n"
                f"Quantity: {submission.quantity}\n\n"
                f"Message:\n{submission.message}"
            ),
            from_email=None,
            recipient_list=[recipient],
            fail_silently=True,
        )
