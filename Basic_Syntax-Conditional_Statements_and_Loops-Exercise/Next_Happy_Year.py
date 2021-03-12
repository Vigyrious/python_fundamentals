year = int(input()) + 1
new_list = []
while True:
    new = year
    i = str(new)
    for j in range(len(i)):
        new_list.append(int(i[j]))
    mylist = list(dict.fromkeys(new_list))
    if len(new_list) == len(mylist):
        print(new)
        break
    new_list.clear()
    year += 1
# year = int(input())
# while True:
#     year += 1
#     if len(set(str(year))) == len(str(year)):
#         print(year)
#         break