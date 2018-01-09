from django.shortcuts import render

from ..PBT2.models import User

from . models import *

def home(request): 
    return render(request,"Pytest_app/home.html")