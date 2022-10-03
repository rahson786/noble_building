from django.db import models

# Create your models here.
class Tag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	image = models.ImageField(upload_to='noble_building_llc/images/')
	url = models.URLField(blank=True)
	tags = models.ManyToManyField(Tag, null=True, blank=True)

	def __str__(self):
		return self.title


class People(models.Model):
	name = models.CharField(max_length=30)
	designation = models.CharField(max_length=30)
	description = models.CharField(max_length=200)
	image = models.ImageField(upload_to='noble_building_llc/images/')

	def __str__(self):
		return self.name