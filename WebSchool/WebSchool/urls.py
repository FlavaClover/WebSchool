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
from school import views as views_user
from admins_tools import views as views_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_user.NewsListView.as_view(), name='home'),
    path('news/<int:id_news>', views_user.news_view, name='news_page'),
    path('feedbacks/', views_user.FeedBacksListView.as_view(), name='feedbacks'),
    path('sendfeedback/', views_user.send_feedback, name='send_feedback'),
    path('courses/', views_user.CoursesListView.as_view(), name='courses'),
    path('request_to_courses/', views_user.request_to_courses, name='request_to_courses'),
    path('login/', views_user.login_page, name='login'),

    path('personal_account/', views_user.personal_account_page, name='personal_account'),
    path('personal_account/exit/', views_user.exit_from_personal_account, name='exit'),
    path('personal_account/course/<int:id_course>/', views_user.my_course, name='my_course'),

    path('personal_account_admin/', views_admin.personal_account, name='admin_personal_account'),

]
