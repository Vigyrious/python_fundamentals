gift_list = input().split(" ")
command = input()
while command != "No Money":

    if "OutOfStock" in command:
        current = command.split(" ")
        for i in range(len(gift_list)):
            if gift_list[i] == current[1]:
                gift_list[i] = "None"
    elif "Required" in command:
        current = command.split(" ")
        if int(current[2]) <= len(gift_list)-1 and int(current[2]) >= 0:
            gift_list[int(current[2])] = current[1]
    elif "JustInCase" in command:
        current = command.split(" ")
        gift_list[-1] = current[1]
    command = input()
    current = ""
string = ""
while "None" in gift_list:
    gift_list.remove("None")
for gift in gift_list:
    print(gift,end=" ")