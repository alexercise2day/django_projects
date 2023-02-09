from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from .models import Vodka, Gin, Rum, Tequila, Whiskey

# Create your views here.
def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def vodka_all(request):
    vodka_list = Vodka.objects.all().values()
    template = loader.get_template('vodka.html')
    context = {
        'vodka_list': vodka_list,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'vodka_list/vodka.html', {'vodka_list': vodka_list})

def vodka_display(request, id):
    vodka_entry = Vodka.objects.get(id=id)
    template = loader.get_template('vodka_display.html')
    context = {
        'vodka_entry': vodka_entry,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'vodka_list/vodka_display.html', {'vodka_entry': vodka_entry})

def rum_all(request):
    rum_list = Rum.objects.all().values()
    template = loader.get_template('rum.html')
    context = {
        'rum_list': rum_list,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'rum_list/rum.html', {'rum_list': rum_list})

def rum_display(request, id):
    rum_entry = Rum.objects.get(id=id)
    template = loader.get_template('rum_display.html')
    context = {
        'rum_entry': rum_entry,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'rum_list/rum_display.html', {'rum_entry': rum_entry})

def gin_all(request):
    gin_list = Gin.objects.all().values()
    template = loader.get_template('gin.html')
    context = {
        'gin_list': gin_list,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'gin_list/gin.html', {'gin_list': gin_list})

def gin_display(request, id):
    gin_entry = Gin.objects.get(id=id)
    template = loader.get_template('gin_display.html')
    context = {
        'gin_entry': gin_entry,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'gin_list/gin_display.html', {'gin_entry': gin_entry})

def tequila_all(request):
    tequila_list = Tequila.objects.all().values()
    template = loader.get_template('tequila.html')
    context = {
        'tequila_list': tequila_list,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'tequila_list/tequila.html', {'tequila_list': tequila_list})

def tequila_display(request, id):
    tequila_entry = Tequila.objects.get(id=id)
    template = loader.get_template('tequila_display.html')
    context = {
        'tequila_entry': tequila_entry,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'tequila_list/tequila_display', {'tequila_entry': tequila_entry})

def whiskey_all(request):
    whiskey_list = Whiskey.objects.all().values()
    template = loader.get_template('whiskey.html')
    context = {
        'whiskey_list': whiskey_list,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'whiskey_list/whiskey.html', {'whiskey_list': whiskey_list})

def whiskey_display(request, id):
    whiskey_entry = Whiskey.objects.get(id=id)
    template = loader.get_template('whiskey_display.html')
    context = {
        'whiskey_entry': whiskey_entry,
    }
    return HttpResponse(template.render(context, request))
    # return render(reqeust, 'whiskey_list/whiskey_display.html', {'whiskey_entry': whiskey_entry})    


