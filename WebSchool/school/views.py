from django.shortcuts import render
from django.http import HttpResponse
from school.models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    objects = News.objects.all()
    objects = list(reversed(objects))
    paginator = Paginator(objects, 3)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        news = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        news = paginator.page(paginator.num_pages)
    return render(request, "html/index.html", context={"News": news, 'page': page})


def news_view(request, id_news):
    news = News.objects.get(id=id_news)
    return render(request, "html/news.html", context={"News": news})