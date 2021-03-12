import re
pattern = r'%(?P<Name>[A-Z][a-z]+)%.*?<(?P<Type>\w+)>.*?\|(?P<Count>\d+)\|.*?(?P<Price>\d+(?:\.\d+)?)\$'
data = input()
total = 0
while data != "end of shift":
    result = re.finditer(pattern, data)
    for res in result:
        name, typee, count, price = res.groups()
        count = int(count)
        price = float(price)
        total += count*price
        print(f"{name}: {typee} - {count*price:.2f}")
    data = input()
print(f"Total income: {total:.2f}")

