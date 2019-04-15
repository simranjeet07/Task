# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Person(models.Model):
    person_name = models.CharField(max_length=100)

    def __str__(self):
        return self.person_name


class Group(models.Model):
    group_name = models.CharField(max_length=150)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.group_name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group)
    date_joined = models.DateField()

    def __str__(self):
        return self.person.person_name

class Country(MPTTModel):
    country = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
    related_name='children')

    class MPTTMeta:
        order_insertion_by = ['country']    

    def __str__(self):
        return self.country
