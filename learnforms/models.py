# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator, EmailValidator, MaxValueValidator, MinValueValidator
from .validators import validate_even
# Create your models here.

class AuthorManager(models.Manager):
    def get_queryset(self):
        return super(AuthorManager, self).get_queryset().filter(role='A')

class EditorManager(models.Manager):
    def get_queryset(self):
        return super(EditorManager, self).get_queryset().filter(role='E')


class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super(DahlBookManager, self).get_queryset().filter(author='Roald Dahl')

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20, validators=[RegexValidator('^(\w+\d+|\d+\w+)+$', message="Password should be a combination of Alphabets and Numbers")])
    email    = models.CharField(max_length=100, validators=[EmailValidator("please enter a valid email")])
    val      = models.IntegerField(validators=[MaxValueValidator(10,"enter value below 10"),
    MinValueValidator(0,"enter value above 0")])
    even_field = models.IntegerField(validators=[validate_even])


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    objects = models.Manager()
    dahl_objects = DahlBookManager()

class Identification(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=(('A', 'Author'), ('E', 'Editor')))
    people=models.Manager()
    authors=AuthorManager()
    editors=EditorManager()

