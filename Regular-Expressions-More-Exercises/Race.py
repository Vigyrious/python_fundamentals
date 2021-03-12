import re
racers = input().split(", ")
winners = {}
data = input()
count = 1
while data != "end of race":
    sum = 0
    name_pattern = r'[A-Za-z]+'
    distance_pattern = r'[0-9]+'
    result_name = re.findall(name_pattern, data)
    result_distance = re.findall(distance_pattern, data)
    current_name = "".join(result_name)
    for current_number in result_distance:
        for smaller_num in current_number:
            sum += int(smaller_num)
    if current_name in racers and current_name not in winners:
        winners[current_name] = 0
        winners[current_name] += sum
    elif current_name in racers:
        winners[current_name] += sum
    data = input()
for key, value in sorted(winners.items(), key=lambda x:-x[1]):
    if count == 1:
        print(f"1st place: {key}")
    elif count == 2:
        print(f"2nd place: {key}")
    else:
        print(f"3rd place: {key}")
        break
    count += 1