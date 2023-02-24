s = input('Введите любое слово ')
print('Введенное слово', s)
try:
    n = int(input('Введите порядковый номер буквы для удаления '))
    s2 = []
    print('Результат ', end='')
    if n <= len(s):
        for i in range(len(s)):
            if n != i:
                s2 += s[i]
    else:
        print('Нет буквы с таким номером')
    for i in s2:
        print(i, end='')
except ValueError:
    print('Вы ввели не номер')
