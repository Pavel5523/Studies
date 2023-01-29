n = int(input('Введите число от 1 до 99 включительно '))
if 1 <= n <= 99:
    print('У вас', n, end=' ')
    if (n > 15 or n < 5) and (n % 10 == 2 or n % 10 == 3 or n % 10 == 4):
        print('копейки')
    elif n == 1 or n > 20 and n % 10 == 1:
        print('копейка')
    else:
        print('копеек')
else:
    print('Вы ввели некорректное значение')
