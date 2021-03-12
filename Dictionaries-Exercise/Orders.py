command = input()
dect_price = {}
dect_quantity = {}
while command != "buy":
    item, price, quantity = command.split(" ")
    price = float(price)
    quantity = int(quantity)
    if item not in dect_quantity:
        dect_price[item] = price
        dect_quantity[item] = quantity
    else:
        dect_quantity[item] += quantity
    if dect_price[item] != price:
        dect_price[item] = price
    command = input()
for item, value in dect_quantity.items():
    print(f"{item} -> {value*dect_price[item]:.2f}")

