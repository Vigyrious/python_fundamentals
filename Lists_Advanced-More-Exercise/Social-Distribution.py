populations = [int(i) for i in input().split(", ")]
minimum_wage = int(input())
is_Possible = True

for i in range(len(populations)):
    biggest = max(populations)
    if populations[i] < minimum_wage:
        difference = minimum_wage - populations[i]
        populations[i] += difference
        if populations[populations.index(biggest)] - difference < minimum_wage:
            is_Possible = False
            break
        else:
            populations[populations.index(biggest)] -= difference
            biggest = max(populations)
        if populations[populations.index(biggest)] < minimum_wage:
            is_Possible = False
            break
if is_Possible:
    print(populations)
else:
    print("No equal distribution possible")