#  Модули OS и OS.PATH
import os
import os.path


# print(' Текущая директория', os.getcwd())  # возвращает путь к текущей деректории
# print(os.listdir())  # текущая директория, возвращает имена
# print(os.listdir('..'))   # на уровень выше
# os.mkdir('folder')  # создание папки
# os.makedirs('nested1/nested2/nested3') # создание папки и всех промежуточных папок
# os.rmdir('folder')
# os.remove('Название файла') # удаляет файл
# os.rename('Что переименовать', 'На что преименовать')  # Переименование файла или папки
# os.rename('Название файла', 'Путь куда переместить и как назвать перемещенный файл')  #  Перемещение по заданному пути, все имена пути должны существовать
# os.renames('что переместить', "перемещение и переименование файла") #  Переносит и создает путь
# print(os.walk('nested1'))

# for root, dirs, files in os.walk('nested1', topdown=True): # topdown=True С верху в низ
#     print('Root', root)
#     print('Subdirs', dirs)
#     print('Files', files)

# def remove_empty_dirs(root_tree):
#     print(f'Удаление пустых директорий в ветке {root_tree}')
#     print('-' * 50)
#     for root, dirs, files in os.walk('nested1'):
#         if  not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория {root} удалена')
#     print('-' * 50)
#
#
# remove_empty_dirs('nested1')

# print(os.path.split(r'/run/media/pavel/sdc/Studies/Python/learn/lesson/lesson19/nested1/nested2/one.txt')) # разбивет путь на кортеж (head, tail)
# tail последний элемент
# print(os.path.dirname(r'/run/media/pavel/sdc/Studies/Python/learn/lesson/lesson19/nested1/nested2/one.txt'))  # head
# print(os.path.basename(r'/run/media/pavel/sdc/Studies/Python/learn/lesson/lesson19/nested1/nested2/one.txt')) #  tail

# print(os.path.join(r'run', 'media','pavel'))  # обьединяет один или несколько компонентов пути с учетом особенности ос

# dirs = ['Work/F1', 'Work/F2/F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     'Work/F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     'Work/F2/F21': ['f211.txt', 'f212.txt']
# }
#
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         open(file_path, 'w').close()
#         # print(file_path)
#
# file_width_text = ['Work/w.txt', 'Work/F1/f12.txt', 'Work/F2/F21/f211.txt', 'Work/F2/F21/f212.txt']
#
# for file in file_width_text:
#     with open(file, 'w') as f:
#         f.write(f'Некоторый текст для документа: {file}')
#
#
# def print_tree(root, topdown=True):
#     print(f'Обход {root} {"сверху вниз" if topdown else "снизу вверх"}')
#     for root, dirs, fl in os.walk(root, topdown):
#         print(root)
#         print(dirs)
#         print(fl)
#     print('-' * 50)
#
#
# print_tree('Work', False)
# print_tree('Work')

# print(os.path.exists(r'/run/media/pavel/sdc/Studies/Python/learn/lesson/lesson19/nested1/nested2/one.txt')) # Возвращает True если файл существует
# import time
# path = '/run/media/pavel/sdc/Studies/Python/Video/Git - Hастройка логина в GitHub через SSH Key на Linux.mp4'
# print(os.path.getsize(path) // 1024, 'kb')  # Возвращает размер в байтах
# print(os.path.getmtime(path)) # возвращает время последнего изменения файла
# print(os.path.getatime(path)) # возвращает время последнего доступа к файлу
# print(os.path.getmtime(path)) # возвращает время создания файла
# atime = os.path.getatime(path)
# print(time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(atime)))
#
# print(os.path.isdir(''))  # Возвращает True, если путь является директорией
# print(os.path.isfile(''))  # Возвращает True, если путь является файлом

# fl = os.path.isfile('Work/w.txt')
# if fl:
#     print(os.path.basename('w.txt'))
#     print(os.path.getatime('Work'))
# else:
#     print('Нет такого файла')

# ООП ООП ООП ООП ООП ООП ООП ООП ООП ООП ООП ООП ООП ООП

# class Point:
#     '''Клас для предоставления координат точки'''
#     x = 1
#     y = 1
#
#
# p1 = Point()
# # print(type(p1))
# # print(p1.x)
# # print(Point.__doc__)
# print(dir(Point))

# class Point:
#     '''Клас для предоставления координат точки'''
#     x = 1
#     y = 2
#
#
# p1 = Point()
# p2 = Point()
# Point.x = 100
# p1.x = 30
# p1.y = 60
# p1.z = 80
# print(p1.x)
# print(p1.y)
# print(p1.__dict__)
# print(Point.__dict__)
# # print(p2.__dict__)
# p2 = Point()
# print(p2.x)
# print(p2.y)
#
# print(id(Point))
# print(id(p1))
# print(id(p2))

class Point:
    '''Клас для предоставления координат точки'''
    x = 1
    y = 2

    def set_courd(self):
        print(self.__dict__)


p1 = Point()
p1.x = 5
p1.y = 10
p1.set_courd()
# Point.set_courd(p1)

p2 = Point()
p2.x = 20
p2.y = 40
p2.set_courd()
