import re


# s = 'Я ищу совпадения в 2023 году. И я их найду в два счета'
# req = 'в'
# print(re.findall(req, s))  # Возвращает список, содержащий все совпадения с шаблоном
# print(re.search(req, s))  # Место расположения первого объекта
# print(re.search(req, s).span())  # Место расположения первого объекта
# # print(re.search(req, s).start())
# # print(re.search(req, s).end())
# # print(re.search(req, s).group())
# print(re.match(req, s))  # местоположение совпадение объекта в начале строки
# print(re.split(req, s, 2))  # Возвращает список в котором строка разбита по шаблону
# print(re.sub(req, 'В', s, 3))  # поиск и замена

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта. [-9863]. Hello'
# # req = '[12][0-9][0-9][0-9]'
# # req = r'\.'
# req = '[^А-я]'
# print(re.findall(req, s))
# print(ord('Ё'))
# print(ord('А'))
# print(ord('я'))
# print(ord('ё'))
# print(chr(96))

# s = 'Час в 24-формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09.'
# req = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(req, s))

# s = 'Я ищу совпадения^ в 2023 году. И я их найду в 2 счё_та. [-9863]. Hello. 200000'
# req = r'20+'
# print(re.findall(req, s))
#
# d = 'Цифры: 7, +17, +-42, 0012, 0.3'
# print(re.findall(r'[+-]?\d+[.\d]*', d))

# s = '06-03-1987 # Дата рождения'
# print('Дата рождения:', re.sub(r'#.*', '', s))
# print('Дата рождения:', re.sub(r'-', '.', s))
# print('Дата рождения:', re.sub(r'-', '.', '06-03-1987'))

# s = 'autor=Пушкин А.С; title = Евгений Онегин; price =200; year= 1831'
# # req = r'\w+\s*=\s*\w+[\s\w.]*'
# req = r'\w+\s*=[^;]+'
# print(re.findall(req, s))

# s = '12 сентября 2021 года 45645634563'
# req = r'\d{,4}'
# print(re.findall(req, s))

# s = '+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578 '
# req = r'\+?7\d{10}'
# print(re.findall(req, s))

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 сче_та.'
# # req = r'^\w+\s\w+'
# req = r'\w+\.$'
# print(re.findall(req, s))

# def validate_login(name):
#     return re.findall(r'^[A-Za-z_0-9-]{3,16}$', name)
#
#
# print(validate_login('Python_master'))
# print(validate_login('Pyt89$$$'))

# s = 'Я ищу совпадения в 2023 году. И я их найду в два счета'
# req = r'я'
# print(re.findall(req, s, re.I))

# text = '''
# one
# two'''
# # print(re.findall(r'one.\w+', text))
# # print(re.findall(r'one.\w+', text, re.S))
# print(re.findall('one$', text,))
# print(re.findall('one$', text, re.M))
# print(re.findall('two$', text))
# print(re.findall('^two', text))
# print(re.findall('^two', text, re.M))

# print(re.findall('''
# [a-z.-]+  # part1
# @         # @
# [a-z.-]+  # part2
#  ''', 'test@mail.ru', re.X))

# text = '''Python,
# python,
# PYTHON'''
# req = '(?im)^python'
# print(re.findall(req, text))
