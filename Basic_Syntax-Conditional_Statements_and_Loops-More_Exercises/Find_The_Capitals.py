word = input()
newLis = []
for i in range(len(word)):
    if word[i].isupper():
        newLis.append(i)
print(newLis)