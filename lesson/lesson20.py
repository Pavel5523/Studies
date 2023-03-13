# class Point:
#     x = 1
#     y = 2
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# Point.set_coord(p1, 5, 10)
#
#
# p2 = Point()
# p2.set_coord(20, 40)

# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self, ):
#         print('Персональные данные'.center(40, '*'))
#         print(f'Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n'
#               f'Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}')
#         print('=' * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_city(self, city):
#         self.city = city
#
#     def get_city(self):
#         return self.city
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#     def set_phone(self, phone):
#         self.phone = phone
#
#     def get_phone(self):
#         return self.phone
#
#     def set_country(self, country):
#         self.country = country
#
#     def get_country(self):
#         return self.country
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_address(self, address):
#         self.address = address
#
#     def get_address(self):
#         return self.address
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info('Юля', '23.05.1986', '45-46-98', 'Россия', 'Москва', 'Чистопрудный бульвар, 1А')
# h1.print_info()
# h1.set_city('Саратов')
# h1.print_info()
# print(h1.get_city())
# h1.set_name('Вася')
# h1.print_info()

# class Person:
#     skill = 10
#
#     # name = ''
#     # surrname = ''
#     def __init__(self, name, surrname):
#         self.name = name
#         self.surrname = surrname
#
#     def print_info(self):
#         # self.name = name
#         # self.surrname = surrname
#         print('Данные сотрудника:', self.name, self.surrname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print('Квалификация сотрудника:', self.skill, '\n')
#
#
# p1 = Person('Viktor', 'Reznik')
# p1.print_info()
# p1.add_skill(3)
# p2 = Person('Anna', 'Dolgih')
# p2.print_info()
# p2.add_skill(2)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print('Удаление экземпляра')
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# # del p1
# p1 = 0
# print(p1.x)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x, y):
#         if isinstance(x, int) and isinstance(y, int):
#             self.x = x
#             self.y = y
#         else:
#             print('Координаты должны быть числами')
#
#     def get_coord(self):
#         return self.x, self.y
#
#
# p1 = Point(5, 10)
# p1.set_coord(20, 'aaa')
# print(p1.__dict__)
# print(p1.get_coord())


# class Point:
#     count = 0
#
#     def __init__(self, x=1, y=1):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point()
# print(p1.count)
# print('Point', Point.count)
# p2 = Point()
# print(p2.count)
# print('Point', Point.count)
# p3 = Point()
# print(p3.count)
# print('Point', Point.count)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print('Инициализация робота', self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, 'выключается')
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, 'был последним')
#         else:
#             print('количеств роботов', Robot.k)
#
#     def say_hi(self):
#         print('Приветствую меня зовут', self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print('Численность роботов:', Robot.k)
# print()
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print('Численность роботов:', Robot.k)
# print('\nЗдесь роботы могут проделать какуют-о работу\n')
# print('Роботы закончили свою работу. Давайте их выключим')
#
# del droid1
# del droid2
#
# print('Численность роботов:', Robot.k)

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __check_value(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    def set_coord(self, x, y):
        if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, int)):
            self.__x = x
            self.__y = y
        else:
            print('координата должна быть числом')

    def get_coord(self):
        return self.__y, self.__x


p1 = Point(5, 10)
# print(p1.__x, p1.__y)
print(p1.__dict__)
p1.__x = 100
print(p1.__dict__)
# p1.x = 100
# p1.y = 'abc'
# print(p1.x, p1.y)
p1.set_coord(80, 120)
print(p1.get_coord())
