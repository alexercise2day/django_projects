from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response

# Create your views here.
def base(request):
    return render(request, 'base.html')

def cocktails(request):
    return render(request, 'cocktails.html')

def vodka(request):
    return render(request, 'vodka.html')



