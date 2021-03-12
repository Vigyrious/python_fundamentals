turns = int(input())
dect = {}
for i in range(turns):
    command = input().split(" ")
    if command[0] == "register":
        name = command[1]
        license = command[2]
        if name not in dect:
            dect[name] = license
            print(f"{name} registered {license} successfully")
        else:
            print(f"ERROR: already registered with plate number {dect[name]}")
    else:
        name = command[1]
        if name not in dect:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            dect.pop(name)
for key, value in dect.items():
    print(f"{key} => {dect[key]}")