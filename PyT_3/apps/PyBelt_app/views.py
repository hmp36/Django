from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt



def index(request):
    return render(request, "PyBelt_app/index.html")

def create(request):
    return render(request, "PyBelt_app/create.html")

def dashboard(request):
    all_wishes = Wish.objects.all()
    user = User.objects.get(id=request.session['user_id'])
    user_wishes=user.items.all()
    for wish in user_wishes:
        all_wishes= all_wishes.exclude(id=wish.id) 

    context = {
        "wishes": all_wishes,
        "my_wishes": user.items.all(),
        "user":user
    }
    return render(request, "PyBelt_app/dashboard.html", context)

def register(request):
        result = User.manager.validateUser(request.POST)
    	check = User.objects.validateUser(request.POST)
	if request.method != 'POST':
		return redirect("/")
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
		#route to wishes page
		return redirect("/dashboard")


# ('/dashboard/{}'.format(result[1].name))



def login(request):
    	if request.method != 'POST':
		return redirect('/')

	user = User.objects.filter(email=request.POST.get('email')).first()

	if user and bcrypt.checkpw(request.POST.get('password').encode(), user.password.encode()):
		request.session['user_id'] = user.id
		return redirect('/dashboard')
	else:
		messages.add_message(request, messages.INFO, 'Invalid', extra_tags="login")
		return redirect('/')
	return redirect('/dashboard')

def logout(request):
    		request.session.clear()
		return redirect('/')

def current_user(request):
    	return User.objects.get(id=request.session['user_id'])
    
def wishes(request):
    	user = current_user(request)

	context = {
		'user': user,
		'wish_wishes': wish.objects.exclude(favorites=user),
		'favorites': user.favorites.all()
	}

	return render(request, 'dashboard.html', context)

def addWish(request, id):
    
	user = current_user(request)
	favorite = Wish.objects.get(id=id)

	user.items.add(favorite)

	return redirect("/dashboard")

def remove_wish(request, id):

	user = current_user(request)
	favorite = Wish.objects.get(id=id)

	user.items.remove(favorite)

	return redirect('/dashboard')

def show_user(request, id):
    
	user = User.objects.get(id=id)
	context = {
		'user': user,
		'favorites': user.favorites.all()
	}

	return render(request, 'dashboard.html', context)

def create(request):
    	if request.method != 'POST':
		return redirect('/')
	##adds item to wishes
	check = Wish.objects.validateWish(request.POST)
	if request.method != 'POST':
		return redirect('/dashboard')
	if check[0] == False:
		for error in check[1]:
			messages.add_message(request, messages.INFO, error, extra_tags="addwish")
			return redirect('/dashboard')
	if check[0] == True:

		quote = Wish.objects.create(
                    content=request.POST.get('content'),
                    poster=current_user(request),
                    author=request.POST.get('author')
                )

		return redirect('/dashboard')
	return redirect('/dashboard')

def show_user(request, id):
    
	user = User.objects.get(id=id)
	context = {
		'user': user,
		'favorites': user.favorites.all()
	}

	return render(request, 'PyBelt_app/user.html', context)

def addItem(request):
    
	if 'user_id' in request.session:
		user = currentUser(request)

		context = {
		"user": user,
		}

	return render(request, 'PyBelt_app/addItem.html', context)

def submitItem(request):
    if request.method == 'POST':
		errors = Wish.objects.validateWish(request.POST)
		if not errors:
			# user = currentUser(request)
			user = User.objects.get (id =request.session['user_id'] )
			print user, "here"
			wish = Wish.objects.create(item=request.POST['item'], user=user)

			user.items.add(wish)

			return redirect("/dashboard")

		for error in errors:
			messages.error(request, error)

	

		return redirect('/dashboard')

def item(request, id):
	if 'user_id' in request.session:
		user = currentUser(request)
		

		context = {
		'user': user,
		'wish': Wish.objects.get(id=id)		
		}

	return render(request, 'PyBelt_app/item.html', context)

def delete(request, id):
    	wish = Wish.objects.get(id=id)
	wish.delete()

	return redirect('/dashboard')

def currentUser(request):
    print request.session['user_id']
	# user = User.objects.get(id=request.session['user_id'])
	# return user


