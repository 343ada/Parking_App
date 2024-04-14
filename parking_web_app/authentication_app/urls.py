from django.urls import path
from authentication_app import views

urlpatterns=[
    path('',views.index, name='index')
]