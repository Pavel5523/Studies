d = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}
for i in d:
    print(i, d[i])
print()
(d['emp3']['salary']) = int(input('Введите новую зарплату Брэда: '))
print()
for i in d:
    print(i, d[i])
