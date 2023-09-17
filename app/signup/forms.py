
from django import forms
from django.contrib.auth.forms import UserCreationForm
from clients.models import ClientModel

class SignUpStep1Form(UserCreationForm):
    class Meta:
        model = ClientModel
        fields = '__all__'

class SignUpStep2Form(forms.ModelForm):
    class Meta:
        model = ClientModel
        fields = ['cuit', 'business_line', 'business_line_interes', 'state', 'city', 'postal_code', 'phone_number', 'avatar']
