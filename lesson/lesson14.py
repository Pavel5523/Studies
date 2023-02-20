# Декораторы
# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am func "hello"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# # test = hello()
# # print(type(test))
# # print(test)
#
# test = hello
# print(type(test))
# print(test())

# def my_decorator(func):  # декорирующая функция
#     def func_wrapper():
#         print('Код до функции')
#         func()
#         print('Код после функции')
#
#     return func_wrapper
#
# @my_decorator  # Декоратор
# def func_test():  # Декорирующая функция
#     print('Тело функции "func_test"')
#
#
# # test = my_decorator(func_test)
# # test()
#
# func_test()

# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#
#     return wrap
#
#
# # print(hello())
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return 'text'
#
#
# print(hello())

# def cnt(fn):
#     s = 0
#
#     def wrap():
#         nonlocal s
#         s += 1
#         fn()
#         print('Вызов функции:', s)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print()
#         fn()
#
#     return wrap
#
#
# @args_decorator
# def print_pull_name(name, surname):
#     print('Меня зовут:', name, surname)
#
#
# print_pull_name('Ирина', 'Леонова')


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print('args', args)
#         print('kwargs', kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_pull_name(a, b, c, study='Python'):
#     print(a, b, c, 'изучают', study, '\n')
#
#
# print_pull_name('Ирина', 'Борис', 'Светлана', study='JavaScript')
# print_pull_name('Владимир', 'Екатерина', 'Виктор')

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=' ')
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor('Сумма', '+')
# def summa(a, b):
#     print(a + b)
#
#
# @decor('Разность', '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# print(int('19'))
# print(int('19.5'))  # ValueError

# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 16))
# print(int('100', 10))

# print(bin(18))  #  Двоичая система
# print(oct(18))  #  Восьмиричная система
# print(hex(18))  #  Шестнадцатиричная система
#
# print(0b10010)
# print(0o22)
# print(0x12)

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
# print('Py' in e)

# s = 'Hello'
# print(s[1])
# print(s[-5])
# print(s[1:4])
# print(s[::-1])

# s = 'python'
# print(s[3])
# #s[3] = 't'
#
# s = s[:3] + 't' + s[4:]
# print(s)

# def change_to_str(s, c_old, c_new):
#     s2 = ''
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования.'
# str2 = change_to_str(str1, 'N', 'P')
# print('str1', str1)
# print('str2', str2)

# print('Привет')
# print(u'Привет')

# print('C:\folder\file.txt')
# print('C:\\folder\\file.txt')
# print(r'C:\folder\file.txt')
# print(r'C:\folder\file.txt\\'[:-1])
# print(r'C:\folder\file.txt' + '\\')
# print('C:\\folder\\file.txt\\')

# name = 'Дмитрий'
# age = 25
# print('Меня зовут', name, '. Мне', age, 'лет')
# print('Меня зовут' + name + '. Мне' + str(age) + 'лет')
# print(f'Меня зовут {name}.Мне {age} лет')

# from math import pi
# print(f'Число PI: {round(pi, 2)}')
# print(f'Число PI: {pi:.2f}')

# x = 10
# y = 5
# print(f'{x=}, {y=}')
# print(f'{x} x {y} / 2 = {x * y / 2}')

# a = 74
# print(f'{{{a}}}')

# dir_name = 'my_doc'
# file_name = 'data_txt'
# print(fr'home\{dir_name}\{file_name}')

# s = "Много " \
#     "строк"
# s1 = ''
# s3 = """Много
#     строк"""
# s4 = ''''''
# print(s3)
# print(s)

# def square(n):
#     '''Принимает число n, возвращает квадрат числа n'''
#     return n ** 2
#
#
# print(square(5))
# # print(sum.__doc__)

from math import pi


def cylinder(r, h):
    '''
    Вычисляет площадь цилиндра.

    Вычисляет площадь цилиндра. На основание заданной высоты и радиуса основания

    :param r: положительное число, радиус основания цилиндра
    :param h: положительное число, высота цилиндра
    :return: положительное число, площадь цилиндра
    '''
    return 2 * pi * r * (r + h)


print(cylinder(2, 4))
print(cylinder.__doc__)
