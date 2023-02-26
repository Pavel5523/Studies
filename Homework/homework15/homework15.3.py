my_str = '''Ежевику для ежат
Принесли два ежа
Ежевику еле-еле
Ежата возле ели съели.'''
print(my_str)
my_str = my_str.lower()
search_str = 'е'
my_str = my_str.split()
count = 0
for i in my_str:
    if i[0].find('е') != -1:
        count += 1
print()
print(f'Количество слов начинающихся на е = {count}')
