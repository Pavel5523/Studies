class Car:
    def __init__(self, model, year, made_in, power, color, price):
        self.model = model
        self.year = year
        self.made_in = made_in
        self.power = power
        self.color = color
        self.price = price

    def __check_int(x):
        if isinstance(x, int):
            return True
        return False

    def __check_str(y):
        if isinstance(y, str):
            return True
        return False

    def set_model(self, model):
        if Car.__check_str(model):
            self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        if Car.__check_int(year):
            self.year = year

    def get_year(self):
        return self.year

    def set_made_in(self, made_in):
        if Car.__check_str(made_in):
            self.made_in = made_in

    def get_made_in(self):
        return self.made_in

    def set_power(self, power):
        if Car.__check_int(power):
            self.power = power

    def get_power(self):
        return self.power

    def set_color(self, color):
        if Car.__check_str(color):
            self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        if Car.__check_int(price):
            self.price = price

    def get_price(self):
        return self.price

    def print_car(self):
        print('Данные автомобиля'.center(40, '*'))
        print(f'''Название модели: {self.model}
Год выпуска: {self.year}
Производитель: {self.made_in}
Мощность двигателя: {self.power} л.с.
Цвет машины: {self.color}
Цена: {self.price}''')
        print('=' * 40)


first_car = Car('X7 M50i', 2021, 'BMW', 530, 'white', 10790000)
first_car.print_car()
print()
first_car.set_model('X8')
print('Модель', first_car.get_model())
first_car.set_year(2022)
print('Год', first_car.get_year())
first_car.set_made_in('MAN')
print('Производитель', first_car.get_made_in())
first_car.set_power(800)
print('Мощность', first_car.get_power())
first_car.set_color('green')
print('Цвет', first_car.get_color())
first_car.set_price(23004500)
print('Цена', first_car.get_price())
print()
first_car.print_car()
