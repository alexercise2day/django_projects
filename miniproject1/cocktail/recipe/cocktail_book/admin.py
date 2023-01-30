from django.contrib import admin
from .models import Vodka, Rum, Gin, Tequila, Whiskey

# Register your models here.
admin.site.register(Vodka)
admin.site.register(Rum)
admin.site.register(Gin)
admin.site.register(Tequila)
admin.site.register(Whiskey)