number = int(input())

def loading_bar(a):
    load = "["
    bar = int(a / 10)
    if bar < 10:
        for i in range(1, bar+1):
            load += "%"
        for i in range(bar,10):
            load+= "."
        load += "]"
        print(f"{a}% {load}")
        print("Still loading...")
    else:
        print("100% Complete!")
        print("[%%%%%%%%%%]")

loading_bar(number)