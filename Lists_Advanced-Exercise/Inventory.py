collection = input().split(", ")
command = input()
stringings = []
final = ""
while command != "Craft!":
    splitted = command.split(" - ")
    if splitted[0] == "Collect":
        item = splitted[1]
        if item not in collection:
            collection.append(item)
    elif splitted[0] == "Drop":
        item = splitted[1]
        if item in collection:
            collection = [i for i in collection if i != item]
    elif splitted[0] == "Combine Items":
        items = splitted[1].split(":")
        oldItem = items[0]
        newItem = items[1]
        if oldItem in collection:
            collection.insert(collection.index(oldItem) + 1, newItem)
    elif splitted[0] == "Renew":
        item = splitted[1]
        if item in collection:
            collection = [i for i in collection if i != item]
            collection.append(item)
    command = input()
for word in collection:
    stringings.append(word)
    stringings.append(", ")
stringings.pop(len(stringings) - 1)
for word in stringings:
    final += word
print(final)