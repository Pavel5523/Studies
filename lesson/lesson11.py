# d = dict()
# d[1] = input('-> ')
# d[2] = input('-> ')
# d[3] = input('-> ')
# d[4] = input('-> ')
# print(d)

# d = {i:input('-> ')for i in range(1, 5)}
# print(d)
# dislike = int(input('Какой ключ исключить: '))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['Core FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3430', 5, 6400],
# }
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб', sep='')
# while True:
#     n = input('№: ')
#     if n != '0':
#         qty = int(input('Количество: '))
#         goods[n][1] += qty
#     else:
#         break
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб', sep='')

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d.copy()
# print('D =', d)
# print('D2 =', d2)
# d['b'] = 5
# d2['e'] = 7
# print('D2 =', d2)
# print('D =', d)


# d = {'a': 1, 'b': 2, 'c': 3}
# # print(d['b'])
# # value = d.get('b1', 'Такого ключа нет')
# # print(value)
# # print(d.keys())  # Ключи
# # print(d.values())  # Значения
# # print(d.items())  # Ключи + Значения
# #
# # for k, v in d.items():
# #     print(k, v)
# #
# # print(list(d.items()))
# print(d)
# # item = d.pop('b1', 'Нет такого ключа')
# # # item = d.popitem()
# # print(item)
# # d.clear()
# # item = d.setdefault('e', 100)  # устанавливает значение по умолчанию
# # print(item)
# d.update([('r', 7), ('c', 6)])  # или ({'r':7, 'c': 6})
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = {}
# # z.update(x)
# # z.update(y)
# z = x | y
# print(z)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# print(d)
# print(new_d)
# d['location'] = d.pop('city')
# print(d)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ':', a[x][y], sep='')

# sales = {
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4882, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
# }
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ':', sales[x][y], sep='')
# person = input('Имя: ')
# region = input('Регион: ')
# print(sales[person][region])
# new_data = int(input('Новое значение: '))
# sales[person][region] = new_data
# print(sales[person])

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print({key: value for key, value in d.items() if value <= 2})

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# zip()
# a = [12, 1, 2]
# b = ['Dec', 'Jan', 'Feb', 3]
# c = [4.0, 8.5, 4.9]
# # d = dict(zip(a, b))
# # f = {k: y for k, y in zip(a, b)}
# # print(d)
# # print(f)
# f = zip(a, b, c)
# print(list(f))

dict_one = {'name': 'Igor', 'email': 'igor@gmail.com', 'job': 'Consultant'}
dict_two = {'name': 'Irina', 'email': 'irina@gmail.com', 'job': 'Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)

