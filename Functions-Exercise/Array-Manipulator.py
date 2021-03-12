numbers = input()


def array_manipulator(a):
    lists = a.split(" ")
    command = input().split(" ")
    while command[0] != "end":




        if command[0] == "exchange":
            new_list = []
            indexing = int(command[1])
            if indexing >= len(lists) or indexing < 0:
                print("Invalid index")
            else:
                for i in range(indexing+1, len(lists)):
                    new_list.append(lists[i])
                for k in range(0, indexing+1):
                    new_list.append(lists[k])
                lists = new_list






        elif command[0] == "max" or command[0] == "min":
            current = []
            count = 0
            checker = 0
            if command[0] == "max":
                if command[1] == "even":
                    ###############################
                    for num in lists:
                        if int(num) % 2 == 0:
                            if len(current) == 0:
                                current.append(count)
                                checker = int(num)
                            else:
                                if int(num) >= checker:
                                    current[0] = count
                                    checker = int(num)
                        count += 1
                else:
                    for num in lists:
                        if int(num) % 2 != 0:
                            if len(current) == 0:
                                current.append(count)
                                checker = int(num)
                            else:
                                if int(num) >= checker:
                                    current[0] = count
                                    checker = int(num)
                        count += 1
            else:
                if command[1] == "even":
                    for num in lists:
                        if int(num) % 2 == 0:
                            if len(current) == 0:
                                current.append(count)
                                checker = int(num)
                            else:
                                if int(num) <= checker:
                                    current[0] = count
                                    checker = int(num)
                        count += 1
                else:
                    for num in lists:
                        if int(num) % 2 != 0:
                            if len(current) == 0:
                                current.append(count)
                                checker = int(num)
                            else:
                                if int(num) <= checker:
                                    current[0] = count
                                    checker = int(num)
                        count += 1
                    #####################################
            if len(current) == 0:
                print("No matches")
            else:
                print(current[0])




        elif command[0]=="first" or command[0]=="last":
            if int(command[1]) > len(lists):
                print("Invalid count")
            else:
                first_last = []
                count = int(command[1])
                if command[0] == "first":
                    if command[2] == "even":
                        for num in lists:
                            if int(num) % 2 == 0:
                                first_last.append(int(num))
                            if len(first_last) == count:
                                break
                    else:
                        for num in lists:
                            if int(num) % 2 != 0:
                                first_last.append(int(num))
                            if len(first_last) == count:
                                break
                else:
                    if command[2] == "even":
                        for num in lists:
                            if int(num) % 2 == 0:
                                first_last.append(int(num))
                            if len(first_last) > count:
                                first_last.pop(0)
                    else:
                        for num in lists:
                            if int(num) % 2 != 0:
                                first_last.append(int(num))
                            if len(first_last) > count:
                                first_last.pop(0)
                print(first_last)
        command = input().split(" ")
    list_final = []
    for num in lists:
        list_final.append(int(num))
    print(list_final)






array_manipulator(numbers)
