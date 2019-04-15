# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class RegisterUser(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20, validators=[RegexValidator('^(\w+\d+|\d+\w+)+$', message="Password should be a combination of Alphabets and Numbers")])
    confirm_password = models.CharField(max_length=20, validators=[RegexValidator('^(\w+\d+|\d+\w+)+$', message="Password should be a combination of Alphabets and Numbers")])
