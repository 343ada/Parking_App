

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# login
def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_home_page')  # Redirect to user home page after successful login
    else:
        form = LoginForm()
    return render(request, 'authentication_app/login.html', {'form': form})

# logout
from django.shortcuts import redirect
from django.contrib.auth import logout

def custom_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


def user_home_page(request):
    return render(request, 'authentication_app/user_home_page.html')