import json


class Countries:
    data = []
    @staticmethod
    def add_data(c):
        # try:
        #     data = json.load(open('file_data.json'))
        # except FileNotFoundError:
        #     data = []
        # data.append(c)
        # # data = {'Страна': a, 'Столица': b}
        # with open('file_data.json', 'a') as f:
        #     json.dump(c, f, indent=2)


        # Countries.data = json.load(open('file_data.json'))
        Countries.data = []
        Countries.data.append(c)
        with open('file_data.json', 'a') as f:
            json.dump(c, f, indent=2)
while True:
    n = int(input('Введите режим '))
    if n == 6:
        break
    a = input('Введите название страны ')
    b = input('Введите название столицы ')
    d = {
        'Страна': a,
        'Столица': b
    }
    Countries.add_data(d)
# import json
# class Countries:
#     data = []
#     @staticmethod
#     def add_data(c):
#     new_data =

