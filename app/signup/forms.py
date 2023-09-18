from django import forms
from clients.models import ClientModel

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ClientModel
        fields = ['email', 'username', 'first_name', 'last_name', 'cuit', 'password', 'password2', 'business_line', 'business_line_interes', 'is_seller', 'is_buyer', 'state', 'city', 'postal_code', 'phone_number']
        