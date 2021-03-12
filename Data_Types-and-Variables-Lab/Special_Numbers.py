num = int(input()) #123
sum_digits = 0
for i in range(1,num+1):
    digits = i
    sum_digits = 0
    while (digits > 0):
        sum_digits += digits % 10
        digits = int(digits / 10)
    if sum_digits == 11 or sum_digits == 5 or sum_digits == 7:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
