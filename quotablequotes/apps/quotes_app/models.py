from __future__ import unicode_literals

from django.db import models
import re
import bcrypt


class UserManager(models.Manager):
	def validateUser(self, post_data):

		is_valid = True
		errors = []

		if len(post_data.get('name')) < 3:
			is_valid = False
			errors.append('Name must be 3 characters or longer!')

		if len(post_data.get('alias')) < 3:
			is_valid = False
			errors.append('Alias must be 3 characters or longer!')

		if len(post_data.get('email')) < 1:
			is_valid = False
			errors.append('Email is required!')

		if not re.search(r'\w+\@\w+.\w+', post_data.get('email')):
			is_valid = False
			errors.append('Invalid Email')

		if len(post_data.get('password')) < 8:
			is_valid = False
			errors.append('Password must be at least 8 characters')

		if post_data.get('password_confirmation') != post_data.get('password'):
			is_valid = False
			errors.append('Confirm Password must match Password!')

		if len(post_data.get('birthdate')) < 1:
			is_valid = False
			errors.append('Date of Birth is required!')
		return (is_valid, errors)


class User(models.Model):
	name = models.CharField(max_length=45)
	alias = models.CharField(max_length=45)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	birthdate = models.DateField()
	favorites = models.ManyToManyField(
		"Quote", related_name="favorites", default=None)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

	def __str__(self):
		return "name:{}, alias:{}, email:{}, password:{}, created_at:{}, updated_at:{}".format(self.name, self.alias, self.email, self.password, self.created_at, self.updated_at)


class QuoteManager(models.Manager):
	def validateQuote(self, post_data):

		is_valid = True
		errors = []

		if len(post_data.get('content')) < 12:
			is_valid = False
			errors.append('Message must be more than 10 characters')
		return (is_valid, errors)


class Quote(models.Model):
	content = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	poster = models.ForeignKey(User, related_name='authored_quotes')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = QuoteManager()

	def __str__(self):
		return 'content:{}, author:{}'.format(self.content, self.user)
