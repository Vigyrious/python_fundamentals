list1 = input().split(" ")
list1.sort(reverse=True)
newnum = ""
for num in list1:
    newnum += num
print(newnum)