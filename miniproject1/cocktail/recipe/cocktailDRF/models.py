from django.db import models

# Create your models here.
class cocktail(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField(max_length=500)
    instructions = models.TextField(max_length=500)
    # image = models.ImageField(upload_to='images/')