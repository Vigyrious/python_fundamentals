number = int(input())

def perfect_checker(a):
    perfect_sum = 0
    for i in range(1,a):
        if a % i == 0:
            perfect_sum += i
    if perfect_sum == a:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect_checker(number)