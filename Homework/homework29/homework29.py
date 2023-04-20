import json


class Countries:
    @staticmethod
    def add_data(data_dict):
        try:
            data = json.load(open('data.json'))
        except FileNotFoundError:
            data = {}
        data.update(data_dict)
        with open('data.json', 'w') as f:
            json.dump(data, f)
        print('Файл сохранен')

    @staticmethod
    def del_data(data_del):
        data = json.load(open('data.json'))
        try:
            data.pop(data_del)
            with open('data.json', 'w') as f:
                json.dump(data, f)
            print('файл удален')
        except KeyError:
            print('Нет такой страны в списке')

    @staticmethod
    def search_data(data_search):
        data = json.load(open('data.json'))
        if data.get(data_search):
            print(data.get(data_search))
        else:
            print('Нет такой страны в списке')

    @staticmethod
    def redaction_data(data_redaction):
        data = json.load(open('data.json'))
        if data_redaction in data.keys():
            new_city = input('Введите название новой столицы ')
            data[data_redaction] = new_city.capitalize()
            with open('data.json', 'w') as f:
                json.dump(data, f)
            print('файл изменен')
        else:
            print('Нет такой страны в списке')

    @staticmethod
    def show_data():
        data = (json.load(open('data.json')))
        for data_country, data_city in data.items():
            print(f'Страна: {data_country}, Столица: {data_city}')


while True:
    print('*' * 40)
    print('''Выбор действия:\n1 - добавление данных
2 - удаление данных
3 - поиск данных
4 - редактирование данных
5 - просмотр данных
6 - завершение работы''')
    n = (input('Введите режим '))
    if n.isdigit():
        n = int(n)
        if n == 6:
            break
        if n == 1:
            country = input('Введите название страны ')
            city = input('Введите название столицы ')
            countries = {
                country.capitalize(): city.capitalize()
            }
            Countries.add_data(countries)
        if n == 2:
            data_del = input('Введите страну для удаления ')
            Countries.del_data(data_del.capitalize())
        if n == 3:
            data_search = input('Введите страну для поиска ')
            Countries.search_data(data_search.capitalize())
        if n == 4:
            data_redaction = input('Введите страну для редактирования ')
            Countries.redaction_data(data_redaction.capitalize())
        if n == 5:
            Countries.show_data()
    else:
        print('Вы ввели не число')
