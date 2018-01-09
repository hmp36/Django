from django.shortcuts import render, redirect
from .models import User

def index(request):
    context = {
        'users': User.objects.all()   
    }
    return render(request, "SRusers_app/index.html", context)

def show(request, user_id):
    context = {
        'users': User.objects.get(id=user_id)}
    print "id of this person is", id   
    return render(request, "SRusers_app/show.html", context)

def new(request):
    print request.POST
    return render(request, "SRusers_app/new.html")

def edit(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user': user
    }
    return render(request, "SRusers_app/edit.html", context)
    

def add_user(request):
    print request.POST
    User.objects.create(first_name = request.POST['first'], last_name = request.POST ['last'],
    email = request.POST['email'])
    print "ansfgbkafk", User
    return redirect('/') 

def update(request, user_id):
    user = User.objects.get(id = user_id)
    user.first_name = request.POST['first']
    user.last_name = request.POST['last']
    user.email = request.POST['email']
    user.save()
    print "ansfgbkafk", User
    return redirect('/')

def remove(request,user_id):
    users = User.objects.get(id=user_id).delete()
    return redirect("/")
