string = input().split(">")
new_string = []
explosion = 0
l=""
for word in string:
    if word[0].isdigit():
        explosion += int(word[0])
        if len(word) <= explosion:
            explosion -= len(word)
            l = ">"
        else:
            l = ">" + "".join(word[explosion:])
            explosion = 0
    else:
        l = word
    new_string.append(l)
print("".join(new_string))



#abv>1>1>2>2asdasd

