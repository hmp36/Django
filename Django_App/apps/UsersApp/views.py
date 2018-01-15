from django.shortcuts import render, HttpResponse

# Create your views here.

def register(request):
    return HttpResponse("placeholder for users to add a new survey")

def login(request):
    return HttpResponse("placeholder for users to login")

def new(request):
    return HttpResponse("same method that handles /register also handle the url request of /users/new")

def index(request):
    return HttpResponse("placeholder to later display all the list of users")
