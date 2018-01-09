from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
def index(request):
    request.session["counter"] += 1
    context = {
         "word": get_random_string(length=32),
         "key": request.session["counter"]
    }
   

    return render(request,"RanWG/index.html",context)

def process(request):
    return redirect("/")
