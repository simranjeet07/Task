# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Album, Song, Genre, Country

# Create your views here.

def display_album_songs(request):
    album_obj = Album.objects.all()
    album_obj1 = Album.objects.get(id=1)
    song_obj = Song.objects.filter(album=album_obj1)
    return render(request,"myapp/home.html",{'album_obj':album_obj,'song_obj':song_obj})

def show_genres(request):
    return render(request,"myapp/genre.html",{'genres':Genre.objects.all()})

def show_country(request):
    return render(request,"myapp/country.html",{'country':Country.objects.all()})

