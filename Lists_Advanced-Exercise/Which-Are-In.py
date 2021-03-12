list2 = input().split(", ")
list1 = input().split(", ")
list3 = []
for num1 in list2:
    for num2 in list1:
        if num1 in num2:
            if num1 not in list3:
                list3.append(num1)
                break
print(list3)