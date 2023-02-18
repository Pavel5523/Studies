# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(10))
#
# add2 = outer(6)
# print(add2(11))
#
# print(outer(5)(10))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + '_new'
#         return a, b, c
#
#     return func2
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def incr():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return incr
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res2()
# res1()
# res1()

# students = {
#     'Alise': 98,
#     'Bob': 67,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = make(80, 101)
# B = make(70, 80)
# C = make(50, 70)
# D = make(0, 50)
#
# print('A =', A(students))
# print('B =', B(students))
# print('C =', C(students))
# print('D =', D(students))


#  Анонимные функции (lambda)
# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func('a', 'b'))

# print((lambda x=2, y=5: x + y)())

# print((lambda x=2, y=5: x**2 + y**2)())

# print((lambda *args: args)(1, 2, 3, 4, 5, 6, 7))

# c = (lambda x: x * 2, lambda x: x * 3, lambda x: x * 4)
#
# for t in c:
#     print(t('abc_'))


# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(10))
#
#
# def outer1(n):
#     return lambda x: n + x
#
#
# add2 = outer1(5)
# print(add2(10))
#
# outer2 = lambda n: lambda x: x + n
# add3 = outer2(5)
# print(add3(10))
#
# print((lambda n: lambda x: x + n)(5)(10))

# print((lambda n: lambda x: lambda c: n + x + c)(5)(10)(12))

# def func(i):
#     return i[i]
#
#
# d = {'d': 10, 'b': 15, 'c': 4}
# # print(sorted(d))
# list_d = list(d.items())
# print(list_d)
#
# # list_d.sort(key=lambda i: i[1])
#
#
# list_d.sort(key=func)
# print(list_d)
# print(dict(list_d))

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# # 12, 3
# print(a[0](12, 3))

# a = {'one': lambda x: x - 1, 'two': lambda x: x * (-1), 'three': lambda x: x ** 5}
# b = [-3, 10, 0, 4]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда')
# }
#
#
# d[2]()

# print((lambda a, b: a if a > b else b)(5, 3))
# print((lambda a, b, c: min(a, b, c))(2, 1, 4))

# map(func, iterables), filter(func, iterables) - циклы

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# a = list(map(mult, lst))
# print(a)
#
# a1 = list(map(lambda t: t * 2, lst))
# print(a)

# t = (2.88, -1.75, 100.55)
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)
#
# t3 = tuple(map(int, t))
# print(t3)

# areas = [3.2332443, 4.4565665, 7.45435435, 1.354235, 8.234546345, 9.123514134, 0.345134543]
# print(list(map(round, areas, [2, 2, 2])))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5, 6]
# print(list(map(lambda x, y: (x, y), st, num)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))


# t = ('adob', 'abc', 'dfsdf', 'sdghg', 'as')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
# import random
#
# b = [random.randint(0, 50) for i in range(10)]
# print(b)
# b2 = list(filter(lambda s: 10 < s < 21, b))
# print(b2)

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10)))))
