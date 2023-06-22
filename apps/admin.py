from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Category


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass