import requests


def get_articles(keyword,country):
    api_key = "f8e007f918624cd08d0980e563efa69d"

    url = "https://newsapi.org/v2/top-headlines?apikey={}".format(api_key)

    params = {
        "q": "{}".format(keyword),
        "country" : "{}".format(country),
    }

    request = requests.get(url, params=params)

    req_json = request.json()

    print(request.url)

    return req_json


def articles(keyword, req_json, i):
    pubdate = req_json["articles"][i]["publishedAt"]
    name = req_json["articles"][i]["source"]["name"]
    title = req_json["articles"][i]["title"]
    description = req_json["articles"][i]["description"]
    link = req_json["articles"][i]["url"]

    return keyword,pubdate,name,title,description,link

if __name__ == "__main__":
    get_articles(keyword = "biden",country = "us")