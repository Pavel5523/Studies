from jinja2 import Template

html = '''
{%-macro text_input(type, name, placeholder)%}
    <p><input type="{{type}}" name="{{name}}" placeholder="{{placeholder}}"> </p>
{%-endmacro%}
    {{-text_input('text', 'firstname', 'Имя')-}}
    {{-text_input('text', 'lastname', 'Фамилия')-}}
    {{-text_input('text', 'address', 'Адрес')-}}
    {{-text_input('tel', 'phone', 'Телефон')-}}
    {{-text_input('email', 'email', 'Почта')-}}
'''

tm = Template(html)
msg = tm.render(html=html)

print(msg)