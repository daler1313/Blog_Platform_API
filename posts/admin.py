from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ("pk", "title", "description","image", "user","date")
  search_fields = ("title","user")
  date_hierarchy = "date"
