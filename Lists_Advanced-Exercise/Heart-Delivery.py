cupids = [int(i) for i in input().split("@")]
count = 0
failed = 0
command = input().split(" ")
while command[0] != "Love!":
    if command[0] == "Jump":
        index = int(command[1])
        count += index
        if count >= len(cupids):
            count = 0
        if cupids[count] == 0:
            print(f"Place {count} already had Valentine's day.")
        else:
            cupids[count] -= 2
            if cupids[count] == 0:
                print(f"Place {count} has Valentine's day.")
    command = input().split(" ")
print(f"Cupid's last position was {count}.")
if sum(cupids) == 0:
    print("Mission was successful.")
else:
    for num in cupids:
        if num != 0:
            failed += 1
    print(f"Cupid has failed {failed} places.")