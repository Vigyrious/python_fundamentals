import re
health_regex = r'[0-9\-\+\.\/\*]+'
base_damage_regex = r'\-?\d+\.?\d*'
symbol_regex = r'[*/]*'
danni = input().split(",")
data1 = [i.strip() for i in danni]
data2 = sorted(data1)
for data in data2:
    current = data.strip()
    health = re.sub(health_regex,"",current)
    health_sum = 0
    for char in health:
        health_sum += ord(char)
    damage = re.findall(base_damage_regex, current)
    damage_sum = 0
    for number in damage:
        damage_sum += float(number)
    symbol = "".join(re.findall(symbol_regex, current))
    for char in symbol:
        if char == "*":
            damage_sum *= 2
        elif char == "/":
            damage_sum /= 2
    print(f"{current} - {health_sum} health, {damage_sum:.2f} damage")


