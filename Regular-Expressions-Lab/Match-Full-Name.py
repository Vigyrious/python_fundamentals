import re
data= input()
regex = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'
names = re.findall(regex, data)
print(' '.join(names))