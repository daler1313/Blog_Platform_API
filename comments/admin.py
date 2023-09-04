from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ("pk", "user", "post", "text","date")
  date_hierarchy =("date")
  
