iterations = int(input())
dect = {}
for i in range(iterations):
    key = input()
    synonym = input()
    if key not in dect:
        dect[key] = []
    dect[key].append(synonym)
for (key, value) in dect.items():
    print(f"{key} - {', '.join(dect[key])}")