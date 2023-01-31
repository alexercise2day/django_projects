from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response

# Create your views here.
def base(request):
    return render(request, 'base.html')

def vodka(request):
    vodka_list = Vodka.objects.all().order_by('name')
    return render(request, 'vodka.html', {'vodka_list': vodka_list})


