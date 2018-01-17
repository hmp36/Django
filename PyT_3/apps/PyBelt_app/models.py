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

    
    
    
    
    # def makeUser(self, form):   
    #     flag = False
    #     errors = {}
    #     data = uni_to_str(form)
    #     for val in data.itervalues():
    #         if len(val) < 1:
    #             flag = True
    #             errors['blank'] = "All fields are required! Please make sure you provided an entry in each."
    #             break
    #     if len(data['name']) < 2:
    #         flag = True
    #         errors['name_length'] = "Your name must be at least two characters long!"
    #     if len(data['username']) < 2:
    #         flag = True
    #         errors['username_length'] = "Your username must be at least two characters long."
    #     if not EMAIL_REGEX.match(data['email']):
    #         flag = True
    #         errors['email'] = "We're going to need a VALID email address."
    #     for char in range(len(data['name'])):
    #         if NUM_REGEX.match(data['name'][char]):
    #             errors['name_number'] = "No numbers are allowed in names."
    #             flag = True
    #             break
        
    #     if len(data['password']) < 8:
    #         flag = True
    #         errors['password_length'] = "Password must be at least 8 characters long."
    #     if data['password'] != data['confirm_pw']:
    #         flag = True
    #         errors['password_match'] = "Password fields must match"
    #     if flag:
    #         return (False, errors)
    #     user = self.create(name=data['name'], username=data['username'],
    #                        email=data['email'], password=bcrypt.hashpw(data['password'], bcrypt.gensalt()))
    #     return (True, user)






#       def validateUser(self, post_data):
    
# 		is_valid = True
# 		errors = []

# 		if len(post_data.get('name')) < 3:
# 			is_valid = False
# 			errors.append('Name must be 3 characters or longer!')

# 		if len(post_data.get('alias')) < 3:
# 			is_valid = False
# 			errors.append('Alias must be 3 characters or longer!')

# 		if len(post_data.get('email')) < 1:
# 			is_valid = False
# 			errors.append('Email is required!')

# 		if not re.search(r'\w+\@\w+.\w+', post_data.get('email')):
# 			is_valid = False
# 			errors.append('Invalid Email')

# 		if len(post_data.get('password')) < 8:
# 			is_valid = False
# 			errors.append('Password must be at least 8 characters')

# 		if post_data.get('password_confirmation') != post_data.get('password'):
# 			is_valid = False
# 			errors.append('Confirm Password must match Password!')

# 		if len(post_data.get('birthdate')) < 1:
# 			is_valid = False
# 			errors.append('Date of Birth is required!')
# 		return (is_valid, errors)


# # class User(models.Model):
# # 	name = models.CharField(max_length=45)
# # 	alias = models.CharField(max_length=45)
# # 	email = models.CharField(max_length=255)
# # 	password = models.CharField(max_length=255)
# # 	birthdate = models.DateField()
# # 	favorites = models.ManyToManyField(
# # 		"Quote", related_name="favorites", default=None)
# # 	created_at = models.DateTimeField(auto_now_add=True)
# # 	updated_at = models.DateTimeField(auto_now=True)
# # 	objects = UserManager()





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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manager = UserManager()
    objects = UserManager()
