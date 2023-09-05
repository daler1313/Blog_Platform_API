from django.db import models


class Post(models.Model):
  title = models.CharField("Название",max_length=50)
  description = models.TextField("Описание")
  date = models.DateTimeField(("Дата созадние"))
  image = models.ImageField("Фото",upload_to='images/')
  user = models.ForeignKey( "users.user", on_delete=models.CASCADE)
  category = models.ManyToManyField( "categories.category")

  class Meta:
    verbose_name = "пост"
    verbose_name_plural = "посты"

  def __str__(self):
    return f"{self.title}"


