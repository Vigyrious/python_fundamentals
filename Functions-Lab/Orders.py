type = input()
quantity = int(input())
def solve(type,quantity):
    if type == "water":
        result = quantity
    elif type == "coke":
        result = 1.4 * quantity
    elif type == "coffee":
        result = 1.5 * quantity
    elif type == "snacks":
        result = 2 * quantity

    return "{:.2f}".format(result)


print(solve(type, quantity))