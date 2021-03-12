import re
data = input().lower()
search = f"\\b{input().lower()}\\b"
result = re.findall(search, data)
print(len(result))