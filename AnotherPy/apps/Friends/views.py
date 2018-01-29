from django.shortcuts import render, redirect
from ..SuperApp.models import User
from .models import *

# logged in user 
def current_user(request):  
    if "user_id" in request.session:
        return User.objects.get(id=request.session['user_id'])

def friends(request):

    me = User.objects.get(id=request.session['user_id'])
    # print "SHOULD BE WHOEVERS LOGGED IN", me.first_name
    everybody = User.objects.all()  # SELECTING ALL USERS
    friends = Friend.objects.all()  # SELECTING USER IDS THAT ALSO HAVE FRIEND IDS
    # ONLY USERS FRIENDS, NOT ALL FRIEND OBJECTS
    my_friends = Friend.objects.filter(user=me)
    # print "ID NUMBER OF FRIENDS", friends[0].id #WHAT DOES TE 0 DO?

    other_users = []

    for person in everybody:
        if person.id != request.session['user_id']:
            other_users.append(person)
    # print "OTHER USERS RE: ", other_users

    my_homies = Friend.objects.filter(user_id=request.session['user_id'])
    not_my_homies = User.objects.all().exclude(id=request.session['user_id'])
    for homie in my_homies:  # remove homies from not my homies
        not_my_homies = not_my_homies.exclude(id=homie.friend.id)
    

    context = {
        "user": me,
        "friends": my_homies,
        "not_friends": not_my_homies
    }

    return render(request, "Friends/friends.html", context)

def show(request, id):
    request.session["user_id"]
    print "M RIGHT HERE", type(request.session["user_id"])
    your_users = User.objects.filter(id=id)
    print your_users
    context = {
        "users": User.objects.all(),
        "user": User.objects.get(id=request.session["user_id"]),
        "your_users":  your_users,
        "friends": Friend.objects.all()
    }
    return render(request, "Friends/show.html", context)

def add(request, id):
    print "JUST PRINT ANYTHING"
    # ID IS TALKING TO ARGUMENT IN DEF, REQUEST.SESSION.USER_ID IS WHOEVER IS LOGGED IN
    Friend.objects.newFriend(request.session['user_id'], id)
    return redirect("/friends")

def remove(request, id):
    Friend.objects.removeFriend(request.session["user_id"], id)
    return redirect("/friends")

def home(request, id):
    request.session["user_id"]
    return render(request, "/Friends/friends.html") 