num_list = [int(i) for i in input().split(", ")]
count = 0
result = []
for num in num_list:
    if num % 2 == 0:
        result.append(count)
    count += 1

print(result)