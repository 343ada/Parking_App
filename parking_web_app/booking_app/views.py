from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Parking_Lot
from django.shortcuts import render, redirect
from .forms import ReservationForm
# Create your views here.

def index(request):
    my_dict={'insert_me': 'Hello im from view.py in Booking_app'}
    return render(request, 'booking_app/index.html', context= my_dict)

def parking_availability(request):
    parking_lots = Parking_Lot.objects.all()
    availability_data = []
    for lot in parking_lots:
        availability_data.append({
            'lot_name': lot.lot_name,
            'total_spaces': lot.lot_totspace,
            'available_spaces': lot.lot_avaspace,
            'status': lot.lot_spcstat
        })
    return render(request, 'booking_app/parking_availability.html', {'parking_lots': availability_data})



def reserve_parking(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            #
            parking_lot = form.cleaned_data['parking_lot']
            parking_lot.lot_avaspace -= 1
            parking_lot.save()
            
            return redirect('parking_availability')  # Redirect to a success page
    else:
        form = ReservationForm()
    return render(request, 'booking_app/reserve_parking.html', {'form': form})
