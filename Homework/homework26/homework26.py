from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):
    def __init__(self, color, a=None, b=None, c=None):
        self.color = color
        self.a = a
        self.b = b
        self.c = c

    @abstractmethod
    def print_info(self):
        print()
        if not self.b and not self.c:
            print('===Квадрат===')
        if self.b and not self.c:
            print('===Прямоугольник===')
        if self.a and self.b and self.c:
            print('===Треугольник===')


class Square(Shape):
    def print_info(self):
        super().print_info()
        print('Сторона:', self.a)
        print('Цвет:', self.color)
        print('Площадь:', self.a ** 2)
        print('Периметр:', self.a * 4)
        for i in range(self.a):
            print('*' * self.a)


class Rectangle(Shape):

    def print_info(self):
        super().print_info()
        print('Длина:', self.a)
        print('Ширина:', self.b)
        print('Цвет:', self.color)
        print('Площадь:', self.a * self.b)
        print('Периметр:', self.a * 2 + self.b * 2)
        for i in range(self.a):
            print('*' * self.b)


class Triangle(Shape):

    def print_info(self):
        p = self.a + self.b + self.c
        pp = p / 2
        s = sqrt(pp * (pp - self.a) * (pp - self.b) * (pp - self.c))
        super().print_info()
        print('Сторона 1:', self.a)
        print('Сторона 2:', self.b)
        print('Сторона 3:', self.c)
        print('Цвет:', self.color)
        print('Площадь:', round(s, 2))
        print('Периметр:', p)
        n = 1
        for i in range(6):
            if i == 0:
                print('*'.center(self.a))
            else:
                n += 2
                print(('*' * n).center(self.a))


q = Square('red', 3)
par = Rectangle('green', 3, 7)
r = Triangle('yellow', 11, 6, 6)
my_set = [q, par, r]
for figure in my_set:
    figure.print_info()
