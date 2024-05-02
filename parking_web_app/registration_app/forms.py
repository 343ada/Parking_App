# forms.py
from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_fname', 'user_lname', 'username', 'user_add1', 'user_add2', 'user_city', 'user_state', 'user_zip', 'user_email', 'user_password']
        widgets = {
            'user_password': forms.PasswordInput(),
        }
