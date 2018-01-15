from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
# Create your views here.


def index(request):
    return render(request, "PyBelt_app/index.html")


def success(request, first_name):
    context = {
        'first_name': first_name
    }
    return render(request, "PyBelt_app/success.html", context)


def registration(request):
    result = User.manager.makeUser(request.POST)
    # result will be either (True, user) or (False, errors)
    if result[0]:
        return redirect('/success/{}'.format(result[1].first_name))
    for message in result[1].itervalues():
        messages.error(request, message)
    return redirect('/')


def login(request):
    result = User.manager.userLogin(request.POST)
    # result will be either (True, user) or (False, errors)
    if result[0]:
        return redirect('/success/{}'.format(result[1].first_name))
    for message in result[1].itervalues():
        messages.error(request, message)
    return redirect('/')
