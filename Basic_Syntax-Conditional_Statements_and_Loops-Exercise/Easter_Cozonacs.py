budget = float(input())
flourPrice = float(input())
eggsPrice = flourPrice * 0.75
milkPrice = flourPrice * 1.25 / 4
cozonac = 0
eggs = 0
while budget > (flourPrice + eggsPrice + milkPrice):
    budget -= (flourPrice + eggsPrice + milkPrice)
    cozonac += 1
    eggs += 3
    if cozonac % 3 == 0:
        eggs -= (cozonac - 2)
print(f"You made {cozonac} cozonacs! Now you have {eggs} eggs and {budget:.2f}BGN left.")
