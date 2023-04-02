# class A:
#     def __init__(self):
#         print('Class A')
#
#
# class B(A):
#     def __init__(self):
#         print('Class B')
#
#
# class C(A):
#     def __init__(self):
#         print('Class C')
#
#
# class D(B, C):
#     # def __init__(self):
#     #     print('Class D')
#     ...
#
#
# d = D()
# print(D.mro())
# # print(D.__mro__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#
# class Styles:
#     def __init__(self, color='red', width='1'):
#         print('Инициализатор Styles')
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print('Инициализатор POS')
#         self._ep = ep
#         self._sp = sp
#         Styles.__init__(self, *args)
#
#
# class Line(Pos, Styles):
#     # def __init__(self, sp, ep, color, width):
#     #     Pos.__init__(self, sp, ep)
#     #     Styles.__init__(self, color, width)
#
#     def draw(self):
#         print(f' Рисование линии: {self._sp}, {self._ep}, {self._width}, {self._color}')
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclasslog.txt')
#
#
# subclass = MySubClass()
# subclass.display('Эта строка будет отображаться и записываться в файл')

# class Goods:
#     def __init__(self, name, weight, price):
#         print('Init Goods')
#         super().__init__()
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def price_info(self):
#         print(f'{self.name}, {self.weight}, {self.price}')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print('Init Mixinlog')
#         MixinLog.ID += 1
#         self.ID = MixinLog.ID
#
#     def save_save_log(self):
#         print(f'{self.ID}: товар был продан в 00:00')
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook('HP', 1.5, 35000)
# n.price_info()
# n.save_save_log()
# print(NoteBook.mro())

n = 24 * 60 * 60
print(n)


class Clock:
    __DAY = n

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise ValueError('Секунды должны быть целым числом')
        self.sec = sec

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f'{self.get_form(h)}:{self.get_form(m)}:{self.get_form(s)}'

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else '0' + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.sec + other.sec)

    def __eq__(self, other):
        # if self.sec == other.sec:
        #     return True
        # return False
        return self.sec == other.sec


c1 = Clock(100)
# print(c1.get_format_time())
c2 = Clock(200)
# print(c2.get_format_time())
# # c3 = c1 + c2
# c2 += c1
# # print(c3.get_format_time())
# print(c2.get_format_time())
if c1 == c2:
    print('Время равно')
else:
    print('Время разное')
