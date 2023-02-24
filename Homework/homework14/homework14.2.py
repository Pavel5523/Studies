str1 = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования.'
str2 = []
for i in str1:
    if i == 'N':
        str2 += 'P'
    else:
        str2 += i
print('str1 = ', str1)
print('str2 = ', end=' ')
for i in str2:
    print(i, end='')
