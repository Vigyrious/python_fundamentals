strings = input().split(" ")
string1 = strings[0]
string2 = strings[1]
total = 0
while len(string1) != 0 and len(string2) != 0:
    total += ord(string1[0]) * ord(string2[0])
    string1 = string1[1:]
    string2 = string2[1:]
if len(string1) > len(string2):
    for char in string1:
        total += ord(char)
elif len(string2) > len(string1):
    for char in string2:
        total += ord(char)
print(total)

