iteration = int(input())
list1 = []
destroyed = 0
for i in range(iteration):
    list1.append(input().split(" "))
moves = input().split(" ")
for i in range(len(list1)):
    for j in range(len(list1[i])):
        list1[i][j] = int(list1[i][j])
for move in moves:
    row, col = move.split("-")
    row = int(row)
    col = int(col)
    if list1[row][col] != 0:
        list1[row][col] -= 1
        if list1[row][col] == 0:
            destroyed += 1















print(destroyed)