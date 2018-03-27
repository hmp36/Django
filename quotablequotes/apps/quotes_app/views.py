from django.shortcuts import render, redirect, Http Response
from .models import *
from django.contrib import messages
# from datetime import datetime
import bcrypt

# Create your views here.

def current_user(request):
	return User.objects.get(id=request.session['user_id'])
def index(request):
	return render(request, 'quotes_app/index.html')
def register(request):
	check = User.objects.validateUser(request.POST)
	if request.method != 'POST':
		return redirect('/')
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
			alias=request.POST.get('alias'),
			email=request.POST.get('email'),
			password=hashed_pw,
			birthdate=request.POST.get('birthdate')
		)

		#add user to session, logging them in
		request.session['user_id'] = user.id
		#route to quotes page
		return redirect('/quotes')
def login(request):
	if request.method != 'POST':
		return redirect('/')

	user = User.objects.filter(email=request.POST.get('email')).first()

	if user and bcrypt.checkpw(request.POST.get('password').encode(), user.password.encode()):
		request.session['user_id'] = user.id
		return redirect('/quotes')
	else:
		messages.add_message(request, messages.INFO, 'Invalid', extra_tags="login")
		return redirect('/')
	return redirect('/quotes')
def logout(request):
		request.session.clear()
		return redirect('/')
def quotes(request):
	user = current_user(request)

	context = {
		'user': user,
		'quotable_quotes': Quote.objects.exclude(favorites=user),
		'favorites': user.favorites.all()
	}

	return render(request, 'quotes_app/quotes.html', context)
def create(request):
	if request.method != 'POST':
		return redirect('/')
	##adds item to quotes
	check = Quote.objects.validateQuote(request.POST)
	if request.method != 'POST':
		return redirect('/quotes')
	if check[0] == False:
		for error in check[1]:
			messages.add_message(request, messages.INFO, error, extra_tags="add_item")
			return redirect('/quotes')
	if check[0] == True:

		quote = Quote.objects.create(
                    content=request.POST.get('content'),
                    poster=current_user(request),
                    author=request.POST.get('author')
                )

		return redirect('/quotes')
	return redirect('/quotes')
def add_favorite(request, id):

	user = current_user(request)
	favorite = Quote.objects.get(id=id)

	user.favorites.add(favorite)

	return redirect('/quotes')
def remove_favorite(request, id):
	user = current_user(request)
	favorite = Quote.objects.get(id=id)

	user.favorites.remove(favorite)

	return redirect('/quotes')
def show_user(request, id):

	user = User.objects.get(id=id)
	context = {
		'user': user,
		'favorites': user.favorites.all()
	}

	return render(request, 'quotes_app/user.html', context)