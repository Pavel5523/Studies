n = [(input('Введите элементы списка-> ')) for i in range(6)]  # Создаем список
print(n)  # Выводим весь список
print('Элементы списка с четными индексами', end=' ')
for i in range(6):
    if i % 2 == 0:
        print(n[i], end=' ')
