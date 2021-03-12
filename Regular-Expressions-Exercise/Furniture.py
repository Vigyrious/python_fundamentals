import re
regex = r'>>(?P<Furniture>[A-Za-z]+)<<(?P<Price>\d+\.?\d+)!(?P<Quantity>\d+($|(?=\s)))'
data = input()
sum = 0
print("Bought furniture:")
while data != "Purchase":
    result =  re.finditer(regex, data)
    for res in result:
        dect = res.groupdict()
        a=5
        print(f"{dect['Furniture']}")
        cena = float(dect['Price']) * int(dect['Quantity'])
        sum += cena
    data = input()
print(f"Total money spend: {sum:.2f}")