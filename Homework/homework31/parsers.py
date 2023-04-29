import requests
from bs4 import BeautifulSoup
import csv


class Parser:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        laptop = self.html.find_all('tr', class_='search-result-row highlight')
        for i in laptop:
            title = i.find('a', class_='t').text
            prise = i.find('td', class_='d tac cell-price').text.strip()
            prise = ''.join(prise.split())
            presense = i.find('td', class_='tac region_order_button_mini').text
            self.res.append({
                'Цена': prise,
                'Наличие': presense,
                'Название': title,
            })
        print(self.res)

    def save(self):
        with open(self.path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('Цена', 'Наличие', 'Название'))
            for i in self.res:
                writer.writerow((i['Цена'], i['Наличие'], i['Название']))

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
