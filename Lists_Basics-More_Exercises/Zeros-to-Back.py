numbers = [int(num) for num in input().split(", ")]
zero_count = numbers.count(0)
while 0 in numbers:
    numbers.remove(0)
for i in range(zero_count):
    numbers.append(0)
print(numbers)