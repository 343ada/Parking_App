from django.shortcuts import render
from .models import CreditCard, Bank, Vehicle
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    # Retrieve credit card, bank, and vehicle information associated with the logged-in user
    credit_cards = CreditCard.objects.filter(user=request.user)
    banks = Bank.objects.filter(user=request.user)
    vehicles = Vehicle.objects.filter(user=request.user)
    
    # Pass the data to the template
    context = {
        'credit_cards': credit_cards,
        'banks': banks,
        'vehicles': vehicles
    }
    
    return render(request, 'info_app/profile.html', context)



# registration
from django.shortcuts import render, redirect
from .forms import CreditCardForm, BankForm, VehicleForm

def register_credit_card(request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            credit_card = form.save(commit=False)
            credit_card.user = request.user
            credit_card.save()
            return redirect('bank')  # Redirect to success page
    else:
        form = CreditCardForm()
    return render(request, 'info_app/credit_card_registration.html', {'form': form})

def register_bank(request):
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            bank = form.save(commit=False)
            bank.user = request.user
            bank.save()
            return redirect('vehicle')  # Redirect to success page
    else:
        form = BankForm()
    return render(request, 'info_app/bank_registration.html', {'form': form})

def register_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()
            return redirect('profile')  # Redirect to success page
    else:
        form = VehicleForm()
    return render(request, 'info_app/vehicle_registration.html', {'form': form})
