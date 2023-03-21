import requests
import sqlite3


def get_sources(keyword,country):
    api_key = "YOUR_API_KEY"

    url = "https://newsapi.org/v2/top-headlines?apikey={}".format(api_key)

    params = {
        "q": "{}".format(keyword),
        "country" : "{}".format(country),
    #    "from": "{}".format(date),
    }

    request = requests.get(url, params=params)

    req_json = request.json()

    print(request.url)

    if req_json["totalResults"] > 5:
        num = 5
    else:
        num = int(req_json["totalResults"])

    for i in range(num):
        try:
            pubdate = req_json["articles"][i]["publishedAt"]
        except:pass
        try:
            name = req_json["articles"][i]["source"]["name"]
        except:pass
        try:
            title = req_json["articles"][i]["title"]
        except:pass
        try:
            description = req_json["articles"][i]["description"]
        except:pass
        try:
            link = req_json["articles"][i]["url"]
        except:pass
        db_add_values(keyword,pubdate,name,title,description,link)


def db_add_values(keyword,pubdate,name,title,description,link):
    db = sqlite3.connect('news.db')
    cursor = db.cursor()

    cursor.execute("""SELECT * FROM sources
      WHERE link=?
      """, (link,))
    
    check = cursor.fetchone()
    print(check)

    if check is None:
        print("ще нема, запишу")
        cursor.execute("""INSERT INTO sources
        (keyword, pubdate, name, title, description, link)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (keyword,pubdate,name,title,description,link))
        db.commit()
    else:
        print("вже є")

    db.close()

def create_table():
    db = sqlite3.connect('news.db')
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS sources (
        keyword TEXT,
        pubdate TEXT,
        name TEXT,
        title TEXT,
        description TEXT,
        link TEXT
    )""")

    db.commit
    db.close()

create_table()
#get_sources(keyword = "biden",country = "us")
