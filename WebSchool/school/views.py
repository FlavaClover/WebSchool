from django.shortcuts import render
from django.http import HttpResponse
from school.models import News

# Create your views here.


def index(request):
    news = News.objects.all()
    news = reversed(news)
    return render(request, "html/index.html", context={"News": news})


def news_view(request, id_news):
    news = News.objects.get(id=id_news)
    return HttpResponse(news.content)