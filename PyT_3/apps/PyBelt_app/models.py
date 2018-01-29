from __future__ import unicode_literals
from django.db import models
import re
import bcrypt


NUM_REGEX = re.compile(r'[^a-zA-Z]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def uni_to_str(myDict):
    data = {}
    for key, val in myDict.iteritems():
        if key != 'csrfmiddlewaretoken':
            data[key] = str(val)
    return data


class UserManager(models.Manager):
    def validateUser(self, post_data):
        
		is_valid = True
		errors = []

		if len(post_data.get('name')) < 3:
			is_valid = False
			errors.append('Name must be 3 characters or longer!')

		if len(post_data.get('username')) < 3:
			is_valid = False
			errors.append('username must be 3 characters or longer!')

		if len(post_data.get('email')) < 1:
			is_valid = False
			errors.append('Email is required!')

		if not re.search(r'\w+\@\w+.\w+', post_data.get('email')):
			is_valid = False
			errors.append('Invalid Email')

		if len(post_data.get('password')) < 8:
			is_valid = False
			errors.append('Password must be at least 8 characters')

		if post_data.get('password_confirmation') == post_data.get('password'):
			is_valid = False
			errors.append('Confirm Password must match Password!')

		
		return (is_valid, errors)

    
     

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
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    # created_at = models.DateTimeField(default=datetime.date, null=True, blank=True)
    # updated_at = models.DateTimeField(default=datetime.date, null=True, blank=True)
    manager = UserManager()
    objects = UserManager()
    yourwishitems = models.ManyToManyField("wish", related_name="favorites", default=None)
    


def __str__(self):
	return "name:{}, username:{}, email:{}, password:{}, created_at:{}, updated_at:{}".format(self.name, self.username, self.email, self.password, self.created_at, self.updated_at)



class WishManager(models.Manager):
    def validateWish(self, post_data):
        is_valid = True
        errors = []
        if len(post_data.get('item')) < 3:
            is_valid = False
            errors.append('Message must be more than 3 characters')
            return (is_valid, errors)

class Wish(models.Model):
    user = models.ForeignKey(User, related_name="wishes")
    item = models.CharField(max_length=255)
    wishers = models.ManyToManyField(User, related_name="items")
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    objects = WishManager()



# created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
