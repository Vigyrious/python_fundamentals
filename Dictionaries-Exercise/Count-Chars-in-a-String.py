string = list(input())

dect = {}
for letter in string:
    if letter not in dect:
        dect[letter] = 0
    dect[letter] += 1
    if letter == " ":
        dect.pop(letter)
for (key, value) in dect.items():
    if key != " ":
        print(f"{key} -> {value}")
