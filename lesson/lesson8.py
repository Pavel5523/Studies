# import math
# num1 = math.sqrt(4)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.2)
# num4 = math.pi
# print(num3)
# print(num2)
# print(num1)
# print(num4)
#
# print(dir(math))

# from math import sqrt
#
# num1 = sqrt(4)
# print(num1)
# from math import pi
#
# r = 9
# s = round(2 * pi * r, 2)
# print(s)

# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "")


# # print(dir(time))
#
# s = time.time()
# print(s)
#
# local = time.ctime()
# print(local)
# b = 8574985784
# res = time.localtime()
# print(res)
# print(res.tm_mday, '.0',res.tm_mon, '.', res.tm_year, sep='')
#
# print(time.strftime('Сегодня %d (%A).%m.%Y', time.localtime(b)))

# pause = 5
# print('Программа запущенна')
# time.sleep(pause)
# print('Программа завершена')

# text = input('Название напоминания: ')
# t = float(input('Через сколько минут: '))
# t = t * 60
# time.sleep(t)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res)
#
# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)


# def hello(name):
#     print('Hellow', name)
#
#
# hello('Pavel')
# hello('Oksana')

# def get_sum(a, b):
#     print('Сумма: ')
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# # get_sum('2', '5')
# print(res)

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#     print()
#
#
# symbol(9, '+', '-')
# symbol(7, 'X', 'O')

# x = int(input('->'))
# y = int(input('->'))
#
#
# def res(a, b):
#     if a > b:
#         print(a - b)
#     else:
#         print(a + b)
#
#
# res(x, y)

# def cub(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, 'в кубе =', cub(i))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     a = lst.pop()
#     b = lst.pop(0)
#     lst.append(b)
#     lst.insert(0, a)
#     return lst
#
#
# print((change([1, 2, 3])))
# print((change([9, 12, 33, 54])))
# print((change(['a', 'b', 'c', 'd'])))

# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
# # print(func(10, 5))
# print(func(10, 15))
# a = 10
# b = 5
# if func(a, b):
#     print('>')
# else:
#     print('<')

# def check_password(password):
#     print(password)
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if 'A' <= ch <='Z':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
# p = input('Введите пароль: ')
# if check_password((p)):
#     print('Надежный пароль:')
# else:
#     print('Не надежный пароль:')

# def get_sum(a=0, b=0, c=0, d=0):
#     return a + b + c + d
#
#
# print(get_sum(1, 2, 3, 4, ))
# print(get_sum(1, 2, 3))
# print(get_sum(1, 2,))
# print(get_sum(1, 2, d=2))
# print(get_sum())

# def display_info(name, age):
#     print('Name', name, )
