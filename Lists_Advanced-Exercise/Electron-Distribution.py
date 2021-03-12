number = int(input())
result = []
index = 0
while number > 0:
    if number >= 2*pow(index+1,2):
        result.append(2*pow(index+1,2))
    else:
        result.append(number)
        break
    number -= (2 * pow(index + 1, 2))
    index +=1
print(result)



# import math
# list1 = [int(i) for i in input().split(", ")]
# iterations = math.ceil(max(list1)/10)
# result = []
# for k in range(1, iterations+1):
#     for num in list1:
#         if (k-1)*10 < num <= k*10:
#             result.append(num)
#     print(f"Group of {k}0's: {result}")
#     result = []