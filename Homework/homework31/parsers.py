import requests
from bs4 import BeautifulSoup


class Parser:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req,'lxml')

    def parsing(self):
        kit = self.html.find('a', class_='name')
        for i in kit:
            print(i)

    def run(self):
        self.get_html()
        self.parsing()

# res = requests.get('https://www.danomsk.ru/shop/769-instrument/774-nabory/').text
# print(res)