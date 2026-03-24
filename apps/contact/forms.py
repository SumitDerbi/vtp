from django import forms

from apps.contact.models import ContactFormSubmission


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormSubmission
        fields = ["name", "email", "phone", "company", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors duration-200",
                "placeholder": "Your Name *",
                "id": "cf-name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors duration-200",
                "placeholder": "Email Address *",
                "id": "cf-email",
            }),
            "phone": forms.TextInput(attrs={
                "class": "w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors duration-200",
                "placeholder": "Phone Number",
                "id": "cf-phone",
            }),
            "company": forms.TextInput(attrs={
                "class": "w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors duration-200",
                "placeholder": "Company Name",
                "id": "cf-company",
            }),
            "subject": forms.TextInput(attrs={
                "class": "w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors duration-200",
                "placeholder": "Subject",
                "id": "cf-subject",
            }),
            "message": forms.Textarea(attrs={
                "class": "w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-colors duration-200",
                "placeholder": "Your Message *",
                "rows": 5,
                "id": "cf-message",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].required = True
        self.fields["email"].required = True
        self.fields["message"].required = True
