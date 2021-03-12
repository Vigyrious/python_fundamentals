tasks = input().split("|")
energy = 100
coins = 100
isBank = False
for task in tasks:
    type, num = task.split("-")
    num = int(num)
    if type == "rest": # energy 99 rest 6
        energy += num
        if energy + num >= 100:
            print(f"You gained {100 - (energy-num)} energy.")
        else:
            print(f"You gained {num} energy.")
        if energy >= 100:
            energy = 100
        print(f"Current energy: {energy}.")
    elif "order" in type:
        energy -= 30
        if energy < 0:
            print("You had to rest!")
            energy += 80
            continue
        else:
            coins += num
            print(f"You earned {num} coins.")
    else:
        coins -= num
        if coins <= 0:
            print(f"Closed! Cannot afford {type}.")
            isBank = True
            break
        else:
            print(f"You bought {type}.")
if not isBank:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
