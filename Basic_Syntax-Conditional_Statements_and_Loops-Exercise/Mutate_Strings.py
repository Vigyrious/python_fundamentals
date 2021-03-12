# word1 = list(input())
# word2 = list(input())
# res1 = ""
# for i in range(len(word2)):
#     word1[i] = word2[i]
#     res = res1.join(word1)
#     if res1 != res:
#         print(res)
#     res1 = res
#     if res == word2:
#         break
#     res1 = ""
word1 = input()
word2 = input()
newWord = ""
oldWord = word1
for i in range(len(word1)):
    for j in range(0, i+1):
        newWord += word2[j]
    for k in range(i+1, len(word1)):
        newWord += word1[k]
    if not newWord == oldWord:
        print(newWord)
    oldWord = newWord
    newWord = ""
