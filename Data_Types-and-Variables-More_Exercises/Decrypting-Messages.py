key = int(input())
range1 = int(input())
for i in range(range1):
    word1 = ord(input()) + key
    newWord = chr(word1)
    print(newWord,end="")
