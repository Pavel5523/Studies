f = open('homework18.1.txt', 'w')
f.write('''Замена строки в текстовом файле;
изменить строку в списке;
записать список в файл;\n''')
f.close()
f = open('homework18.1.txt', 'r')
print(f.read())
f.close()
try:
    one_str = int(input('Введите номер первой заменяемой строки: '))
    two_str = int(input('Введите номер второй заменяемой строки: '))
    f = open('homework18.1.txt', 'r')
    list_txt = f.readlines()
    print(len(list_txt))
    if 0 < one_str <= len(list_txt) and 0 < two_str <= len(list_txt):
        list_txt[one_str - 1], list_txt[two_str - 1] = list_txt[two_str - 1], list_txt[one_str - 1]
        f.close()
        print()
        f = open('homework18.1.txt', 'r+')
        for i in list_txt:
            print(i)
            f.writelines(i)
        f.close()
    else:
        print('Нет строки с таким номером')
except ValueError:
    print('Это не номер')
