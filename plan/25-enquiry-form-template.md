# Prompt 25 — Enquiry Form Template (Product-Linked)

## Goal

Create the enquiry form that appears on product pages, pre-linked to the product.

## Prompt

```
Create the enquiry form component for VTP product pages.

1. File: apps/enquiry/forms.py

   Create EnquiryForm(forms.ModelForm):
   class Meta:
       model = EnquiryFormSubmission
       fields = ['name', 'email', 'phone', 'company', 'quantity', 'message']
       widgets = {
           'name': TextInput(attrs={
               'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-primary focus:border-primary',
               'placeholder': 'Your Name *',
           }),
           'email': EmailInput(attrs={...similar styling}),
           'phone': TextInput(attrs={...}),
           'company': TextInput(attrs={...}),
           'quantity': TextInput(attrs={
               ..., 'placeholder': 'Approximate Quantity',
           }),
           'message': Textarea(attrs={
               ..., 'placeholder': 'Your Requirements / Message',
               'rows': 4,
           }),
       }

   Set name and email as required.

2. File: templates/includes/enquiry_form.html

   Reusable include that can be placed on any product page:
   - Receives 'product' variable from context
   - Form heading: "Enquire About {{ product.title }}"
   - Hidden field: product_page_id (product.id)
   - Hidden field: product_name (product.title)
   - All form fields rendered with labels
   - Submit button (btn-primary)
   - CSRF token included
   - Form action: /enquiry/submit/ (will be created in Prompt 27)

3. Update ProductPage template (product_page.html) to include:
   {% include "includes/enquiry_form.html" with product=self %}

Form is inline on the product page (not a modal for simplicity).
Uses AJAX submit if possible, or standard POST with redirect back.
```

## Verification

1. Enquiry form renders on product pages
2. Product name pre-filled
3. Form fields styled with Tailwind
4. All input sizes readable

## Expected Result

- Reusable enquiry form component on product pages
