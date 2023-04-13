# Декораторы

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print('перед вызовом функции')
#         self.func()
#         print('после вызова функции')
#
#
# @MyDecorator
# def hello():
#     print('hello')
#
#
# # def hello():
# #     print('hello')
#
#
# hello()

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         res = 'перед вызовом функции\n'
#         res += str(self.func(a, b))
#         res += '\nпосле вызова функции'
#         return res
#
#
# @MyDecorator
# def hello(a, b):
#     return a * b
#
#
# print(hello(2, 5))

# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         return (self.func(a, b)) ** 2
#
#
# @Power
# def summ(a, b):
#     return a * b
#
#
# print(summ(3, 4))

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         res = 'перед вызовом функции\n'
#         res += str(self.func(*args))
#         res += '\nпосле вызова функции'
#         return res
#
#
# @MyDecorator
# def hello(a, b):
#     return a * b
#
#
# @MyDecorator
# def hello1(a, b, c):
#     return a * b * c
#
#
# print(hello(2, 5))
# print(hello1(2, 5, 3))

# class MyDecorator:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             res = 'перед вызовом функции\n'
#             res += str(self.func(*args, **kwargs))
#             res += '\nпосле вызова функции'
#             return res
#
#
# @MyDecorator('test')
# def hello(a, b):
#     return a * b
#
#
# print(hello(2, 5))

# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs)
#             return func(*args, **kwargs) ** self.n
#
#         return wrap
#
#
# @Power(n)
# def summ(a, b):
#     return a * b
#
#
# print(summ(3, 4))

# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('Значение должно быть положительным')
#         instance.__dict__[self.name] = value
#
#
# class Order:
#     price = NonNegative()
#     quantity = NonNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple = Order('apple', 5, 10)
# print(apple.total())

# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(int, coord):
#             return f'Координата {coord} должна быть числом'
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#
# class Point_3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point_3D(1, 2, 3)
# print(p1.__dict__)

# Создание модулей

class RecTangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_per(self):
        return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_per(self):
        return 4 * self.a


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_per(self):
        return self.a + self.b + self.c


r1 = RecTangle(1, 2)
r2 = RecTangle(3, 4)
# print(r1.get_per_rect(), r2.get_per_rect())

s1 = Square(10)
s2 = Square(20)
# print(s1.get_per_sq(), s2.get_per_sq())

t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

shape = [r1, r2, s1, s2, t1, t2]
for g in shape:
    print(g.get_per())
