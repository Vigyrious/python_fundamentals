num = int(input())
if num == 2:
    print("True")
elif num == 1:
    print("False")
else:
    isPrime = True
    for i in range(2,num):
        if num % i == 0:
            isPrime = False
if isPrime:
    print("True")
else:
    print("False")