num = int(input())
biggest_snow = 0
biggest_time = 0
biggest_quality = 0
biggest_sum = 0
for i in range(num):
    snow = int(input())
    time = int(input())
    quality = int(input())
    formula = pow((snow / time), quality)
    if formula > biggest_sum:
        biggest_snow = snow
        biggest_time = time
        biggest_quality = quality
        biggest_sum = formula
print(f"{biggest_snow} : {biggest_time} = {biggest_sum:.0f} ({biggest_quality})")
