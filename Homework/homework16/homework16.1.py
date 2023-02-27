import re
s = 'my-p@ssw0rd'
req = r'^[\da-z@_-]{6,18}$'
print(re.findall(req, s, re.I))
