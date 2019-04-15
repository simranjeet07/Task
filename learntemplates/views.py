# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Person
import datetime

# Create your views here.

def learn_template(request):
    obj = Person.objects.all()
    x = datetime.datetime(2019, 4, 4)
    return render(request, "learntemplates/home.html", 
    {'obj': obj, 'list1': [1,2,3], 'list2': [4,5,6], 
    'value':'django app', 'datetime_obj': x, 
    'num': 20, 'phone':'800-COLLECT', 
    'pick': [1,2,3,4], 
    'val': 'Joe Roy Great Person'})