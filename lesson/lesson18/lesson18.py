# def remove(text):
#     if not text:
#         return ''
#     if text[0] == '\t' or text[0] == ' ':
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove('  Hellow\tWorld '))

#  Файлы

# f = open('text1.txt')
# print(f)
# print(*f)
# print(f.closed)
# f.close()
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)

# f = open('text.txt')
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('text1.txt')
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open('text1.txt')
# print(f.readlines(1))
# print(f.readlines())
# f.close()

# f = open('text1.txt')
# for i in f:
#     print(i)
# f.close()

# f = open('text1.txt')
# print(len(f.readlines()))
# f.close()

# f = open('xyz', 'w')
# f.write('Hello\nWorld\n')
# f.close()

# f = open('xyz.txt', 'a')
# # f.write('New text\n')
# line = ['This is line 1', 'This is line 2']
# f.writelines(line)
# f.close()

# f = open('xyz.txt', 'a')
# lst = [i ** 5 for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(str(index) + '\t')
# f.close()

# f = open('text2.txt', 'w')
# f.write('''Заменить строку в текстовом файле;
# изменить строку в списке;
# записать список в файл''')
# f.close()
#
# f = open('text2.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# read_file[1] = 'Hello world!\n'
# print(read_file)
# f.close()
#
# f = open('text2.txt', 'w')
# f.writelines(read_file)
# f.close()

# f = open('text2.txt', 'w')
# f.write('''Заменить строку в текстовом файле;
# изменить строку в списке;
# записать список в файл''')
# f.close()
# n = int(input('введите номер строки удаляемой строки '))
# f = open('text2.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# if 0 < n <= len(read_file):
#     del read_file[n - 1]
# print(read_file)
# f.close()
#
# f = open('text2.txt', 'w')
# f.writelines(read_file)
# f.close()

# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell())  # 3 - возвращает условную позицию виртуального курсора в файле
# print(f.seek(1))  # 1 - перемещение курсора в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open('text5.txt', 'r+')
# # print(f.write('I am learning Python'))
# # print(f.seek(3))
# # print(f.write('-new string-'))
# # print(f.tell())
# f.close()

# with open('text.txt', 'r+') as f:
#     print(f.write('1234567889'))
#
# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line[:3])

# file_name = 'res.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 4.33, 7, 777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print('Done')
#
#
# with open('res.txt', 'r') as f:
#     n = f.read().split(' ')
#     print(n)
#     len(n)
#     print(sum(map(float, n)))

# def longest_world(file):
#     with open(file) as text:
#         w = text.read().split()
#         max_lehgth = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_lehgth]
#         print(w)
#         print(res)
#         if len(res) == 1:
#             return res[0]
#         return max_lehgth
#
#
# print(longest_world('test.txt'))

# text = 'Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n'
#
# with open('one.txt', 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия - ')
#         fw.write(line)

# with open('one_txt.txt', 'r') as one, open('two_txt.txt', 'r') as two, open('three_txt.txt', 'w') as three:
#     one = one.read()
#     two = two.read()
#     # с = one + two
#     # print(c)
#     # # three.write(c)
#     # # print(three)
#     for i, j in zip(one, two):
#         three.write(i)
#         three.write(j)

