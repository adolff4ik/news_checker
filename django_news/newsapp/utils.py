from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from .get_articles import *
from django.contrib.sessions.backends.db import SessionStore
from .models import *
from .parser import *


class SearchView(ListView):
    context_object_name = 'results'
    paginate_by = 4
    api_url =''

    def post(self, request):
        keyword = self.request.POST.get('q','')
        user = request.user

        post_data = request.POST.dict()

        del post_data['csrfmiddlewaretoken']
        
        articles_json = get_articles(self.api_url,post_data)
        queryset = results(articles_json, keyword, user)
        
        self.object_list = queryset

        request.session['object_list'] = self.object_list

        for key, value in post_data.items():
            request.session[key] = value

        return self.get(request)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)

        session_dict = dict(self.request.session.items())
        del session_dict['object_list']

        for key, value in session_dict.items():
            context[key] = value

        return context
    
    def get_queryset(self):
        return self.request.session['object_list']


def results(articles_json,keyword,user):
    
    num = min(20, articles_json.get("totalResults", 0))
    
    if articles_json["totalResults"] > 20:
        num = 20
    else:
        num = int(articles_json["totalResults"])
    
    results = []

    for i in range(num):
        print(f'починаю статтю {i}')
        article = articles_json["articles"][i]
        pubdate = article.get("publishedAt", "")
        name = article.get("source", {}).get("name", "")
        title = article.get("title", "")
        description = article.get("description", "")
        link = article.get("url", "")
        print('отримав данні')

        try:
            content = parsed(url=link)
        except:
            content = 'не доросли ви до такого....'
        
        print('отримав контекст')

        db_create(user=user,keyword=keyword,pubdate=pubdate,name=name,
                    title=title,description=description,
                    link=link,content=content)

        results.append({'title': f'{title}', 'description': f'{description}', 'link': f'{link}'})
        print(f'стаття {i}')
    return results

def db_create(user,keyword,pubdate,name,title,description,link,content):
    if Article.objects.filter(link=link).exists():
        pass
    else:
        article = Article(user=user,
        keyword=keyword, pubdate=pubdate, name=name, title=title,
        description=description, link=link, content=content
        )
        article.save()

        cat_name, _ = Category.objects.get_or_create(name=name)
        cat_num = CategoryNum.objects.filter(name=cat_name).first()

        if cat_num:
            cat_num.num += 1
            cat_num.save()
        else:
            CategoryNum(name=cat_name, num=1).save()