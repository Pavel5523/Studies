try:
    new_n = []
    max_n = 0
    n = [int(input('Введите элементы списка числом: ')) for i in range(int(input('Введите количество элементов списка: ')))]
    print('Весь список:', n)
    for i in n:
        if i > 0:
            new_n.append(i)
        if i > max_n:
            max_n = i
    print('Новый список из положительных элементов:', new_n)
    print('Наибольший элемент списка:', max_n)
except ValueError:
    print('это не число')
