# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Books, Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['sku', 'title', 'unit', 'unitCost', 'quantity']
    list_filter = ('sku', 'unit') 
    fieldsets = (
        ('Section 1', {
            'fields': ('title','description')
        }),        
        ('Section 2', {
            'fields': ('sku','barcode','unit', 'unitCost','quantity','minQuantity')
        }),
    ) 
admin.site.register(Books)
admin.site.register(Product, ProductAdmin)
admin.site.site_header = 'LearnDjango'
admin.site.site_title = 'LearnDjango'