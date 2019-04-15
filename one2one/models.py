# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Engine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    engine = models.OneToOneField(Engine)

    def __str__(self):
        return self.name

class Country(MPTTModel):
    country = models.CharField(max_length=100, unique=True)
    clinic_name = models.CharField(max_length=100, unique=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['country']    

    def __str__(self):
        return self.country
