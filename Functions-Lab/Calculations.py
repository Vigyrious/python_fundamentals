operation = input()
num1 = int(input())
num2 = int(input())
def calc(arg1,arg2,arg3):
    if arg1 == "multiply":
        result =  arg2*arg3
    elif arg1 == "divide":
        result = int(arg2/arg3)
    elif arg1 == "add":
        result =  arg2 + arg3
    elif arg1 == "subtract":
        result =  arg2 - arg3
    return result
print(calc(operation,num1,num2))