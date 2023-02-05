# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hellow', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t     # распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
# user = get_user()
# # print(user)
# # print(user[0])
# # print(user[1])
# # print(user[2])
# first_name, year, married = get_user()
# print(first_name, year, married)

# t = (1, 2, 3)
# del t
# print(t)

# lst = [1, 2, 3, 4, 5]
# print(type(lst))
# print(lst)
# tpl = tuple(lst)
# print(type(tpl))
# print(tpl)
# lst = list(tpl)
# print(type(lst))
# print(lst)

# countries = (
#     ('Германия', 80.2, (('Берлин', 3.236), ('Гамбург', 1.718))),
#     ('Франция', 66, (('Париж', 2.2), ('Марсель', 1.6)))
# )
# print(countries)
# for country in countries:
#     country_name, country_population, cities = country
#     print('\nСтрана', country_name, '\nНаселение:', country_population)
#     for city in cities:
#         city_name, city_population = city
#         print('\tГород:', city_name, '(население:', city_population, ')', sep='')

# множество (set)
# s = {'banana', 'apple', 'orange'}
# print(s)
# print(type(s))

# a = set('hello')
# print(type(a))
# print(a)

# s = {x * x for x in range(10)}
# print(s)

# def to_set(a):
#     x = set(a)
#     n = len(x)
#     return x, n
# print(to_set('строка'))

# users = {'Tom', 'Alice', 'Bob'}
# users.add('Ann')
# print(users)
# user = 'Rob'
# if user in users:
#     users.remove(user)
# print(users)

# users.discard('Rob')
# print(users)

# users.pop()
# print(users)

# users.clear()
# print(users)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)  # аналог a | b
# a |= b
# c = a & b  # a &= b
# c = a - b  # a -= b
# c = a ^ b
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s2 | s3 | s4 | s5 | s5 | s6 | s7 | s1
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# a = set(input())
# b = set(input())
# c = a & b
# print(c)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a >= b)
#
# drafting = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
# s = drafting & music
# print(s)
#
# drafting = drafting - s
# print(s)

# frouzenset (замороженное множество)
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
#
# a = frozenset({'hello', 'world'})
# print(a)

# Словарь (dict)

# s = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3}
# print(s[1])
# print(d['two'])

# d = {'one': 1, 'two': 2}
# print(d)
# print(type(d))
# d1 = dict(one=1, two=2)
# print(d1)

# d = {'one': 1, 'two': 2, 'three': 3}
# print(list(d))
# lst = ['one', 'two', 'three']
# print(dict(lst))

# a = [
#     ('one', 1),
#     ('two', 2),
#     ('three', 3)
# ]
# print(dict(a))

# d = {'one': 45, 0: 'text', (1, 2.3): 'Кортеж', 43: [2, 3, 6, 7], 1: 'text', True: False}
# print(d[0][1])
from random import randint

# d = {i: i ** 2 for i in range(2, 7)}
# d = {i: input('-> ') for i in range(7)}
# d = {i: randint(1, 100) for i in range(1, 11)}
# d = {str(i) + '-й элемент': randint(1, 100) for i in range(1, 11)}
# d = {input('n='): input('->') for i in range(3)}
# print(d)
#
# d = {'one': 1, 'two': 2, 'three': 3}
# print(d)
# d['two'] = 200
# print(d)
# d['one'] += 100
# print(d)
#
# for key in d:
#     print(key, ':', d[key])
