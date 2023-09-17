from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm

class SignUpView(View):
    template_name = 'registration/signup.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('../templates/registration/base.html')  
        return render(request, self.template_name, {'form': form})
