string = input()
emojis = ""
for i in range(len(string)):
    if len(emojis) > 0:
        emojis += string[i]
        print(emojis)
        emojis = ""
    if string[i] == ":":
        emojis += ":"
