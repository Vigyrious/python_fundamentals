numbers = input().split(" ")
strings = list(input())
result = ""
for num in numbers:
    current = 0
    for single in num:
        current += int(single)
    if current >= len(strings):
        while True:
            current -= len(strings)
            if current < len(strings):
                break
    result += strings[current]
    strings.pop(current)
print(result)