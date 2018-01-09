from __future__ import unicode_literals

from django.db import models

class Owner(models.Model):
	name = models.CharField(max_length=255)

class Pet(models.Model):
	name = models.CharField(max_length=255)
	species = models.CharField(max_length=255)
	breed = models.CharField(max_length=255)
	owner = models.ForeignKey(Owner, related_name="pets")
