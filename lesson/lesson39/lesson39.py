# Шаблонизатор
# Jinja
# pip install jinja2
from jinja2 import Template

# name = 'Игорь'
# age = 28
# per = {'name': 'Игорь', 'age': 28}

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# per = Person('Игорь', 28)
#
# tm = Template('Привет {{ p.get_name()}}. Тебе {{p["age"]}} лет?')
# msq = tm.render(p=per)
# print(msq)

# per = [9, 5, 6, 7, 8, 4, 2]
# link = """{% for i in p -%}
# {{i}}
# {% endfor %}
# """
#
# tm = Template(link)
# msq = tm.render(p=per)
# print(msq)

# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Ялта'},
#     {'id': 5, 'city': 'Ярославль'},
# ]
# link = """<select name='sities'>
# {%-for c in cities %}
#     {%-if c.id > 3%}
#     <option value="{{c.id}}">{{c.city}}</option>
#     {%elif c.city == 'Москва' %}
#     <option>{{c.city}}</option>
#     {%else%}
#     {{c.city}}
#     {%-endif%}
# {%-endfor %}
# </select>
# """
#
# tm = Template(link)
# msq = tm.render(cities=cities)
# print(msq)

# cars = [
#     {'models': 'Audi', 'price': 24000},
#     {'models': 'Skoda', 'price': 23000},
#     {'models': 'Renault', 'price': 22000},
#     {'models': 'Wolksvagen', 'price': 21000}
# ]
#
# # tpl = '{{(cs | max(attribute="price")).models }}'
# tpl = "{{cs | replace('models', 'brand') }}"
# tm = Template(tpl)
# msq = tm.render(cs=cars)
# print(msq)

persons = [
    {'name': 'Алексей', 'year': 18, 'weight': 78.5},
    {'name': 'Никита', 'year': 28, 'weight': 82.8},
    {'name': 'Виталий', 'year': 33, 'weight': 94.5}
]

# tpl = '''
# {%- for u in users%}
# {%filter upper %} {{u.name}} {%endfilter%}
# {%-filter string %}{{u.year}} - {{u.weight}} {%endfilter%}
# {%-endfor%}
# '''
#
# tm = Template(tpl)
# msg = tm.render(users=persons)
#
# print(msg)

html = '''
{%macro text_input(name, value='', type='text', size=20)%}
<input type='{{type}}' name='{{name}}' value='{{value}}' size='{{size}}'>
{%endmacro%}
<p>{{text_input('username')}}</p>
<p>{{text_input('email')}}</p>
<p>{{text_input('password', 'Пароль', 'password')}}</p>
'''
tm = Template(html)
msg = tm.render()

print(msg)