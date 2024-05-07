from django.urls import path
from booking_app import views

urlpatterns=[
    path('booking',views.index, name='booking'),
    path('parking_availability/', views.parking_availability, name='parking_availability'),
    path('reserve_parking/', views.reserve_parking, name='reserve_parking'),
    path('history_reservation/', views.history, name='history_reservation'),
]