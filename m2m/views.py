# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Person, Group

# Create your views here.

def display_groups(request):
    group_obj = Group.objects.all()
    return render(request,"m2m/home.html",{'group_obj':group_obj})
