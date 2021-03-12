num1 = int(input())
num2 = int(input())
num3 = int(input())


def solve(a,b,c):
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    return smallest
print(solve(num1,num2,num3))