items = input().split("|")
budget = int(input())
profit = 0
for item_category in items:
    type, price = item_category.split("->")
    price = float(price)
    is_true = (
            (type == "Clothes" and price <= 50 or
             type == "Shoes" and price <= 35 or
             type == "Accessories" and price <= 20.5) and
            budget >= price
    )
    if is_true:
        budget-=price
        profit += price * 1.4
        print(f"{price*1.4:.2f}",end=" ")
print(f"\nProfit: {profit/1.4 * .4:.2f}")
if budget + profit >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
