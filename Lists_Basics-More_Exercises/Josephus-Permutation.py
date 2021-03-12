count = 0
index = 0
people = input().split(" ")
dead = int(input())
result = []
while len(people) != 0:
    count +=1
    if count % dead == 0:
        result.append(people.pop(index))
    else:
        index += 1
    if index >= len(people):
        index = 0
print(str(result).replace("'","").replace(" ",""))

