import re
s = '1login@ru.name.ru'
req = r'^[\w._-]+@[a-z]+\.[a-z]{2,}[.]?[a-z]*$'
print(re.findall(req, s))
