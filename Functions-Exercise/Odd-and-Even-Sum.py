numbers = input()

def odd_even(num):
    odd_sum = 0
    even_sum = 0
    for i in range(len(num)):
        if int(num[i]) % 2 == 0:
            even_sum += int(num[i])
        else:
            odd_sum += int(num[i])
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

odd_even(numbers)