import math
party_size = int(input())
days = int(input())
my_coins = 0
for i in range(1, days+1):
    if i % 10 == 0:
        party_size -= 2
    if i % 15 == 0:
        party_size += 5
        my_coins-= 2 * party_size
    my_coins += (50-(party_size*2))
    if i % 5 == 0:
        my_coins += 20*party_size
    if i % 3 == 0:
        my_coins -= 3*party_size
print(f"{party_size} companions received {math.floor(my_coins/party_size)} coins each.")


