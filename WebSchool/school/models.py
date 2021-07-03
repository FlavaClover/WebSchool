from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=150, null=False)
    content = models.TextField(max_length=5555, null=False)
    author = models.CharField(max_length=100, null=False)
    img = models.CharField(max_length=30, null=False, default="news.jpg")