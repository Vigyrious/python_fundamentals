range1 = int(input())
capacity = 255
capacity1 = 0
for i in range(range1):
    liter = int(input())
    if capacity >= liter:
        capacity -= liter
        capacity1 += liter
    else:
        print("Insufficient capacity!")
print(capacity1)
