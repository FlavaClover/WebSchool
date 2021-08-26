from django.contrib import admin
from school.models import News, Course, Feedback, Teachers, Schedule

# Register your models here.
admin.site.register(News)
admin.site.register(Course)
admin.site.register(Feedback)
admin.site.register(Teachers)
admin.site.register(Schedule)