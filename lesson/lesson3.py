# match выражение:
#     case шаблон_1:
#         действие_1
#     case шаблон_2:
#         действие_2:
#     case шаблон_n:
#     case шаблон_n:
#     case _:
#         действие по умолчанию

# password = 'admin'
#
# match password:
#     case 'user':
#         print('Пользователь')
#     case 'moderator':
#         print('Модератор')
#     case 'admin':
#         print('Администратор')
#     case _:
#         print('Пароль не верен')

# day = 'вторник'
# time = 17
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print('Рабочий день')
#     case 'суббота' | 'воскресенье':
#         print('Выходной день')
#     case _:
#         print('Такого дня недели не существует')

# a, b = 10, 20
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
# print('a == b' if a == b else 'a > b' if a > b else 'b > a')

# a = int(input('Введите первое число'))
# b = int(input('Введите второе число'))
# print('На ноль делить нельзя' if b == 0 else a / b)

# tru ... except

# try:
#     n = int(input('Введите целое число: '))
#     print(n * 2)
# except ValueError:
#     print('Что-то пошло не так')
# print('Код далее')


# try:
#     n = int(input('Введите делимое число: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except ValueError:
#     print('Что-то пошло не так')
# except ZeroDivisionError:
#     print('Что-то пошло не так')
# print('Код далее')

# try:
#     n = int(input('Введите делимое число: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print('Что-то пошло не так')
# else:                            # Отработает если не отработал except
#     print('Все нормально')
# finally:                         # Отработает в любом случае
#     print('Конец программы')
# print('Код далее')

# a = input('Введите первое значение: ')
# b = input('Введите второе занчение: ')
# try:
#     print(int(a) + int(b))
# except ValueError:
#     print(a + b)

                        # Циклы

# i = 2
# while i <= 20:
#     print('i =', i)
#     i += 2

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print('i =', i)
#     i += 1

# n = int(input('Укажите количество символов: ' ))
# i = 0
# while i < n:
#     print('*', end='')
#     i += 1

# n = int(input('Укажите количество символов: ' ))
# # i = 0
# while n > 0:
#     print('*', end='')
#     n -= 1

# a = int(input('Введите начало диапазона'))
# b = int(input('Введите конец диапазона'))
# res = 0
# while a < b:
#     print(a, end=' ')
#     if a % 2:
#         res += a
#     a += 1
# print('\n', res)

# n = input('Введите целое число: ')
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print('Число не целое')
#         n = input('Введите целое число: ')
#
# if n% 2 == 0:
#     print('Четное число')
# else:
#     print('Нечетное число')

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print('\nЦикл завершен')

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     a = 1
#     n = int(input('Введите положительное число: '))
#     if n == 0:
#         break
#     a *= n
# print(a)

i = 0
while i < 10:
    print(i)
    i += 1
else:
    print('Цикл закончен, i =', i)
















