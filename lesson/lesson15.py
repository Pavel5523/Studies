# print(ord('a'))
# print(ord('#'))
# print(ord('м'))
#
# while True:
#     n = input('-> ')
#     if n != -1:
#         print(ord(n))
#     else:
#         break

# my_str = 'Test string for me'
# arr = [ord(i) for i in my_str]
# print('ASCII коды:', arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print(arr)
#
# arr += [ord(x) for x in input('-> ')[:3] if ord(x) not in arr]
# print(arr)
# print('Количество последних элементов: ', arr.count(arr[-1]) -1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(50))

# a = 122
# b = 97
# if a > b:
#     code = [chr(i) for i in range(b, a + 1)]
# else:
#     code = [chr(i) for i in range(a, b + 1)]
# # if b > a:
# #     a, b = b, a
# print(code)

# print('apple' == 'Apple')
# print(ord('a'))
# print(ord('A'))

# from random import randint
#
# short = 7
# long = 10
# min_ASCII = 33
# max_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(short, long)
#     res = ''
#     for i in range(rand_len):
#         rand_char = chr(randint(min_ASCII, max_ASCII))
#         res += rand_char
#     return res
#
#
# print('Случайный пароль:', random_password())

# Методы строк
# print(dir(list), '\n')
# print(dir(str))
#
# s = 'hello, WORLD! I am learning Python.'
# print(s.capitalize())  Hello, world! i am learning python.
# print(s.lower())  hello, world! i am learning python.
# print(s.upper())  HELLO, WORLD! I AM LEARNING PYTHON.
# # print(s.swapcase())  HELLO, world! i AM LEARNING pYTHON.

# print(s.lower().count('h'))

# print(s.find('Python', start, end))  # Первый индекс начала подстроки или -1 если элемента нет

# print(s.index('Python1', start, stop))  # Первый индекс начала подстроки или ошибку ValueError если элеменета нет

# print(s.rfind('h'))  # Тоже только поиск с правой стороны
# print(s.rindex('h')) # Тоже только поиск с правой стороны


# my_str = 'один два'
# # prob2 = my_str.rfind(' ')
# # prob1 = my_str.find(' ')
# one = my_str[:my_str.find(' ')]
# two = my_str[my_str.find(' '):]
# print(two + ' ' + one)

# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     if '1234567890'.find(i) != -1:
#         # digits += int(i)
#         digits.append(int(i))
# print(digits)

# my_str = input('->: ')
# symbol = input()
# if my_str.count(symbol) == 1:
#     print(my_str.find(symbol))
# elif my_str.count(symbol) >= 2:
#     print(my_str.find(symbol), my_str.rfind(symbol))
# else:
#     print('Символа нет')

# s = 'print(my_str.find(symbol), my_str.rfindsymbol'


# print(s.endswith(' ', start, end))   # Заканчивается ли строка определенным символом
# print(s.startswith(' ', start, end))   # Начинается ли строка определенным символом

# print('abc123'.isalnum())  # Состоит ли строка из букв и цифр
# print('abc123'.isalpha())  # Состоит ли строка только из букв
# print('abc123'.isdigit())  # Состоит ли строка только из цифр
# print('abc123'.islower())  # Состоит ли строка из символов нижнего регистра
# print('abc123'.isupper())  # Состоит ли строка из символов верхнего регистра

# print('py'.center(10))  # выравнивает строку по центру относительно заданного кол-ву символов
# print('py'.center(10, '-'))  # выравнивает строку по центру относительно заданного кол-ву символов

# print('   py'.lstrip())  # Удаляет пробельные символы с левой стороны
# print('py    '.rstrip())  # Удаляет пробельные символы с правой стороны
# print('   py    '.strip())  # Удаляет пробельные символы с любой стороны

# print('https://www.python.orgw'.lstrip('/:pthsw'))
# print('https://www.python.orgw'.rstrip('/:pthsw'))
# print('https://www.python.orgw'.strip('/:pthsw'))
# print('https://www.python.orgw'.ltrip('/:pths').rstrip('orgw'))


# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace('N', 'P', 2))

# s = 'Заменить в этой строке все появления буквы "о" на букву "О" кроме первого и последнего вхождения'
# a = s.find('о')
# b = s.rfind('о')
# print(a, b)
# # s = s.replace()
# r = s[13:89]
# print(r)
# r = r.replace('о', 'О')
# print(r)

# s = '-'
# seq = ['a', 'b', 'c']
# print(s.join(seq))
# print(seq)
# print('..'.join(['1', '2']))
# print(':'.join('Hello'))
# print('H:e:l:l:o'.split())
# print('www.python.org.ru'.split('.', 1))
# print('www.python.org.ru'.rsplit('.', 1))

# a = input('-> ').split()
# print(a)

# a = input('Введите ФИО: ').split()
# print(a)
# print(a[0], a[1][0], a[2][0])

