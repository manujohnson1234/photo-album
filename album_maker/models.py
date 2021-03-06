from django.db import models

# Create your models here.



class Category(models.Model):
	name = models.CharField(max_length=200, null=False, blank=False)

	def __str__(self):
		return self.name


class Album(models.Model):
	photo = models.ImageField(null=False, blank=False)
	description = models.TextField()
	date = models.DateField(auto_now_add=True)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.description
