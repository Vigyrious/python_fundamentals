list_1 = [x for x in input().split(" ")]
shuffle_count = int(input())
top_bottom = [list_1[0], list_1[len(list_1)-1]]
list2 = [x for x in list_1[1:len(list_1)-1]]
first_half = []
second_half = []
shuffled_deck = []
count = 0
for shuffles in range(1, shuffle_count+1):
    for i in range(int(len(list2)/2)):
        first_half.append(list2[i])
    for i in range(int(len(list2)/2), len(list2)):
        second_half.append(list2[i])
    for i in range(int(len(list2)/2)):
        shuffled_deck.append(second_half[i])
        shuffled_deck.append(first_half[i])

    list2 = shuffled_deck
    shuffled_deck = []
    first_half.clear()
    second_half.clear()
    count = 0
list2.insert(0, top_bottom[0])
list2.append(top_bottom[1])
print(list2)
