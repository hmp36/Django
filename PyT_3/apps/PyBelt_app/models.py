from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

# Create your models here.
NUM_REGEX = re.compile(r'[^a-zA-Z]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def uni_to_str(myDict):
    data = {}
    for key, val in myDict.iteritems():
        if key != 'csrfmiddlewaretoken':
            data[key] = str(val)
    return data


class UserManager(models.Manager):
    def makeUser(self, form):
        flag = False
        errors = {}
        data = uni_to_str(form)
        for val in data.itervalues():
            if len(val) < 1:
                flag = True
                errors['blank'] = "All fields are required! Please make sure you provided an entry in each."
                break
        if len(data['first_name']) < 2:
            flag = True
            errors['first_name_length'] = "Your first name must be at least two characters long!"
        if len(data['last_name']) < 2:
            flag = True
            errors['last_name_length'] = "Your last name must be at least two characters long."
        if not EMAIL_REGEX.match(data['email']):
            flag = True
            errors['email'] = "We're going to need a VALID email address."
        for char in range(len(data['first_name'])):
            if NUM_REGEX.match(data['first_name'][char]):
                errors['first_name_number'] = "No numbers are allowed in first names."
                flag = True
                break
        for char in range(len(data['last_name'])):
            if NUM_REGEX.match(data['last_name'][char]):
                errors['last_name_number'] = "No numbers are allowed in last names."
                flag = True
                break
        if len(data['password']) < 8:
            flag = True
            errors['password_length'] = "Password must be at least 8 characters long."
        if data['password'] != data['confirm_pw']:
            flag = True
            errors['password_match'] = "Password fields must match"
        if flag:
            return (False, errors)
        user = self.create(first_name=data['first_name'], last_name=data['last_name'],
                           email=data['email'], password=bcrypt.hashpw(data['password'], bcrypt.gensalt()))
        return (True, user)

    def userLogin(self, form):
        flag = False
        errors = {}
        data = uni_to_str(form)
        try:
            current_user = User.manager.get(email=data['email'])
        except Exception:
            errors['email'] = "That email does not exist in our records."
            return (False, errors)
        if not bcrypt.checkpw(data['password'].encode(), current_user.password.encode()):
            flag = True
            errors['password'] = "That password doesn't match the one we have..."
        if flag:
            return (False, errors)
        return (True, current_user)


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manager = UserManager()
