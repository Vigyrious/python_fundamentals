string = input()
index = 0
new_list = ""
check = ""
while index < len(string):
    if not string[index].isdigit():
        check += string[index]
        index += 1
    else:
        number = ""
        while index < len(string) and string[index].isdigit():
            number += string[index]
            index += 1
        check = check.upper() * int(number)
        new_list += check
        check = ""

print(f"Unique symbols used: {len(set(new_list))}")
print(new_list)