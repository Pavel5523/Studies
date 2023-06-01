from jinja2 import Template

html = '''
{%-macro text_input(href, text, class=None)%}
{%-if class%}
    <li><a href="{{href}}" class="{{class}}"> {{text}} </a></li>
{%-else%}
    <li><a href="{{href}}"> {{text}} </a></li>
{%-endif%}
{%-endmacro%}
<ul>
    {{-text_input('/index', 'Главная', 'activ')-}}
    {{-text_input('/news', 'Новости')-}}
    {{-text_input('/about', 'О компании')-}}
    {{-text_input('/shop', 'Магазин')-}}
    {{-text_input('/contacts', 'Контакты')}}
</ul>
'''

tm = Template(html)
msg = tm.render(html=html)

print(msg)