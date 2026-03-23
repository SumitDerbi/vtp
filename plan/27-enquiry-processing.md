# Prompt 27 — Product Enquiry Form Processing

## Goal

Make the product enquiry form functional — save to DB, link to product, send email.

## Prompt

```
Create the enquiry form processing for VTP.

1. File: apps/enquiry/views.py

   from django.shortcuts import redirect
   from django.views.decorators.http import require_POST
   from django.core.mail import send_mail
   from .forms import EnquiryForm

   @require_POST
   def submit_enquiry(request):
       form = EnquiryForm(request.POST)
       if form.is_valid():
           submission = form.save(commit=False)
           # Set product_page from hidden field
           product_page_id = request.POST.get('product_page_id')
           if product_page_id:
               from wagtail.models import Page
               try:
                   submission.product_page = Page.objects.get(id=product_page_id)
               except Page.DoesNotExist:
                   pass
           submission.product_name = request.POST.get('product_name', '')
           submission.save()

           # Send notification email
           send_enquiry_notification(submission)

           # Redirect back to product page with success flag
           referer = request.META.get('HTTP_REFERER', '/')
           separator = '&' if '?' in referer else '?'
           return redirect(f'{referer}{separator}enquiry_sent=true')

       # If form invalid, redirect back
       return redirect(request.META.get('HTTP_REFERER', '/'))

   def send_enquiry_notification(submission):
       from apps.common.models import SiteSettings
       from wagtail.models import Site
       site = Site.objects.get(is_default_site=True)
       settings = SiteSettings.for_site(site)
       recipient = settings.email
       if recipient:
           send_mail(
               subject=f'Product Enquiry: {submission.product_name}',
               message=f'Product: {submission.product_name}\n'
                       f'Name: {submission.name}\nEmail: {submission.email}\n'
                       f'Phone: {submission.phone}\nCompany: {submission.company}\n'
                       f'Quantity: {submission.quantity}\n'
                       f'Message:\n{submission.message}',
               from_email=None,
               recipient_list=[recipient],
               fail_silently=True,
           )

2. File: apps/enquiry/urls.py
   urlpatterns = [
       path('submit/', submit_enquiry, name='submit_enquiry'),
   ]

3. Update vtp/urls.py to include:
   path('enquiry/', include('apps.enquiry.urls')),

4. Update product template to show success message:
   {% if request.GET.enquiry_sent %}
   <div class="bg-green-100 text-green-800 p-4 rounded-lg">
       Thank you! Your enquiry has been submitted.
   </div>
   {% endif %}
```

## Verification

1. Enquiry form submits from product page
2. Saved to DB with product link
3. Email notification sent
4. Success message shown
5. Back on product page after submit

## Expected Result

- Working product enquiry form with product linkage
