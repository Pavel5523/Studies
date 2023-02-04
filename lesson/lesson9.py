# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print('Сумма четных цифр:')
# print(digits_sum(98740238))
# print(digits_sum(3821234))
# print(digits_sum(12345566))
# print(digits_sum(65432345))
# print('Сумма нечетных цифр:')
# print(digits_sum(65432345, even=False))
# print(digits_sum(895947847, even=False))
# print(digits_sum(958736298, even=False))
# print(digits_sum(574873647, even=False))

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
# print(id(lt1))
# print(id(lt2))
#
# a = 2
# b = 2
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# print(id(lt1))
# lt1.pop(1)
# print(lt1)
# print(id(lt1))
# lt1(1) = ['Hellow']
# print(lt1)
# print(id(lt1))

# s = 'Hellow'
# print(id(s))
# s += 'World'
# print(s)
# print(id(s))

# a = 5
# print(id(a))
# a += 1
# print(a)
# print(id(a))

# s = list('Hellow')
# print(s[1])
# s[1] = 't'
# print(s)

# def add_number(n):
#     print('n', n, '=', id(n))
#     n += [4]
#     print('n', n, '=', id(n))
#
#
# x = [1, 2, 3]
# print('x:', x, '=', id(x))
# add_number(x)
# print('x:', x, '=', id(x))

#  Кортеж (tuple)

# lst = [1, 2, 3]
# tpl = (1, 2, 3)
# # print(lst.__sizeof__())
# # print(tpl.__sizeof__())
#
# print(type(tpl))

# a = (1,)
# print(a)
# print(type(a))
# b = tuple('Hellow')
# print(b)
# print(type(b))

# tpl = (1, 2, 3, 4, 5, 6, 7)
# print(tpl)
# print(tpl[2])
# # tpl[2] = 10
# print(tpl[1:3])
from random import randint


# s = tuple(randint(1, 30) for i in range(10))
# # s = (input('->') for i in range(3))
# print(s)

# s = tuple(2 ** i for i in range(1, 12))
# print(s)

# t1 = tuple('Hello')
# t2 = tuple('World')
# t3 = t1 + t2
# print(t1)
# print(t3)
# print(t3 * 2)
# print(len(t3))
# print(t3.count('l'))
# print(t3.count('a'))
# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print('Такого нет')
# for i in t3:
#     print(i, end=' ')

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 3, 8, 6, 5, 4, 3), 8))

# def tl(a=0, b=5, c=-5):
#     return = tuple(randint(a, b) for i in range(10))
#     return = tuple(randint(c, a) for i in range(10))
#
#
# print(tl(a, b, c))
