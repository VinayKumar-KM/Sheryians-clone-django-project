from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

# Register your models here.

@register(Course)
class AdminCourse(admin.ModelAdmin):
    model=Course
    list_display=['cou_name','final_price']