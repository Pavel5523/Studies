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
        kit = self.html.find_all('tr', class_='search-result-row highlight')
        for i in kit:
            title = i.find('a', class_='t').text
            prise = i.find('td', class_='d tac cell-price').text.strip()
            prise = ''.join(prise.split())
            presense = i.find('td', class_='tac region_order_button_mini').text
            self.res.append({
                'Название': title,
                'Цена': prise,
                'Наличие': presense,
            })
        print(len(self.res))

    def save(self):
        with open(self.path, 'w') as f:

            for i in self.res:
                # print(i)
                writer = csv.writer(f)
                writer.writerow((f[i]))
#
#     def run(self):
#         self.get_html()
#         self.parsing()
#
# # res = requests.get('https://www.danomsk.ru/shop/769-instrument/774-nabory/').text
# # print(res)
