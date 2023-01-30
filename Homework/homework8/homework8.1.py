from math import pi


def orthogon(a, b):
    return a * b


def triangle(a, b, ):
    return (a * b) / 2


def circle(a):
    return pi * a ** 2


try:
    n = int(input('Введите желаемую фигуру (0 - прямоугольник, 1 - треугольник, 2 - круг): '))
    if n == 0:
        length = int(input('Введите высоту: '))
        width = int(input('Введите ширину: '))
        print('Площадь прямоугольника =', orthogon(length, width))
    if n == 1:
        base = int(input('Введите ширину основания: '))
        height = int(input('Введите высоту: '))
        print('Площадь треугольника =', triangle(base, height))
    if n == 2:
        radius = int(input('Введите радиус: '))
        print('Площадь круга =', round(circle(radius), 2))
except ValueError:
    print('Вы ввели что-то не верно')
