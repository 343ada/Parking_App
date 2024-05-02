# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('user', views.register, name='register'),
    # Other URL patterns
]
