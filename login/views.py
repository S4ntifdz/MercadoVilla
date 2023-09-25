from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.template import loaders
 
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'login_form': form}) 
        #{'login_form': form} es un diccionario que se pasa a la plantilla login.html, 
        # para que se pueda acceder a la variable form desde la plantilla.
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None: 
            
                login(request, user)
                #TODO SE MUESTRA EN EL ADMIN messages.info(request, f"You are now logged in as {username}.")
                return redirect('web/')  

            else:
                messages.error(request, "Usuario y/o Contraseñas invalidos.")
        else:
            messages.error(request, "Usuario y/o Contraseñas invalidos.")
        return render(request, 'registration/login.html', {'login_form': form})
