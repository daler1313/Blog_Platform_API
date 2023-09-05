from django.db import models


class Category(models.Model):
    title = models.CharField('имя',max_length=50)
    description = models.TextField('опесание', blank=True, null=True)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name