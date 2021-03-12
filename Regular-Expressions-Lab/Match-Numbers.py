import re
data = input()
regex = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
current = re.finditer(regex, data)
listings = [p.group() for p in current]
print(*listings)