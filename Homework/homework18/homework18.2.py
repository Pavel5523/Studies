f = open('homework18.2.txt', 'w')
f.write('''Замена строки в текстовом файле;
изменить строку в списке;
записать список в файл;
''')
f.close()
f = open('homework18.2.txt', 'r')
print(f.read())
f.close()
f = open('homework18.2.txt', 'r')
text_line = f.readlines()
f.close()
f = open('homework18.2.txt', 'w')
for i in reversed(text_line):
    f.writelines(i)
f.close()
f = open('homework18.2.txt', 'r')
print(f.read())
f.close()

