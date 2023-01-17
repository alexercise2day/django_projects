from django.contrib import admin
from .models import cocktail, Vodka, Rum

# Register your models here.
admin.site.register(cocktail)
admin.site.register(Vodka)
admin.site.register(Rum)