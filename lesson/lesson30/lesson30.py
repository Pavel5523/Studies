# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# print(type(response.text))
# todos = json.loads(response.text)
# # print(type(todos))
# # print(todos)
#
# todos_by_user = {}
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
# print(users)
#
# max_user = ' and '.join(users)
# print(max_user)
# n = 's' if len(users) > 1 else ''
# print(f'Use{n} {max_user} completed {max_complete} TODOs')
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count
#
#
# with open('filtered_data.json', 'w') as f:
#     filtered_todos = list(filter(keep, todos))
#     print(filtered_todos)
#     json.dump(filtered_todos, f, indent=2)

# CSV (Comma Separated Values - переменные разделенные запятыми)


# with open('Data.csv') as f:
#     file_reader = csv.reader(f, delimiter=',')  # []
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#
#         # count += 1
#
#         else:
#             print(f'\t\t{row[0]} - {row[1]}. Родился в {row[2]} году.')
#     count += 1
# print(f'Всего в файле {count} строки.')

# with open('data2.csv') as f:
#     file_reader = csv.reader(f, delimiter=';')
#     for row in file_reader:
#         print(row)

# with open('Data.csv') as f:
#     fields = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=',')
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы {", ".join(row)}')
#         print(f'\t\t{row["Имя"]} - {row["Профессия"]}. Родился{row["Год рождения"]} году.')
#         count +=1

# with open('student.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Имя', 'Класс', 'Возраст'])
#     writer.writerow(['Женя', '9', '15'])
#     writer.writerow(['Саша', '5', '12'])
#     writer.writerow(['Маша', '11', '18'])

# data = [['hostname', 'vendor', 'models', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('data_new.csv', 'w') as f:
#     writer = csv.writer(f)
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)

# with open('student1.csv', 'w') as f:
#     names = ['Имя', 'Возраст']
#     writer = csv.DictWriter(f, fieldnames=names)
#     writer.writeheader()
#     writer.writerow({'Имя': 'Саша', 'Возраст': '6'})
#     writer.writerow({'Имя': 'Маша', 'Возраст': '15'})
#     writer.writerow({'Имя': 'Вова', 'Возраст': '14'})

# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'models': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'models': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'models': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'models': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict_writer.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# import requests
# import json
# import csv
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# print(type(response.text))
# todos = json.loads(response.text)
#
# with open('todos.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=list(todos[0].keys()))
#     writer.writeheader()
#     for d in todos:
#         writer.writerow(d)


# f = open('index.html', 'r').read()
# # print(type(f))
# soup = BeautifulSoup(f, 'html.parser')
# # row = soup.find('div', class_='name').text
# # row = soup.find_all('div', class_='name')[1].find('div', id='whois1')
# # row = soup.find('div', string='Alena').parent
# # row = soup.find('div', string='Alena').find_parent('div', class_='row')
# row = soup.find('div', id='whois3').find_previous_sibling()
# print(row)
# def get_copywriter(tag):
#     whois = tag.find('div', class_='whois')
#     if 'Copywriter' in whois:
#         return tag
#     return None
#
#
# f = open('index.html', 'r').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find_all('div', class_='row')
# copywriter = []
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)

# import re
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_salary(s):
#     pattern = r'\d+'
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html', 'r').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find_all('div', {'data-set': 'salary'})
# for i in row:
#     get_salary(i.text)
