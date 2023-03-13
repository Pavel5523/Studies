import os.path

for i in os.listdir('testFolder'):
    if os.path.isdir(os.path.join('testFolder', i)):
        print(i, '- dir')
    else:
        print(i, '- file -', os.path.getsize(os.path.join('testFolder', i)), 'bytes')
