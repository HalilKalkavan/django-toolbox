from django.shortcuts import render
from django.http import HttpRequest

def index(request):
    return HttpRequest('Hello world')

# Create your views here.
