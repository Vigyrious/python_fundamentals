string = input().split(" ")
count = 0
for word in string:
    new_word = ""
    numbers = ""
    word1 = ""
    for letter in word:
        if letter.isdigit():
            numbers += letter
        else:
            word1 += letter
    if len(word1) < 2:
        new_word = chr(int(numbers)) + word1
    else:
        new_word = chr(int(numbers)) + word1[-1:] + word1[1:-1] + word1[:1]
    print(new_word,end=" ")
