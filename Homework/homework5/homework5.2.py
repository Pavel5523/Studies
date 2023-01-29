try:
    first_list = [input('Введите элементы списка: ') for i in range(int(input('Введите количество элементов в списке: ')))]
    print(first_list)
    k = int(input('Введите индекс: '))
    c = input('Введите значение: ')
    first_list.insert(k, c)
    print(first_list)
except ValueError:
    print('Вы ввели что-то не правильно')
