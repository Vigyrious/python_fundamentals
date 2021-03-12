import re
regex = r"(^|(?<=\s))[A-Za-z0-9]+[\._-]?[A-Za-z0-9]+@[A-Za-z]+\-?[A-Za-z]+(\.[A-Za-z]+)+"
data = input()
result = re.finditer(regex, data)
for res in result:
    print(res.group())
