winner = {"shards":"Shadowmourne","fragments":"Valanyr","motes":"Dragonwrath"}
key_dect = {"shards":0,"fragments":0,"motes":0}
chungus = {}
shards = 0
frags = 0
motes = 0
is_broke = False
while not is_broke:
    string = input().split(" ")
    for i in range(0, len(string), 2):
        quantity = int(string[i])
        element = string[i+1].lower()
        if element in key_dect:
            key_dect[element] += quantity
        else:
            if element not in chungus:
                chungus[element] = quantity
            else:
                chungus[element] += quantity
        for key, value in key_dect.items():
            if value >= 250:
                print(f"{winner[key]} obtained!")
                key_dect[key] -= 250
                is_broke = True
                break
        if is_broke:
            break


ordered_key_dect = sorted(key_dect.items(), key = lambda x:(-x[1], x[0]))
ordered_chungus = sorted(chungus.items(), key = lambda x:x[0])
for loot, quant in ordered_key_dect:
    print(f"{loot}: {quant}")
for loot, quant in ordered_chungus:
    print(f"{loot}: {quant}")