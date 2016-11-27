from django.db import models

# Create your models here.

class Person(models.Model):
	first_name = models.CharField(max_length=20,null=True,blank=True)
	last_name = models.CharField(max_length=20,null=True,blank=True)
	birth_year = models.CharField(max_length=4,null=True,blank=True)
	position = models.IntegerField(null=True,blank=True)

	def __unicode__(self):
		return self.first_name