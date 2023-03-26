from math import pi


class Table:
    def __init__(self, width=None, length=None, radius=None):
        if length is None:
            self._width = width
            self._length = width
        if radius is None and length is not None:
            self._width = width
            self._length = length
        if width is None and length is None:
            self._radius = radius

    def calc_area(self):
        raise NotImplementedError('В дочернем классе должен быть реализован метод calc_area()')


class SqTable(Table):
    def calc_area(self):
        return self._width * self._length


class RoundTable(Table):
    def calc_area(self):
        return round(pi * self._radius ** 2, 2)


t = SqTable(20, 10)
print(t.__dict__)
print(t.calc_area())
tsquare = SqTable(20)
print(tsquare.__dict__)
print(tsquare.calc_area())
tround = RoundTable(radius=20)
print(tround.__dict__)
print(tround.calc_area())

