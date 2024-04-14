from django.urls import path
from payment_app import views

urlpatterns=[
    path('',views.index, name='index')
]