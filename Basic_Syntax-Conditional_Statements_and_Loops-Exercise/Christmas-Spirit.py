quantity = int(input())
days = int(input())
count = 1
spirit = 0
cost = 0
for i in range(days):
    if count % 11 == 0:
        quantity += 2
    if count % 10 == 0:
        spirit -= 20
        cost += 23
        if count == days:
            spirit -= 30
    if count % 5 == 0:
        spirit += 17
        cost += (15*quantity)
        if count % 3 == 0:
            spirit += 30
    if count % 3 == 0:
        cost += (8*quantity)
        spirit += 13
    if count % 2 == 0:
        spirit += 5
        cost += (2 * quantity)
    count += 1
print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")