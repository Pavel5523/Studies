# name = 'Pavel'
# print('Hello,', name)
# age = 20
# print(age)

# a = 5
# print(type(a))
# a = 'Hellow'
# print(type(a))
# b = '6'
# print(type(b))
# a = 4
# b = 5
# print(a)
# print(id(a))
# print(id(b))
# a = b
# print(a)
# print(id(a))
# a = b = c = 5
# print(a, b, c)
# print(id(a), id(b), id(c))
# a, b, c = 2, 'Hellow', 4.5
# print(a, b, c)
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = False
# print(type(a))

# print('Строка символов')
# print('Строка')
# s1 = 'Hellow'
# s2 = 'Python'
# print(s1 + ', ' + s2)
# s3 = s1 + ', ' + s2 + '!\t\t'
# print(s3 * 3)
# print(3837484748476387364836488594756)
# print(3.837484748476387364836488594756)
# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 ** 2)
# print(6 / 4)
# print(6 // 4)
# print(6 % 4)
# a = 5
# b = 7
# c = 3
# print('Сумма:', a + b + c)
# print('Произведение:', a * b * c)
# print('Среднее арифметическое:', (a + b + c) / 3)
# n = 4321
# a = n // 1000
# b = (n // 100) % 10
# c = (n // 10) % 10
# d = n % 10
# print(a)
# print(b)
# print(c)
# print(d)
# print(d, c, b, a, sep='')

# from faker import Faker
#
# fake = Faker('ru_RU')
# for i in range(10):
#     print(fake.name(), fake.address())

# res = 0
# for i in range(2,6+1,2):
#     res = res + i
#     print(i)
# print(res)

# num = input('--> ')
# len_num = len(num)
# num = [1, 3, 5, 8]
# res = ''
# for i in range(len(num) - 1, -1, -1):
#     print(num[i])
#     res += i
# print(res)

num = input('--> ')
len_num = len(num)
res = ''
for i in num:
    len_num -= 1
    if len_num > 0 and i != '0':
        res += i + len_num * '0' + ' + '
    if len_num == 0:
        res += i + len_num * '0'

print(res)


