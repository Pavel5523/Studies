n = input('Введите число символов: ')
symboll = input('Введите символ: ')
bearings = input('Введите направление линии, если горизонтальное то-"0", если вертикальное то-"1": ')
try:
    n = int(n)
    bearings = int(bearings)
except ValueError:
    print('Вы ввели что-то не правильно')
else:
    if bearings == 0:
        while n > 0:
            print(symboll, end=" ")
            n -= 1
    elif bearings == 1:
        while n > 0:
            print(symboll, end="\n")
            n -= 1
    else:
        print('Вы ввели недопустимую ориентацию')


