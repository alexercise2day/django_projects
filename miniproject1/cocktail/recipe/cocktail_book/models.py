from django.db import models

# Create your models here.

class Vodka(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    notes = models.TextField()
    image = models.ImageField(upload_to='media/img/', default='')
    background = models.TextField(max_length='2000', default='')

class Rum(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField(max_length='1000', default='')
    instructions = models.TextField(max_length='1000', default='')
    notes = models.TextField(max_length='1000', default='')
    image = models.ImageField(upload_to='media/img/', default='')
    background = models.TextField(max_length='2000', default='')

class Gin(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField(max_length='1000', default='')
    instructions = models.TextField(max_length='1000', default='')
    notes = models.TextField(max_length='1000', default='')
    image = models.ImageField(upload_to='media/img/', default='')
    background = models.TextField(max_length='2000', default='')

class Tequila(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField(max_length='1000', default='')
    instructions = models.TextField(max_length='1000', default='')
    notes = models.TextField(max_length='1000', default='')
    image = models.ImageField(upload_to='media/img/', default='')
    background = models.TextField(max_length='2000', default='')
    
class Whiskey(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField(max_length='1000', default='')
    instructions = models.TextField(max_length='1000', default='')
    notes = models.TextField(max_length='1000', default='')
    image = models.ImageField(upload_to='media/img/', default='')
    background = models.TextField(max_length='2000', default='')