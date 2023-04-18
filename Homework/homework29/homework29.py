import json


class Countries:
    @staticmethod
    def add_data(data_dict):
        try:
            data = json.load(open('data.json'))
        except FileNotFoundError:
            data = []
        data.append(data_dict)
        # data = {'name': self.name, 'marks': self.marks}
        with open('data.json', 'w') as f:
            json.dump(data, f)


while True:
    n = int(input('Введите режим '))
    if n == 6:
        break
    if n == 1:
        country = input('Введите название страны ')
        city = input('Введите название столицы ')
        countries = {
            'Страна': country,
            'Столица': city
        }
        Countries.add_data(countries)
