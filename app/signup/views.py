from django.shortcuts import render, redirect
from .forms import SignUpStep1Form, SignUpStep2Form
from clients.models import ClientModel

def signup_step1(request):
    if request.method == 'POST':
        form = SignUpStep1Form(request.POST)
        if form.is_valid():
            request.session['step1_data'] = form.cleaned_data
            return redirect('signup_step2')  # Redirige al segundo paso
    else:
        form = SignUpStep1Form()
    
    return render(request, 'signup_step1.html', {'form': form})

def signup_step2(request):
    step1_data = request.session.get('step1_data')
    if not step1_data:
        return redirect('signup_step1')  # Redirige de nuevo al primer paso si no hay datos del primer paso

    if request.method == 'POST':
        form = SignUpStep2Form(request.POST, request.FILES)
        if form.is_valid():
            user_data = {**step1_data, **form.cleaned_data}
            ClientModel.objects.create_user(**user_data)
            del request.session['step1_data']  # Limpia los datos del primer paso
            return redirect('signup_success')  # Redirige a una página de éxito o a donde lo necesites
    else:
        form = SignUpStep2Form()
    
    return render(request, 'signup_step2.html', {'form': form})
