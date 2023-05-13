import requests


def get_articles_headlines(keyword,country,category):
    api_key = "API_KEY"

    url = "https://newsapi.org/v2/top-headlines?apikey={}".format(api_key)

    params = {
        "q": "{}".format(keyword),
        "country" : "{}".format(country),
        "category": "{}".format(category),
    }

    request = requests.get(url, params=params)

    req_json = request.json()

    print(request.url)

    return req_json

def get_articles_everything(keyword,language):
    api_key = "API_KEY"

    url = "https://newsapi.org/v2/everything?apikey={}".format(api_key)

    params = {
        "q": "{}".format(keyword),
        "language" : "{}".format(language),
    }

    request = requests.get(url, params=params)

    req_json = request.json()

    print(request.url)

    return req_json


if __name__ == "__main__":
    get_articles_everything(keyword = "biden",country = "us")