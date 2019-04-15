# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Album, Song, Genre, Country, Clinic, SubClinic

# Register your models here.

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Clinic)
admin.site.register(SubClinic)