list1 = input().split(".")
num1 = int(list1[0])
num2 = int(list1[1])
num3 = int(list1[2])
if num3 == 9:
    num3 = 0
    if num2 == 9:
        num2 = 0
        num1 += 1
    else:
        num2 += 1
else:
    num3 += 1
print(f"{num1}.{num2}.{num3}")