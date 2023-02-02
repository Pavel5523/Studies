from random import randint
n = int(input('Введите размер списка: '))
lst = [randint(0, 20) for i in range(n)]
prime_number = []
composite_number = []
print(lst)
for i in range(len(lst)):
    for j in range(2, lst[i] - 1):
        if lst[i] % j == 0:
            composite_number.append(lst[i])
        else:
            prime_number.append(lst[j])
print(prime_number)
print(composite_number)


        
