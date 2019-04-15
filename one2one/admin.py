# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Engine, Car, Country

# Register your models here.

admin.site.register(Car)
admin.site.register(Engine)
admin.site.register(Country)