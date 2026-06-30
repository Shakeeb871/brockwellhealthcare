from django import forms

from .models import ContactLead


class ContactForm(forms.ModelForm):
    # Honeypot: bots fill hidden fields, humans don't.
    website = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = ContactLead
        fields = ["name", "email", "phone", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your full name", "autocomplete": "name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com", "autocomplete": "email"}),
            "phone": forms.TextInput(attrs={"placeholder": "+971 ..", "autocomplete": "tel"}),
            "subject": forms.TextInput(attrs={"placeholder": "How can we help?"}),
            "message": forms.Textarea(attrs={"rows": 5, "placeholder": "Tell us about your enquiry"}),
        }

    def is_spam(self):
        return bool(self.data.get("website"))
