# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def search_user(request):
    if request.method == "POST":
        user_name = request.POST.get('search')
        users = User.objects.filter(username__icontains=user_name)
        return render(request, "searchusers/home.html", {'users': users})
    return render(request, "searchusers/search.html", {})

