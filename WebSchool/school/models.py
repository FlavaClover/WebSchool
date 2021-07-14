from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=150, null=False)
    content = models.TextField(max_length=5555, null=False)
    author = models.CharField(max_length=100, null=False)
    img = models.CharField(max_length=30, null=False, default="news.jpg")

    def __repr__(self):
        return f'{News.__name__}({self.title})'


class Feedback(models.Model):
    title = models.CharField(max_length=150, null=False)
    content = models.TextField(max_length=5555, null=False)
    author = models.CharField(max_length=100, null=False)
    date = models.DateField(null=False)

    def __repr__(self):
        return f'{Feedback.__name__}({self.title}, {self.author}, {self.date})'


class Course(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(null=False)
    price = models.IntegerField(null=False)

    def __repr__(self):
        return f'{Course.__name__}({self.name}, {self.price})'


class RequestToCourse(models.Model):
    name = models.CharField(max_length=150, null=False)
    telegram = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=False)

