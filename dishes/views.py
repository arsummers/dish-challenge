from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Dish

class HomePageView(ListView):
    model = Dish
    template_name = 'home.html'