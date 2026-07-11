from django import forms
from django.conf import settings

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
            "phone": forms.TextInput(attrs={"placeholder": "Phone number", "autocomplete": "tel"}),
            "subject": forms.TextInput(attrs={"placeholder": "How can we help?"}),
            "message": forms.Textarea(attrs={"rows": 5, "placeholder": "Tell us about your enquiry"}),
        }

    def __init__(self, *args, region=None, **kwargs):
        """Set the phone placeholder to the current region's dialing code so US
        pages never hint a UAE number (and vice-versa)."""
        super().__init__(*args, **kwargs)
        code = None
        if isinstance(region, dict):
            code = region.get("code")
        elif isinstance(region, str):
            code = region
        conf = settings.REGIONS.get(code) or settings.REGIONS.get(settings.DEFAULT_REGION)
        dial = (conf or {}).get("dial")
        if dial:
            self.fields["phone"].widget.attrs["placeholder"] = f"{dial} .."

    def is_spam(self):
        return bool(self.data.get("website"))
