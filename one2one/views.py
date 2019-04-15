# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Car, Engine, Country

# Create your views here.

def display_car_engine(request):
    engine_obj = Engine.objects.all()
    return render(request,"one2one/home.html",{'engine_obj':engine_obj})

def show_country(request):
    return render(request,"one2one/country.html",{'country':Country.objects.all()})