import json


class Countries:
    @staticmethod
    def add_data(b):
        try:
            data = json.load(open('file_data.json'))
        except FileNotFoundError:
            data = []
        data.append(b)
        with open('file_data.json', 'a') as f:
            json.dump(b, f, indent=2)


while True:
    n = int(input('Введите режим'))
    if n == 6:
        break
    a = input('Введите название страны')
    b = input('Введите название столицы')
    d = {
        'Страна': a,
        'Столица': b
    }
Countries.add_data(d)
