
# n = [(input('Введите элементы списка -> ')) for i in range(8)]  # Создание списка
n = [2, 5, 't', 7, 2, 5, 'f', 7, 'f', 3]  # Готовый список
print('Весь список: ', n)
print('Неповторяющиеся элементы списка: ', end=' ')
for i in range(len(n)):
    for j in range(len(n)):
        if n[i] == n[j] and i != j:  # Завершение цикла если найдено повторение
            break
        if j == len(n) - 1:          # Вывод неповторяющегося элемента
            print(n[i], end=' ')
