from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Parking_Lot
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