tpl = tuple(input('Введите шесть элементов кортежа: ') for i in range(6))
s = input('Введите элемент кортежа: ')
print('Исходный кортеж:', tpl)
if tpl.count(s):
    print('Yes')
else:
    print('Нет такого элемента')
