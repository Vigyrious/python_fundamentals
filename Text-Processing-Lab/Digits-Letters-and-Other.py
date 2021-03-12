string = input()
chars = ""
nums = ""
others = ""
for i in string:
    if i.isdigit():
        nums += i
    elif i.isalpha():
        chars += i
    else:
        others += i
print(nums)
print(chars)
print(others)