from django.shortcuts import render
from .get_articles import get_articles
from .models import *


def home(request):
    context = {
        'title': 'bebra.site'
    }
    return render(request, 'newsapp/index.html', context=context)

def search(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        keyword = request.POST.get('keyword')

        try:
            articles_json = get_articles(keyword=keyword,country=country)

            if articles_json["totalResults"] > 5:
                num = 5
            else:
                num = int(articles_json["totalResults"])
            
            results = []

            for i in range(num):
                pubdate = articles_json["articles"][i]["publishedAt"]
                name = articles_json["articles"][i]["source"]["name"]
                title = articles_json["articles"][i]["title"]
                description = articles_json["articles"][i]["description"]
                link = articles_json["articles"][i]["url"]

                if Article.objects.filter(link=link):
                    pass
                else:
                    article = Article(
                    keyword=keyword, pubdate=pubdate, name=name, title=title, description=description, link=link
                    )
                    article.save()

                results.append({'title': f'{title}', 'description': f'{description}', 'link': f'{link}'})
        except:results = None
        context = {'country': country, 'keyword': keyword, 'results': results}
        return render(request, 'newsapp/search_results.html', context)
    else:
        return render(request, 'newsapp/search_form.html')