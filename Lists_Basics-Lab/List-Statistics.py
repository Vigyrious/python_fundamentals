num = int(input())
negativeList = []
positiveList = []
for i in range(num):
    num1 = int(input())
    if num1 > 0:
        positiveList.append(num1)
    else:
        negativeList.append(num1)
print(positiveList)
print(negativeList)
print(f"Count of positives: {len(positiveList)}. Sum of negatives: {sum(negativeList)}")