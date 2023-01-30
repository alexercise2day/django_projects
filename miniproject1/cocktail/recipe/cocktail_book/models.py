from django.db import models

# Create your models here.

class Vodka(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.TextField(max_length='1000', default='')
    instructions = models.TextField(max_length='1000', default='')

class Rum(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.TextField(max_length='1000', default='')
    instructions = models.TextField(max_length='1000', default='')

class Gin(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.TextField(max_length='1000', default='')
    instructions = models.TextField(max_length='1000', default='')

class Tequila(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.TextField(max_length='1000', default='')
    instructions = models.TextField(max_length='1000', default='')
    
class Whiskey(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.TextField(max_length='1000', default='')
    instructions = models.TextField(max_length='1000', default='')