number = int(input())


def tribonnacci(num):
    tribbonacci_list = [1, 1, 2]
    if num == 1:
        print("1")
    elif num == 2:
        print("1 1")
    elif num == 3:
        print("1 1 2")
    else:
        print("1 1 2",end=" ")
        for i in range(number-3):
            result = sum(tribbonacci_list[len(tribbonacci_list) - 3:])
            tribbonacci_list.append(result)
            print(result,end=" ")


tribonnacci(number)