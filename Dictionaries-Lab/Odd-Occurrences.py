elements = input().split(" ")
diction = {}
for word in elements:
    lower = word.lower()
    if lower not in diction:
        diction[lower] = 0
    diction[lower] += 1
for (key, value) in diction.items():
    if value % 2 != 0:
        print(key, end=" ")