race = [int(i) for i in input().split(" ")]
current = len(race) - 1
car1 = race[:int(current / 2)]
car2 = race[int( current / 2) + 1:]
car1_time = 0
car2_time = 0
for num in car1:
    if num != 0:
        car1_time += num
    else:
        car1_time *= 0.8
for num1 in car2[::-1]:
    if num1 != 0:
        car2_time += num1
    else:
        car2_time *= 0.8
if car1_time < car2_time:
    print(f"The winner is left with total time: {car1_time:.1f}")
else:
    print(f"The winner is right with total time: {car2_time:.1f}")