snowwhite_dect = {}
colors = {}
command = input()
while command != "Once upon a time":
    name, color, physics = command.split(" <:> ")
    physics = int(physics)
    combo = name+":"+color
    if combo not in snowwhite_dect:
        if color not in colors:
            colors[color] = 1
        else:
            colors[color] += 1
        snowwhite_dect[combo] = [0, color]
    snowwhite_dect[combo][0] = max(physics, snowwhite_dect[combo][0])
    command = input()

sorted_dwars = sorted(snowwhite_dect.items(),key=lambda x: (-x[1][0], -colors[x[1][1]]))
for key, value in sorted_dwars:
    current = key.split(":")
    print(f"({current[1]}) {current[0]} <-> {value[0]}")