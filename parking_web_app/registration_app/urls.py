from django.urls import path
from registration_app import views

urlpatterns=[
    path('',views.index, name='index')
]