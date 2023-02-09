tpl = tuple(input('Введите по порядку без пробелов элементы кортежа: '))
print(tpl)
new_list = []
for i in tpl:
    new_list.append('количество ' + str(i) + ' = ' + str(tpl.count(i)))
new_list = set(new_list)
for i in new_list:
    print(i)
