from django.db import models
from django.contrib.auth.models import User
from school.validators import *


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


class Teachers(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100, null=True)
    mail = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, validators=[validate_phone])

    def __repr__(self):
        return f"{Teachers.__name__}({self.second_name} {self.first_name}, " \
               f"{self.phone}, {self.telegram})"


class Course(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(null=False)
    price = models.IntegerField(null=False)
    link_to_materials = models.CharField(max_length=500, null=True, default="https://disk.yandex.ru/d/Peol1rVjZTEjrA")
    schedule_number = models.IntegerField(null=True)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return f'{Course.__name__}({self.name}, {self.price})'


class RequestToCourse(models.Model):
    name = models.CharField(max_length=150, null=False)
    telegram = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=False)


class Groups(models.Model):
    id_student = models.IntegerField(null=False)
    id_course = models.IntegerField(null=False)

    def __repr__(self):
        return f'{Groups.__name__}(student: {self.id_student}, course: {self.id_course})'


class Schedule(models.Model):
    id_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    schedule_number = models.IntegerField(null=False)
    day = models.IntegerField(validators=[validate_day])
    time = models.TimeField()

    class Meta:
        ordering = ['time', 'day']

    def __repr__(self):
        return f'{Schedule.__name__}(number: {self.schedule_number}, day: {self.day}, course: {self.id_course}, ' \
               f'time: {self.time})'

