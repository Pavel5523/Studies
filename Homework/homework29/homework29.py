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
    def redaction_data(data_redaction, new_city):
        data = json.load(open('data.json'))
        if data_redaction in data.keys():
        # data[data_redaction] = new_city
        # with open('data.json', 'w') as f:
        #     json.dump(data, f)
        # except KeyError:
        #     print('Нет такой страны в списке')
        # print(data.keys())
    @staticmethod
    def show_data():
        print(json.load(open('data.json')))


while True:
    n = int(input('Введите режим '))
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
        new_city = input('Введите название новой столицы ')
        Countries.redaction_data(data_redaction.capitalize(), new_city.capitalize())
    if n == 5:
        Countries.show_data()
