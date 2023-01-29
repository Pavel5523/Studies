# Функции явного преобразования типов
# int()
# str()
# float()
# bool()


# num1 = '2'
# num2 = 3
# res = int(num1) + num2
# print(res)
# a = 3.891
# a = round(a, 2)
# print(a)
# print(type(a))

# name = 'Виктор'
# age = 26
# print('Меня зовут', name, '.Мне', age, 'лет.', sep='--', end=' ')
# # print()
# print('Я учу Python')

# name = input('Введите имя: ')
# print('Вас зовут', name)

# num = int(input('Введите число: '))
# power = int(input('Введите степень: '))
#
# res = num ** power
# print('Число', num, 'в степени', power, 'равно', res)

# a = int(input('Введитек первое число:'))
# b = int(input('Введите второе число:'))
# c = int(input('Введите третье число:'))
# d = int(input('Введите четвертое число:'))
# print(round((a + b) / (c + d), 2))

# b1 = True
# b2 = False
# print(b1 + 5)  # True (1) + 5 = 6
# print(int(b1))
# print(b2 + 5)  # False (0) + 5 = 5
# print(int(b2))

# print(bool('Python'))
# print(bool(''))
# print(bool('9'))
# print(bool('0'))
# print(bool(False))
# print(bool(None))

# cnt = 5
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input('Введите свой возраст: '))
# if age >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')

# a = 15
# b = 5
# if a > b:
#     print('a > b')
# else:
#     print('b > a')

# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# if a == b == c:
#     print('Равносторонний')
# elif (a == b) or (b == c) or (a == c):
#     print('Равнобедренный')
# else:
#     print('Разносторонний')

# day = int(input('Введите день недели (цифрой): '))
# if 1 <= day <= 5:   #(day >= 1) and (day <= 5):
#     print('Рабочий день', end=' ')
#     if day == 1:
#         print('Понедельник')
#     if day == 2:
#         print('Вторник')
#     if day == 3:
#         print('Среда')
#     if day == 4:
#         print('Четверг')
#     if day == 5:
#         print('Пятница')
# elif day == 6 or day == 7:
#     print('Выходной', end=' ')
#     if day == 6:
#         print('Суббота')
#     if day == 7:
#         print('Воскресенье')
# else:
#     print('Такого дня недели не существует')

# a = int(input('Введите номер месяца: '))
# if 0 < a <= 2 or a == 12:
#     print('Зима')
# elif 2 < a <= 5:
#     print('Весна')
# elif 5 < a <= 8:
#     print('Лето')
# elif 5 < a <= 11:
#     print('Осень')
# else:
#     print('Такого времени года не существует')


