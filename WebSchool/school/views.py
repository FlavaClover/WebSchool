import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from school.models import News, Feedback, Course, RequestToCourse, Groups, Schedule, Teachers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from school import forms


# Create your views here.

class NewsListView(ListView):
    paginate_by = 3
    model = News
    template_name = "html/index.html"


class FeedBacksListView(ListView):
    paginate_by = 3
    model = Feedback
    template_name = "html/feedbacks.html"


class CoursesListView(ListView):
    paginate_by = 3
    model = Course
    template_name = "html/courses.html"


def news_view(request, id_news: int) -> HttpResponse:
    """Страница под новость"""
    news = News.objects.get(id=id_news)
    return render(request, "html/news.html", context={"News": news})


def send_feedback(request) -> HttpResponse:
    """Отправка отзыва"""
    if request.POST:
        form = forms.Feedbacks(request.POST)
        short = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        date = datetime.date.today()
        f = Feedback.objects.create(title=short, content=content, author=author, date=date)
        f.save()

    return render(request, "html/send_feedback.html", context={"FeedbackForm": forms.Feedbacks})


def request_to_courses(request) -> HttpResponse:
    """Форма отправки заявки на обучение"""
    if request.POST:
        name = request.POST.get('name')
        telegram = request.POST.get('telegram') if request.POST.get('telegram') != '' else '-'
        phone = request.POST.get('phone')
        r = RequestToCourse.objects.create(name=name, telegram=telegram, phone=phone)
        r.save()

    return render(request, "html/send_request_course.html", context={"RequestForm": forms.RequestToCourses})


def login_page(request) -> HttpResponse:
    """Страница входа в личный кабинет"""
    err_msg = ""
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            err_msg = 'Пользователя не существует'
        elif not user.is_active:
            err_msg = 'Пользователь заблокирован'
        else:
            login(request, user)
            return redirect('personal_account')

    return render(request, 'html/login.html', context={'LoginForm': forms.LoginForm, 'err_msg': err_msg})


@login_required(login_url='login')
def personal_account_page(request) -> HttpResponse:
    user = request.user

    user_courses = list()

    groups = Groups.objects.all()
    for i in groups:
        if i.id_student == user.id:
            user_courses.append(Course.objects.get(id=i.id_course))
    print(user_courses)
    return render(request, 'html/personal_account.html', context={
        'User': user,
        'Courses': user_courses,
    })


@login_required(login_url="login")
def my_course(request, id_course: int) -> HttpResponse:
    course = Course.objects.get(id=id_course)
    user = request.user

    schedule_of_course = Schedule.objects.filter(id_course=course.id)
    times = list()
    for s in schedule_of_course:
        if s.time not in times:
            times.append(s.time)

    days = list(range(1, 8))

    schedule = list()
    for t in times:
        sch = []
        for d in days:
            flag = False
            for s in schedule_of_course:
                if s.time == t and s.day == d:
                    flag = True
                    sch.append(s.time)
            if not flag:
                sch.append("")
        schedule.append(sch)

    print(schedule)

    teacher = course.teacher

    return render(request, "html/my_course.html", context={
        "Course": course,
        "User": user,
        "Schedule": schedule,
        "Days": days,
        "Times": times,
        "Teacher": teacher,
    })


@login_required(login_url='login')
def exit_from_personal_account(request):
    logout(request)
    return redirect('home')
