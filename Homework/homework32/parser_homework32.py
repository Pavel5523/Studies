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
        elements = self.html.find_all('table', class_='table-t tb-tovr')
        # print(elements)
        k = 0
        for i in elements:
            if k == 1:
                break
            print(i.text)
            k += 1
            # description = i.find('td').text
            # print(title)
            # print(description)
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
                writer.writerow((i['Цена'], i['Наличие'], i['Название']))

    def run(self):
        self.get_html()
        self.parsing()
        # self.save()

#
# res = requests.get('https://radec-m.ru/radiodetali/13772/')
# print(res)
