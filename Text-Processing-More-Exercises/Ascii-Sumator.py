range1 = ord(input())
range2 = ord(input())
sum = 0
string = input()
for char in string:
    if ord(char) in range(range1+1,range2):
        sum += ord(char)
print(sum)