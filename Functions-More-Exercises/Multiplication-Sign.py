num1 = int(input())
num2 = int(input())
num3 = int(input())


def solvings(a,b,c):

    if a == 0 or b == 0 or c == 0:
        return "zero"
    new_list = [a, b, c]
    count = 0
    for num in new_list:
        if int(num) < 0:
            count += 1
    if count == 2:
        return "positive"
    elif count == 0:
        return "positive"
    else:
        return "negative"

print(solvings(num1, num2, num3))