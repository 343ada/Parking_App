# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('user_home_page', views.user_home_page, name='user_home_page'),
]
