# i = 1
# while i < 5:
#     print('Внешний цикл: i =', i)
#     j = 1
#     while j < 4:
#         print('\tВнутренний цикл: j =', j)
#         j +=1
#     i +=1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, '=', i * j, end='\t\t')
#         j += 1
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end='')
#         else:
#             print('-', end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     print(' ' * i, '*')
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(end=' ')
#         j += 1
#     print('*')
#     i += 1

#                   for

# for element in collection:
#   тело цикла


# for i in 'Hellow':
#     print(i)

# for color in 'red', 'orange', 'yellow', 'green':
#     print(color)

# range(start, stop, step)

# print(range(9))
#
# for i in range(2, 9, 1):
#     print(i, end=' ')
#
# i = 0
# while i < 9:
#     print(i)
#     i += 1

# n = int(input('Введите целое число '))
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)

# for i in range(11, 101, 11):
#     print(i)

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done!')

# a = int(input('Введите ширину прямоугольника'))
# b = int(input('Введите высоту прямоугольника'))
# symbol = input('Введите символ')
# for i in range(b):
#     for i in range(a):
#         print(symbol, end='')
#     print()

# a = 16
# b = 4
# symbol = '*'
# for i in range(b):
#         for j in range(a):
#             if i == 0 or i == b - 1 or j == 0 or j == a - 1:
#                 print(symbol, end='')
#             else:
#                 print(end=' ')
# print()

# w = [letter for letter in 'Hellow']
# print(w)
#
# for letter in 'Hellow':
#     print(letter)
#
# num = [i for i in range(30)]
# print(num)

# Списки

# nums = [2, 54, 6, [5, 3, 7], 'v', 3, 5, True]
# print(nums)
# print(type(nums))

# nums = [3, 5, 6, 4, 0, 6]
# print(nums)
# print(nums[1])
# print(nums[4])
# # print(nums[6])
# print(nums[-1])
# nums[2] = 256
# print(nums[2])
# print(nums)
# print(len(nums))

# s = [5] * 6
# print(s)
# print(type(s))
#
# b = list('Hellow')
# print(b)
#
# c = s + b
# print(c)

# n = range(10)
# print(n)

# n = list(range(2, 10, 2))
# print(n)
# n2 = [2, 4, 6, 8]
# print(n2)
# if n == n2:
#     print(1)
# else:
#     print(0)

# a = [i**2 for i in range(5)]
# print(a)

# c = [i * 3 for i  in 'list']
# print(c)

# a = [0] * int(input('Введите количество элементов списка: '))
# print(a)
# for i in range(len(a)):
#     a[i] = input('Введине некое значение: ')
# print(a)

# a = [input('-> ')for i in range(int(input('n = ')))]
# print(a)

a = [2, 3, 4, 7, 8, ]
for i in range(len(a)):
    print(i, end=' : ')
    print(a[i])

for i in a:
    print(i)
