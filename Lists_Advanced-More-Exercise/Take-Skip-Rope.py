string = list(input())
numbers_list = [int(i) for i in string if i.isdigit()]
alpha_symbol_list = [i for i in string if not i.isdigit()]
take_list = []
skip_list = []
result = ""
count = 0
for i in range(len(numbers_list)):
    if i % 2 == 0:
        take_list.append(numbers_list[i])
    else:
        skip_list.append(numbers_list[i])
for i in range(len(take_list)):
    take = take_list[i]
    skip = skip_list[i]
    for i in range(take):
        result+=alpha_symbol_list[count]
        count += 1
        if count == len(alpha_symbol_list):
            break
    count += skip
print(result)