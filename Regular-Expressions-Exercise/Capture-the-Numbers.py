import re
data = input()
while data:
    result = re.findall(r'\d+', data)
    if len(result) != 0:
        print(*result, end=" ")
    data = input()