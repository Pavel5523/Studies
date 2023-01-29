# import random
# print(random.random())
# print(random.randint(0, 5))
# print(random.randrange(0, 5, 2))
# print(random.randrange(0, 5, 2))

# import random as r
# print(r.random())

# from random import randint, randrange as rr
#
# print(randint(0, 5))
# print(rr(6, 15, 2))

from random import *

# print(randint(0, 5))
# print(randrange(2, 16, 2))
# print(round(uniform(10.5, 25.5), 2))

# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи']
# print(choice(city_list))
# print(choices(city_list, k=3))
#
# s = [55, 66, 45, 6, 7, 67, 65, 88]
# print(choice(s))
# print(choices(s, k=3))
# print(s)
# shuffle(s)
# print(s)

# mas = [randint(0, 20) for i in range(5)]
# print(mas)

#  Функции агрегирования
# lst = [7, 12, 20, 18, 9]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# max_1 = max(mas)
# print(max_1)
# mas.remove(max_1)
# mas.insert(0, max_1)
# print(mas)
#
# mas = [randint(-20, 20) for i in range(10)]
# mas_1 = []
# print(mas)
# mas.sort(reverse=True)
# print(mas)

# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# m = min(mas)
# print(m)
# ind = mas.index(m)
# # del mas[:ind]
# # print(mas)
# print(mas[ind:])

# lst = []
# if len(lst) == 0:
#     print('Пусто')
#
# if not lst:
#     print('Дважды пусто')

# first_list = [randint(0, 10) for i in range(int(input('Кол-во элементов')))]
# last_list = [randint(0, 10) for i in range(int(input('Кол-во элементов')))]
# print(first_list)
# print(last_list)
# second_list = first_list + last_list
# print(second_list)
# second_list = []
# for i in range(len(first_list)):
#     if first_list[i] not in second_list:
#         second_list.append(first_list[i])
# for i in range(len(last_list)):
#     if last_list[i] not in second_list:
#         second_list.append(last_list[i])
# print(second_list)

# second_list = []
# for i in range(len(first_list)):
#     if first_list[i] in last_list and first_list[i] not in second_list:
#         second_list.append(first_list[i])
# print(second_list)
# second_list = [min(first_list), min(last_list), max(first_list), max(last_list)]

# p = int(input('Размер списка'))
# s = []
# # mas = [randint(0, 10) for i in range(p)]
# # print(mas)
#
# while len(s) < p:
#     w = randint(0, p - 1)
#     if w not in s:
#         s.append(w)
# print(s)

# n = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 0, 1, 2],
# ]
# print(n)
# print(n[1][2])
#
# a = [2, 'Hellow', 5]
# print(a[1][1])

# for row in range(len(n)):
#     # print(n[row])
#     for col in range(len(n[row])):
#         print(n[row][col], end='\t\t')
#     print()
# print()
# for row in n:
#     #print(row)
#     for x in row:
#         print(x, end='\t\t')
#     print()
# print()
# for row in n:
#     #print(row)
#     for x in row:
#         print(x**2, end='\t\t')
#     print()

# matrix = [[0 for x in range(5)]for y in range(3)]
# matrix = []
# for y in range(3):
#     new_row = []  # [[0,0,0,0,0,], []]
#     for x in range(5):
#         new_row.append(0)
#     matrix.append(new_row)
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     # print('x=', x, 'y=', y)
#     print(x, '+', y, '=', x + y)

# matrix = [[randint(1, 30) for x in range(5)] for y in range(3)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# matrix = [[randint(-20, 10) for x in range(4)] for y in range(3)]
# print(matrix)
# s = 0
# for i in matrix:
#     for j in i:
#         if j < 0:
#             s += 1
# print(s)

n = int(input('Введите размер списка: '))
m = [[randint(0, 100) for x in range(n)] for y in range(n)]
for row in m:
    for x in row:
        print(x, end='\t')
    print()
t = m[0][0]
for k in range(n):
    if t > m[k][k]:
        t = m[k][k]
print(t)

# github.com