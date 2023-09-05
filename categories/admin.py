from django.contrib import admin
from .models import Category


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
  list_display = ("pk", "title", "description","parent_category")