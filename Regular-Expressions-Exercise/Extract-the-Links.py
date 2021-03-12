import re
pattern = r'www.[A-Za-z0-9]+((\-[A-Za-z0-9]+)?)+\.[a-z]+((\.[a-z]+)?)+'
data = input()
while data:
    result = re.finditer(pattern, data)
    for res in result:
        print(res.group())
    data = input()