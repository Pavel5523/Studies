from random import randint

n = int(input('Введите размер списка: '))
lst = [randint(0, 20) for i in range(n)]
prime_number = []
composite_number = []
print('Весь список', lst)
for i in range(len(lst)):
    count = 2
    while count < lst[i]:
        if lst[i] % count == 0:
            composite_number.append(lst[i])
            break
        if count == lst[i] - 1:
            prime_number.append(lst[i])
            break
        count += 1
try:
    print('Минимальное простое число списка =', min(prime_number))
except ValueError:
    print('Отсутствует простое число')
try:
    print('Максимальное составное число списка =', max(composite_number))
except ValueError:
    print('Отсутствует составное число ')
