from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict={'insert_me': 'Hello im from view.py in Profile_app'}
    return render(request, 'profile_app/index.html', context= my_dict)