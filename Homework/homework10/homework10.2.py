str_one = input('Введите первую строку: ')
str_two = input('Введите вторую строку: ')
str_one = set(str_one)
str_two = set(str_two)
print('Искомыми буквами являются:')
for i in str_one - str_two:
    print(i, end=' ')
