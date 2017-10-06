# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Size_Chart, Image_Chart
class Size_ChartAdmin(admin.ModelAdmin):
    list_display = ('Length_ID','Gender', 'Length', 'UK', 'EU')

class Image_ChartAdmin(admin.ModelAdmin):
    list_display = ('image','Gender')    

admin.site.register(Size_Chart, Size_ChartAdmin)
admin.site.register(Image_Chart, Image_ChartAdmin)