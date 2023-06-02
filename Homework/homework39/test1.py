from jinja2 import Template

info = [{'path':'/index', 'inf':'Главная'},
        {'path':'/news','inf':'Новости'},
        {'path':'/about','inf':'О компании'},
        {'path':'/shop','inf':'Магазин'},
        {'path':'/contacts','inf':'Контакты'}]
html = '''
<ul>
{%- for i in html %}
{%-if i.path == '/index'%}
<li><a href="{{i.path}}" class="active">{{i.inf}}</a></li>
{%else-%}
<li><a href="{{i.path}}">{{i.inf}}</a></li>
{%endif%}
{%- endfor -%}
</ul>
'''

tm = Template(html)
msg = tm.render(html=info)

print(msg)
