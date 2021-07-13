import datetime

from django.shortcuts import render
from django.http import HttpResponse
from school.models import News, Feedback, Course
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from school import forms

# Create your views here.


def index(request) -> HttpResponse:
    """Главная"""
    objects = News.objects.all()
    objects = list(reversed(objects))
    paginator = Paginator(objects, 3)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, "html/index.html", context={"News": news, 'page': page})


def news_view(request, id_news: int) -> HttpResponse:
    """Страница под новость"""
    news = News.objects.get(id=id_news)
    return render(request, "html/news.html", context={"News": news})


def feedbacks(request) -> HttpResponse:
    """Отзывы"""
    objects = Feedback.objects.all()
    objects = list(reversed(objects))
    paginator = Paginator(objects, 3)
    page = request.GET.get('page')
    try:
        feedbacks_models = paginator.page(page)
    except PageNotAnInteger:
        feedbacks_models = paginator.page(1)
    except EmptyPage:
        feedbacks_models = paginator.page(paginator.num_pages)
    return render(request, "html/feedbacks.html", context={"Feedbacks": feedbacks_models, 'page': page})


def send_feedback(request) -> HttpResponse:
    """Отправка отзыва"""
    if request.POST:
        short = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        date = datetime.date.today()
        f = Feedback.objects.create(title=short, content=content, author=author, date=date)
        f.save()

    return render(request, "html/send_feedback.html", context={"FeedbackForm": forms.Feedbacks})


def courses(request) -> HttpResponse:
    objects = Course.objects.all()
    objects = list(reversed(objects))
    paginator = Paginator(objects, 3)
    page = request.GET.get('page')
    try:
        courses_model = paginator.page(page)
    except PageNotAnInteger:
        courses_model = paginator.page(1)
    except EmptyPage:
        courses_model = paginator.page(paginator.num_pages)

    return render(request, "html/courses.html", context={"Courses": courses_model, 'page': page})

def request_to_courses(request) -> HttpResponse:
    return HttpResponse("Ok")