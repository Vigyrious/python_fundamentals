people = int(input())
capacity = int(input())
turns = 0
while people > 0:
    people -= capacity
    turns += 1
print(turns)