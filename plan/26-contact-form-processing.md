# Prompt 26 — Contact Form Processing with Email

## Goal

Make the contact form functional — save to DB and send email notification.

## Prompt

```
Create the contact form processing for VTP.

1. File: apps/contact/forms.py

   Create ContactForm(forms.ModelForm):
   - Fields: name, email, phone, company, subject, message
   - Tailwind-styled widgets (consistent with enquiry form)
   - name, email, message required

2. Update ContactPage model — add serve() method:

   def serve(self, request):
       from .forms import ContactForm

       if request.method == 'POST':
           form = ContactForm(request.POST)
           if form.is_valid():
               submission = form.save()
               self.send_notification_email(submission)
               from django.shortcuts import redirect
               return redirect(self.url + '?submitted=true')
       else:
           form = ContactForm()

       return self.render(request, context_overrides={
           'form': form,
           'submitted': request.GET.get('submitted') == 'true',
       })

   def send_notification_email(self, submission):
       from django.core.mail import send_mail
       recipient = self.notification_email or self.email
       if recipient:
           send_mail(
               subject=f'New Contact Form: {submission.subject or "No Subject"}',
               message=f'Name: {submission.name}\nEmail: {submission.email}\n'
                       f'Phone: {submission.phone}\nCompany: {submission.company}\n'
                       f'Message:\n{submission.message}',
               from_email=None,
               recipient_list=[recipient],
               fail_silently=True,
           )

3. Update contact template to use form:
   - Render form fields from the form object
   - Show success message when submitted=true

Uses PRG (Post/Redirect/Get) pattern to prevent double-submit.
```

## Verification

1. Contact form submits and saves to DB
2. Success message shows after submission
3. Email sent (check console in dev)
4. No double-submit on page refresh

## Expected Result

- Working contact form with DB storage and email notification
