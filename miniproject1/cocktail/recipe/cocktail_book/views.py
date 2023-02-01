from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Vodka

# Create your views here.
def base(request):
    return render(request, 'base.html')

def vodka(request):
    vodka_list = Vodka.objects.all().order_by('name')
    return render(request, 'vodka.html', {'vodka_list': vodka_list})

def vodka_display(request):
    entry = get_object_or_404(Vodka, pk=pk)
    return render(request, 'vodka_display.html', {'entry': entry} )


