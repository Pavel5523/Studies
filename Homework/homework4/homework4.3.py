score = 0
p = 1
while score < p:
    try:
        p = int(input('Введите количество элементов в списке: '))
        n = [int(input('Введите элемент списка "Целое число" -> ')) for i in range(p)]
        print('Элементы списка ,которые, больше предыдущего: ', end=' ')
        for i in range(p):
            score += 1
            if n[i] > n[i - 1] and i > 0:
                print(n[i], end=' ')
    except ValueError:
        print('Это не целое число. Вводим с начала')
