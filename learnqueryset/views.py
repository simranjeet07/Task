# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Blog, Entry, Author
from django.db.models import Q
# Create your views here.

def home_view(request):
    blog_obj1 = Blog.objects.all()
    blog_obj2 = Blog.objects.filter(name='Beatles Blog')
    blog_obj3 = Blog.objects.filter(name__contains='Blog')
    blog_obj4 = Blog.objects.filter(name__exact='Beatles Blog')
    blog_obj5 = Blog.objects.filter(name__iexact='beatles blog')
    blog_obj6 = Blog.objects.filter(name='Beatles Blog').exclude(tagline='hello')
    blog_obj7 = Blog.objects.all().order_by('name')
    blog_obj8 = Blog.objects.all().distinct('name')
    blog_obj9 = Blog.objects.filter(name__icontains='blog')
    blog_obj10 = blog_obj7.union(blog_obj8)
    blog_obj11 = blog_obj7.intersection(blog_obj8)
    blog_obj12 = Blog.objects.filter(id__lte=2)
    blog_obj13 = Blog.objects.filter(id__gt=2)
    blog_obj14 = Blog.objects.filter(Q(name__contains='Blog') | Q(name__contains='singh'))
    blog_obj15 = Blog.objects.filter(Q(name__contains='Blog') & Q(name__contains='singh'))
    blog_obj16 = Blog.objects.filter(Q(name__icontains='blog') | Q(name__contains='singh'))
    blog_obj18 = Blog.objects.all()[:3]
    blog_obj19 = Blog.objects.all()[1:3]
    blog_obj20 = Blog.objects.get(id=2)
    entry_obj1 = Entry.objects.filter(blog=blog_obj20)
    

    print blog_obj1
    print blog_obj2
    print blog_obj3
    print blog_obj4
    print blog_obj5
    print blog_obj6
    print blog_obj7
    print blog_obj8
    print blog_obj9
    print blog_obj10
    print blog_obj11
    print blog_obj12
    print blog_obj13
    print blog_obj14
    print blog_obj15
    print blog_obj16
    print blog_obj18
    print blog_obj19
    print blog_obj20
    print entry_obj1
    for q in entry_obj1:
        print q.body_text
        for x in q.authors.all():
            print x.name

    return render(request,"learnqueryset/home.html",{})
