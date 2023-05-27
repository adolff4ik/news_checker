from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods
from django.views.generic.list import ListView
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

class ShowArticles(DataMixin, ListView):
    paginate_by = 8
    model = Article
    template_name = 'newsapp/articles.html'
    context_object_name = 'articles'


class HeadlineSerch(ListView):
    template_name = 'newsapp/search_results.html'
    context_object_name = 'results'
    paginate_by = 4

    def post(self, request, *args, **kwargs):
        country = self.request.POST.get('country')
        keyword = self.request.POST.get('keyword')
        category = self.request.POST.get('category')

        self.request.POST.keys()
        
        articles_json = get_articles_headlines(keyword=keyword, country=country, category=category)
        queryset = DataMixin().results(articles_json, keyword)
        
        self.object_list = queryset

        request.session['object_list'] = self.object_list

        request.session['country'] = country
        request.session['keyword'] = keyword
        request.session['category'] = category

        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)

        context['country'] = self.request.session['country']
        context['keyword'] = self.request.session['keyword']
        context['category'] = self.request.session['category']
        return context
    
    def get_queryset(self):
        return self.request.session['object_list']



class EverythingSearch(ListView):
    template_name = 'newsapp/everything_results.html'
    context_object_name = 'results'
    paginate_by = 4

    def post(self, request, *args, **kwargs):
        language = self.request.POST.get('language')
        keyword = self.request.POST.get('keyword')

        self.request.POST.keys()
        
        articles_json = get_articles_everything(keyword=keyword, language=language)
        queryset = DataMixin().results(articles_json, keyword)
        
        self.object_list = queryset

        request.session['object_list'] = self.object_list

        request.session['language'] = language
        request.session['keyword'] = keyword

        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)

        context['language'] = self.request.session['language']
        context['keyword'] = self.request.session['keyword']
        return context
    
    def get_queryset(self):
        return self.request.session['object_list']



def show_artcl(request, artcl_id):
    articles = get_object_or_404(Article, id=artcl_id)

    context = {
        'title': 'articles',
        'article': articles,
    }
    return render(request, 'newsapp/artcl.html', context=context)


