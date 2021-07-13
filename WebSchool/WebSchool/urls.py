"""WebSchool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('news/<int:id_news>', views.news_view, name='news_page'),
    path('feedbacks/', views.feedbacks, name='feedbacks'),
    path('sendfeedback/', views.send_feedback, name='send_feedback'),
    path('courses/', views.courses, name='courses'),
    path('request_to_courses/', views.request_to_courses, name='request_to_courses'),
]
