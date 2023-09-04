from django.db import models


class Comment(models.Model):
  user = models.ForeignKey("users.user",on_delete=models.CASCADE)
  post = models.ForeignKey("posts.post", on_delete=models.CASCADE)
  text = models.TextField("комметарий")
  date = models.DateTimeField("Дата созадние")

  class Meta:
    verbose_name = "комметарий"
    verbose_name_plural = "комметарии"

  def __str__(self):
    return f"{self.text}"
