num = int(input())
key = input()
new_list = []
newer_list = []
for i in range(num):
    new_list.append(input())
for i in new_list:
    if key in i:
        newer_list.append(i)
print(new_list)
print(newer_list)
