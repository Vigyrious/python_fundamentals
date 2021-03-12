number = input().split(", ")


def palindrome_check(a):
    reverse = ""
    for num in a:
        for i in range(len(num)-1,-1,-1):
            reverse += num[i]
        if num == reverse:
            print("True")
        else:
            print("False")
        reverse = ""


palindrome_check(number)