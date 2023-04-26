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
        kit = self.html.find_all('tr', class_='search-result-row highlight')
        for i in kit:
            title = i.find('a', class_='t').text
            prise = i.find('td', class_='d tac cell-price').text
            presense = i.find('td', class_='tac region_order_button_mini').text
            # print(f'Название: {title} Наличие: {presense} Цена: {prise.strip()}')
            self.res.append({
                'Цена': prise,
                'Наличие': presense,
                'Название': title,
            })
            print(self.res)
#
#     def run(self):
#         self.get_html()
#         self.parsing()
#
# # res = requests.get('https://www.danomsk.ru/shop/769-instrument/774-nabory/').text
# # print(res)
