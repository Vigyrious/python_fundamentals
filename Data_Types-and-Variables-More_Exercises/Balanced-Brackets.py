num = int(input())
bracket = 0
open = 0
isBalance = True
for i in range(num):
    symbol = input()
    if symbol == "(":
        bracket +=1
        open += 1
    elif symbol == ")":
        open -= 1
        bracket += 1
    if open == 2 or open == -2:
        isBalance = False
if bracket % 2 == 0 and isBalance:
    print("BALANCED")
else:
    print("UNBALANCED")