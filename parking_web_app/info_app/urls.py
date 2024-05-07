from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('profile/', views.profile, name='profile'),
    path('credit_card/', views.register_credit_card, name='credit_card'),
    path('bank/', views.register_bank, name='bank'),
    path('vehicle/', views.register_vehicle, name='vehicle'),
]
