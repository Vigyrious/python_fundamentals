number = int(input())
train_list = [0] * number


def add(amount):
    train_list[len(train_list)-1] += amount


def insertings(index, amount):
    train_list[index] += amount


def leavings(index, amount):
    train_list[index] = train_list[index] - amount
    if train_list[index] < 0:
        train_list[index] = 0


def execute(command):
    order = command.split(" ")
    if order[0] == "add":
        add(int(order[1]))
    elif order[0] == "insert":
        index = int(order[1])
        amount = int(order[2])
        insertings(index, amount)
    else:
        index = int(order[1])
        amount = int(order[2])
        leavings(index, amount)


while True:
    command = input()
    if command == "End":
        print(train_list)
        break
    else:
        execute(command)


