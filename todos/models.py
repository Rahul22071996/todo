from django.db import models

# Create your models here.


class ToDOWorks(models.Model):
	name_of_work = models.CharField(max_length=255)
	complete = models.BooleanField(default= False)
	incomplete = models.BooleanField(default=False)