str_one = input('Введите первую строку: ')
str_two = input('Введите вторую строку: ')
for i in set(str_one) | set(str_two):
    print(i, end=' ')
