first = int(input())
second = int(input())
third = int(input())
biggest = first
if biggest < second:
    biggest = second
if biggest < third:
    biggest = third
print(biggest)