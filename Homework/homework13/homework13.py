from math import pi

figures = {'окружность': lambda r: pi * r ** 2, 'прямоугольник': lambda a, b: a * b,
           'трапеция': lambda h, a, b: (h * (a + b)) / 2}

n = int(input('введите номер фигуры (1 - окружность, 2 - прямоугольник, 3 - трапеция): '))
if n == 1:
    figures1 = figures['окружность'](int(input('Введите радиус: ')))
    print('Площадь выбранной фигуры =', figures1)
elif n == 2:
    figures2 = figures['прямоугольник'](int(input('Введите первую сторону: ')),
                                        (int(input('Введите вторую сторону: '))))
    print('Площадь прямоугольника =', figures2)
elif n == 3:
    x = int(input('Введите высоту: '))
    y = int(input('Введите первую сторону: '))
    z = int(input('Введите вторую сторону: '))
    figures3 = figures['трапеция'](x, y, z)
    print('Площадь трапеции =', figures3)
else:
    print('Нет такой фигуры')
