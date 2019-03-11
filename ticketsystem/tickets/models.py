from django.db import models
from datetime import datetime 

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=200)


class Tickets(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	stage = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=datetime.now, blank=True)


