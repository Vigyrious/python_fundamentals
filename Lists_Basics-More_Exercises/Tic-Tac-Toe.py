tic = [input().replace(" ", ""), input().replace(" ", ""), input().replace(" ", "")]
has_won = False
winner = ""
for row in tic:
    if row.count(str(1)) == 3 or row.count(str(2)) == 3:
        if row.count(str(1)) == 3:
            winner = "First"
        else:
            winner = "Second"
        has_won = True
        break
if not has_won:
    for i in range(3):
        current = ""
        for k in range(3):
            current += tic[k][i]
        if current.count(str(1)) == 3 or current.count(str(2)) == 3:
            has_won = True
            if current.count(str(1)) == 3:
                winner = "First"
            else:
                winner = "Second"
            break
if not has_won:
    diag1 = tic[0][0] + tic[1][1] + tic[2][2]
    diag2 = tic[0][2] + tic[1][1] + tic[2][0]
    if diag1.count("1") == 3 or diag1.count("2") == 3:
        has_won = True
        if diag1.count("1") == 3:
            winner = "First"
        else:
            winner = "Second"
    if diag2.count("1") == 3 or diag2.count("2") == 3:
        has_won = True
        if diag2.count("1") == 3:
            winner = "First"
        else:
            winner = "Second"
if has_won:
    print(f"{winner} player won")
else:
    print("Draw!")