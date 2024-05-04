from django.shortcuts import render
from django.http import HttpResponse
from registration_app.models import User, Credit_Card, Bank, Vehicle, Date_Time
from registration_app.views import RegistrationForm
from forms import RegistrationForm
# Create your views here.

def sign_up(request);
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'users/register.html', {'form':form})