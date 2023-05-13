from django.shortcuts import get_object_or_404, render
from .get_articles import get_articles_everything, get_articles_headlines
from .models import *
from .parser import *

class DataMixin():
    def results(self, articles_json,keyword):
        
        if articles_json["totalResults"] > 20:
            num = 20
        else:
            num = int(articles_json["totalResults"])
        
        results = []

        for i in range(num):
            pubdate = articles_json["articles"][i]["publishedAt"]
            name = articles_json["articles"][i]["source"]["name"]
            title = articles_json["articles"][i]["title"]
            description = articles_json["articles"][i]["description"]
            link = articles_json["articles"][i]["url"]

            content = parsed(url=link)

            self.db_create(keyword=keyword,pubdate=pubdate,name=name,
                        title=title,description=description,
                        link=link,content=content)

            results.append({'title': f'{title}', 'description': f'{description}', 'link': f'{link}'})
        return results

    def db_create(self, keyword,pubdate,name,title,description,link,content):
        if Article.objects.filter(link=link):
            pass
        else:
            article = Article(
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