sequence = input().split(" ")
command = input()
index = 0
while command != "find":
    treasure = ""
    for i in range(len(command)):
        treasure += chr(ord(command[i]) - int(sequence[index]))
        index += 1
        if index == len(sequence):
            index = 0
    command = input()
    first_type = treasure.index("&")
    second_type = treasure.index("&",first_type+1)
    element = treasure[first_type+1:second_type]
    first_coords = treasure.index("<")
    second_coords = treasure.index(">")
    coords = treasure[first_coords+1:second_coords]
    index = 0
    print(f"Found {element} at {coords}")