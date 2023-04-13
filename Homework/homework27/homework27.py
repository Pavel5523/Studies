class Descript:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if isinstance(value, str):
            raise TypeError(f'значение ({self.__name}) должно быть числом')
        if value <= 0 or isinstance(value, float):
            raise ValueError(f' значение ({self.__name}) должно быть целым числом больше нуля ')

        instance.__dict__[self.__name] = value


class Triangle:
    a = Descript()
    b = Descript()
    c = Descript()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def existence(self):
        if self.a + self.b > self.c and self.c + self.b > self.a and self.a + self.c > self.b:
            print(f'Треугольник со сторонами ({self.a}, {self.b}, {self.c}) существует.')
        else:
            print(f'Треугольник со сторонами ({self.a}, {self.b}, {self.c}) не существует.')


t1 = Triangle(2, 5, 6)
t2 = Triangle(5, 2, 8)
t3 = Triangle(7, 3, 6)
t1.existence()
t2.existence()
t3.existence()
t1.a = 10
t1.b = '1'
t1.c = -5
t1.existence()
