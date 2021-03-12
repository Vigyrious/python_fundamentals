word = input().split(" ")
final = ""
for chars in word:
    for i in range (len(chars)):
        final += chars
print(final)