# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Album(models.Model):
    album_title = models.CharField(max_length=150)
    album_singer = models.CharField(max_length=100)

    def __str__(self):
        return self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    song_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.song_name

class Genre(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']    

    def __str__(self):
        return self.name


class Country(MPTTModel):
    country = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
    related_name='children')

    class MPTTMeta:
        order_insertion_by = ['country']    

    def __str__(self):
        return self.country

class Clinic(MPTTModel):
    clinic_name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True, related_name='child1')


class SubClinic(MPTTModel):
    subclinic_name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey(Clinic, on_delete=models.CASCADE, null=True, blank=True, related_name='child2')
    