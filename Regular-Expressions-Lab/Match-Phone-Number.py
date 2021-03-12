import re
data = input()
reges = r'(\+359\s2\s\d{3}\s\d{4})|(\+359-2-\d{3}-\d{4}\b)'
list1 = re.finditer(reges, data)
new_list = [p.group(0) for p in list1]
print(", ".join(new_list))