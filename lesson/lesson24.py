# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if length is None:
#             self._width = width
#             self._length = width
#         if radius is None and length is not None:
#             self._width = width
#             self._length = length
#         if width is None and length is None:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError('В дочернем классе должен быть реализован метод calc_area()')
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
# tsquare = SqTable(20)
# print(tsquare.__dict__)
# print(tsquare.calc_area())
# tround = RoundTable(radius=20)
# print(tround.__dict__)
# print(tround.calc_area())

# from abc import ABC, abstractmethod


# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         # super().print_value()
#         # print(Dollar.suffix, end=' ')
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#
# d = Dollar(5), Dollar(10), Dollar(50), Dollar(100),
# for i in elem:
#     d.print_value()
#     print(f' = {d.convert_to_rub():.2f} RUB')


# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print('Child')
#
#
# class GrandChild(Child):
#     def display2(self):
#         print('GrandChild')
#
#
# qc = GrandChild()
# qc.display2()
# qc.display1()

# def func():
#     x = 2
#
#     def inner():
#         n = 4
#         return n + x
#
#     return inner()
#
#
# print(func())

# class MyOuter:
#     age = 10
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print('outer_class_method')
#
#     def outer_obj_method(self):
#         print('outer_obj_method')
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print('inner_method', MyOuter.age)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('Внешний')
# print(out.name)
# inner = out.MyInner('Внутренний', out)
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print('Name', self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light Green'
#
#         def display(self):
#             print('Name', self.name)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()

# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Name', self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = 'Smith'
#
#         def display(self):
#             print('Name', self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#
#         def display(self):
#             print('Name', self.name)
#
#
# outer = Employee()
# outer.show()
# d1 = outer.intern
# d1.display()
# d2 = outer.head
# d2.display()

# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print('Внешний класс')
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print('Вложенный класс')
#
#         class InnerClass:
#             def show(self):
#                 print('Класс внутри вложенного класса')
#
#
# outer = Outer()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = inner1.inner_inner
# inner2.show()

# class Computer:
#     def __init__(self):
#         self.name = 'pc001'
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return 'Windows 10'
#
#     class CPU:
#         def make(self):
#             return 'intel'
#
#         def models(self):
#             return 'Core-i7'
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.models())


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print('Базовый класс')
#
#     class Inner:
#         def display1(self):
#             print('Вложенный класс внутри базового')
#
#
# class SubClass:
#     def __init__(self):
#         print('Дочерний класс')
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print('Вложенный клас внутри дочернего')
#
#
# a = SubClass()

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# cat = [Cat('Пушок'), Cat('Мурзик')]
# print(cat)

# class Point:
#     def __init__(self, *args):
#         self.__courd = args
#         print(args)
#
#     def __len__(self):
#         return len(self.__courd)
#
#
# p = Point(3, 9)
# print(len(p))
# from math import sqrt
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(5, 10)
# print(p1.length)
# p1.length = 10
# print(p1.length)
# # p1.z = 20
# # print(p1.__dict__)

# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# # print(p1.__dict__)
# p2 = Point2D(5, 10)
# print('p1 =', p1.__sizeof__())
# print('p2 =', p2.__sizeof__() + p2.__dict__.__sizeof__())
# print('p2 =', p2.__sizeof__())

# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z',
#
#     def __init__(self, x, y, z):
#         self.z = z
#         super().__init__(x, y)
#
#
# p1 = Point(5, 10)
# p3 = Point3D(5, 10, 20)
# p3.z = 20
# print(p3.x, p3.y, p3.z)

#  Множественное наследования Множественное наследования

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name, 'is sleeping')
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name, 'is playing')
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name, 'is barking')
#
#
# b = Dog('Buddy')
# b.bark()
# b.sleep()
# b.play()

class A:
    def __init__(self):
        print('Class A')


class B(A):
    def __init__(self):
        print('Class B')


class C(A):
    def __init__(self):
        print('Class C')


class D(B, C):
    # def __init__(self):
    #     print('Class D')
    ...


d = D()
print(D.mro())
# print(D.__mro__)