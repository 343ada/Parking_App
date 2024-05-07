# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'parking_web_app/home.html')
