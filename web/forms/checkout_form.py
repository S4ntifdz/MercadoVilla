from django import forms




class CheckoutForm(forms.Form) :
    card_number = forms.IntegerField(max_value=9999999999999999, min_value=1000000000000000)
    card_expiration_month = forms.IntegerField(max_value=12, min_value=1)
    card_expiration_year = forms.IntegerField(max_value=99, min_value=21)
    security_code = forms.IntegerField(max_value=999, min_value=100)
    card_holder_name = forms.CharField(max_length=50)
    card_holder_identification_type = forms.CharField(initial="DNI", max_length=3, min_length=3) 
    card_holder_identification_number = forms.IntegerField(max_value=99999999999, min_value=10000000) 
# "card_number ": ,
# "card_expiration_month": ,
# "card_expiration_year": ,
# "security_code":  ,
# "card_holder_name":  ,
# "card_holder_identification": {
# "type": "dni" ,
# "number": 
#     }