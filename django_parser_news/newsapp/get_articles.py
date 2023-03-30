import requests


def get_articles(keyword,country):
    api_key = "api_key"

    url = "https://newsapi.org/v2/top-headlines?apikey={}".format(api_key)

    params = {
        "q": "{}".format(keyword),
        "country" : "{}".format(country),
    }

    request = requests.get(url, params=params)

    req_json = request.json()

    print(request.url)

    return req_json


if __name__ == "__main__":
    get_articles(keyword = "biden",country = "us")