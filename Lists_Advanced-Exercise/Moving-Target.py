target = input().split(" ")
targets = []
for num in target:
    targets.append(int(num))


def shot(index, amount):
    targets[index] -= amount
    if targets[index] <= 0:
        targets.pop(index)


def add(index, amount):
    targets.insert(index, amount)


def strike(targets1, start, end):
    del targets1[start: end + 1]
    return  targets1

def execute(command):
    global targets

    current = command.split(" ")
    if current[0] == "Shoot":
        index = int(current[1])
        amount = int(current[2])
        if 0 <= index < len(targets):
            shot(index, amount)
    elif current[0] == "Add":
        index = int(current[1])
        amount = int(current[2])
        if 0 <= index < len(targets):
            add(index, amount)
        else:
            print("Invalid placement!")
    elif current[0] == "Strike":
        index = int(current[1])
        amount = int(current[2])
        start = index-amount
        end = index+amount
        if 0 <= start and end < len(targets):
            targets = strike(targets, start, end)
        else:
            print("Strike missed!")

while True:
    command = input()
    if command == "End":
        final = []
        for num in targets:
            final.append(num)
            final.append("|")
        final.pop(len(final) - 1)
        string = ""
        for numerino in final:
            string +=str(numerino)
        print(string)
        break
    else:
        execute(command)