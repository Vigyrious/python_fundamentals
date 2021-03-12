element = input()
diction = {}
while element != "statistics":
    current_element = element.split(": ")
    item = current_element[0]
    quantity = int(current_element[1])
    if item not in diction:
        diction[item] = 0
        diction[item] = quantity
    else:
        diction[item] += quantity
    element = input()
print("Products in stock:")
for word in diction:
    print(f"- {word}: {diction[word]}")
print(f"Total Products: {len(diction)}")
print(f"Total Quantity: {sum(diction.values())}")