from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
# Create your views here.

def sign_up(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'registration_app/user_info.html', {'form':form})