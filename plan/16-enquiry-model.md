# Prompt 16 — Enquiry Model (Linked to Product)

## Goal

Create the product enquiry submission model, linked to specific products.

## Prompt

```
Create the Enquiry model for VTP.

File: apps/enquiry/models.py

1. EnquiryFormSubmission(Model):
   - product_page = ForeignKey('wagtailcore.Page', on_delete=SET_NULL,
       null=True, blank=True, related_name='enquiries',
       help_text="Product this enquiry is about")
   - product_name = CharField(max_length=255, blank=True,
       help_text="Stored separately in case product page is deleted")
   - name = CharField(max_length=255)
   - email = EmailField()
   - phone = CharField(max_length=50, blank=True)
   - company = CharField(max_length=255, blank=True)
   - quantity = CharField(max_length=100, blank=True)
   - message = TextField(blank=True)
   - created_at = DateTimeField(auto_now_add=True)
   - is_read = BooleanField(default=False)

   class Meta:
       ordering = ['-created_at']

   def __str__(self):
       return f"Enquiry: {self.name} — {self.product_name} ({self.created_at:%Y-%m-%d})"

   def save(self, *args, **kwargs):
       # Auto-fill product_name from product_page if not set
       if not self.product_name and self.product_page:
           self.product_name = self.product_page.title
       super().save(*args, **kwargs)

This is NOT a Wagtail page — it's a standalone Django model.
Enquiry submissions come from the product detail page (modal/inline form).
Each enquiry is linked to the specific product the user was viewing.

Run: python manage.py makemigrations enquiry && python manage.py migrate
```

## Verification

1. Migrations run
2. Model accessible via Django admin / Wagtail ModelAdmin
3. product_page FK works

## Expected Result

- EnquiryFormSubmission model linked to products
- Stored with product name backup (in case page is deleted)
