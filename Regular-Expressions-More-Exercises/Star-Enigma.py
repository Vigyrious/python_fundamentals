import re
pattern = r'[starSTAR]'
repetition = int(input())
attack_count = 0
destroy_count = 0
attacked_planets = []
destroyed_planets = []
for i in range(repetition):
    data = input()
    message = ""
    result = re.findall(pattern, data)
    for char in data:
        message += chr(ord(char) - len(result))
    regex = r'@(?P<Name>[A-Za-z]+)[^@:!\->]*:(?P<Population>\d+)[^@:!\->]*!(?P<Command>[AD])![^@:!\->]*\->(?P<SoldierCount>\d+)'
    new_data = re.finditer(regex, message)
    if re.search(regex, message):
        for datas in new_data:
            dect = datas.groupdict()
            planet_name = dect['Name']
            planet_population = int(dect['Population'])
            planet_command = dect['Command']
            planet_soldiers = int(dect['SoldierCount'])
    else:
        continue
    if planet_command == "A":
        attack_count += 1
        attacked_planets.append(planet_name)
    else:
        destroy_count += 1
        destroyed_planets.append(planet_name)
print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")
