import csv
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
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        elements = self.html.find_all('div', class_='product-card__body')
        # print(elements)
        for i in elements:
            name = i.find('div', class_='product-card__model').text
            prise = i.find('div', class_='product-card__price-new').text
            nal = i.find('div', class_='product-card__instock').text.strip()
            print(nal)
            # print(name)
            # print(prise)
            # self.res.append({
            #     'Цена': prise,
            #     'Наличие': presense,
            #     'Название': title,
            # })
        # print(self.res)

    def save(self):
        with open(self.path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('Цена', 'Наличие', 'Название'))
            for i in self.res:
                print((i['Цена'], i['Наличие'], i['Название']))

    def run(self):
        self.get_html()
        self.parsing()
        # self.save()

#
# res = requests.get('https://omsk.velostrana.ru/velozapchasti/kolesa//')
# print(res)
