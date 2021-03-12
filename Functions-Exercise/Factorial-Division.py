num1 = int(input())
num2 = int(input())


def factorial_devider(a,b):
    first_factorial = 1
    second_factorial = 1
    for i in range(a,0,-1):
        first_factorial *= i
    for k in range(b,0,-1):
        second_factorial *= k
    return "{:.2f}".format(first_factorial / second_factorial)


print(factorial_devider(num1,num2))
