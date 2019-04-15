# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render, redirect, reverse
# Create your models here.

class Product(models.Model):
    sku = models.CharField(max_length=13,help_text="Enter Product Stock Keeping Unit")
    barcode = models.CharField(max_length=13,help_text="Enter Product Barcode (ISBN, UPC ...)")

    title = models.CharField(max_length=200, help_text="Enter Product Title")
    description = models.TextField(help_text="Enter Product Description")

    unitCost = models.FloatField(help_text="Enter Product Unit Cost")
    unit = models.CharField(max_length=10,help_text="Enter Product Unit ")

    quantity = models.FloatField(help_text="Enter Product Quantity")
    minQuantity = models.FloatField(help_text="Enter Product Min Quantity")

class Books(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('list')