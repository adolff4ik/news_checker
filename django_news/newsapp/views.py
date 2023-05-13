from django.shortcuts import get_object_or_404, render
from .get_articles import get_articles_everything, get_articles_headlines
from .models import *
from .parser import *
from .utils import *


def home(request):
    context = {
        'title': 'bebra.site'
    }
    return render(request, 'newsapp/index.html', context=context)


def headlines(request):
    return render(request, 'newsapp/top-headlines.html')


def everything(request):
    return render(request, 'newsapp/everything.html')


def articles(request):
    articles = Article.objects.all()

    context = {
        'title': 'articles',
        'articles': articles,
    }

    return render(request, 'newsapp/articles.html', context=context)


def headlines_search(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        keyword = request.POST.get('keyword')
        category = request.POST.get('category')


        articles_json = get_articles_headlines(keyword=keyword,country=country,category=category)

        results=DataMixin().results(articles_json,keyword)

        context = {'country': country, 'keyword': keyword, 'category': category, 'results': results}
        return render(request, 'newsapp/search_results.html', context)
    else:
        return render(request, 'newsapp/search_results.html')


def everything_search(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        language = request.POST.get('language')

        articles_json = get_articles_everything(keyword=keyword,language=language)

        results=DataMixin().results(articles_json,keyword)

        context = {'keyword': keyword, 'language': language, 'results': results}
        return render(request, 'newsapp/everything_results.html', context)
    else:
        return render(request, 'newsapp/everything_results.html')


def show_artcl(request, artcl_id):
    articles = get_object_or_404(Article, id=artcl_id)

    context = {
        'title': 'articles',
        'article': articles,
    }
    return render(request, 'newsapp/artcl.html', context=context)