try:
    new_list = [int(input('Введите элементы списка: ')) for i in range(int(input('Введите количество элементов списка: ')))]
    ch = int(input('Введите число: '))
    if ch in new_list:
        print('Число', ch, 'присутствует в элементах списка')
    else:
        print('нет такого числа в списке')
except ValueError:
    print('Вы ввели что-то не верно')
