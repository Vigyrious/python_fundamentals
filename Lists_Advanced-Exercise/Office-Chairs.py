rooms = int(input())
avaliable = 0
free_chairs = 0
is_enough = True
for i in range(1, rooms+1):
    chairs, used = input().split(" ")
    used = int(used)
    avaliable = len(chairs)
    if avaliable > used:
        free_chairs += avaliable - used
    if avaliable < used:
        print(f"{used-avaliable} more chairs needed in room {i}")
        is_enough = False
if is_enough:
    print(f"Game On, {free_chairs} free chairs left")