from django.db import models

# Create your models here.
<<<<<<< HEAD
class Category(models.Model):
	name = models.CharField(max_length =128, unique = True)
	views = models.IntegerField(default = 0)
	likes = models.IntegerField(default = 0)

	def __str__(self):
		return self.name

class page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length = 128)
	url = models.URLField()
	views = models.IntegerField(default = 0) 


	def __str__(self):
		return self.title
=======
>>>>>>> 2a624b6a079f0b36308200f492c8ead6f59515ea
