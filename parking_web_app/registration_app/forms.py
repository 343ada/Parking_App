from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm (UserCreationForm):
    class Meta:
        model=User
        fields = ['user_fname', 'user_lname', 'username','user_password']