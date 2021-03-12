list_1 = [int(x) for x in input().split(" ")]
count = int(input())
smallest = list_1[0]
for i in range(count):
    for j in range(len(list_1)):
        if list_1[j] < smallest:
            smallest = list_1[j]
    list_1.remove(smallest)
    smallest = list_1[0]
print(list_1)