
from django import forms
from .models import ParkingReservation, Parking_Lot

class ReservationForm(forms.ModelForm):
    parking_lot = forms.ModelChoiceField(queryset=Parking_Lot.objects.all())
    start_datetime = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_datetime = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = ParkingReservation
        fields = ['parking_lot', 'start_datetime', 'end_datetime']