string = input()
string1 = string.replace(",", "")
newList = list(string1.split(" "))
if newList[len(newList)-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for i in range(1, len(newList)+1):
        if newList[i-1] == "wolf":
            print(f"Oi! Sheep number {len(newList)-i}! You are about to be eaten by a wolf!")