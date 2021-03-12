word = input()
newWord = ""
for i in range(len(word)-1,-1,-1):
    newWord += word[i]
print(newWord)