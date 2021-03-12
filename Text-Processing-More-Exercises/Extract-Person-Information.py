repetitions = int(input())
for i in range(repetitions):
    data = input()
    name_start = data.index("@")
    name_end = data.index("|")
    number_start = data.index("#")
    number_end = data.index("*")
    name = data[name_start+1:name_end]
    number = data[number_start+1:number_end]
    print(f"{name} is {number} years old.")
