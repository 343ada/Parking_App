# views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def index(request):
    return render(request, 'registration_app/index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['user_password']
            user.set_password(password)
            user.save()
            return redirect('index')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'registration_app/user_info.html', {'form': form})
