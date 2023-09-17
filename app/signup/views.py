from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.template import loader
from signup.forms import SignUpForm
from clients.models import ClientModel

class SignUpView(View):

    def get(self, request):
        template = loader.get_template("signup.html")

        context = {
            "form": SignUpForm
        }
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        
        data = {
            "email": request.POST.get("email"),
            "username": request.POST.get("email"),
            "password": request.POST.get("password1"),
            "first_name":request.POST.get("first_name"),
            "last_name": request.POST.get("last_name"),
            "cuit": request.POST.get("cuit"),
            "business_line_interes": request.POST.get("business_line_interes"),
            "state": request.POST.get("state"),
            "city": request.POST.get("city"),
            "postal_code": request.POST.get("postal_code"),
            "phone_number": request.POST.get("phone_number"),
        }

        ClientModel.objects.create_user(**data)
        template = loader.get_template("signup.html")
        return HttpResponse(template.render(data, request))