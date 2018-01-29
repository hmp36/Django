from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re
import bcrypt

NUM_REGEX = re.compile(r'[^a-zA-Z]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    
    def register(self, name, username, email, dob, password, confirm):
        response = {
            "valid": True,
            "errors": [],
            "user": None
        }

        if len(name) < 1:
            response["errors"].append("name is required")
        elif len(name) < 2:
            response["errors"].append(
                "Name must be 2 characters or longer")
        
        if len(username) < 1:
            response["errors"].append("Username is required")
        elif len(username) < 3:
            response["errors"].append(
                "Username must be 3 characters or longer")

        if len(email) < 1:
            response["errors"].append("Email is required")
        elif not EMAIL_REGEX.match(email):
            response["errors"].append("Invalid Email")
        else:
            email_list = User.objects.filter(email=email.lower())
            if len(email_list) > 0:
                response["errors"].append("Email is already in use.")

        if len(dob) < 1:
            response["errors"].append("Date of Birth is required")
        else:
            date = datetime.strptime(dob, '%Y-%m-%d')
            today = datetime.now()
            if date > today:
                response["errors"].append("Date of Birth must be in the past")

        if len(password) < 1:
            response["errors"].append("Password is required")
        elif len(password) < 8:
            response["errors"].append(
                "Password must be 8 characters or longer")

        if len(confirm) < 1:
            response["errors"].append("Confirm Password is required")
        if confirm != password:
            response["errors"].append("Confirm Password must match password")

        if len(response["errors"]) > 0:
            response["valid"] = False
        else:
            response["user"] = User.objects.create(
                name=name,
                username=username,
                email=email.lower(),
                dob=date,
                password=bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            )
        return response
   
    def login(self, email, password):
        response = {
            "valid": True,
            "errors": [],
            "user": None
        }

        if len(email) < 1:
            response["errors"].append("Email is required")
        elif not EMAIL_REGEX.match(email):
            response["errors"].append("Invalid Email")
        else:
            email_list = User.objects.filter(email=email.lower())
            if len(email_list) == 0:
                response["errors"].append("Email is already in use.")

        if len(password) < 1:
            response["errors"].append("Password is required")
        elif len(password) < 8:
            response["errors"].append("Password must be 8 character or longer")

        if len(response["errors"]) == 0:
            hashed_pw = email_list[0].password
            if bcrypt.checkpw(password.encode(), hashed_pw.encode()):
                response["user"] = email_list[0]
            else:
                response["errors"].append("Password is incorrect")
        if len(response["errors"]) > 0:
            response["valid"] = False

        return response

class FriendManager(models.Manager):
    def newFriend(self, user_id, friend_id):
        sender = User.objects.get(id=user_id)
        receiver = User.objects.get(id=friend_id)
        Friend.objects.create(user=sender, friend=receiver)
        Friend.objects.create(user=receiver, friend=sender)

    def removeFriend(self, user_id, friend_id):
        sender = User.objects.get(id=user_id)
        receiver = User.objects.get(id=friend_id)
        Friend.objects.get(user=sender, friend=receiver).delete()
        Friend.objects.get(user=receiver, friend=sender).delete()


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    dob = models.DateField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    



class Friend(models.Model):
    user = models.ForeignKey(User, related_name="sender")
    friend = models.ForeignKey(User, related_name="receiver")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = FriendManager()




