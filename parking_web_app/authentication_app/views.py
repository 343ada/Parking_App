from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
   # return HttpResponse('Authentication Page')
    my_dict={'insert_me': 'Hello im from view.py in Authentication_app'}
    return render(request, 'authentication_app/index.html', context= my_dict)