# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split('.'))
#         return cls(day, month, year)
#
#     def string_to_db(self):
#         return f'{self.day}-{self.month}-{self.year}'
#
#     @staticmethod
#     def is_date_valid(string_date):
#         if string_date.count('.') == 2:
#             day, month, year = map(int, string_date.split('.'))
#             return day <= 31 and month <= 12 and year <= 3999
#
#
# dates = [
#     '30.12.2020'
#     '30.12.20.20'
#     '01.01.2021'
#     '12.31.2020'
#     '30-12-2020'
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         print(date.string_to_db())
#     else:
#         print('Неправильная дата или формат строки с датой')
# # # string_date = '23.10.2022'
# # # day, month, year = map(int, string_date.split('.'))
# # date = Date.from_string('23.10.2022')
# # print(date.string_to_db())
# # date2 = Date.from_string('1.1.1')
# # print(date2.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
#         print('*' * 40)
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         usd_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета {usd_val} {Account.suffix_eur}')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.value} {Account.suffix}')
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_parcents(self):
#         self.value += self.value * self.percent
#         print('Проценты были начислены')
#         self.print_balance()
#
#     def width_drow_many(self, val):
#         if val > self.value:
#             print(f'У вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято')
#
#         self.print_balance()
#
#     def add_maney(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено')
#         self.print_balance()
#
#     def print_info(self):
#         print('Информация о счете')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')
#
#
# acc = Account('Долгих', '12345', 0.03, 1000)
# # acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.set_usd_rate(2)
# acc.convert_to_usd()
# acc.set_eur_rate(3)
# acc.convert_to_eur()
# acc.edit_owner('Дюма')
# acc.print_info()
# acc.add_parcents()
#
# acc.width_drow_many(100)
# print()
# acc.width_drow_many(3000)
# print()
# acc.add_maney(5000)
# acc.width_drow_many(3000)

# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.virify_old(old)
#         self.verify_fio(fio)
#         self.verify_weight(weight)
#         self.verify_ps(ps)
#         self.__fio = fio
#         self.__old = old
#         self.__password = ps
#         self.__weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError('ФИО должно быть строкой')
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError('Неверный формат ФИО')
#         letters = ''.join(re.findall(r'[a-zа-яё-]', fio, re.IGNORECASE))
#         # print(letters)
#         for s in f:
#             print(s.strip(letters))
#             if len(s.strip(letters)) != 0:
#                 raise TypeError('В ФИО можно использовать только буквы и дефис')
#
#     @staticmethod
#     def virify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError('Возраст должен быть числом в диапазоне от 14 до 120')
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError('Вес должен быть числом от 20кг и выше')
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError('Паспорт должно быть строкой')
#
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError('Не верный формат паспорта')
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError('Серия и номер паспорта должны быть числами')
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.virify_old(year)
#         self.__old = year
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.weight = w
#
#
# p1 = UserData('Волков Игорь Николаевич', 26, '1234 567890', 80.5)
#
# p1.fio = 'Соболев Игорь Николаевич'
# print(p1.__dict__)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width


class Line(Prop):
    # def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
    #     self._sp = sp
    #     self._ep = ep
    #     self._color = color
    #     self._width = width

    def drow_line(self) -> None:
        print(f'рисование линии: {self._sp} {self._ep} {self._color} {self._width}')


class Rect(Prop):
    # def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
    #     self._sp = sp
    #     self._ep = ep
    #     self._color = color
    #     self._width = width

    def drow_rect(self) -> None:
        print(f'рисование прямоугольника: {self._sp} {self._ep} {self._color} {self._width}')


line = Line(Point(1, 2), Point(10, 20))
print(line)
line.drow_line()

rect = Rect(Point(30, 40), Point(70, 80))
rect.drow_rect()
# print(issubclass(Point, object))
# DRY
