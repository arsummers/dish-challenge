from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, world. The dish list will go here')
