from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request,"PBT2/index.html")


def register(request):

    response = User.objects.register(
        request.POST["first"],
        request.POST["last"],
        request.POST["username"],
        request.POST["email"],
        request.POST["dob"],
        request.POST["password"],
        request.POST["confirm"]

    )

    if response["valid"]:
        request.session["user_id"] = response["user"].id
        return redirect("/home")
    else:
        for error_message in response["errors"]:
            messages.add_message(request, messages.ERROR, error_message)
        return redirect("/")


def login(request):
    response = User.objects.login(
        request.POST["email"],
        request.POST["password"]
    )
    if response["valid"]:
        request.session["user_id"] = response["user"].id
        return redirect("/home")
    else:
        for error_message in response["errors"]:
            messages.add_message(request, messages.ERROR, error_message)
        return redirect("/")


# def home(request):
#     if "user_id" not in request.session:
#         return redirect("/")

#     user = User.objects.get(id=request.session["user_id"])

#     # return render(request, "friends_app/friends.html", {"user": user})


def logout(request):
    request.session.clear()
    return redirect("/")
