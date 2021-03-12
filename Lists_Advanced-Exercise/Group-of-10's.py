import math
list1 = [int(i) for i in input().split(", ")]
iterations = math.ceil(max(list1)/10)

for k in range(1,iterations+1):
    result = [int(x) for x in list1 if (k-1)*10 < int(x) <= k*10]
    print(f"Group of {k*10}'s: {result}")
    result = []