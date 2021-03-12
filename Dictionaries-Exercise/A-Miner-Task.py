type = input()
dect = {}
while type != "stop":
    quantity = int(input())
    if type not in dect:
        dect[type] = 0
    dect[type] += quantity
    type=input()
for (key, value) in dect.items():
    print(f"{key} -> {value}")