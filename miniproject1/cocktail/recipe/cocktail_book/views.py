from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response

# Create your views here.
def home(request):
    return render(request, 'home.html')

