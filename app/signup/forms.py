from django import forms
from clients.models import ClientModel

class SignUpForm(forms.ModelForm):
    password1= forms.CharField()
    password2= forms.CharField()

    class Meta:
        model = ClientModel
        fields = ("email", "first_name", "last_name", "cuit", "business_line_interes", "state", "city", "postal_code", "phone_number", "password1", "password2")