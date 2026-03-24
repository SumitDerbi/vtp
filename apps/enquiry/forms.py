from django import forms

from apps.enquiry.models import EnquiryFormSubmission


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = EnquiryFormSubmission
        fields = ["name", "email", "phone", "company", "quantity", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors duration-200",
                "placeholder": "Your Name *",
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors duration-200",
                "placeholder": "Email Address *",
            }),
            "phone": forms.TextInput(attrs={
                "class": "w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors duration-200",
                "placeholder": "Phone Number",
            }),
            "company": forms.TextInput(attrs={
                "class": "w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors duration-200",
                "placeholder": "Company Name",
            }),
            "quantity": forms.TextInput(attrs={
                "class": "w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors duration-200",
                "placeholder": "Approximate Quantity",
            }),
            "message": forms.Textarea(attrs={
                "class": "w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors duration-200",
                "placeholder": "Your Requirements / Message",
                "rows": 4,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].required = True
        self.fields["email"].required = True
