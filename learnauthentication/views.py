# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import RegistrationForm
# Create your views here.

def home(request):
    return render(request, 'learnauthentication/home.html', {})
