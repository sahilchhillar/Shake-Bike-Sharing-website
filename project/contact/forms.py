from django import forms
from .models import Feedback

class FeedbackForm(forms.Form):
    bikeCode = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Bike Code",
            "name": "bikeCode"
        }
    ), required=True)

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "placeholder": "Email Address", 
            "name": "email"
        }
    ), required=False)

    message = forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder": "Message",
            "name": "message"
        }
    ), required=True, max_length=500)

    class Meta:
        model = Feedback