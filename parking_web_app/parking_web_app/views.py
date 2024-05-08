# views.py
from django.shortcuts import render
from booking_app.models import Parking_Lot

def home(request):
    parking_lots = Parking_Lot.objects.all()
    availability_data = []
    for lot in parking_lots:
        availability_data.append({
            'lot_name': lot.lot_name,
            'total_spaces': lot.lot_totspace,
            'available_spaces': lot.lot_avaspace,
            'status': lot.lot_spcstat
        })
    return render(request, 'parking_web_app/home.html', {'parking_lots': availability_data})
