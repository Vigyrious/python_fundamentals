iterations = int(input())
dect = {}
for i in range(iterations):
    command = input()
    tip, name, damage, health, armor = command.split(" ")
    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10
    if tip not in dect:
        dect[tip] = {}
    if name not in dect[tip]:
        dect[tip][name] = 0
    dect[tip][name] = str(damage)+":"+str(health)+":"+str(armor)
for tipes in dect:
    avg_damage = 0
    avg_health = 0
    avg_armor = 0
    for key, value in dect[tipes].items():
        damage, health, armor = value.split(":")
        avg_armor += int(armor)
        avg_damage += int(damage)
        avg_health += int(health)
    avg_health /= len(dect[tipes])
    avg_armor /= len(dect[tipes])
    avg_damage /= len(dect[tipes])
    print(f"{tipes}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
    for key, value in sorted(dect[tipes].items(),key=lambda x: x[0]):
        damage, health, armor = value.split(":")
        print(f"-{key} -> damage: {damage}, health: {health}, armor: {armor}")