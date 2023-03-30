from bs4 import BeautifulSoup
import requests
import lxml


def parser(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    article = soup.find_all('p')
    return article

def parsed(url):
    article_list = []
    for q in parser(url):
        article_list.append(q.text)
    return article_list
