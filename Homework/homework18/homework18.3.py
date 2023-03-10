f = open('homework18.3.txt', 'w')
f.write('''первая строка
строка номер два
третья строка
4 строка''')
f.close()
f = open('homework18.3.txt', 'r')
f.close()
f = open('homework18.3.txt', 'r')
n_line = len(f.readlines())
f.close()
f = open('homework18.3.txt', 'r')
line = f.readlines()
f.close()
for i in range(n_line):
    if i < n_line - 1:
        print(line[i], end='')
        print(' ', len(line[i]), 'симв.', len(line[i].split()), 'сл.')
    else:
        print(line[i])
        print(' ', len(line[i]), 'симв.', len(line[i].split()), 'сл.')
print(n_line, 'стр.')
