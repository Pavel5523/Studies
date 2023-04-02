class Clock:
    __DAY = 8640

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

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.sec % other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.sec - other.sec)

    def __eq__(self, other):
        return self.sec == other.sec

    def __lt__(self, other):
        if self.sec < other.sec:
            return True
        return False

    def __gt__(self, other):
        if self.sec > other.sec:
            return True
        return False

    def __le__(self, other):
        if self.sec <= other.sec:
            return True
        return False

    def __ge__(self, other):
        if self.sec >= other.sec:
            return True
        return False


c1 = Clock(100)
c2 = Clock(200)
c3 = c1 + c2
c4 = c1 * c2
c5 = c2 // c1
c6 = c1 % c2
c7 = c2 - c1
print(f'c1: {c1.get_format_time()}')
print(f'c1 * c2: {c4.get_format_time()}')
print(f'c2 // c1: {c5.get_format_time()}')
print(f'c1 % c2: {c6.get_format_time()}')
print(f'c2 - c1 {c7.get_format_time()}')
c3 -= c1
print(f'c3 -= c1: {c3.get_format_time()}')
c3 *= c1
print(f'c3 *= c1: {c3.get_format_time()}')
c3 //= c1
print(f'c3 //= c1: {c3.get_format_time()}')
c3 %= c1
print(f'c3 % c1: {c3.get_format_time()}')
print(f'c1 < c2 {c1 < c2}')
print(f'c1 > c2 {c1 > c2}')
print(f'c1 <= c2 {c1 <= c2}')
print(f'c1 >= c2 {c1 >= c2}')
