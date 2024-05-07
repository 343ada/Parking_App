
from django import forms
from .models import CreditCard, Bank, Vehicle

class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['card_number', 'expiration_date']

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['bank_name', 'account_number']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['make', 'model', 'year']
