import re

# text = '<body>Пример жадного соответствия регулярных выражений</body>'
# print(re.findall('<.*?>', text))
# s = '<p>Изображение <img src="bg.jpg"> - фон страницы</p>'
# # req = r'<img.*?>'
# req = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(req, s))

# # s = 'Петр, Ольга и Виталий отлично учаться!'
# s = 'int = 4, float = 4.0, double = 8.0f'
# # req = 'Петр|Ольга|Виталий'
# # req = r'\w+\s*=\s*\d[.\w]*'
# req = r'(?:int|double)\s*=\s*(?:\d[.\w]*)'  # () - сохраняющие скобки
# #  (?:) - не сохраняющие круглые скобки
# print(re.findall(req, s))
# print(re.search(req, s))

# s = 'Word2016, PS6, AI5'
# req = r'([a-z]+)(\d*)'
# print(re.findall(req, s, re.I))
# print(re.search(req, s, re.I))

# s = '5 + 7*2 - 4'
# req = r'\s*([+*-])\s*'
# print(re.split(req, s))

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счета.'
# req = r'(\d+)\s(\D+)'
# print(re.findall(req, s))
# print(re.search(req, s).group())
# m = re.search(req, s)
# print(m[1])
# print(m[2])
# print(m[0])

# text = '''
# Самара
# Москва
# Тверь
# Уфа
# Казань
# '''
# count = 0
#
#
# def repl_count(m):
#     global count
#     count += 1
#     return f'<option value="{count}">{m.group(1)}</option>\n'
#
#
# print('<select name="city">')
# print(re.sub(r'\s*(\w+)\s', repl_count, text))
# print('<\select>')

# s = 'Самолет прилетает 10/23/2021. Будем рады вас видеть после 10/24/2021'
# req = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(req, r'\2.\1.\3', s))  # 23.10.2021

# s = 'yandex.ru and yandex.com'
# req = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(req, r'http://\1', s))


#  Рекурсия

# def elevator(n):
#     if n == 0:  # базовый случай
#         print('Вы в подвале')
#         return
#     print('=>', n)
#     elevator(n - 1)
#     print(n, end=' ')
#
#
# n1 = int(input('На каком вы этаже: '))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):  # (356, 10)
#     convert = '012345679ABCDEF'
#     if n < base:
#         return convert[n]  # convert[3] = 3
#     else:
#         return to_str(n // base, base) + convert[n % base]  # 6 5
#
#
# print(to_str(254, 16))

names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]


# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
#
# print(names[1][1])
# print(isinstance(names[1][1], list))

# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))
