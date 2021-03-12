word = input()
newWord = ""
for i in range(len(word)):
    newWord += word[i] + word[i]
print(newWord)
# print("".join([i*2 for i in input()]))