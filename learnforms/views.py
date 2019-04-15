# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import LoginForm, UrlForm
from .models import Login, Identification
from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse_lazy
# Create your views here.

def user_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "learnforms/login.html",{'user':request.user})
    return render(request, "learnforms/home.html", {'form':form})


def user_email(request):
    form = UrlForm(request.POST or None)
    if form.is_valid():
        url = form.cleaned_data['url']
        return redirect(url)
    return render(request, "learnforms/url.html", {'form':form})


def learn_manager(request):
    obj = Identification.people.all()
    return render(request, "learnforms/manager.html",{'obj':obj})
    