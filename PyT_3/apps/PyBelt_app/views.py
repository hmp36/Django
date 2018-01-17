from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
import bcrypt
from django.contrib.auth.models import AbstractUser
from django.db import models


def index(request):
    return render(request, "PyBelt_app/index.html")

def create(request):
    return render(request, "PyBelt_app/create.html")



def dashboard(request, name):
    context = {
        'name': name
    }
    return render(request, "Pybelt_app/dashboard.html", context)


# def registration(request):
#     result = User.manager.makeUser(request.POST)
#     # result will be either (True, user) or (False, errors)
#     if result[0]:
#         return redirect('/dashboard/{}'.format(result[1].name))
#     for message in result[1].itervalues():
#         messages.error(request, message)
#     return redirect('/')

def registration(request):
        result = User.manager.validateUser(request.POST)
    	check = User.objects.validateUser(request.POST)
	if request.method != 'POST':
		return redirect("Pybelt_app/dashboard.html")
	if check[0] == False:
		for error in check[1]:
			messages.add_message(request, messages.INFO, error,
			                     extra_tags="registration")
			return redirect('/')
	if check[0] == True:
		#has password
		hashed_pw = bcrypt.hashpw(request.POST.get(
			'password').encode(), bcrypt.gensalt())

		#create user
		user = User.objects.create(
			name=request.POST.get('name'),
			username=request.POST.get('username'),
			email=request.POST.get('email'),
			password=hashed_pw,
			
		)

		#add user to session, logging them in
		request.session['user_id'] = user.id
		#route to quotes page
		return redirect("Pybelt_app/dashboard.html")


# ('/dashboard/{}'.format(result[1].name))



def login(request):
    result = User.manager.userLogin(request.POST)
    # result will be either (True, user) or (False, errors)
    if result[0]:
        return redirect("Pybelt_app/dashboard.html")
    for message in result[1].itervalues():
        messages.error(request, message)
    return redirect('/')

def logout(request):
    		request.session.clear()
		return redirect('/')

def current_user(request):
    	return User.objects.get(id=request.session['user_id'])
    

