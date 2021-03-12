command = input()
while command != "end":
    current = ""
    for i in range(len(command)-1,-1,-1):
        current += command[i]
    print(f"{command} = {current}")
    command = input()