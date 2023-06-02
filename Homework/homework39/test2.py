from jinja2 import Template

html = '''
{%-macro text_input(name, placeholder, type='text')%}
    <p><input type="{{type}}" name="{{name}}" placeholder="{{placeholder}}"> </p>
{%-endmacro%}
    {{-text_input('firstname', 'Имя')}}
    {{-text_input('lastname', 'Фамилия')}}
    {{-text_input('address', 'Адрес')}}
    {{-text_input('tel', 'phone', 'Телефон')}}
    {{-text_input('email', 'email', 'Почта')}}
'''

tm = Template(html)
msg = tm.render(html=html)

print(msg)