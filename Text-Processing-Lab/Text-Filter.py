banned = input().split(", ")
string = input()
for word in banned:
    while word in string:
        length = len(word) * "*"
        string = string.replace(word,length)
print(string)