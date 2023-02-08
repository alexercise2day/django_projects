from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Vodka, Gin, Rum, Tequila, Whiskey

# Create your views here.
def base(request):
    return render(request, 'base.html')

def vodka_all(request):
    vodka_list = Vodka.objects.all()
    return render(request, 'vodka_list/vodka.html', {'vodka_list': vodka_list})

def vodka_display(request, pk):
    vodka_entry = get_object_or_404(Vodka, pk=pk)
    return render(request, 'vodka_list/vodka_display.html', {'vodka_entry': vodka_entry})

def rum_all(request):
    rum_list = Rum.objects.all()
    return render(request, 'rum_list/rum.html', {'rum_list': rum_list})

def rum_display(request, pk):
    rum_entry = get_object_or_404(Rum, pk=pk)
    return render(request, 'rum_list/rum_display.html', {'rum_entry': rum_entry})

def gin_all(request):
    gin_list = Gin.objects.all()
    return render(request, 'gin_list/gin.html', {'gin_list': gin_list})

def gin_display(request):
    gin_entry = get_object_or_404(Gin, pk=pk)
    return render(request, 'gin_list/gin_display.html', {'gin_entry': gin_entry})

def tequila_all(request):
    tequila_list = Tequila.objects.all()
    return render(request, 'tequila_list/tequila.html', {'tequila_list': tequila_list})

def tequila_display(request):
    tequila_entry = get_object_or_404(Tequila, pk=pk)
    return render(request, 'tequila_list/tequila_display', {'tequila_entry': tequila_entry})

def whiskey_all(request):
    whiskey_list = Whiskey.objects.all()
    return render(request, 'whiskey_list/whiskey.html', {'whiskey_list': whiskey_list})

def whiskey_display(request):
    whiskey_entry = get_object_or_404(Whiskey, pk=pk)
    return render(reqeust, 'whiskey_list/whiskey_display.html', {'whiskey_entry': whiskey_entry})    


