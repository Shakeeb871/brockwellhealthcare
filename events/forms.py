from django import forms

from .models import EventRegistration


class RegistrationForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.HiddenInput)  # honeypot

    class Meta:
        model = EventRegistration
        fields = ["name", "email", "phone"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Full name", "autocomplete": "name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com", "autocomplete": "email"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone (optional)", "autocomplete": "tel"}),
        }

    def is_spam(self):
        return bool(self.data.get("website"))
