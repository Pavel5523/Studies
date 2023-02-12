# a = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
# d = list(a.items())
# print(d)
# n, m = zip(*d)
# print(n)
# print(m)
# c = list(zip(n, m))
# print(c)
# c.sort()
# print(c)
#
# c = list(zip(m, n))
# print(c)
# c.sort()
# print(c)
# print(dict(c))
# c = {v: k for k, v in c}
# print(c)

# month = ['January', 'February', 'March']
# total_sales = [52000.00, 51000.00, 48000]
# prod_cost = [46000.00, 45900.00, 43200.00]
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print('Чистая прибыль в', m, '=', profit)

# one = {'a': 1, 'b': 2}
# two = {'c': 3, 'd': 4}
# print({**one, **two})

# data = ['red', 'green', 'blue']
# ind = 1
# for i in data:
#     print(ind, i)
#     ind += 1
#
# for n, i in enumerate(data, 1):
#     print(n, i)

# dict_one = {'name': 'Igor', 'email': 'igor@gmail.com', 'job': 'Consultant'}
# for i, (j, v) in enumerate(dict_one.items(), 1):
#     print(i, j, v)

# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5,3))
# print(func(5,3,2,7))
# print(func())

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(3, 4, 5))

# def dict_one(*args):
#     return {k: k for k in args}
#
#
# print(dict_one(1, 2, 3, 4))
# print(dict_one('gray', (2, 17), 3.11), -4)

# def fun(*param):
#     s = sum(param) / len(param)
#     print(s)
#     return [x for x in param if x < s]
#
#
# print(fun(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(fun(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(2))
# print(func(2, 5, 67, 8, 9))

# def print_scores(student, *scores):
#     print(*scores)
#     print(scores)
#     print('\nStudent Name: ', student)
#     for score in scores:
#         print(score, end=' ')
#
#
# print_scores('Jonathan', 18, 95, 88, 92, 99)
# print_scores('Rick', 96, 20, 30, 56, 33)

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a='python'))

# def intro(**data):
#     for k, v in data.items():
#         print(k, 'is', v)
#     print()
#
#
# intro(name='Irina', suname='Sharma', age=22)
# intro(name='Igor', suname='Wood', email='igor@gamil.con', age=25, phone=987236374)

# my_dict = {'one': 'first'}


# def db(**kwargs):
#     # my_dict = my_dict | kwargs
#     # return my_dict
#     my_dict.update((kwargs))
#
#
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, k3=11, k4=91)
# print(my_dict)

# def func1(*args):
#     print(args[0])
#
#
# func1(1, 2, 3, 4, 5, 6)
# func1(5)

# def func(first, *args, **kwargs):
#     return first, args, kwargs
#
#
# print(func(5, 4, 8, 9, 7, a=6, b=2, c=10))

# Области видимости

# name = 'Tom'
# surname = ''
#
# def hi():
#     global name, surname
#     name = 'Sam'
#     surname = 'Johnson'
#     print('Hello', name, surname)
#
#
# def bye():
#     print('Good bye', name)
#
#
# print(name)
# hi()
# bye()
# print(name)

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()
# x = 3
#
#
# def add_two(a):
#     x = 2
#
#     def add_some():
#         # x = 5
#         return a + x
#
#     return add_some()
#
#
# print(add_two(3))
# #  add_some()

# import builtins
#
# names = dir(builtins)
#
# for i in names:
#     print(i)

# min = 5
# print(min)
# a = [4, 5, 6, 7, 8, 9]
# print(a)
# print(min(a))

# def outer_func(who):
#     def inner_func():
#         print('Hellow,', who)
#
#     inner_func()
#
#
# outer_func('World')

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print('Сумма:', a + b)
#
#     print('a =', a)
#     fun2(4)
#
#
# fun1()


# x = 25
# t = 0


# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         # t = a
#     inner()
#
#     t = a
#
#
# fn()
# z = x + t
# print(z)


# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x', x)
#
#     fn2()
#     print('fn1.x', x)
#
#
# fn1()

def outer(a1, a2, b1, b2):
    a = 0
    b = 0

    def inner():
        nonlocal a, b
        a = a1 + a2
        b = b1 + b2
        print(a, b)

    inner()
    return [a, b]


print(outer(2, 3, 5, 7))
