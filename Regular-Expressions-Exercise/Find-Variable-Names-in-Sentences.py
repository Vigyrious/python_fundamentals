import re
pattern = r'(?<=\b_{1})[A-Z+|a-z+|\d+]+\b'
result = re.findall(pattern, input())
print(",".join(result))