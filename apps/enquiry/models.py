from django.db import models


class EnquiryFormSubmission(models.Model):
    product_page = models.ForeignKey(
        "wagtailcore.Page",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="enquiries",
        help_text="Product this enquiry is about",
    )
    product_name = models.CharField(
        max_length=255,
        blank=True,
        help_text="Stored separately in case product page is deleted",
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=255, blank=True)
    quantity = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Enquiry: {self.name} — {self.product_name} ({self.created_at:%Y-%m-%d})"

    def save(self, *args, **kwargs):
        if not self.product_name and self.product_page:
            self.product_name = self.product_page.title
        super().save(*args, **kwargs)
