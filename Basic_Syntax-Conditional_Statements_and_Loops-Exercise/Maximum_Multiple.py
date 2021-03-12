div = int(input())
bond = int(input())
for i in range(bond, 0, -1):
    if i % div == 0:
        print(i)
        break
