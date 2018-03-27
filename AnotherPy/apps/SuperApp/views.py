from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, "SuperApp/index.html")

def login(request):
    	if request.method != 'POST':
		return redirect('/')

	user = User.objects.filter(email=request.POST.get('email')).first()

	if user and bcrypt.checkpw(request.POST.get('password').encode(), user.password.encode()):
		request.session['user_id'] = user.id
		return redirect('/friends')
	else:
		messages.add_message(request, messages.INFO, 'Invalid', extra_tags="login")
		return redirect('/')
	return redirect('/friends')

def logout(request):
    		request.session.clear()
		return redirect('/')

def register(request):
    response = User.objects.register(
        request.POST["name"],
        request.POST["username"],
        request.POST["email"],
        request.POST["dob"],
        request.POST["password"],
        request.POST["confirm"]

    )

    if response["valid"]:
        request.session["user_id"] = response["user"].id
        return redirect("/friends")
    else:
        for error_message in response["errors"]:
            messages.add_message(request, messages.ERROR, error_message)
        return redirect("/")

def dashboard(request):
   
    
    if "user_id" not in request.session:
        return redirect("/")

    user = User.objects.get(id=request.session["user_id"])

    return render(request, "Friends/friends.html", {"user": user})
