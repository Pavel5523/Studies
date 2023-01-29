from random import randint
first_list = [[randint(0, 10) for i in range(6)]for j in range(6)]
print('Список случайных чисел 6х6')
for x in first_list:
    print(x)
print()
second_list = [randint(0, 10) for k in range(6)]
# second_list = [0, 0, 0, 0, 0, 0]
print('Список из 6-ти случайных чисел ')
print(second_list)
print()
for w in range(len(first_list)):
    if w % 2 == 0:
        first_list.pop(w)
        first_list.insert(w, second_list)
print('Нечетные строки первого списка заменены вторым списком')
for y in first_list:
    for t in y:
        print(t, end='\t\t')
    print()
