fires = input().split("#")
water = int(input())
high = range(81,126)
med = range(51,81)
low = range(1,51)
effort = 0
total = 0
print("Cells:")
for fire in fires:
    type, amount = fire.split(" = ")
    amount = int(amount)
    if water < amount:
        continue
    if type == "High" and amount not in high:
        continue
    elif type == "Medium" and amount not in med:
        continue
    elif type == "Low" and amount not in low:
        continue
    effort += amount /4
    water -= amount
    print(f" - {amount}")
    total += amount
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total}")