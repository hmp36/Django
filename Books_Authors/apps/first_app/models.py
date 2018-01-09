from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Authors(models. Model):
    books = models.ManyToManyField(Books,related_name="anything")
    firs_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nodes = models.TextField(max_length=1000)
class Authors_Books(models. Model):
    book=models.ForeignKey(Books, related_name="author")
    author=models.ForeignKey(Authors,related_name="books")

