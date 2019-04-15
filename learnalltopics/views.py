# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Contacts
from django.core.paginator import Paginator, PageNotAnInteger
from django.core import serializers
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.

def learn_pagination(request):
    contact_list = Contacts.objects.all()
    paginator = Paginator(contact_list, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'learnalltopics/pagination.html', {'contacts': contacts})


def learn_serializers(request):
    data = serializers.serialize("xml", Contacts.objects.all())
    return render(request, "learnalltopics/serialization.html", {'data': data})


def send_email(request):
    send_mail('Never Give Up', 
    'Be focussed', 
    'simran909singh@gmail.com', 
    ['simran9098singh@gmail.com'],
    fail_silently=True,
    )
    return HttpResponse("Email Sent")
