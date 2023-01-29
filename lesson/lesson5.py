# n = [int(input('->')) for i in range(int(input('n = ')))]
# print(n)
# s = 0
# # for i in range(len(n)):
# #     if n[i] < 0:
# #         s += a[i]
# for i in n:
#     if i < 0:
#         s += i
#
# print(s)
# sum1 = 0
# sum2 = 0
# n = list(range(21, 41))
# print(n)
# for i in n:
#     if i % 2 == 0:
#         sum1 += 1
#     if i % 2 != 0:
#         sum2 += i
# print('Количество четных элементов', sum1)
# print('Сумма нечетных элементов', sum2)
# sum1 = 0
# s = 0
# n = [int(input('->')) for i in range(int(input('n = ')))]
# print(n)
# for i in range(len(n)):
#     if n[i] != 0:
#         sum1 += 1
#         s += a[i]
# print(s / sum1)

# n = [6, 5, 4, 3, 1,]
# print(n)
# n[0], n[-1] = n[-1], n[0]
# print(n)

#   Срезы списка
# список[start:stop:step]

# n = [2, 4, 5, 6, 2, 8, 9]
# print(n[1:4])
# print(n[2:])
# print(n[:2])
# print(n[0:-1:2])
# print(n[::-1])

# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[6:])
# print(s[-1:])
# print(s[3:4])
# print(s[-3:])
# print(s[2:5])
# print(s[-3:1:-1])

# a = 'Hellow'
# print(a[1:3])
# print(list(a))

# n = [2, 4, 5, 6, 2, 8, 9]
# print(n[:])
# n[1:3] = [1, 1, 1, 1,]
# print(n)
#
# del n[2]
# print(n)
# del n[2:5]
# print(n)

# n = [2, 4, 5, 6, 2, 8, 9]
# print(n)
# n[7] = 99
# print(n)

# Методы списка

# n = [2, 4, 5, 6, 2, 8, 9]
# print(n)
# n.append(99)    # Добавляет элемент в конец списка
# print(n)
# n.extend([5, 6, 7]) # Добавляет несколько элементов в конец списка
# print(n)
# n.extend('add')
# print(n)

# n = []
# # n.extend([i**2 for i in range(1, 11)])
# n.extend([i**2]) for i in range(1, 11)
# print(n)

# n = [2, 3, 4, 5, 6, 5, 4, 5, 6, 7]
# print(n)
# n.insert(2, 100)  # Добавляет элемент списка в определенное место
#                   # insert(куда добавить, что добавить)
# print(n)

# s = []
# n = int(input('Количество элементов списка: '))
# for num in range(n):
#     x = int(input('Введите число: '))
#     s.append(x)
# print(s)

# s = []
# n = int(input('Количество элементов списка: '))
# for num in range(n):
#     x = int(input('Введите число: '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print('Число не кратно трем')
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 44]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)

# a = [5, 4, 3, 2, 1, 2, 3, 4, 5, ]
# print(a)
# a.remove(1)    # Удаляет первый по найденному совпадению элемент из списка по значению
# print(a)
# last = a.pop()  # Удаляет последний элемент из списка (без параметров) и возвращает удаленный элемент
# print(a)
# print(last)
# second = a.pop(0)  # Удаляет элемент по индексу
# print(a)
# print(second)
# a.clear()   # Очищает список
# print(a)

# n = [int(input('Элементы списка')) for i in range(int(input('Количество элементов')))]
# print(n)
# k = int(input('Введите индекс: '))
# n.pop(k)
# print(n)

# a = [5, 2, 3, 4, 5, 6, 2, 4, 2, 5, ]
# num = a.count(2)  # Считает количество значений в списке
# print(num)
#
# ind = a.index(2, 4, -1)  # Возвращает положение первого индекса по заданному значению
# print(ind)
# b = 2
# if b in a:
#     ind = a.index(4, 4, -1)  # Возвращает положение первого индекса по заданному значению
#     print(ind)

# c = [1, 2, 3, ]
# d = c.copy()  # возвращает копию списка
# c.append(4)
# d.insert(0, 100)
# print('c =', c)
# print('d =', d)

# a = [1, 2, 3, 4, 5, 6, 7, 8,]
# print(a)
# # a.reverse() # Разворачивает список в обратном порядке
# # print(a)
# #
# # a.sort(reverse=False) # сортирует список по возрастанию
# # print(a)
# # a.sort(reverse=True) # сортирует список по убыванию
# # print(a)
# #
# # s = ['Павел','Сергей','Виталий','Анна']
# # print(s)
# # s.sort(key=len) #Сортировка по длинне
# # s.sort() # Сортировка по алфавиту
# # print(s)
#
# a.reverse()
# print(a)
# b = sorted(a)
# print(b)

