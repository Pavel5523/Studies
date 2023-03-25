import re


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.surname = surname
        self.num = num
        self.percent = percent
        self.value = value
        print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
        print('*' * 40)

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        usd_val = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счета {usd_val} {Account.suffix_eur}')

    def print_balance(self):
        print(f'Текущий баланс {self.value} {Account.suffix}')

    def edit_owner(self, surname):
        surname = ''.join(re.findall(r'^[а-яё-]+$', surname, re.IGNORECASE))
        if isinstance(surname, str) and surname:
            self.surname = surname
        else:
            print('Фамилия может содержать только буквы и тире')

    def add_parcents(self):
        if self.value > 0:
            self.value += self.value * self.percent
            print('Проценты были начислены')
            self.print_balance()

    def width_drow_many(self, val):
        if isinstance(val, (int, float)):
            if val > self.value:
                print(f'У вас нет {val} {Account.suffix}')
            else:
                self.value -= val
                print(f'{val} {Account.suffix} было успешно снято')
        else:
            print('Сумма должна быть числом')

        self.print_balance()

    def add_maney(self, val):
        if isinstance(val, (float, int)):
            self.value += val
            print(f'{val} {Account.suffix} было успешно добавлено')
            self.print_balance()
        else:
            print('Сумма должна быть числом')

    def print_info(self):
        print('Информация о счете')
        print('-' * 20)
        print(f'#{self.num}')
        print(f'Владелец {self.surname}')
        self.print_balance()
        print(f'Проценты: {self.percent:.0%}')
        print('-' * 20)

    def __del__(self):
        print('*' * 50)
        print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')


acc = Account('Долгих', '12345', 0.03, 1000)
acc.print_balance()
# acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.set_usd_rate(2)
acc.convert_to_usd()
acc.set_eur_rate(3)
acc.convert_to_eur()
acc.edit_owner('Дюма')
acc.print_info()
acc.add_parcents()

acc.width_drow_many(100)
print()
acc.width_drow_many(3000)
print()
acc.add_maney(5000)
acc.width_drow_many(3000)
