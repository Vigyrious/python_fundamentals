string = input()
new_list = string.split(" ")
newer_list = []
count = 0
for num in new_list:
    newer_list.append(int(num))
for num in newer_list:
    if num > 0:
        num = -num
    elif num < 0:
        num = abs(num)
    newer_list[count] = num
    count += 1
print(newer_list)