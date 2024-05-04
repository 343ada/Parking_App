from django.urls import path
from registration_app import views

urlpatterns=[
    path('register',views.index, name='register')
]