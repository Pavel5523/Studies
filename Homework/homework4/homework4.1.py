print('\t\t\t\t Игра "Угадай число от 0 до 100"', end='\n\n')
n = 48  # Загаданное число
score = 0  # Счетчик попыток
while True:
    try:
        a = float(input('Введите число от 1 до 100, если хотите завершить игру введите 0 -> '))
        score += 1
        if a == 0:  # Условие завершения игры
            print('Игра закончена')
            break
    except ValueError:
        print('Это не число! Попробуйте еще раз')
    else:
        if a < n:
            print('Введенное число меньше')
        elif a > n:
            print('Введенное число число больше')
        else:
            print('Поздравляю вы угадали! с', score, 'раза.')
            break

