# registration_app/views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'registration_app/user_info.html', {'form': form})
